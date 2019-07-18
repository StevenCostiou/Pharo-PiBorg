#1701 port is for the Pharo-PiBorg ui server
sudo iptables -A INPUT -p tcp --dport 1701 --j ACCEPT

#40423 port is for the Telepharo server
sudo iptables -A INPUT -p tcp --dport 40423 --j ACCEPT

#Need sudo access
sudo pkill -9 python
sudo pkill -9 pharo

#starting the borg
cd piBorg
sudo ./pharo-server
