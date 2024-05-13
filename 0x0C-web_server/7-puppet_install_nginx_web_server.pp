package {"nginx":
	ensure  => present,
}
file { '/etc/nginx/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

class { 'nginx':
  manage_repo => true,
  service_manage => true,
}

nginx::resource::vhost { 'index.html':
  ensure       => present,
  www_root     => '/etc/nginx/html',
  listen_port  => '80',
  redirect_to        => 'http://twitter.com/home',
  redirect_from => ['/'],
  redirect_status => 'permanent',
}
