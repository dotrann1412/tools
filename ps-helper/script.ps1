# port control on Windows
netsh interface portproxy delete v4tov4 listenport=PORT listenaddress=*
netsh interface portproxy add v4tov4 listenport=PORT_1 connectaddress=192.168.99.2 connectport=PORT_2
netsh interface portproxy show v4tov4

# assign static ip for WSL
interface ip add address "vEthernet (WSL)" 192.168.99.1 255.255.255.0
wsl --exec sudo ip addr add 192.168.99.2/24 broadcast 192.168.99.255 dev eth0 label eth0:1;
# or if the script is executed directly from WSL 
sudo ip addr add 192.168.99.2/24 broadcast 192.168.99.255 dev eth0 label eth0:1;