#Let’s practice using Puppet to make changes to our configuration file
file {'ssh_config':
    ensure   => present,
    path     => '~/.ssh/config',
    content  => "PasswordAuthentication no\nIdentityFile ~/.ssh/school",
    mode     => '0600',
}
