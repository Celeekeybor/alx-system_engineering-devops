# Kill the "killmenow" process using pkill
exec { 'killmenow':
  command => 'pkill -f "killmenow"',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
  onlyif  => 'pgrep -f "killmenow"',
}

