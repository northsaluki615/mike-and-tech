+++
title = "Ads? What Ads?"
slug = "ads-what-ads"
date = 2017-03-22
tags = ["ads", "diy", "networking", "raspberry pi"]
+++

![wp-1490186202317.png](https =//mikehelmers.com/wp-content/uploads/2017/03/wp-1490186202317.png)For the last month or so there has been a noticeable decrease in the number of ads that

appear on our network. Why? I installed a Pi-hole. Using a Raspberry Pi Zero, the same one from my OpenVPN project, I installed a program call 'Pi-hole'. This nifty little piece of software shuttles off ad requests into a black hole. It does this by acting as a DNS/web server, identifying ad domains before they download, and sending them down a virtual black hole.

What is DNS?

DNS stands for Domain Name Servers. To quote [sidewaysdictionary.com](https =//sidewaysdictionary.com/#/term/domain-name-servers) =

'It's like a contact list on your mobile phone. You know your correspondents by their names but the contact list has telephone numbers and postal addresses. When you want to go to a particular website, you look up the site's name (such as www.google.com) in the Domain Name lookup service and get back from that the Internet Protocol address of the destination Web Site. '

Pi-hole has a list of millions of ad domains, and whenever is sees one of those addresses, it throws it way.

This project only had two steps for me.

1. Install the Pi-hole
2. Configure DNS settings on my router

##### 1. Install the [Pi](https =//pi-hole.net)-hole

This was incredibly simple to get up and running. I simply ran one script in the command line =

    curl -sSL https =//install.pi-hole.net | bash

This is from the [Pi-Hole.net](https =//pi-hole.net) instructions, and it really is that easy! After that script runs, it'll ask you some questions, and after that, you're good to go!

##### 2. Configure DNS settings on my router

This can be a bit scarier, but if you're comfortable enough with a Raspberry Pi, it won't be that bad! I logged into my router by entering the router's local IP address into a web browser (192.1.1.1). I navigated to the DHCP settings and setup a static DNS using the Pi's local address (192.168.1.104). This routes all traffic through my Pi, cleansing the ads from it.

##### 3. Update [OpenVPN settings](http =//mikehelmers.com/2017/03/11/i-made-a-vpn/) (I added a step)

OpenVPN uses a default DNS of 8.8.8.8, which is Google's DNS servers. I want to change that to use my Pi. First I edited the DHCP options in the server.conf (located /etc/openvpn/server.conf) file, which directed the VPN's tunnel to the new Pi-hole DNS server. I also had to create a new file in the dnsmasq.d directory (located /etc/dnsmasq.d/) called 00-openvpn.conf . Here I added the line 'interface=tun0 '.

This is important. The Pi-hole is only listening to my eth0 network interface (ethernet), and not the tun0 (VPN virtual tunnel). This file enables the Pi-hole to filter data coming from the VPN.

Why go through this trouble for my phone? Blocking ads while using my cellular connection can save data. Going through my VPN stops those ads from loading, I could save quite a few MBs per month.

![Screenshot_20170321-203750.png](https =//mikehelmers.com/wp-content/uploads/2017/03/screenshot_20170321-203750.png)Overall, this was a fun little project. It was simple, and I enjoy looking at the stats. In this image, you can see what our network traffic is like while sleeping, and what it changes to when we start using our phones in the morning!

Another great aspect of the Pi-hole, is its user interface. By using any web browser on my local network, I can go look at stats and settings. In this case, I navigated to 192.168.1.104/admin. Here I can manipulate the white-list and black-list of what sites are allowed on my network.

##### Takeaways and future thoughts =

**Unexpected problems =**

Port 80. The Pi-hole creates a small web server that uses port 80 (HTTP) to communicate the admin console and direct ad traffic. I was trying to set up a separate web server, and I couldn't figure out why it wasn't working. It's because my Pi-hole was blocking port 80. I have not solved for this yet.

**Future Concerns =**

I can't use port 80 for anything else on this Pi. For now, that's ok. As anything public facing should be using HTTPS (which is more secure), or port 443.

**Future Enhancements =**

Maybe use this to monitor traffic, and look for unusual spikes in DNS requests. This could identify malware or bots on my network.

Follow the developers on GitHub here = [https =//github.com/pi-hole](https =//github.com/pi-hole)

Learn more at [pi-hole.net](https =//pi-hole.net)

I also had some troubleshooting help from [https =//www.reddit.com/r/pihole/comments/5oh4ef/protip_getting_openvpn_and_pihole_working_together](https =//www.reddit.com/r/pihole/comments/5oh4ef/protip_getting_openvpn_and_pihole_working_together)
