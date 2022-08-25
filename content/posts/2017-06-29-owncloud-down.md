+++
title = "ownCloud Down!!!"
slug = "owncloud-down"
date = 2017-06-29
tags = ["raspberry pi"]
+++

The other day I was updating the Raspberry Pi, and some updates got pushed out to the Pi running ownCloud. And it broke&#8230; Apparently, ownCloud itself was updated, but the update pushed the application into Maintenance Mode. I had to fix it. 

Went to /var/www/owncloud/config/config.php and changed &#8216;maintenance' ==> true, to  &#8216;maintenance' ==> false, and then returned to the ownCloud login page. Fortunately for me, from there it was easy. ownCloud asked if I wanted to install the update, and I said yes. Next thing you know, I was up and running.

That's one of the cool things about these projects, new issues keep coming up. It's good to always have an opportunity to try something new practice my troubleshooting skills.
