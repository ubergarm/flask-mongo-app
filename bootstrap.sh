#!/usr/bin/env bash
# This vagrant bootstrap script is run as root at boot time
# It must be idempotent! My favorite $5 word these days.

# First portion will only run one time on each fresh box.
if [ ! -f /home/vagrant/boot_strapped ]; then

    #update default locale to UTF8
    sed -i.bak 's/en_US\"/en_US.UTF-8\"/g' /etc/default/locale
    sed -i.bak 's/en_US$/en_US.UTF-8/g' /etc/default/locale

    #update apt sources
    apt-get update

    #install ansible
    apt-get install -y ansible

    #use ansible to finish provisioning system
    #setup /etc/ansible/hosts
    echo "[servers]" > /etc/ansible/hosts
    echo localhost >> /etc/ansible/hosts

    #setup ssh agent authorized keys
    #this might not be the best/safest, but it makes ansible happy...
    if [ ! -d /root/.ssh ]; then
        ssh-keygen -t dsa -N '' -C 'root@precise32' -f ~/.ssh/id_dsa
        cat /root/.ssh/id_dsa.pub > /home/vagrant/.ssh/authorized_keys2
        chown vagrant:vagrant /home/vagrant/.ssh/authorized_keys2
    fi
    #test ansible setup
    ansible servers -m ping -u vagrant --sudo
   
    #if ansible is ready to go, then dont run this stuff again
    if [ $? -eq 0 ]; then
        touch /home/vagrant/boot_strapped
    fi
fi

#finish up using the ansible playbook
ansible-playbook /vagrant/ansible/flask-mongo-playbook.yml

