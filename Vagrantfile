Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.ssh.insert_key = 'true'
  config.vm.network "public_network"
  config.vm.network "private_network", ip: "172.10.0.140"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "9216"
    vb.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    sudo yum -y update
    sudo yum -y install gedit
  SHELL
  
end
