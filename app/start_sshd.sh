PASSWORD=$(pwgen -n 20 -1 -s)
echo root:$PASSWORD | chpasswd 
echo "\033[31m===============\nSSH Password: $PASSWORD\n===============\033[0m"
/usr/sbin/sshd
