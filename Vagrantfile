# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define :web do |web_config|
    web_config.vm.box = "precise32"
    config.vm.box_url = "http://files.vagrantup.com/precise32.box"
    web_config.vm.network :forwarded_port, host: 5000, guest: 5000
    web_config.vm.network :private_network, ip: "192.168.33.3"
    #web_config.vm.synced_folder "./data", "/vagrant_data"

    #the bootstrap script installs ansible in the VM itself    
    web_config.vm.provision :shell, :path => "bootstrap.sh"

    #don't do the next section, as ansible is installed in the VM itself
    #web_config.vm.provision :ansible do |ansible|
    #  ansible.playbook = "ansible/flask-mongo-playbook.yml"
    #  ansible.hosts = "servers"
    #end
  
    web_config.vm.provider :virtualbox do |vb|
      #vb.gui = true
      vb.customize [
		    "modifyvm", :id,
		    "--name", "flask-app-server",
		    "--memory", "1024"
	 	   ]
    end
  end
end
