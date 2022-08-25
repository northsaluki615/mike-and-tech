+++
title = "Mapping a Domain Name"
slug = "mapping-a-domain-name"
date = 2017-07-11
tags = ["raspberry pi", "networking"]
+++

I want to map my Domain name to my apartment's IP address. There are a couple reasons for this. First, I think it would be fun, and it is the first step to hosting a website 100% at home, so I only rely on my ISP to provide an Internet connection.

DNS serves as the phone book of the internet.

Lets say I want to visit Mike. So, I pull out a phone book. I look up Mike, and learn he lives at 123 Main St. Now I can visit him!

DNS works in a similar fashion. I want to visit Google. I type Google.com into my web browser, and thanks to DNS, my browser knows to go to Google's IP address! So, DNS connects a Domain to an IP Address.

Now, how can I send my domain, to my apartment's IP address? BTW, this whole posts assumes you are using a Debian-based Linux system and that Google is your Domain Registrar.

1. Buy a domain name
2. Setup DNS settings
3. Map to web server
4. Setup Dynamic DNS

##### 1. Buy a domain name

There are several registrars out there who you can purchase domains from. Godaddy is a large name in this industry, known for their ridiculous ads and poor treatment of women. I choose to go a more ethical route, and went with Google. This was easy enough, I started by going to [domains.google.com](https//domains.google.com) for the domains I wanted. In this case, [mikehelmers.com](https//mikehelmers.com) and [helmershomestead.org](https//helmershomestead.org). Each of these ran at $12 a pop. But you can get nearly any domain that's available. I entered my credit card info, bought my domains. Easy.

##### 2. Setup DNS settings

Now that I had my domains, I had to point them at my websites. Since WordPress is hosting mikehelmers.com, I need to set up that domain to use WordPress DNS servers. WordPress provided their server names, and most companies make it pretty easy. For helmershomestead.org, I kept it on the default Google provided DNS servers.

##### 3. Map to web server

For the WordPress hosted mikehelmers.com, I'm done. They'll take care of everything else. But for the soon to be self-hosted helmershomestead.org, there's still quite a bit more. Under the &#8216;Registered Hosts' part of the DNS Settings page, I added my IP address. I did this for both www.helmershomestead.org and helmershomestead.org because people might enter both URLs.

I also updated the Customer Resource records, the &#8216;A' records, the &#8216;TXT' record, and the &#8216;CNAME' record. The A Record is the primary method that a Domain maps to an IP address. The TXT Record is added because I have my sites connected to Keybase to verify that I own them. I'll write about Keybase at a later time. CNAME further helps with mapping subdomains (www) to the primary domain.

##### 4. Setup Dynamic DNS (Optional for most people)

One of the issues with mapping a domain name to your homes IP address is that it is not static, meaning that it can spontaneously change. Now, is that likely? No. But it can happen, and at some point, will happen. ISP's are loathe to give someone like me a static IP address and, generally speaking, home servers are frowned upon. But whatever, they're shady companies. To get around this issue I am going to use Dynamic DNS(DynDNS). This technology uses software to automatically check what a devices IP Address is, and then tell the DNS server what the IP address is. At domains.google.com go to the DNS settings for your domain name. Go to the &#8216;Synthetic Records' section of the page and select &#8216;Dynamic DNS' from the dropdown menu. This will generate the username and password that you will use after installing DDClient.

Next, install DDclient from the command line =

    sudo apt-get install ddclient

You will be asked some questions, fill them out the best you can, but it doesn't really matter. Once installation is complete open up the &#8216;ddclient.conf' file =

    sudo nano /etc/ddclient.conf

Overwrite the existing text with the following lines =

    protocol=dyndns2
    use=web
    server=domains.google.com
    ssl=yes
    login=Google_generated_username
    password=Google_generated_password
    whateveryourdomainis.com

Save and close the document and run the following command =

    sudo ddclient -verbose -foreground

This will let you know if ddclient has successfully updated Google's DNS servers with your external IP address.

There we go. now when I go to mikehelmers.com, is hosted by WordPress.com and helmershomestead.org independently in my apartment. Now if my public IP address changes for any reason, DDClient will check and update Google's DNS servers accordingly.

### **Takeaways and future thoughts**

**Unexpected problems =**

There was some hiccups with setting up the Dynamic DNS service, but it was because I mistyped some words.

**Future Concerns =**

Nothing

**Future Enhancements =**

Nothing at this time. This porject does exactly what I expected it to do.

I received a much help from the authors of the following sites =

[https//support.google.com/domains/answer/3251147](https//support.google.com/domains/answer/3251147)

 
