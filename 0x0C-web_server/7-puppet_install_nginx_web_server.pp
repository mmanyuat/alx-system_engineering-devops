#automating configuration with puppet

package { 'nginx':
  ensure => present,
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.mbusa.com/en/vehicles/class/g-class/suv permanent;',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

