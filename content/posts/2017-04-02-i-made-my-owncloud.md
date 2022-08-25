+++
title = "I made my ownCloud!"
slug = "i-made-my-owncloud"
date = 2017-04-03
tags = ["diy", "https", "raspberry pi", "security"]
+++

![wp-1491187033641.jpg](https//mikehelmers.com/wp-content/uploads/2017/04/wp-1491187033641.jpg)Have you heard the saying, 'There Is No Cloud It's Just Someone Else's Computer'? And have you ever thought about what would happen if that person's computer disappeared overnight? While the chances of Google or Dropbox disappearing are slim, these things do happen. After my wife and I got married, we started discussing how we'll save all these digital photos from our wedding. We have them on a flash drive and on our Google Drive, but I wanted more control. It was time to build a Helmers Family Dropbox.

Why did I choose [ownCloud](https//owncloud.org/)? ownCloud is open source, to it is free and transparent. It has an app at the [Google Play Store](https//play.google.com/store/apps/details?id=com.owncloud.android/hl=en) so I can backup photos from my phone. I happen to like the interface. Finally, there is a lot of community support and needed to rely on their help.

For this project, I used a full-sized [Raspberry Pi 3](https//www.raspberrypi.org/products/raspberry-pi-3-model-b/). This model includes a built-in wifi card, 4 USB ports, HDMI port, and an ethernet jack. It also has a more powerful processor than the Raspberry Pi Zero, which is what I wanted. I also bought a 1TB Seagate External hard drive. This hard drive would be what our data would eventually be stored in.

Below I'll go through the steps of building my ownCloud.

1. Raspberry Pi Prep

&#8211;[Basic instructions are located here](https//www.raspberrypi.org/documentation/installation/installing-images/README.md)

2. Build a Webserver

-I'm essentially building a website that I can store pictures on. To build and access a website, I need a server.

3. Add SSL to Webserver

-I don't want people to be snooping and intercepting my data when I upload information, so I'm going to include a security certificate that created a secure message between my device (client) and ownCloud (server)

4. Install ownCloud

&#8211; ownCloud is an open source program that mimics Dropbox. I chose it because it has a mobile app for Android phones, and an easy to understand interface. There is also a ton of support on the web for any troubleshooting needs.

5. Prep and Mount hard drive

-The Raspberry Pi needs to know where to store my pictures, and the 16GB SD card is not enough space. I must point ownCloud towards the external hard drive.

6. Configure access to my phone, the internet, and sync data

-Time to make the device usable. Here I'll get the program up and running, and then sync it to my phone and start copying files over.

##### 1. Raspberry Pi Prep =

The easiest part. I used Jessie Lite with no GUI in order to save some space on the Pi and decrease its need for processing power. Once the Pi was setup, I ran apt-get update, to ensure all the package lists were current.

I also setup a static IP address for the Raspberry Pi on my local network. I went into my routers settings and used the DHCP Reservations feature. In this case, it was 192.168.1.143

##### 2. Build a Webserver =

The web server was the second easiest part. I ran the following commands =

    sudo apt-get install apache2
    sudo apt-get install php5 libapache2-mod-php5 -y
    sudo service apache2 restart

This installed an Apache webserver and PHP (a programming language used on the web). This forms the foundation of how I will access my ownCloud. To test that the web server was setup correctly, I navigated to my Pi's local IP address, 192.68.1.143. This brought up a default webpage.

##### 3. Add SSL to Webserver =

This step is all about enabling HTTPS. Our friends at [Sidewaysdictionary.com](https//sidewaysdictionary.com/#/term/https) explain it the best:'It’s like living in a glass house. With HTTP, you have to bear in mind everything is unencrypted and theoretically open for others to see. That’s fine for some activities but gets awkward with others. With HTTPS, you can draw the curtains and close the shutters.' This ensures that regardless of where in the world I'm accessing ownCloud, no one else can see my data.

Here we go =

First, I needed to create a folder to store the security certificate.

    sudo mkdir /etc/apache2/ssl

Then using openssl I generate a certificate and key.

    sudo openssl req -x509 -nodes -days 1095 -newkey rsa =2048 -out /etc/apache2/ssl/server.crt -keyout /etc/apache2/ssl/server.key
    nano /etc/apache2/sites-available/default-ssl.conf

After creating the key I replace the placeholder SSL Certificates (SSLCertificateFile /etc/ssl/certs/ssl-cert-snakeoil.pem and SSLCertificateKeyFile /etc/ssl/private/ssl-cert-snakeoil.key) in /etc/apache2/sites-available/default-ssl.conf with the keys I just created (SSLCertificateFile /etc/apache2/ssl/server.crt and

SSLCertificateKeyFile /etc/apache2/ssl/server.key).

Then I activate the encryption.

    sudo a2enmod ssl

And restarted Apache

    sudo service apache2 reload

Boom, I have a HTTPS site!

##### 4. Install ownCloud

I followed the instructions found on the [ownCloud website](https//download.owncloud.org/download/repositories/stable/owncloud/) =

    sudo wget -nv https//download.owncloud.org/download/repositories/stable/Debian_8.0/Release.key -O Release.key
    sudo apt-key add - < Release.key
    sudo sh -c "echo 'deb https//download.owncloud.org/download/repositories/stable/Debian_8.0/ /' > /etc/apt/sources.list.d/owncloud.list"
    sudo apt-get install owncloud

After ownCloud installed, I had to redirect the default Apache webpage to ownCloud. I completed this by editing lines within the '000-default.conf ' file. I entered =

    sudo nano /etc/apache2/sites-enabled/000-default.conf

Within the 000-default.conf file, I changed the DocumentRoot to /var/www/owncloud. This redirects any port 80 (HTTP) traffic on the Raspberry Pi from the Apache Default page to the ownCloud Default page.

Expand ownCloud ability to upload =

Now, I want to make sure ownCloud can upload any files I want it to. I edited the settings in a couple of files. ownCloud can upload files up to 2GB. These edits will allow me to do that.

    sudo nano /var/www/owncloud/.htaccess
    hp_value_upload_max_filesize 2000M
    php_value_post_max_size 2000M
    php_value_memory_limit 2000M
    
    sudo nano /var/www/owncloud/.user.ini
    upload_max_filesize=2000M
    post_max_size=2000M
    memory_limit=2000M

##### 5. Prep and Mount hard drive

This will allow ownCloud to store data

on my 1TB external drive. Why? The 16GB SD card within the Raspberry Pi is nowhere near large enough to store all of the files I want.

![wp-1490186169806.jpg](https//mikehelmers.com/wp-content/uploads/2017/03/wp-1490186169806.jpg)

I need to format the drive to NTFS. This is a format that Windows can read, so down the road I can view the contents of the drive on a Windows computer if needed. I need to install a formatting program and then format the drive.

    sudo apt-get install ntfs-3g

Then I formatted the drive to NTFS

    sudo mkfs.ntfs /dev/sda1 -f -v -I -L untitled

Next, I made a directory to mount the drive to, a permanent location ownCloud will always know to look.

    sudo mkdir /media/ownclouddrive

Now I needed the UUID. This is a unique identifier on my external drive. After updating some files, anytime the Raspberry Pi detects this UUID, it will connect it to the /media/ownclouddrive directory that we just made.

Detect the UUID with

    sudo blkid

Open the fstab file

    sudo nano /etc/fstab

Paste the following:UUID='UUID from blkid' /media/ownclouddrive auto nofail,uid=33,gid=33,umask=0027,dmask=0027,noatime 0 0

##### 6. Configure access to my phone, the internet, and sync data

Initial Setup:Now that ownCloud is up and running, it’s time to set it up! Through a web browser, navigate to the Pi’s local IP address. https//192.168.1.143 or https//192.168.1.143/owncloud. I received a certificate error message, but that is OK. I just clicked on it. That error shows up because your browser sees the certificate, but does not recognize it as trusted. But I built it, so I trust it.

The first action ownCloud will have you take is to create an admin account. Do that. Then select the storage & database option. Through that link, direct ownCloud to /media/ownclouddrive. This tells ownCloud to store data on your external hard drive.

Enable access from the outside world. I forwarded TCP port 443 (HTTPS) on my router to my Pi. This means that if I enter my external IP address and point it toward port 443 (XXX.XXX.XXX.XXX =443), I can access ownCloud from anywhere on Earth.

Download the app from your preferred app store, [Google](https//play.google.com/store/apps/details?id=com.owncloud.android/hl=en) or [IOS](https//itunes.apple.com/us/app/owncloud/id543672169?mt=8). After installing the app, it was straightforward to set it up.

You can also download [desktop clients](https//owncloud.com/download/), but I have not played around with that yet.

Take some time to dive into the literature at owncloud.org, as there is a ton of settings to tweak. You can even run your own email server or version of Google docs!

That’s it. Enjoy your “own” ownCloud!

##### Takeaways and future thoughts =

**Unexpected problems =**

I made so many mistakes. I constantly edited wrong files, mistyped commands&#8230; I eventually just wanted to start from scratch but wanted to overwrite what I have already edited. It took awhile, but I finally found the command to do that with =

    sudo -o Dpkg:=Options:=="--force-overwrite" apt-get install apache2

**Future Concerns =**

As always, what happens if my IP address changes? I need to find a permanent solution. I am also curious to know if I can really read the data on the external drive from a Windows machine. This is tricky to test, as I don't want to lose what I've already stored.

**Future Enhancements =**

I want to sync my already existing Google Drive and Photos with my new cloud. I will have to look into that in the future.

I received a much help from the authors of the following sites =

[https//pimylifeup.com/raspberry-pi-owncloud/](https//pimylifeup.com/raspberry-pi-owncloud/)

[https//projpi.com/diy-home-projects-with-a-raspberry-pi/pi-owncloud-drop-box-clone/](https//projpi.com/diy-home-projects-with-a-raspberry-pi/pi-owncloud-drop-box-clone/)
