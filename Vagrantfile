BOX               = 'ubuntu/trusty64'

Vagrant.configure("2") do |config|
  config.vm.network 'public_network'
  config.vm.synced_folder ".", "/vagrant"
	name = "flaskMachine"
	config.vm.define name do |machine|
		machine.vm.box   = BOX
		machine.vm.provision "shell", inline: <<-SHELL
		sudo adduser vsftpduser
		sudo echo "vsftpduser:haslo" | chpasswd 
		sudo apt-get update
		sudo apt-get install -y mc
		sudo apt-get install -y vsftpd
		sudo echo "" >> /etc/vsftpd.conf
		sudo echo "local_enable=YES" >> /etc/vsftpd.conf
		sudo echo "" >> /etc/vsftpd.conf
		sudo echo "write_enable=YES" >> /etc/vsftpd.conf
		sudo echo "" >> /etc/vsftpd.conf
		sudo service vsftpd restart
		sudo apt-get update	  
		sudo apt-get install python3-pip -y
		sudo apt-get install python-dev -y
		sudo apt-get install curl -y
		
		sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
		echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
		sudo apt-get update
		sudo apt-get install -y mongodb-org
		sudo service mongod start
		
		sudo pip3 install requests
		sudo pip3 install flask
		sudo pip3 install mongoengine
		sudo pip3 install flasgger
		SHELL
    end
end

