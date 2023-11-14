# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  if Vagrant.has_plugin? "vagrant-vbguest"
    config.vbguest.no_install  = true
    config.vbguest.auto_update = false
    config.vbguest.no_remote   = true
  end

  config.vm.define :servidorRest do |servidorRest|
    servidorRest.vm.box = "bento/ubuntu-22.04"
    servidorRest.vm.network :private_network, ip: "192.168.60.3"
    servidorRest.vm.provision "file", source: "apirest_mysql.py", destination: "/home/vagrant/apirest_mysql.py"
    servidorRest.vm.provision "file", source: "init.sql", destination: "/home/vagrant/init.sql"
    servidorRest.vm.provision "shell", path: "script.sh"
    servidorRest.vm.hostname = "servidorRest"
  end
end
