# Ensure the apt package manager is up to date
exec { 'apt-update':
  command => '/usr/bin/apt-get update -y',
  path    => ['/usr/bin', '/bin'],
  unless  => '/usr/bin/test -f /var/lib/apt/periodic/update-success-stamp',
}

# Install Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update'],
}

# Ensure the hostname command is available
package { 'hostname':
  ensure => installed,
}

# Configure Nginx to add the custom header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'), # Use a template for the configuration
  require => Package['nginx'],
  notify  => Service['nginx'],  # Notify the service to restart when the file changes
}

# Create a template file for the Nginx configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => @("END"),
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        add_header X-Served-By \$hostname;
        try_files \$uri \$uri/ =404;
    }
}
| END
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

