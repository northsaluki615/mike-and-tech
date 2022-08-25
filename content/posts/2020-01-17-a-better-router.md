+++
title = "A Better Router"
slug = "a-better-router"
date = 2020-01-18
tags = ["diy", "networking", "security", "upgrade"]
+++

Did you know that you can do more with your router? It is possible to have very granular control over everything that this all-important machine does. You just must unlock it.

I installed DD-WRT onto my Linksys WRT1900ACS router.

What is DD-WRT? “DD-WRT is Linux-based firmware for wireless routers and access points.” [https//en.wikipedia.org/wiki/DD-WRT](https//en.wikipedia.org/wiki/DD-WRT) It is the software that enables your router work, just open-sourced, meaning it can be much more powerful and flexible than what comes prepackaged on your store-bought router. The tradeoff is that it is more convoluted to setup and it is much easier to break.

## **Steps to Follow =**

1. Download the required software for my Linksys WRT1900ACS
2. Flash the DD-WRT image to my router
3. Setup DD-WRT
4. Setup Pi-Hole to serve as DNS server

### 1. Download the required software =

I went out to the [DD-WRT website](https//dd-wrt.com/), and searched for my router. I own a Linksys WRT1900ACS Version 2. This ultimately led me to [https//dd-wrt.com/support/router-database/?model=WRT1900ACS_v2](https//dd-wrt.com/support/router-database/?model=WRT1900ACS_v2). I also needed to download an older version of the Linksys firmware to install DD-WRT. It took some searching, but eventually I found what I was looking for here:[https//www.userdrivers.com/LAN-Network-Adapter/Linksys-WRT1900AC-Router-Firmware-Update-1-1-8-161917/download/](https//www.userdrivers.com/LAN-Network-Adapter/Linksys-WRT1900AC-Router-Firmware-Update-1-1-8-161917/download/). This was required due to changes in Linksys more recent firmware. I could not just upload the new software. Fortunately, Linksys makes this easy. After the router rebooted, the firmware update was complete.

### 2. Flash the DD-WRT image to my router =

The first part of this is downgrading the current firmware on my router. Using the 1.1.8 version I obtained from [userdrivers.com](https//userdrivers.com), I logged into my router at 192.168.1.1 and navigated to the “Connectivity” Tab. From there I selected “Firmware Update” and selected the appropriate file. Then I clicked “Start” followed by “Yes” and let the program run.

Now, I could load DD-WRT. I followed the exact same steps as above, but instead selected the DD-WRT Firmware instead of the Linksys. This time after the router rebooted, I had DD-WRT running!

### 3. Setup DD-WRT =![](__GHOST_URL__/content/images/wordpress/2020/01/ddwrtlogin-221x300.png)

This is the long and tedious part. Many aspects of a router are automatically configured in most commercial models. I need to define everything. So, here’s a brief rundown of the basic setup I did.

##### Setup Tab =

> - Router Name:Router Name
> - Domain Name:URL pointed at my IP address
> - DHCP Type:DHCP Server
> - DHCP Server:Enable
> - Start IP Address:192.168.1.XXX
> - Static DNS 1:1.1.1.1
> - Static DNS 2:1.0.0.1
> - NTP Client:Enable
> - Time Zone:US/Central

Then I clicked “Save” and then “Apply Changes”

##### Wireless Tab =

Since this is a dual-band router, it has two frequencies it broadcasts on, 2.4 GHz and 5 GHz. Each needs to be set up separately. The settings are the same for both channels except as noted.

> - Wireless Mode:AP
> - Wireless Network Mode:AC-Only (5GHz) and Mixed (2.4GHz)
> - Wireless Network Name (SSID):The Banana Stand 5GHz (5GHz) and The Banana Stand (2.4GHz)

Then I clicked “Save” and then “Apply Changes” and I switched to the “Wireless Security” tab nested under the “Wireless” Tab

> - Security Mode:WPA
> - Network Authentication:WPA2 Personal
> - WPA Algorithms:CCMP-128 (AES)
> - WPA Shared Key:WiFi Password

Then I clicked “Save” and then “Apply Changes”

Now the router is ready for business as usual!

### 4. Setup Pi-Hole to serve as DNS server =

Using the Linksys Smartwifi software that came default on my router, all I had to do is enter the IP address of my Pi-Hole as a Static DNS server. And I was good to go. No longer. DD-WRT is a bit for tricky, but I did get it going.![](__GHOST_URL__/content/images/wordpress/2020/01/ddwrtarticle_dnsmaswpihole-e1579297459119-300x179.png)

1. Open the 'Services Tab'
2. Select the next tab named 'Services'\
3. Scroll down to the DNSmasq settings
4. Enable and Disable as seen in the image
5. Under 'Additional Dnsmasq Options' type:dhcp-option=6,192.168.1.101
6. Scroll to the bottom of the page and hit apply settings, your pihole is now the DNS server for your router!

![](__GHOST_URL__/content/images/wordpress/2020/01/ddwrtarticle_piholefirewallrules-300x235.png)An additional setting can ensure that even devices with a DNS address hardcoded (I'm looking at you android phones and Chromecasts&#8230;) use the pihole.

Go to the Administration Tab > Commands and enter the commands and Firewall rules in the left image. Hit 'Run Commands' and 'Save Startup' when done.

    Commands =
    iptables -t nat -I PREROUTING -i br0 -p tcp --ddport 53 -j DNAT --to 192.168.1.101 =53
    iptables -t nat -I PREROUTING -i br0 -p udp --ddport 53 -j DNAT --to 192.168.1.101 =53
    iptables -t nat -I PREROUTING -i br0 -p tcp -s 192.168.1.101 =53 --dport 53 -j ACCEPT
    iptables -t nat -I PREROUTING -i br0 -p udp -s 192.168.1.101 =53 --dport 53 -j ACCEPT
    
    Firewall =
    #keep network on pi-hole
    iptables -t nat -I PREROUTING -i br0 -p tcp --ddport 53 -j DNAT --to 192.168.1.101 =53
    iptables -t nat -I PREROUTING -i br0 -p udp --ddport 53 -j DNAT --to 192.168.1.101 =53
    #punch DNS hole for pi-hole
    iptables -t nat -I PREROUTING -i br0 -p tcp -s 192.168.1.101 =53 --dport 53 -j ACCEPT
    iptables -t nat -I PREROUTING -i br0 -p udp -s 192.168.1.101 =53 --dport 53 -j ACCEPT

Once setup I logged into my pihole settings and went to the 'Conditional Forwarding' section. I typed in the IP Address of the router and the Domain Name I assigned to the router. This enables the pihole to resolve DNS queries by hostname instead of the default by IP Address.

## Takeaways and future thoughts =

**Unexpected problems =** Complicated setup with so-so documentation
**Future Concerns =** Future-proofing and updates will be fun
**Future Enhancements =** I expect much tinkering to ensue, I'm not even sure of all the capabilities

This project was almost completely done following the DD-WRT documentation and forums. All can be located here:[https//dd-wrt.com/](https//dd-wrt.com/)
