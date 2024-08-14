
#    headers = {'user=agent': 'request'}
 #   headerfest to fix Apache 500 error

# Ensure a file exists
file { '/var/www/html/index.php':
  ensure  => file,
  source  => 'puppet:///modules/custom_module/index.php',
  mode    => '0644',
  owner   => 'www-data',
  group   => 'www-data',
}

# Ensure the Apache service is running
service { 'apache2':
  ensure     => running,
  enable     => true,
  require    => File['/var/www/html/index.php'],
}
s = {'user=agent': 'request'}
