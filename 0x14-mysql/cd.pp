package { 'mysql-server-5.7':
  ensure => "5.7.x",
}

service { 'mysql':
  ensure => running,
  enable => true,
  require => Package['mysql-server-5.7']
}

