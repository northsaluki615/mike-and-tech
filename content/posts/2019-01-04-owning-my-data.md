+++
title = "Owning my Data"
slug = "owning-my-data"
date = 2019-01-04
tags = ["ownmydata", "privacy", "selfhosted"]
+++

Hey there avid readers. Sorry for the delay, and welcome to 2019! Here you go.

For the last few months, I’ve focused on consolidating the devices on my network.  It is time to give purpose to the projects I've worked on. I have also been studying up for some CompTIA certifications, but that’s another post. Let's get to this project.

I want to host more of the data that I own at home. I want this for several reasons. Did you know you don’t really “own” a digital copy of a movie you bought from Google? Or that e-book you purchased from Amazon or Barnes and Nobles? The way we buy digital copies of things is much more like leasing a car rather than buying a car. You only have access to that Movie from Google or Amazon as long as they want you to.  Now, is it likely Google is going to shut down in the near future? No. But it can happen. In 2016 Barnes and Nobles decision to stop supporting the Nooks in the United Kingdom. Here’s the [link for that article](https//help.barnesandnoble.com/app/answers/detail/a_id/3481/~/changes-to-nook-in-the-uk). If you didn’t take action to secure your Nook books before a certain date, you would lose them. That’s not real ownership. That’s not even that you can’t easily share digital books and movies like a physical copy. Despite owning it! Often any type of sharing is against their terms of service, if not illegal.

It would be nice to have access to my books, movies, music, photos, and more without having to rely on someone else.

This will not be a typical post, as it is much more of an outline for me to follow. This page is a home for this project that will be continuously updated.
**
Steps to Follow =**
Establish what projects I want to have running
Map out my network
Acquire appropriate hardware
Build out sub-projects
Establish access for software

**1. Establish what projects I want to have running =**

Here’s a short list of what I want to run on my network

Pihole&#8211; Ad blocking DNS and DHCP server for my home
OpenVPN- To access my network safely and securely
Emby&#8211; Self-hosted version of Netlix
Calibre&#8211; Self-hosted ebook server and library
Rocket.Chat- A private chat and communication service, similar to Slack
Bit Torrent Box- A place to download files and give back to the community
Nextcloud&#8211; A place to store passwords, contacts, calendars, and more
Piwigo- A place to share pictures and photos
Ampache&#8211; For music
Nginx- To serve as a Reverse-Proxy to access my server from the web and provide HTTPS support
Docker- A program that will allow me to host services without breaking too much
A testing environment

**2. Map out my network =**

All of these devices have to be physically placed around my home. I don’t have space in any one location, so I need to map out where my servers and computers will be located, along with a logical map of how traffic will flow across my network.

**3. Acquire appropriate hardware =**

My router only has 4 ethernet ports on it. That’s not enough. I will need to invest in a Switch. I also want something more powerful than a Raspberry Pi to handle streaming video. I also will invest in ethernet cables and a pair of crimpers to terminate my own cables.

**4. Establish external access for software**

I will need to take time to configure NGINX and SSL certificates to access my network over the internet. This will be an ongoing project that I will work on with each completed sub-project.
**
1. Build out sub-projects =** This will be a growing list of completed projects

**Takeaways and future thoughts =**
Unexpected problems:There will be many
Future Concerns:Future-proofing and updates will be fun
Future Enhancements:I expect much tinkering to follow
