# Define class for MySQL installation and management
class mysql {
    # Install MySQL server version 5.7.x
    package { 'mysql-server':
        ensure => '5.7.1',
    }

    # Start and enable MySQL service
    service { 'mysql':
        ensure => 'running',
        enable => true,
        require => Package['mysql-server'],
    }
}

# Include the mysql class
include mysql

