#!/usr/bin/pup
# Install pip
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip'
}
