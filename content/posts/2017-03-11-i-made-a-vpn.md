+++
title = "I Made a VPN"
slug = "i-made-a-vpn"
date = 2017-03-11
tags = ["networking", "raspberry pi", "vpn"]
+++

While learning about networking it became clear how easy it was to snoop on someone's internet activity when out in the public. If you're connected to a wifi network that isn't yours, all of your traffic can be captured and read. Now, does the coffee shop that you're sitting at bother to look at all that information? Probably not. But they could, and so could that creepy guy staring at his laptop across the room. This raised the question, what can I do about this?

![IMG_20170311_085750](https =//mikehelmers.com/wp-content/uploads/2017/03/img_20170311_085750.jpg)The easiest solution is not to use wifi and use my phone as a hotspot. But that's no fun! I decided to take a Raspberry Pi and turn it into a personal VPN.

A Raspberry Pi is a computer that's roughly the size of a deck of cards. For its small size, it's quite versatile and can perform a surprisingly large amount of tasks. For more information on the Pi, [click here](https =//www.raspberrypi.org/).

Now, a VPN works by creating an encrypted tunnel between your device (the client) and the end-point of the tunnel (VPN server). In this case, the client will be my Pixel phone, and the Raspberry Pi connected to my home network will be my server. At the end of this project, I'll be able to securely send data from my phone over the open internet, without having to worry about someone snooping. It essentially allows me to access my home network from anywhere on Earth, which is pretty cool.

To do this project, I broke it down into 4 steps =

1. Install Raspbian

2. Install OpenVPN

3. Configure my router

4. Configure my phone

##### 1. Install Raspbian =

Raspbian is a version of GNU/Linux that runs as the Raspberry Pis operating system (think Windows or OSX on Apple computers). I'm using a Raspberry Pi Zero, so I installed Raspbian Jessie-Lite, a smaller profile OS that does not have a GUI. This was simple. There are many different ways to install Raspbian, I won't go into it. Google it, or follow the official instructions from the [Raspberry Pi Foundation located here](https =//www.raspberrypi.org/).

##### 2. Install [OpenVPN](https =//openvpn.net/) =

This took some time. OpenVPN is an open source VPN that is free to use and is quite secure. I also like it because they have an [app for Android](https =//play.google.com/store/apps/details?id=net.openvpn.openvpn/hl=en), allowing me to use the VPN on my phone. After searching the best instructions I found were at [pivpn.io](http =//www.pivpn.io/). It only took one line of code =

    curl -L https =//install.pivpn.io | bash

It installs the VPN server, runs you through generating security keys, and generating your OpenVPN profile (this is important in Step 4). The OpenVPN profile is saved as a .ovpn file.

##### 3. Configure my router =

In order to contact my VPN from the outside internet, I needed to perform Port Forwarding. I went into my router (a Linksys WRT1900ACS) and forwarded port 1194 to my Pi's local IP address. This told my router to send any VPN traffic it received to my Pi, allowing me to connect to the server I just created.

##### 4. Configure my phone

OpenVPN has an [app for Android](https =//play.google.com/store/apps/details?id=net.openvpn.openvpn/hl=en) that I used. Download it here. I also had to install an FTP server on my Pi so I could transfer the .ovpn profile created in Step 2 onto my phone. I prefer AndFTP. Using AndFTP I transferred the .ovpn file to my phone while connected to my home network.

This profile is the key to accessing the VPN server. Once imported into the OpenVPN app, I entered my password, hit connect, and voila! I was in!

I know had a secure connection to my home network! Time to pay bills in absolute privacy.

##### Takeaways and future thoughts =

**Unexpected problems =** Getting the .ovpn profile to my phone. After I set up the VPN server, I didn't have a clue how to get the profile onto my phone. After a little research, I decided that an FTP server would make the most sense. Once AndFTP was installed, navigating to the OVPN folder and downloading the file was super easy. I liked the tool, so I installed it on the other Pis in my home too

**Future Concerns =** I don't have a static IP address. At some point, my ISP will probably change my IP address, which means I'll have to reconfigure my OpenVPN server. I should look into Dynamic DNS to see if I can create a custom address to solve this problem.

**Future Enhancements =** I want to install a [Pi-Hole](https =//pi-hole.net/) on this Pi to block Ads. Because, why not?
