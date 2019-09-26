Vagrant.configure("2") do |config|

	$cluster_begin_ip_range = 100
	$cluster_net = "172.0.5."
	$vbox_img = "ubuntu/xenial64"
	$cluster_name_prefix = "ubuntu"
	$domain = "my.home"
	
	#Run ubuntu cluster
	(1..6).each do |i|
		config.vm.define "#{$cluster_name_prefix}#{i}" do |ubuntu|
			ubuntu.vm.box = "#{$vbox_img}"
			ubuntu.vm.hostname = "#{$cluster_name_prefix}#{i}.#{$domain}"
			ubuntu.vm.network :private_network, ip: "#{$cluster_net}#{$cluster_begin_ip_range+i}"
			ubuntu.vbguest.auto_update = false
			ubuntu.vm.provider :virtualbox do |vb|
				vb.customize [
					"modifyvm", :id,
					"--cpuexecutioncap", "80",
					"--memory", "20248",
					"--cpus", "2",
					"--audio", "none",
				]
			ubuntu.vm.provision "shell", inline: <<-SHELL
				sed -i 's/PermitRootLogin no/PermitRootLogin yes/g' /etc/ssh/sshd_config
				sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
				echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBT8ioWVWIAnRhlxmYKtRNJz6HQiZQ1y4ZkGu/k0Aw5y725EfkpRYfMZoayvVqzSK0V3+PmdRGDBne2FO+ZFTk0SjMqQHDzm3B0xwOVBB4sx6e4WeL+07PJw6eOa+CZLSvNt3YH+avQm9pLA1MN3dViwF+bN2QvN/UCSuwVbTvA84SQUzeC+vva1sUQ+AURjaZoYhLFK/8BafhCWS4ZSTH1uXoloQRK//MraLP4M0fr5LaV22FYtsEnr5XZkP1LnxSKu1WgsDGTT7uCEaagx6SsFeAYj+6D9azotaazLP7aVNodQ9cIM3cUUSTjzKDI9EocdqY5/cBRFh+aMjN1Qlb root@myansible.my.ru' >> ~/.ssh/authorized_keys
				systemctl restart ssh || systemctl restart sshd
			SHELL
			end
		end
	end
end
