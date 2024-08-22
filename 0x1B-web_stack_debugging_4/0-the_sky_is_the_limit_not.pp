#fix nginx to accept and serve more requests

exec {'modify max open files limit setting':
	command => 'sed -i \'s/15/4096/\' /etc/default/nginx && sudo service nginx restart',
	path    => '/usr/local/sbin:/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
	unless  => 'grep -q "4096" /etc/default/nginx',
}

