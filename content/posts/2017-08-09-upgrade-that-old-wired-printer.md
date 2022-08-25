+++
title = "Upgrade that old wired printer"
slug = "upgrade-wired-printer"
date = 2017-08-09
tags = ["printer", "networking", "raspberry pi"]
+++

This is for my father, who has an old wired Brother Printer/copier.

Do you have a printer at home that works well, but you have to plug into it with a USB cable to print? Me too. My wife, Kristin, has a fantastic Brother printer from college. It's fast and quite the workhorse. But we often print from our phones, tablets, and in our house, non-windows machines. Using an open-source program called CUPs. This can be done on almost any machine, but I chose to use my Ubuntu-powered PC. There are some variations if you use Windows.

This is a smaller project, and pretty easy.

##### Install and setup CUPs

To begin, download and install CUPs on your computer.

    sudo apt-get install cups

Now it's time to set up CUPs

Navigate to CUP server at 127.0.0.1 =631 through a web browser.

Navigate to Administration Tab

Click 'Add a Printer'

Select your printer.

Fill out the fields and enable 'Share This Printer'. Click continue

Select your print driver (this could take a few attempts). In my case for the Brother HL2140, I chose Brother HL-2140 Foomatic/hl1250

##### Add to Google Cloud Print

Once it's tested open up the Google Chrome browser (or Chromium) and perform the following =

1. Navigate to chrome =//devices/ in the Omnibar.
2. Select 'Classic printer'
3. Add printers
4. Manage printers
5. Select the printer you want to add

Now that the printer is added, you can manage it at https =//www.google.com/cloudprint/. Here you can share the printer with anyone with a Google account.

##### Takeaways and future thoughts

**Unexpected problems =**

Finding the correct Print Driver was a pain. I had to dive pretty deep into the Internet to figure out what to use, but I eventually found it!

**Future Concerns =**

Nothing. Just need to make sure that my PC is powered on at all times when I want to print.

**Future Enhancements =**

CUPs is currently installed on my PC. I may move it to a Raspberry Pi at some point. This will decrease the power required to run the print server (the Pi uses less juice than myPC), and it will allow the printer to become wireless, meaning it can be moved anywhere in my home.
