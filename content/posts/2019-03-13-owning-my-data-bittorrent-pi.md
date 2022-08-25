+++
title = "Owning my Data: BitTorrent Pi"
slug = "bittorrent-pi"
date = 2019-03-14
tags = ["raspberry pi", "torrent", "vpn"]
+++

Who remembers Limewire from the early Aughts?

[Limewire](https//en.wikipedia.org/wiki/LimeWire) was one of the early Peer-to-Peer (P2P) networks out there. It was used mostly to share music files across the Internet. I remember a version of it installed on my high school’s network in a secret folder. Because back in 2003, educators thought it was a good idea to give high schoolers admin privileges on a network!

Limewire was eventually shut down, but not forgotten. Here are a couple great articles =

- [https//melmagazine.com/en-us/story/limewire-memes-millennials](https//melmagazine.com/en-us/story/limewire-memes-millennials)
- [https//www.forbes.com/sites/hughmcintyre/2018/03/21/what-happened-to-the-piracy-sites-that-nearly-destroyed-the-music-industry-limewire/#2794fced32d7](https//www.forbes.com/sites/hughmcintyre/2018/03/21/what-happened-to-the-piracy-sites-that-nearly-destroyed-the-music-industry-limewire/#2794fced32d7)

While Limewire and Napster are gone, their legacy survives today in the form of BitTorrent.

What is BitTorrent? From [Wikipedia](https//en.wikipedia.org/wiki/BitTorrent):“BitTorrent (abbreviated to BT) is a communication protocol for peer-to-peer file sharing (P2P) which is used to distribute data and electronic files over the Internet.”  Essentially BitTorrent works by downloading a little bit of a file from everyone in the BitTorrent network who has already downloaded that file. This is different from traditional downloading where you download the entire file from a single server. Now you can download a file from several servers at the same time. This leads to faster downloads. Why faster downloads? The moment you start downloading a torrent file, you start to also share. So the parts you have downloaded, you also begin to upload. This is what good torrenters do.  
![](https//upload.wikimedia.org/wikipedia/commons/0/09/BitTorrent_network.svg)
When I download an .ISO file from Ubuntu or Raspberry Pi Foundation, I select the torrent option. This takes the burden of downloading a file from their servers and onto other users. This decreases the amount of traffic going to and from their servers, saving them money.

Now why am I building a whole Raspberry Pi to do this? When you participate in the BitTorrent network, you expose your IP address to everyone who is connected. What if I don’t want that? What if I’m interested in privacy? That’s where this project comes in.

Today I’m creating a Raspberry Pi Torrentbox that can always be on and will be hidden behind a VPN.

As always, start with a fresh Pi with Raspbian Lite.

**Install Deluge**

This is a BitTorrent client that will facilitate our sharing of torrents. I like deluged because the program has  decent web client, to access through a browser, or you can install a thin client on another computer, and use it there.

    sudo apt-get install deluged deluge-web deluge-console

To run the web console run =

    deluge-web

default password= deluge

navigate to the Pi’s IP address 192.168.1.0 =8112 and finish setting it up.

The different tabs are were you will want to tweak what's left.

Networks Tab:Use Random Ports checked
 Downloads Tab:point to folders on external hdd
 Other setup stuff
 Daemon Tab:Allow remote connections

To setup deluge so you can use remotely from the command line, use the commands below =

    deluge-console
     sudo nano ~/.config/deluge/auth
     changed user =password =level
     config -s allow_remote True
     config allow_remote exit
     sudo pkill deluged

You will also want to enable Deluge to run at startup.

Enable for startup =

    sudo nano /etc/rc.local

# Start Deluge on boot =

    sudo -u pi /usr/bin/python /usr/bin/deluged
    sudo -u pi /usr/bin/python /usr/bin/deluge-web

Next I installed a VPN to encrypt the Torrent traffic and hide my IP Address. I choose Proton VPN as my provider. I like the folks at Proton Technologies a lot, and I trust them not to keep logs, making it tougher for hackers and/or governments to spy on your data. Also, they’re based in Switzerland, a country with strong privacy laws.

For this process to work, you must install it as Root.

First we’ll install the dependencies required by Proton VPN

     sudo su
     sudo apt-get install openvpn dialog -y

Now for the Proton VPN Command Line (CLI) client

sudo wget 'https//github.com/ProtonVPN/protonvpn-cli/raw/master/protonvpn-cli.sh' -O 'protonvpn-cli.sh' && sudo bash protonvpn-cli.sh &#8211;install

To run enter the command below and follow the instructions =

    sudo protonvpn-cli --init

 Entered info from Proton VPN
 Enter OpenVPN username and password
 Select ProtonVPN Plan
 Use custom DNS Server?
 Decrease OpenVPN privileges? [Y/n]:Y 

Now that it’s active, run sudo pvpn -p2p to connect to a VPN node that supports Peer-To-Peer (What BitTorrent it) traffic.

To see that it is up and running =

    sudo pvpn -status

Finally, we’ll disconnect before running some more  configuration.

    sudo pvpn -disconnect

To make Proton-VPN easier to start, stop, and run at startup, we need to set it up as a service in SystemMD. A program that runs several processes in Debian.

Setting up as service in SystemMD

Create the following file =

    sudo nano /etc/systemd/system/protonvpn-cli.service
    [Unit]
    Description=ProtonVPN CLI Auto-Start
    After=network.target
    
    [Service]
    Type=forking
    User=root
    ExecStart=/usr/bin/protonvpn-cli -p2p
    ExecReload=/usr/bin/protonvpn-cli --disconnect && /usr/bin/protonvpn-cli -p2p
    ExecStop=/usr/bin/protonvpn-cli -p2p
    Restart=always
    
    [Install]
    WantedBy=multi-user.target

Reboot and you are good to go! Enjoy the modern world of file sharing. Here are a few links to get you going!

Problems =

Error:I really did not have many problems with this project. The programs used are all very stable, and well supported.

Help From =

- [server-with-deluge-on-a-raspberry-pi/](https//www.techjunkie.com/create-a-headless-torrent-server-with-deluge-on-a-raspberry-pi/)
- [https//www.howtogeek.com/142044/how-to-turn-a-raspberry-pi-into-an-always-on-bittorrent-box/](https//www.howtogeek.com/142044/how-to-turn-a-raspberry-pi-into-an-always-on-bittorrent-box/)

- [https//blog.x86txt.com/protonvpn/security/…/protonvpn-cli-as-systemd-service.html](https//blog.x86txt.com/protonvpn/security/%E2%80%A6/protonvpn-cli-as-systemd-service.html)

- [https//github.com/ProtonVPN/protonvpn-cli](https//github.com/ProtonVPN/protonvpn-cli)
