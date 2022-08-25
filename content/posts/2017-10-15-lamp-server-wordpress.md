+++
title = "Creating a LAMP Server for Wordpress"
slug = "lamp-server-wordpress"
date = 2017-10-15
tags = ["website", "networking", "raspberry pi"]
+++

I want to host a web server at home. Why do you ask? I say, Why not? This will be a fun project. Ultimately, I want a website for my family. A single location on the Internet where you can come and learn about the Helmers family. To do this, I am going to install a LAMP (Linux Apache MySQL PHP) server onto a Raspberry Pi.

I'm ultimately choosing Apache as the web server because it is so widely supported. There is a ton of knowledge about this program out there, and it's a bit more user-friendly than nginx, another popular web server (At least in my experience). Alright, let's get to it!

##### Steps to Follow =

1. Setup Raspberry Pi
2. Install needed applications except for WordPress
3. Setup MySQL
4. Install WordPress
5. Configure Apache
6. Configure WordPress

##### 1. Setup Raspberry Pi =

Along with the standard Raspbian Lite install, I also suggest installing ddclient for DynamicDNS. These programs are further explained in their own respective posts.

##### 2. Install needed applications =

Use the following command =

    sudo apt-get install apache2 php7.0 php7.0-curl php7.0-gd php7.0-imap php7.0-json php7.0-mcrypt php7.0-mysql php7.0-opcache php7.0-xmlrpc libapache2-mod-php7.0 mysql-server -y

While installing MySQL, you will need to create a password.

##### 3. Setup MySQL =

Now we will create a database where WordPress will store its data.

The username for MySQL is 'root'. Type =

    sudo mysql -uroot -p

Then enter the password you created during installation, and you will be in MySQL. Now create the database.

Create a database

    create database WordPress;

Create a dedicated user for the database. use &#8216;root' as the username.

GRANT ALL PRIVILEGES ON WordPress.* TO root@'localhost' IDENTIFIED BY &#8216;password’';

Exit MySQL by typing &#8216;exit'

##### 4. Install WordPress =

    sudo mkdir /var/www/html/wordpress
    cd /var/www/html/wordpress
    sudo rm *
    sudo wget http =//wordpress.org/latest.tar.gz

Then we will extract the content via the command “tar”.

    sudo tar xzf latest.tar.gz
    sudo mv wordpress/* .
    sudo rm -rf wordpress latest.tar.gz

A new folder will be created during the extraction, the “wordpress” folder. We also removed the now useless installation files.

##### 5. Configure Apache =

We will ensure that Apache has access to the file. To do this, run the following command =

    sudo chown -R www-data /var/www/html/wordpress

You'll need to enable Apache's rewrite mod =

    sudo a2enmod rewrite

You'll also need to tell the virtual host serving the site to allow requests to be overwritten.

Edit the Apache configuration file for your virtual host =

    sudo nano /etc/apache2/sites-available/000-default.conf

Make sure the top of the document looks like this =

    <VirtualHost * =80>
    <Directory "/var/www/html/wordpress">
    AllowOverride All
    </Directory>

All you have to do now is restart the Apache server with the following command =

    sudo service apache2 restart

##### 6. Configure WordPress =

First connection to WordPress on your Raspberry Pi

Walk through install steps that WordPress provides, it is pretty self-explanatory. When asked for database information, use the WordPress database created earlier, and user &#8216;Root' with the password you created.

Once you are done there, you have a functioning website!

Now, to make sure that the domain name you want to be attached to it is correct, Click 'Run Install'

Fill out the info as WordPress asks for it.

Go to Settings then Permalinks. This will make your site more user-friendly.

Select the Post name option and click Save Changes.

Make sure to update your DNS settings with your registrar and then go to the &#8216;Settings' tab on the left of your WordPress site. Update the &#8216;WordPress Address' and &#8216;Site Address' to reflect your domain name. This should allow you to access your site from the domain you created. In this case, [helmershomestead.org.](http =//helmershomestead.org)

##### Takeaways and future thoughts

**Unexpected problems =**

After running &#8216;sudo service apache2 restart' in step 5, I received the following error =

> Job for apache2.service failed because the control process exited with error code.
> 
> See 'systemctl status apache2.service' and 'journalctl -xe' for details.

I realized that on this Raspberry Pi I was running my PiHole on. This means that Port 80 (http) is beign used by the Lighttpd server that the PiHole is using. Using the command

grep -ri listen /etc/apache2

I was able to see what ports Apache was listening to. Sure enough, Port 80 was being heard. So, I went into the following files and changed them all to be listening to Port 8080. When the time comes, I will have my router forward any external Port 80 requests to Port 8080 on my Raspberry Pi.

I have not solved this issue yet. Having identified the problem, I can work towards a solution. In the meantime, I fired up another Pi to install WordPress on.

I also struggled with SSL not working. My original ambition was to have this page be encrypted, but it's taking a bit for me to figure out how to to add SSL to it.

**Future Concerns =**

I suppose my ISP could get irritated that I'm hosting my little webserver, but I'm not too worried. That's a bridge all cross when I come to it. My other concern is that my Raspberry Pi is too weak to really power my website. Time will tell on that one.

**Future Enhancements =**

I want to enhance the website and maybe someday move it to a better server. This is mostly just a fun project for me now. Here's a short list of what I would like to do to this page =

&#8211; Add SSL encryption

&#8211; Make a subdomain for NextCloud

I received a much help from the authors of the following sites =

https =//www.raspberrypi.org/learning/lamp-web-server-with-wordpress/
