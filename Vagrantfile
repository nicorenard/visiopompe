# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "debian/bullseye64"
  config.vm.box_url = "file://./packer-debian-buster-x64-vagrant.box"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Set VM name
  #     See https://stackoverflow.com/questions/17845637/how-to-change-vagrant-default-machine-name
  @vm_name = "visiopompe"
  config.vm.hostname = @vm_name
  config.vm.define @vm_name

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  #config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 80

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  #config.vm.network "private_network", ip: "127.0.0.1"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Configure share folders
  config.vm.synced_folder "./vagrant", "/vagrant",
    mount_options: ['ro']
  config.vm.synced_folder ".", "/usr/share/visiopompe",
    mount_options: ['rw']

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Configure VirtualBox
  config.vm.provider "virtualbox" do |virtualbox, override|
    virtualbox.name = @vm_name

    # Double memory size from default
    virtualbox.memory = 2048

    # Prevent VirtualBox from interfering with host audio stack
    virtualbox.customize ["modifyvm", :id, "--audio", "none"]
  end

  # Configure plugins
  # - vagrant-vbguest
  #     deactivate automatic update of VBox Guest Additions
  #config.vbguest.auto_update = false
  # - vagrant-hostupdater
  #config.hostsupdater.aliases = ["#{@vm_name}-default"]

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
  #

  # Provision VM with Bash scripts, already mounted on guest filesystem
  #    For running script already standing on guest filesystem, see: 
  #    see https://www.vagrantup.com/docs/provisioning/shell#external-script
  #
  #   Default provisionner, running *all* configuration steps.
  config.vm.provision "all",
    type: "shell",
    run: "once",
    inline: "/usr/bin/bash /vagrant/main.sh"

  #   Create and populate project's dedicated virtualenv.
  config.vm.provision "venv",
    type: "shell",
    run: "never",
    inline: "/usr/bin/bash /vagrant/venv.sh"

  #   Install and configure MariaDB
  config.vm.provision "mariadb",
    type: "shell",
    run: "never",
    inline: "/usr/bin/bash /vagrant/mariadb.sh"
end
