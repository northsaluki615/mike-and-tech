+++
date = 2023-04-04T05:57:32Z
description = "Hunting down URLs to make a blocklist"
draft = true
slug = "blocking-bytedance-and-tiktok"
title = "Creating a Blocklist from Scratch"

+++
# Creating a Blocklist from Scratch

# Finding URLs that are connected to an IP

## Find the primary IP of a URL

In this case, I'm looking into Bytedance's IP addresses. This is in reaction to the Federal/State governments decisions to start blocking anything tangentially related to TikTok. I begin by performing a simple *nslookup*
```
nslookup bytedance.com
Server:  CSWMAD0P4733.AD.DOT.STATE.WI.US
Address:  10.68.15.51

DNS request timed out.
    timeout was 2 seconds.
Non-authoritative answer:
Name:    bytedance.com
Addresses:  122.14.229.7
          122.14.229.102
```
This gives me 122.14.229.7 and 122.14.229.102.

## What other URLs are linked to these IP addresses?

I used a platform called [Netify](https://www.netify.ai/resources/applications/bytedance) to further research what domains are owned by Bytedance.
