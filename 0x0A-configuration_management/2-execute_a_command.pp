#Kill the process named killmenow using pkill

exec { 'kill killmenow process':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin',
  onlyif  => 'pgrep killmenow',
}
