+++
title = "Owning My Data:The Equipment"
slug = "owning-my-data-the-equipment"
date = 2019-01-18
tags = ["ownmydata", "raspberry pi", "selfhosted"]
+++

**This will be a quick post. Here is a list of equipment I have purchased to build out my network. This post includes a description of the equipment and why I purchased it.**

[**Ethernet Crimper & Cable Tester**](https//www.amazon.com/gp/product/B008UY5WL0/ref=ppx_yo_dt_b_asin_title_o07__o00_s00?ie=UTF8/psc=1) =
**What**:A tool to create my own Ethernet cables
**Why**:It can be cost effective to create your own cables. It also gives me some flexibility to create different sizes. The Cable Tester allows me to test cables before I install them. 
**Setting it up =** Crimping cables is super easy. I started making cables back in 2003 when I was in High School. 15 years later, the process hasn’t changed. There are several tutorials all over the web.

**Unmanaged and Managed Network Switch** =
**What**:Essentially a switch turns one Ethernet port into many
**Why**:A switch allows me to use ethernet wires to connect to many more devices than I could through a router alone. Wired connections are more stable and secure than wireless, so switches allow me to have a more consistent network connection.
**Setting it up =** Easy. These are essentially Plug and Play. The Unmanaged switch has some expanded capabilities, such as establishing VLANs, that I plan on playing with in the future.

**Powerline Ethernet Adapters** =
**What**:Allows me to use the copper powerlines running through my home as a wired network connection.
**Why**:This gives me the ability to have a wired network at home, avoiding the cost and effort of running Ethernet throughout my apartment. There is some signal degradation, so I do experience slower speeds than pure Cat5e cabling.
**Setting it up**:Easy. I plugged the adapters into power outlets near my equipment. I then [lugged my Cat5 cables into the adapters. Boom. Wired network.

**[Libre Computer Board ROC-RK3328-CC](https//libre.computer/products/boards/roc-rk3328-cc/)**[https//libre.computer/products/boards/roc-rk3328-cc/](https//libre.computer/products/boards/roc-rk3328-cc/)
**What**:A Raspberry Pi sized computer with 4GB of RAM, USB 3.0, and a Gigabit Ethernet Port
**Why**:I want to host my own version of Netflix at home. To make sure this was doable, I need something beefier than a Raspberry Pi. After some research, I decided on this board, but I do question this. I probably should have gone with the [ODROID-XU4](https//www.amazon.com/dp/B01MY6AHDC/?coliid=I10V77IZ2GUCXK/colid=2X5NJ1VE7U991/psc=0/ref_=lv_ov_lig_dp_it), it has fare better support. However, the Renegade board has been a learning experience that’s taught me far more about Linux than a well-supported board would. 
**Setting it up =** This was an interesting experience with several hiccups. I’m still learning the ins and outs of this computer. Essentially it’s the same as setting up Raspberry Pi. I burned an OS to an SD card. For the Renegade board, I had the option of using Ubuntu 18.04, Debian 9, or Armbian (Debian 9). I decided to use Armbian. It seemed to have the most support. After my first boot, I set up everything like I normally would.

**Issues Setting up Computer Libre Renegade =**

There was one problem that took me forever to figure out. This machine was not being issued an IPv4 address, only IPv6. After much tinkering, I discovered that the /etc/network/interfaces file kept being overwritten on reboot. Here’s what I did to fix it.

First I went into /etc/NetworkManager/NetworkManager.conf and made the following changes:

*managed=false*
 To
*managed=true*

And added the following lines =

*auto eth0
     allow-hotplug eth0
     # iface eth0 inet manual
     iface eth0 inet dhcp*

I rebooted and everything worked!

More equipment will be added over time, but for now here’s a list of what I have running =

- [Linksys WRT 1900ACS](https//www.linksys.com/us/p/P-WRT1900ACS/)
- [TP-Link 5 Port Gigabit Ethernet Network Switch](https//www.amazon.com/gp/product/B00A128S24/ref=ppx_yo_dt_b_asin_title_o01__o00_s00?ie=UTF8/psc=1﻿)
- [TP-Link 8-Port Gigabit Ethernet Easy Smart Switch | Unmanaged](https//www.amazon.com/gp/product/B00K4DS5KU/ref=ppx_yo_dt_b_asin_title_o01__o00_s00?ie=UTF8/psc=1﻿)
- [TP-Link AV600 Powerline Ethernet Adapter](https//www.amazon.com/gp/product/B00AWRUICG/ref=oh_aui_search_asin_title?ie=UTF8/psc=1)
- [Libre Computer Board ROC-RK3328-CC ](https//libre.computer/products/boards/roc-rk3328-cc/)
- x3 [Raspberry Pi 3 Model B+](https//www.raspberrypi.org/products/#buy-now-modal﻿)
- x2 [Raspberry Pi Zero](https//www.raspberrypi.org/products/#buy-now-modal﻿)
- [Ubuntu PC (Homebuilt)](https//tech.mikehelmers.com/i-built-a-pc/)&#8211; Currently, I'm running Ubuntu 18.10
