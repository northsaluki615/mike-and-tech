+++
title = "Better Graphics, More Power!!!"
slug = "better-graphics-more-power"
date = 2018-10-06
tags = ["computer", "graphics", "linux", "ubuntu", "upgrade"]
+++

Hello friends in tech! It's been awhile. But I'm back and ready to dive back in. I thought I would start with a small simple post that will play a big role in my computer.

Most computers today have what is called 'integrated graphics'. Or, graphics that are baked onto your CPU. This allows your system to let you do simple tasks like browse the Internet, play Minesweeper, or do basic office work. But what if you want to play GTA V? This is a modern game and your computer is not up to the task of rendering graphics quickly enough for the game to play well.

To solve this problem, I bought a graphics card.

A graphics processing unit (GPU), is a circuit board that plugs into my computers motherboard. This board has one job = Making graphics run smoother. The card I purchased, NVIDIA GP107 [GeForce GTX 1050 Ti], has it's own RAM, and was designed from the bottom up to optimize graphics output. This takes burden of quickly processing graphics off of my CPU, allowing the CPU to focus on other tasks, allowing a game to run smoother.

While the initial step of plugging the card into my motherboard was simple, getting the hardware to interface with Ubuntu was a bit trickier. After installing and rebooting the hardware I found that my computer detected the Graphics Card, but wasn't using it. I had to install NVIDIA drivers instead of using what came with the Linux Kernel.
As discussed in previous posts, drivers are what allows your operating system to interface with hardware. Most of the time Linux systems have these drivers already installed, allowing you to plug in anything and go crazy. This is not the case for several graphics cards. These are proprietary drivers that were written by NVIDIA, and their competitors, that contain code they don't wan their competition to have. Hence, it is not open-source, and not included in the Linux Kernel.

I searched out the drivers I needed and go to work.

**Steps =**

1. **Purge existing drivers**
2. **Add NVIDIA driver repository**
3. **Install Drivers**
4. **Configure drivers on the computer**

**1.  ****Purge existing drivers**** =**Use the following command =

>     sudo apt-get purge nvidia*

This removes all existing NVIDIA drivers. It's best to work with a clean slate.

**2. Add ****NVIDIA driver repository**
Use the following command =

>     sudo add-apt-repository ppa =graphics-drivers
>     sudo apt-get install ubuntu-drivers
>     sudo apt-get update

This tells Ubuntu to look at a location where graphics drivers are stored, and then the update refreshes what programs/drivers are available to your computer.

**3. Install Drivers =**
Use the following command to show what drivers are compatible with your system =

>     ubuntu-drivers devices

![](__GHOST_URL__/content/images/wordpress/2018/10/Screenshot-from-2018-10-04-22-05-19-300x138.png)

Out of that list, select the one for your GPU. I choose nvidia-driver-396 and installed it with =

>     sudo apt-get install nvidia-driver-396

**4. Configure Drivers on Computer =**

![](__GHOST_URL__/content/images/wordpress/2018/10/Screenshot-from-2018-10-04-22-07-26-300x201.png)

I had to go into Ubuntu's settings to make sure that my computer is using the correct graphics card. These setting are under **Software & Updates** under the **Additional Drivers** tab.

**Takeaways and future thoughts =**

**Unexpected problems =** The system defaulted to the nvidia-390 driver. This did not work. I switched to the nvidia-396 driver, rebooted the computer, and boom. I had fast graphics.
**Future Concerns =** The only real concern I have will appear when the PlayStation 5 is released. Do I upgrade my game console? Probably not. I think I'm a PC gamer going forward.
**Future Enhancements** = I will upgrade the card as needed, but this should be good for awhile.

There are other applications for graphics cards, beyond gaming. Mining cryptocurrency is the biggest. Because GPUs are designed to be pointed at a singe task, they are ideal for running the algorithms used to mine bitcoins. Maybe I'll try my had at this too&#8230;.

I received a much help from the authors of the following sites =

[linuxconfig.org](https =//linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux)
