+++
title = "How to Hack Censorship"
slug = "how-to-hack-censorship"
date = 2021-05-25
+++

## The Technology

Many employers use some type of web filtering technology. We've all come across this. You try to go to Youtube, only to receive a message "You have attempted to access a blocked website. Access to this website has been blocked for operational reasons", or similar.

Web filtering, Content-control software, web blocker, and my favorite, censorware. These are different names for essentially the same technology.

What does it do? Essentially, these pieces of software look at the URL (ex = helmers.io, netflix.com, google.com) that your computer/phone/IoT device is trying to reach, and compare the URL against a list. If that website is on a list that the filter admin doesn't want you visiting, you'll receive a message telling you so, or the site just won't load.

It's as simple as that.

A few of the larger companies that provide this service are =

- Blue Coat- Owned by Symantec

- Zscaler - I actually bought some of their stock, it's paid off

- Palo Alto - One of the larger Cybersecurity companies in America

A service I love that does this is the FOSS [Pi-hole](https =//pi-hole.net).

## The Situation

Why is this done? Lots of reasons. Security is a big one. Organizations will block known sites that host malware, or are prone to be spammy. This can prevent users from being phished, downloading malware, or being served ads.

Other times organizations feel that certain sites inhibit productivity. Streaming services, blogs, social media sites tend to fall into this category.

I, Mike Helmers, use a [pihole](__GHOST_URL__/ads-what-ads/) to block ads and third-party trackers on my network.

I strongly feel that from a security perspective, blocking known malware-ridden URLs is a good best practice. I also think it's important to block ads, and tracking services that you might not even know are on a webpage.

I have different feelings when it comes to blocking sites like Youtube. Is there a lot of time wasting on Youtube? Yes. But blocking a site like that also keeps a vast warehouse of knowledge from users hands. As an example, if I'm in the Army and want to learn how to setup an antenna, [Youtube has a video](https =//www.youtube.com/watch?v=WyEw0mycoYI) on how to to that. Why would you limit the tools that your employees have? Just one person's opinion.

## The Lists

Where do these lists come from? Most organizations do not have the time to create their own lists of questionable sites, or to classify sites according to their content. So where do they come from? There are two primary sources

### Community developed

Hobbyists and nerds across the Internet create hundreds of lists that show different trackers, advertisers, malware providers, etc... These list are often saved publicly to Github for others to use, or compiled on other websites.

Here's a few examples =

- [https =//avoidthehack.com/best-pihole-blocklists](https =//avoidthehack.com/best-pihole-blocklists)

- [https =//firebog.net/](https =//firebog.net/)

- [https =//github.com/topics/pihole-blocklists](https =//github.com/topics/pihole-blocklists)

### Company Built

Blue Coat, Palo Alto, Zscaler, and others have also developed their own lists. They even go a step further and will classify URLs. For example =

**Streaming Service** = Youtube, Netflix, Hulu
**Social** = Media Twitter, Myspace, Facebook
**News** = CNN, NPR, Reddit
**Blog** = Medium, Wordpress

It is these classifications that large organizations use in addition to blocking known malicious sites. This is how you are stopped from watching Netflix during the day.

## What to do

Now, how do you get around these services? There's a few options. I'm going to list a few, but I'm sure there's more.

### Whitelist

This is especially important for Pi-hole users. Occaisionally the Pi-hole will block things you don't want. Take a look at these lists to determine if this is for you.

[https =//github.com/anudeepND/whitelist](https =//github.com/anudeepND/whitelist)
[https =//discourse.pi-hole.net/t/commonly-whitelisted-domains/212](https =//discourse.pi-hole.net/t/commonly-whitelisted-domains/212)

#### Signal

There are a few whitelist that people suggest for certain services like Signal.

> signal.org
> www.signal.org
> updates2.signal.org
> textsecure-service-whispersystems.org
> giphy-proxy-production.whispersystems.org
> cdn.signal.org
> whispersystems-textsecure-attachments.s3-accelerate.amazonaws.com
> d83eunklitikj.cloudfront.net
> souqcdn.com
> cms.souqcdn.com
> api.directory.signal.org
> contentproxy.signal.org
> turn1.whispersystems.org

### Use your own device

This is really the simple solution. If you want to watch Netflix, use your own phone. Or wait till you get home. If you live in a country, like China, that censors broad swathes of the Internet, keep reading.

### VPN

I've talked about VPNs on this site before. They're great tools for circumventing censorship, and protecting your privacy. in the use case I've been talking about today, VPNs are best used on your own device that is connected to an untrusted network. Why your own device? Your organization probably won't let you install third party software onto your computer.

### Alternate Sites

Did you know that you can watch Youtube through other websites? Enter my favorite search engine = [DuckDuckGo](https =//duckduckgo.com)

Just follow these simple steps =

1. Go to [duckduckgo.com](https =//duckduckgo.com)
2. Search for a video a you want to watch
3. Click on the "Videos" search results
4. Select the video and watch through DuckDuckGo's video player

An added perk for this method, is Youtube can't track you through your browser.

### Infiltrate the Lists

So, this is a weirder one. Hypothetically, lets say I want to watch (for business reasons) my movie collection stored on my [Jellyfin](https =//jellyfin.org) server while at the office. But alas! For some reason MYDOMAIN.COM is flagged as a "Games" website! Fortunately the web filter told the category. I guess my self-hosted website is in a category that they don't want.

Do not panic. Here's a workaround. The lists that large companies use aren't perfect. They know this. So most list maintainers have the ability to test what a URL is classified as, and change that classification if it is erroneous.

So, I know what service my employer is using, so I can go to that provider, via the links below, and request a review. This was a super easy process, and MYDOMAIN.COM is no longer classified as "Games", but rather "Arts & Entertainment". Guess what, the employer doesn't block the "Arts & Entertainment" category.

Here are some of the bigger sites to test your URL and request a category change =

- [Z-Scaler](https =//sitereview.zscaler.com/)
- [Palo Alto](https =//urlfiltering.paloaltonetworks.com/)
- [Blue Coat Web Filter](http =//sitereview.bluecoat.com)

I hope this is educational and helpful to some of you. The Internet is a big and complicated place, that's why there are so many holes. Have fun, stay safe, and remember = If you don't own the equipment or the network, you're probably being watched.
