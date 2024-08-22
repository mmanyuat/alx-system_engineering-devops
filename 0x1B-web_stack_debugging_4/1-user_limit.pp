# Enabling the user holberton to logon and change setting
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.cong",
  path    => '/usr/local/bin/:/bin/'
}

# increase soft file limit
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
