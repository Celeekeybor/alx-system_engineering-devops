# install Flask using pip3
package { 'python3-pip':
  ensure => installed,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
