# Crawled Documentation


## Integrations - Home Assistant

Source: https://www.home-assistant.io/integrations

All
Featured
Partners
### Category
All3D printingAIAlarmAlarm Control PanelAutomationBackupBinary sensorButtonCalendarCameraCarClimateCoverDateDate/TimeDevice automationDevice trackerDIYDoorbellDownloadingEnergyEnvironmentEventFanFinanceFront endGeolocationHealthHelperHistoryHubHumidifierImageImage processingIntentIrrigationLawn mowerLightLockMailboxMedia playerMedia sourceMultimediaNetworkNotificationsNotifyNumberOrganizationPlugPostal ServicePresence detectionPumpRemoteSceneSelectSensorSirenSocialSpeech-to-textSwitchSystem monitorTag scannerTextText-to-speechTimeTo-do listTransportUpdateUtilityVacuumValveVoiceWater heaterWater managementWeatherOther
### Version
All2025.122025.112025.102025.92025.82025.72025.62025.52025.42025.32025.22025.12024.122024.112024.102024.92024.82024.72024.62024.52024.42024.32024.22024.12023.122023.112023.102023.92023.82023.72023.62023.52023.42023.32023.22023.12022.122022.112022.102022.92022.82022.72022.62022.52022.42022.32022.22021.122021.112021.102021.92021.82021.72021.62021.52021.42021.32021.22020.120.1180.1170.1160.1150.1140.1130.1120.1110.1100.1090.1080.1070.1060.1050.1040.1030.1020.1010.1000.990.980.970.960.950.940.930.920.910.900.890.880.870.860.850.840.830.820.810.800.790.780.770.760.750.740.730.720.710.700.690.680.670.660.650.640.630.620.610.600.590.580.570.560.550.540.530.520.510.500.490.480.470.450.440.430.420.410.400.390.380.370.360.350.340.330.320.310.300.290.280.270.260.250.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.90.80.7.60.7.50.7.40.7.30.7.20.70.0
### IoT Class
AllLocal PushLocal PollingCloud PushCloud PollingAssumed StateCalculatedConfigurable
### Quality Scale
All 🏆 Platinum 🥇 Gold 🥈 Silver 🥉 Bronze 🏠 Internal 💾 Legacy
brands: featured 



## Documentation - Home Assistant

Source: https://www.home-assistant.io/docs/

The documentation covers beginner to advanced topics around the installation, setup, configuration, and usage of Home Assistant.
To see what Home Assistant can do, take a look at the . 
#  Documentation



## Understanding Home Energy Management - Home Assistant

Source: https://www.home-assistant.io/docs/energy/

#  On this page
Home Assistant allows you to get on top of your energy use with its home energy management feature. Gain new insights, optimize your solar panel production, plan energy usage and save money.
Home energy management works with three different types of information sources. You can start using it even if you just have one source connected to Home Assistant. Every source you add will complement the other sources, giving you even more insight into energy in your home.
Home Assistant is an open platform and so home energy management is not restricted to specific hardware. Any energy monitoring hardware that integrates with Home Assistant can be used as a data source. Check out the following sections for in-depth explanations and hardware recommendations.
If you have a sensor that returns instantaneous power readings (W or kW), then to add a sensor that returns energy usage or generation (kWh), refer to the .
You can also configure power sensors alongside energy sensors in the Energy dashboard. Power inputs accept sensors with state_class: measurement and appropriate units (for example W or kW).
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Configuration.yaml - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/

#  On this page
While you can configure most of Home Assistant from the user interface, for some integrations, you need to edit the configuration.yaml file.
This file contains integrationsIntegrations connect and integrate Home Assistant with your devices, services, and more. [Learn more] to be loaded along with their configurations. Throughout the documentation, you will find snippets that you can add to your configuration file to enable specific functionality.
Example of a configuration.yaml file, accessed using the File editor add-on on a Home Assistant Operating System installation. 
## Editing configuration.yaml 
How you edit your configuration.yaml file depends on your editor preferences and the you used to set up Home Assistant. Follow these steps:
  1. .
  2. .
  3. .
  4. Save your changes and to apply the changes.


### To set up access to the files and prepare an editor 
Before you can edit a file, you need to know how to access files in Home Assistant and setup an editor. File access depends on your . If you use Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users., you can use editor add-ons, for example. If you use Home Assistant ContainerHome Assistant Container is a standalone container-based installation of Home Assistant Core. Any OCI compatible runtime can be used, but the documentation focus is on Docker. [Learn more], add-ons are not available.
To set up file access on the Home Assistant Operating System, follow these steps:
  * If you are unsure which option to choose, install the . 
    * Alternatively, use the . This editor offers live syntax checking and auto-fill of various Home Assistant entities. But it looks more complex than the file editor.
    * If you prefer to use a file editor on your computer, use the .


### To find the configuration directory 
  1. To look up the path to your configuration directory, go to .
     * Select the three dots menu and select System information.
  2. Find out the location of the Configuration directory.
     * Unless you changed the file structure, the default is as follows: - 
       * Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users.: the configuration.yaml is in the /config folder of the installation.
       * Home Assistant ContainerHome Assistant Container is a standalone container-based installation of Home Assistant Core. Any OCI compatible runtime can be used, but the documentation focus is on Docker. [Learn more]: the configuration.yaml is in the config folder that you mounted in your container.


### To edit the configuration file 
Once you have located the config folder, you can edit your configuration.yaml file. How you edit the file depends on the editor you set up in step 1:
  * If you are using the File editor add-on: Open the add-on, navigate to the /config folder in the file browser on the left, and select the configuration.yaml file to open it in the editor.
  * If you are using the Studio Code Server add-on: Open the add-on, use the file explorer on the left to navigate to the configuration.yaml file, and select it to open in the editor.
  * If you are using Samba to access files: Navigate to the shared folder on your computer, locate the configuration.yaml file, and open it with your favorite text editor like or .


Note
If you have watched any videos about setting up Home Assistant using configuration.yaml (particularly ones that are old), you might notice your default configuration file is much smaller than what the videos show. Don’t be concerned, you haven’t done anything wrong. Many items in the default configuration files shown in those old videos are now included in the default_config: line that you see in your configuration file. Refer to the for more information on what’s included in that line.
## Validating the configuration 
After changing configuration or automation files, you can check if the configuration is valid. A configuration check is also applied automatically when you reload the configuration or when you restart Home Assistant.
The method for running a configuration check depends on your . Check the common tasks for your installation type:


## Reloading the configuration to apply changes 
For configuration changes to become effective, the configuration must be reloaded. Most integrations in Home Assistant (that do not interact with devicesA device is a model representing a physical or logical unit that contains entities. or servicesThe term “service” in Home Assistant is used in the sense of an information service. For example, the municipal waste management service that provides entities for organic, paper, and packaging waste. In terms of functionality, the information service is like a device. It is called service to avoid confusion, as it does not come with a piece of hardware.) can reload changes made to their configuration in configuration.yaml without needing to restart Home Assistant.
  1. Under Settings, select the three dots menu (top right) , select Restart Home Assistant > Quick reload.
  2. If you find that your changes were not applied, you need to restart.
     * Select Restart Home Assistant.
     * Note: This interrupts automations and scripts.


## Troubleshooting the configuration 
If you run into trouble while configuring Home Assistant, refer to the .
## Related topics 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Automating Home Assistant - Home Assistant

Source: https://www.home-assistant.io/docs/automation/

#  On this page


Home Assistant contains information about all your devicesA device is a model representing a physical or logical unit that contains entities. and servicesThe term “service” in Home Assistant is used in the sense of an information service. For example, the municipal waste management service that provides entities for organic, paper, and packaging waste. In terms of functionality, the information service is like a device. It is called service to avoid confusion, as it does not come with a piece of hardware.. This information is available for the user in the dashboard and it can be used to trigger automationsAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more]. And that’s fun!
Automations in Home Assistant allow you to automatically respond to things that happen. You can turn the lights on at sunset or pause the music when you receive a call.
If you are just starting out, we recommend that you start with blueprint automations. These are ready-made automations by the community that you only need to configure.
### 
If you have got the hang of blueprints and would like to explore more, it’s time for the next step. But before you start creating automations, you will need to learn about the automation basics.
### 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Grouping your assets - Home Assistant

Source: https://www.home-assistant.io/docs/organizing/

#  On this page
Once you have more devices, you may want to target entire groups of devices in automations. It also becomes more challenging to find items in lists.
There are a few tools to group your assets: , , , and .
Taxonomy | Automation target | Entity can have multiple  
---|---|---  
Area  
Floor  
Label  
Category  
Group Integration  
## Area 
## Floor 
## Labels 
  * Can be assigned to areas, devices, entities, automations, scenes, scripts, and helpers.
  * Can be used in automations and scripts as a target for actions.
  * Labels can also be used to filter data in tables. For example, you can filter the list of devices to show only devices with the label heavy energy usage or turn these devices off when there is not a lot of solar energy available.


## Category 
  * Groups items in a table.
  * Categories are unique for each table. The automations page can have different categories than the scene, scripts, or helpers settings page.


## Group Integration 
## Related topics 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Installation - Home Assistant

Source: https://www.home-assistant.io/installation/

#  On this page
The first step to getting started with Home Assistant is to install it on a device. There are many ways to run it for all kinds of scenarios and all kinds of skill levels. 
Easiest 
## Plug and play with Home Assistant Green 
The affordable Home Assistant Green is the easiest way to start using Home Assistant. It's plug-and-play and comes with already installed. 
### Home Assistant Green 
The easiest way to get started with Home Assistant
SKILLS REQUIRED 
  * Interest in setting up a smart home


TOOLS REQUIRED 
  * Ethernet connection


Easy 
## DIY with Raspberry Pi 
Raspberry Pi, a mini low-cost computer, is one of the most popular platforms for running Home Assistant. If you want to learn how to DIY, this is a good way to start and gain experience. 
### Install Home Assistant on Raspberry Pi 
A low-cost DIY solution to get started with Home Assistant
SKILLS REQUIRED 
  * Assembling a Raspberry Pi setup
  * Flashing a Raspberry Pi


TOOLS REQUIRED 
  * Raspberry Pi 4 or 5 with power supply (minimum 2 GB RAM)
  * MicroSD card
  * Ethernet connection


## About installation types 
Home Assistant offers two different installation types. Home Assistant Operating System is the recommended installation type. 
  * Home Assistant Operating System: An embedded, minimalistic operating system designed to run the Home Assistant ecosystem on single board computers (like the Home Assistant Green or a Raspberry Pi) or Virtual Machines. It is the most convenient option in terms of installation and maintenance and it supports add-onsAdd-ons are additional standalone third-party software packages that can be installed on Home Assistant OS. [Learn more]. Home Assistant Operating System is the recommended installation type for most users.
  * Home Assistant Container: Container-based installation of Home Assistant. You need to bring your own system (such as Linux) with container orchestration (like Docker), and manually handle updates. Home Assistant Container installations don’t have access to add-onsAdd-ons are additional standalone third-party software packages that can be installed on Home Assistant OS. [Learn more]. 
    * Note: Some integrations, such as Thread and Z-Wave, are controlled by add-onsAdd-ons are additional standalone third-party software packages that can be installed on Home Assistant OS. [Learn more]. There is no out-of-the-box support for these on Container installations. 


HA OS1  | Container1   
---|---  
One-click updates   
1: Names are abbreviated. The full names of the installation types are: Home Assistant Operating System Home Assistant Container 
Intermediate 
## Extend with Home Assistant Yellow 
The extensible Home Assistant Yellow comes with all the ingredients you need to help you build a robust smart home. All you need to do is to bring your own Raspberry Pi Compute Module. 
### Home Assistant Yellow 
The powerful way to run Home Assistant
SKILLS REQUIRED 
  * You're comfortable following instructions on:
  * Installing a compute module and a heat sink
  * Flashing a Raspberry Pi


TOOLS REQUIRED 
Hard 
## Install on other hardware 
Home Assistant can be repurposed and installed on various hardware, such as an Odroid or a generic x86-64 machine. The Home Assistant Operating System allows you to install Home Assistant on these devices even if you have little to no Linux experience. 
### Install Home Assistant on Odroid devices 
A more powerful alternative to Raspberry Pi
SKILLS REQUIRED 
  * You're comfortable following instructions on:
  * Writing boot images
  * Installing an SD card or eMMC


TOOLS REQUIRED 
  * An Odroid device
  * MicroSD card or eMMC
  * Ethernet connection


### Install Home Assistant on x86-64 machines 
Repurpose workstation hardware to run Home Assistant
SKILLS REQUIRED 
  * You can use a command line and install a boot medium on your hardware
  * You're comfortable configuring the BIOS based on instructions.


TOOLS REQUIRED 
Expert 
### Install Home Assistant variants on Raspberry Pi 
A low-cost DIY solution to get started with Home Assistant
SKILLS REQUIRED 
TOOLS REQUIRED 
  * Raspberry Pi 3, 4 or 5 with power supply
  * MicroSD card
  * Ethernet connection


### Install Home Assistant on Linux 
Use Home Assistant OS, Container
SKILLS REQUIRED 
  * Advanced knowledge of Linux
  * Using Linux command line
  * Using Docker Compose (for HA Container)


TOOLS REQUIRED 
  * Machine with Linux installed


### Install Home Assistant on macOS 
Use Home Assistant OS on a VM
SKILLS REQUIRED 
  * Advanced knowledge of macOS
  * Using macOS command line


TOOLS REQUIRED 
  * Machine with macOS installed


### Install Home Assistant on Windows 
Use Home Assistant OS on a VM
SKILLS REQUIRED 
  * Know how to find an IP address on your router
  * Advanced knowledge of Windows
  * Using Linux command line


TOOLS REQUIRED 
  * Machine with Windows installed
  * VirtualBox (for VM)


### Install Home Assistant on other systems 
Use Home Assistant on virtual machines, NAS, and more
SKILLS REQUIRED 
  * Know how to find an IP address on your router
  * Advanced knowledge of Windows
  * Using Linux command line


TOOLS REQUIRED 
  * Machine with Windows installed
  * VirtualBox (for VM)


### Deprecated installation types 
Home Assistant used to offer two additional installation types for advanced users: Home Assistant CoreHome Assistant Core is the Python program at the heart of Home Assistant. It is part of all installation types. It can be installed standalone (without Home Assistant Supervisor) as a container using Docker (this is typically referred to as the Home Assistant Container installation type). For development, Core can also be run using a Virtual Environment (previously referred as the Home Assistant Core installation type). For production setup, the Home Assistant Core installation type is deprecated. and Home Assistant SupervisedThe Home Assistant Supervised installation type is a full UI managed home automation ecosystem that runs the Home Assistant Core program, the Home Assistant Supervisor and add-ons. It comes pre-installed on Home Assistant OS, but can be installed standalone on Debian Linux systems. It leverages Docker, which is managed by the Home Assistant Supervisor. The Home Assistant Supervised installation type is deprecated.. These two methods are now . 
  * Home Assistant Supervised: Manual installation of the Supervisor. 
  * Home Assistant Core: Manual installation using Python virtual environment. 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Getting started
#  On this page



## Deprecating Core and Supervised installation methods, and 32-bit systems - Home Assistant

Source: https://www.home-assistant.io/blog/2025/05/22/deprecating-core-and-supervised-installation-methods-and-32-bit-systems/

#  On this page
We are today officially deprecating two installation methods and three legacy CPU architectures. We always strive to have Home Assistant run on almost anything, but sometimes we must make difficult decisions to keep the project moving forward. Though these changes will only affect a small percentage of Home Assistant users, we want to do everything in our power to make this easy for those who may need to migrate.
Beginning with Home Assistant 2025.6, affected systems will display a notification after updating, indicating that support will end in six months (with release 2025.12) and include a recommendation to . In this post, we’ll go into our thinking on these deprecations and our findings after consulting the community on these changes.
We have deprecated the following installation methods:
  * Home Assistant Core installation method, where you run your system in a Python environment, not to be confused with Container (for example, running your system in Docker).
  * Home Assistant’s Supervised installation method, which involves running your own operating system, then installing the Supervisor and other requirements on top of that.


These are advanced installation methods, with only a small percentage of the community opting to use them. If you are using these methods, you can continue to do so (you can even continue to update your system), but in six months time, you will no longer be supported, which I’ll explain the impacts of in the next section. References to these installation methods will be removed from our documentation after our next release (2025.6). Going forward and will become the only supported installation methods.
In the future, only the currently supported 64-bit architectures (aarch64 and amd64) will be used. The following legacy architectures are being deprecated:
  * i386 (32-bit x86) is an architecture used by Intel and AMD predominantly before 2003, but some later processors still utilized it (e.g., early Intel Atom models).
  * armhf (32-bit ARM hard-float) was used by very early single-board computers, notably the original Raspberry Pi.
  * armv7 (32-bit ARM) was used by a number of early single-board computers, most notably the Raspberry Pi 2.


If you are one of the few with a system using these architectures, you will receive a notification after updating to 2025.6, and it will describe how to migrate your system. In six months, your system will become unsupported and will no longer receive updates.
## What does deprecated and unsupported mean 
In the simplest terms, deprecation is where you stop recommending a certain feature to users as you intend to remove it soon. As we deprecated the Core and Supervised installations methods today, that means we are now working to remove all references to them from our documentation. The goal is to guide new users towards installation methods we plan to support long term, and discourage the use of those that are being phased out.
Even though they are being deprecated, we are committing to support them for a further six months (until release 2025.12), giving existing users time to migrate to Home Assistant OS or Container. During this time we will ensure these installation types keep functioning as normal during the deprecation period. However, after those six months have elapsed, these methods will become unsupported, which means issue reports will no longer be accepted. As these installation methods are used for the development of Home Assistant, it will still be technically possible to update them. We still would recommend migrating to a supported method, but that’s your choice.
As i386, armhf, and armv7 architectures have also been deprecated, we are currently removing references to them from our documentation. More importantly, they will also be subject to a six-month support window. After that support ends (from release 2025.12 onwards), we will no longer build or release distributions or containers targeting these platforms. This will mean that in six months’ time, there will be no more updates for these systems, and if users encounter issues, they will no longer be able to ask for support from Home Assistant maintainers.
## Why we made this decision 
### Core and Supervised 
From our 
The Core and Supervised installation methods are not only complex for users to install and maintain — they’re also challenging for the Home Assistant team to support. In the past, there were compelling reasons, outside Home Assistant development, to run these installation methods, but for most people those reasons are disappearing. Home Assistant OS is very capable with a rich ecosystem of add-ons, while also being easy to run in a virtual machine. Container adoption has become mainstream, now being widely available along with systems having more resources to run them. Steadily, we’ve seen year-on-year reductions in the percentage of Core and Supervised installations (currently standing at 2.5% and 3.3% respectively).
As Core and Supervised are more complex to maintain, they generate more issues that are more difficult to solve. This complexity places a disproportionate burden on our community-driven support system, where volunteers generously give their time to help others. It also takes time away from assisting the vast majority of users who are on the simpler to maintain installation methods. Along with this, new users could sometimes be swayed into running Core or Supervised, and have a bad experience that could cause them to give up on the best way to automate their home. By focusing our support and documentation on OS and Container methods, we can greatly improve the onboarding experience and ensure a smoother start for new users.
### Legacy 32-bit architectures 
Though Home Assistant is very lean and can run great on older or low-spec hardware, the architectures we’re deprecating are definitely on the leaner side of the spectrum. That probably explains why we see such low usage figures, with i386 and armhf architectures representing less than 0.5% of installations each, and armv7 at only 0.95% of installations. More than half of Home Assistant systems using armv7 have hardware that is capable of running 64-bit operating systems, like Raspberry Pi 3 and 4. This hardware can actually upgrade and migrate to a supported 64-bit version of our Home Assistant Operating System
The broader software and hardware industries have also shifted away from these older 32-bit systems. Most have adopted 64-bit architectures such as amd64 and aarch64, and we are seeing more projects we depend on no longer supporting these 32-bit architectures. There have already been several instances where keeping support for these architectures has held back the development of new features.
## Your feedback 
For any major change, it is our goal to make sure the community guides this decision-making. When our maintainers initially proposed these deprecations, we shared this plan with the community (in our forum, GitHub, Discord, Reddit, and other social channels), using it to gather feedback. It was a constructive, civil discussion, and we learned a couple of interesting things that have helped us move this decision forward.
First, our current wording is confusing to the community. Core and Supervisor are components of Home Assistant OS, but are also similar—or the same—as the names of installation methods, which is not super clear for new users. We also found these installation methods being used in ways we never expected, and there are a good number of people who were already running Home Assistant in custom and unsupported ways, not even realizing they were unsupported.
Many of those impacted asked for better guidance on how to migrate. A good number were unaware of our expansion of backup and restore features to all installation methods, significantly smoothing their transition to a new platform.
## Check if you’re affected 
The blue arrow shows your installation type, and the red arrow displays the architecture.
If you are unsure which installation method you are running:
  * Select OR Navigate to Settings > System > Repairs, select the three-dotted menu in the top right corner, and select System information.
  * Check the Installation type field. If you are running Home Assistant OS, or Container, you are fine as the installation method deprecation doesn’t apply to you.


In this , you can find the architecture as well:
  * The CPU architecture field will tell you exactly which architecture you are using. If you are seeing aarch64 or x86_64 here, you are fine as the architecture deprecation doesn’t apply to you.


## How to migrate 
Green are staying, and red are deprecated.
If it’s been a while since you’ve migrated Home Assistant systems, a lot has improved over the past several years. Switching systems is as easy as , downloading it, and it during the initialization of your new system (Home Assistant Cloud subscribers using off-site backups can restore ). Every Home Assistant installation method now has backups, and you can restore backups from any method onto another regardless of the differences in architecture. In many cases, very little needs to be done once the restore is successful (). Our documentation has a full list of guides on .
Before you think about migrating to a different installation method, you can always choose to stick with what you have. Just because it becomes unsupported by the Home Assistant project, it doesn’t mean you can’t keep running it like you do today. That choice is up to you.
Need | Currently using | Migrate to  
---|---|---  
Home Assistant with add-ons | Supervised | Home Assistant OS  
A system without Home Assistant OS support | Supervised | Container (many add-ons can be run as containers alongside Home Assistant)  
Full control of the host system | Supervised | Run Home Assistant OS in a VM, or Container (alongside add-on containers)  
Lightweight solution | Core | Container  
For Home Assistant Core users, the closest alternative is Home Assistant Container, which is most commonly used with Docker. If you can dedicate a device exclusively to Home Assistant, the recommended installation method is Home Assistant OS, which gives an appliance-like setup.
For Home Assistant Supervised users, we recommend migrating to Home Assistant OS—it supports everything Supervised does, including add-ons. If you want more control over the OS, you can also run Home Assistant OS in a virtual machine, like with Proxmox, or go the Home Assistant Container path alternatively.
For deprecated architectures, there is generally no supported migration path using your existing hardware. You will therefore need to find alternative hardware compatible with Home Assistant OS or Container. Second-hand single-board computers and recycled small-form-factor office machines are affordable and sustainable options. In some cases, your system may be running a 32-bit operating system, but is capable of running a 64-bit one (Raspberry Pi 3 and 4 are examples of systems often running a 32-bit OS despite being capable of running 64-bit). In this case, you will need to install a 64-bit capable operating system and restore Home Assistant on that system.
## Frequently asked questions 
#  Share this post
#  Recent Posts
#  On this page



## Alternative - Home Assistant

Source: https://www.home-assistant.io/installation/alternative

#  On this page
## Install Home Assistant Operating System 
### Download the appropriate image 
  * (.vdi)
  * (.qcow2)
  * (.ova)


After downloading, decompress the image. If the image comes in a ZIP file, for example, unzip it.
Follow this guide if you already are running a supported virtual machine hypervisor. If you are not familiar with virtual machines, install Home Assistant OS directly on a , a , or an .
### Create the virtual machine 
Load the appliance image into your virtual machine hypervisor. (Note: You are free to assign as much resources as you wish to the VM, please assign enough based on your add-on needs).
Minimum recommended assignments:
  * 2 GB RAM
  * 32 GB Storage
  * 2vCPU


All these can be extended if your usage calls for more resources.
### Hypervisor specific configuration 
VirtualBox
Unraid
KVM (virt-manager)
KVM (virt-install)
VMware ESXi/vSphere
  1. Create a new virtual machine.
  2. Select type Linux, subtype Oracle Linux and version Oracle Linux (64-bit) or Oracle Linux (ARM 64-bit) depending on your hardware.
  3. Under Hardware, select the amount of memory and number of CPUs. Then, select Enable EFI. 
     * Make sure EFI is enabled. If EFI is not enabled, HAOS won’t boot.
  4. Under Hard Disk, select Use an existing virtual hard disk file, select the unzipped VDI file from above.
  5. Then go to Network > Adapter 1. Choose Bridged Adapter and choose your network adapter (i.e. en0:Wi-Fi).
  6. Then go to Audio and choose Intel HD Audio as audio controller.


By default, VirtualBox does not free up unused disk space. To automatically shrink the vdi disk image the discard option must be enabled using your host machine’s terminal:
```
VBoxManage storageattach <VM name> --storagectl "SATA" --port 0 --device 0 --nonrotational on --discard on

```

More details can be found about the command can be found .
  1. Download the .qcow2 image above and decompress it. (Extract all in Windows)
  2. Store the image in the isos share on your server.
  3. Make sure under Settings > VM manager, Enable VMs is enabled.
  4. Create a new virtual machine: VMS > Add VM.
  5. Select type Linux and give the VM a name and a description.
  6. Select the CPU cores you want to let the VM use and give it some memory.
  7. Under Primary vDisk Location, select Manual and then select the qcow2 image.
  8. Select your keyboard language under VM Console Keyboard.
  9. Select br0 under Network Source.
  10. Select virtio under Network model.
  11. Select any USB-devices that you want to pass through to Home Assistant, such as Zigbee- or Z-Wave controllers.
  12. Deselect Start VM after creation.
  13. Select Create.
  14. Select the name of your new VM and select the capacity number for your disk. Here, you can expand the disk to whatever your needs are. The default is 32 GB.
  15. Select the icon of your new VM and select start with console (VNC).


  1. Create a new virtual machine in virt-manager.
  2. Select Import existing disk image, provide the path to the QCOW2 image above.
  3. Choose Generic Default for the operating system.
  4. Check the box for Customize configuration before install.
  5. Under Network Selection, select your bridge.
  6. Under customization select Overview > Firmware > UEFI x86_64: …. Make sure to select a non-secureboot version of OVMF (does not contain the word secure, secboot, etc.), e.g., /usr/share/edk2/ovmf/OVMF_CODE.fd.
  7. Click Add Hardware (bottom left), and select Channel.
  8. Select device type: unix.
  9. Select name: org.qemu.guest_agent.0.
  10. Finally, select Begin Installation (upper left corner).


```
virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk <PATH TO QCOW2 FILE>,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi

```

If you have a USB dongle to attach, you need to add the option --hostdev busID.deviceId. You can discover these IDs via the lsusb command. As example, if lsusb output is:
```
  Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
  Bus 003 Device 004: ID 30c9:0052 Luxvisions Innotech Limited Integrated RGB Camera
  Bus 003 Device 003: ID 1a86:55d4 QinHeng Electronics SONOFF Zigbee 3.0 USB Dongle Plus V2
  Bus 003 Device 002: ID 06cb:00fc Synaptics, Inc. 
  Bus 003 Device 005: ID 8087:0033 Intel Corp. 
  Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
  Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
  Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

```

You can recognize the Sonoff dongle at Bus 003 Device 003. So the command to install the VM will become:
```
virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk <PATH TO QCOW2 FILE>,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi --hostdev 003.003

```

Note that this configuration (bus 003, device 003) is just an example, your dongle could be on another bus and/or with another device ID. Please check the correct IDs of your USB dongle with lsusb.
Use the E1000 or E1000E virtual network adapter. There are confirmed mDNS/Multicast discovery issues when using VMware’s VMXnet3 virtual network adapter.
### Start up your virtual machine 
  1. Start the virtual machine.
  2. Observe the boot process of the Home Assistant Operating System.
  3. Once completed, you will be able to reach Home Assistant on . If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your virtual machine’s IP address).


With the Home Assistant Operating System installed and accessible, you can continue with onboarding.
## Install Home Assistant Container 
### Synology NAS 
Synology with DSM now supports container management through the Container Manager package, allowing you to install Home Assistant without the need for command-line. For details about the package (including compatibility-information, if your NAS is supported), see The steps would be:
If you are using the built-in firewall, you must also add the port 8123 to allowed list. This can be found in “Control Panel -> Security” and then the Firewall tab. Click “Edit Rules” besides the Firewall Profile dropdown box. Create a new rule and select “Custom” for Ports and add 8123. Edit Source IP if you like or leave it at default “All”. Action should stay at “Allow”.
To use a Z-Wave USB stick for Z-Wave control, the HA Docker container needs extra configuration to access to the USB stick. While there are multiple ways to do this, the least privileged way of granting access can only be performed via the Terminal, at the time of writing. See this page for configuring Terminal access to your Synology NAS:
Tip
Adjust the following Terminal command as follows :
  * Replace /PATH_TO_YOUR_CONFIG points at the folder where you want to store your configuration - make sure that you keep the :/config part
  * Replace /PATH_TO_YOUR_USB_STICK matches the path for your USB stick (e.g., /dev/ttyACM0 for most Synology users)
  * Replace “Australia/Melbourne” with 


Run it in Terminal.
```
sudo docker run --restart always -d --name homeassistant -v /PATH_TO_YOUR_CONFIG:/config --device=/PATH_TO_YOUR_USB_STICK -e TZ=Australia/Melbourne --net=host ghcr.io/home-assistant/home-assistant:stable

```

Complete the remainder of the Z-Wave configuration by 
Remark: to update your Home Assistant on your Docker within Synology NAS, you just have to do the following:
Remark: to restart your Home Assistant within Synology NAS, you just have to do the following:
  * Go to the “Container Manager”-app and move to “Container”-section
  * Right-click on it and select “Action”->“Restart”.


Note
If you want to use a USB Bluetooth adapter or Z-Wave USB Stick with Home Assistant on Synology Docker these instructions do not correctly configure the container to access the USB devices. To configure these devices on your Synology Docker Home Assistant you can follow the instructions provided by Phil Hawthorne.
### QNAP NAS 
QNAP with QTS supports Docker, allowing you to install Home Assistant using Docker without the need for command-line. For details about the package (including compatibility-information, if your NAS is supported), see 
The steps would be:
Remark: To update your Home Assistant on your Docker within Qnap NAS, you just remove container and image and do steps again (Don’t remove “config” folder).
### Community Notes 
Note that some users have reported issues creating Home Assistant containers on ARM QNAP systems (e.g., TS-233) with Container Station 3. A possible workaround is the “Docker compose” approach based on a YAML file (see section “Docker compose”). In the QNAP Container Station 3 UI, this can be accessed by going to the “Applications” section and clicking on “Create”. You are then prompted to enter YAML code, which can be copied from that shown in the “Docker compose” section. Take care to modify this code in two ways: firstly, add a first line reading “version: ‘3’”; secondly, replace the text “/PATH_TO_YOUR_CONFIG” by a valid path on your NAS system, e.g., “/share/Container/HomeAssistant/config”.
Once the Home Assistant Container is running Home Assistant should be accessible using http://<host>:8123 (replace  with the hostname or IP of the system). You can continue with onboarding.
### Restart Home Assistant 
If you change the configuration, you have to restart the server. To do that you have 3 options.
  1. In your Home Assistant UI, go to the Settings > System and click the Restart button.
  2. You can go to the Developer Tools > Actions, select homeassistant.restart and select Perform action.
  3. Restart it from a terminal.


Docker CLI
Docker Compose
```
docker restart homeassistant

```

```
docker compose restart

```

### Docker compose 
Tip
docker compose should on your system. If not, you can install it.
As the Docker command becomes more complex, switching to docker compose can be preferable and support automatically restarting on failure or system restart. Create a compose.yaml file:
```
 services:
  homeassistant:
   container_name: homeassistant
   image: "ghcr.io/home-assistant/home-assistant:stable"
   volumes:
    - /PATH_TO_YOUR_CONFIG:/config
    - /etc/localtime:/etc/localtime:ro
    - /run/dbus:/run/dbus:ro
   restart: unless-stopped
   privileged: true
   network_mode: host
   environment:
    TZ: Europe/Amsterdam

```

Start it by running:
```
docker compose up -d

```

Once the Home Assistant Container is running, Home Assistant should be accessible using http://<host>:8123 (replace  with the hostname or IP of the system). You can continue with onboarding.
### Exposing devices 
In order to use Zigbee or other integrations that require access to devices, you need to map the appropriate device into the container. Ensure the user that is running the container has the correct privileges to access the /dev/tty* file, then add the device mapping to your container instructions:
Docker CLI
Docker Compose
```
docker run ... --device /dev/ttyUSB0:/dev/ttyUSB0 ...

```

```
services:
 homeassistant:
  ...
  devices:
   - /dev/ttyUSB0:/dev/ttyUSB0

```

### Optimizations 
The Home Assistant Container is using an alternative memory allocation library for better memory management and Python runtime speedup.
As the jemalloc configuration used can cause issues on certain hardware featuring a page size larger than 4K (like some specific ARM64-based SoCs), it can be disabled by passing the environment variable DISABLE_JEMALLOC with any value, for example:
Docker CLI
Docker Compose
```
docker run ... -e "DISABLE_JEMALLOC=true" ...

```

```
services:
 homeassistant:
 ...
  environment:
   DISABLE_JEMALLOC: true

```

The error message <jemalloc>: Unsupported system page size is one known indicator.
## Community provided guides 
Additional installation guides can be found on our .
These Community Guides are provided as-is. Some of these install methods are more limited than the methods above. Some integrations may not work due to limitations of the platform.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Getting started
#  On this page



## Alternative - Home Assistant

Source: https://www.home-assistant.io/installation/alternative/

#  On this page
## Install Home Assistant Operating System 
### Download the appropriate image 
  * (.vdi)
  * (.qcow2)
  * (.ova)


After downloading, decompress the image. If the image comes in a ZIP file, for example, unzip it.
Follow this guide if you already are running a supported virtual machine hypervisor. If you are not familiar with virtual machines, install Home Assistant OS directly on a , a , or an .
### Create the virtual machine 
Load the appliance image into your virtual machine hypervisor. (Note: You are free to assign as much resources as you wish to the VM, please assign enough based on your add-on needs).
Minimum recommended assignments:
  * 2 GB RAM
  * 32 GB Storage
  * 2vCPU


All these can be extended if your usage calls for more resources.
### Hypervisor specific configuration 
VirtualBox
Unraid
KVM (virt-manager)
KVM (virt-install)
VMware ESXi/vSphere
  1. Create a new virtual machine.
  2. Select type Linux, subtype Oracle Linux and version Oracle Linux (64-bit) or Oracle Linux (ARM 64-bit) depending on your hardware.
  3. Under Hardware, select the amount of memory and number of CPUs. Then, select Enable EFI. 
     * Make sure EFI is enabled. If EFI is not enabled, HAOS won’t boot.
  4. Under Hard Disk, select Use an existing virtual hard disk file, select the unzipped VDI file from above.
  5. Then go to Network > Adapter 1. Choose Bridged Adapter and choose your network adapter (i.e. en0:Wi-Fi).
  6. Then go to Audio and choose Intel HD Audio as audio controller.


By default, VirtualBox does not free up unused disk space. To automatically shrink the vdi disk image the discard option must be enabled using your host machine’s terminal:
```
VBoxManage storageattach <VM name> --storagectl "SATA" --port 0 --device 0 --nonrotational on --discard on
```

Bash
Copy
More details can be found about the command can be found .
  1. Download the .qcow2 image above and decompress it. (Extract all in Windows)
  2. Store the image in the isos share on your server.
  3. Make sure under Settings > VM manager, Enable VMs is enabled.
  4. Create a new virtual machine: VMS > Add VM.
  5. Select type Linux and give the VM a name and a description.
  6. Select the CPU cores you want to let the VM use and give it some memory.
  7. Under Primary vDisk Location, select Manual and then select the qcow2 image.
  8. Select your keyboard language under VM Console Keyboard.
  9. Select br0 under Network Source.
  10. Select virtio under Network model.
  11. Select any USB-devices that you want to pass through to Home Assistant, such as Zigbee- or Z-Wave controllers.
  12. Deselect Start VM after creation.
  13. Select Create.
  14. Select the name of your new VM and select the capacity number for your disk. Here, you can expand the disk to whatever your needs are. The default is 32 GB.
  15. Select the icon of your new VM and select start with console (VNC).


  1. Create a new virtual machine in virt-manager.
  2. Select Import existing disk image, provide the path to the QCOW2 image above.
  3. Choose Generic Default for the operating system.
  4. Check the box for Customize configuration before install.
  5. Under Network Selection, select your bridge.
  6. Under customization select Overview > Firmware > UEFI x86_64: …. Make sure to select a non-secureboot version of OVMF (does not contain the word secure, secboot, etc.), e.g., /usr/share/edk2/ovmf/OVMF_CODE.fd.
  7. Click Add Hardware (bottom left), and select Channel.
  8. Select device type: unix.
  9. Select name: org.qemu.guest_agent.0.
  10. Finally, select Begin Installation (upper left corner).


```
virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk <PATH TO QCOW2 FILE>,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi
```

Bash
Copy
If you have a USB dongle to attach, you need to add the option --hostdev busID.deviceId. You can discover these IDs via the lsusb command. As example, if lsusb output is:
```
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 004: ID 30c9:0052 Luxvisions Innotech Limited Integrated RGB Camera
Bus 003 Device 003: ID 1a86:55d4 QinHeng Electronics SONOFF Zigbee 3.0 USB Dongle Plus V2
Bus 003 Device 002: ID 06cb:00fc Synaptics, Inc.
Bus 003 Device 005: ID 8087:0033 Intel Corp.
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

Bash
Copy
You can recognize the Sonoff dongle at Bus 003 Device 003. So the command to install the VM will become:
```
virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk <PATH TO QCOW2 FILE>,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi --hostdev 003.003
```

Bash
Copy
Note that this configuration (bus 003, device 003) is just an example, your dongle could be on another bus and/or with another device ID. Please check the correct IDs of your USB dongle with lsusb.
Use the E1000 or E1000E virtual network adapter. There are confirmed mDNS/Multicast discovery issues when using VMware’s VMXnet3 virtual network adapter.
### Start up your virtual machine 
  1. Start the virtual machine.
  2. Observe the boot process of the Home Assistant Operating System.
  3. Once completed, you will be able to reach Home Assistant on . If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your virtual machine’s IP address).


With the Home Assistant Operating System installed and accessible, you can continue with onboarding.
## Install Home Assistant Container 
### Synology NAS 
Synology with DSM now supports container management through the Container Manager package, allowing you to install Home Assistant without the need for command-line. For details about the package (including compatibility-information, if your NAS is supported), see The steps would be:
If you are using the built-in firewall, you must also add the port 8123 to allowed list. This can be found in “Control Panel -> Security” and then the Firewall tab. Click “Edit Rules” besides the Firewall Profile dropdown box. Create a new rule and select “Custom” for Ports and add 8123. Edit Source IP if you like or leave it at default “All”. Action should stay at “Allow”.
To use a Z-Wave USB stick for Z-Wave control, the HA Docker container needs extra configuration to access to the USB stick. While there are multiple ways to do this, the least privileged way of granting access can only be performed via the Terminal, at the time of writing. See this page for configuring Terminal access to your Synology NAS:
Tip
Adjust the following Terminal command as follows :
  * Replace /PATH_TO_YOUR_CONFIG points at the folder where you want to store your configuration - make sure that you keep the :/config part
  * Replace /PATH_TO_YOUR_USB_STICK matches the path for your USB stick (e.g., /dev/ttyACM0 for most Synology users)
  * Replace “Australia/Melbourne” with 


Run it in Terminal.
```
sudo docker run --restart always -d --name homeassistant -v /PATH_TO_YOUR_CONFIG:/config --device=/PATH_TO_YOUR_USB_STICK -e TZ=Australia/Melbourne --net=host ghcr.io/home-assistant/home-assistant:stable
```

Bash
Copy
Complete the remainder of the Z-Wave configuration by 
Remark: to update your Home Assistant on your Docker within Synology NAS, you just have to do the following:
Remark: to restart your Home Assistant within Synology NAS, you just have to do the following:
  * Go to the “Container Manager”-app and move to “Container”-section
  * Right-click on it and select “Action”->“Restart”.


Note
If you want to use a USB Bluetooth adapter or Z-Wave USB Stick with Home Assistant on Synology Docker these instructions do not correctly configure the container to access the USB devices. To configure these devices on your Synology Docker Home Assistant you can follow the instructions provided by Phil Hawthorne.
### QNAP NAS 
QNAP with QTS supports Docker, allowing you to install Home Assistant using Docker without the need for command-line. For details about the package (including compatibility-information, if your NAS is supported), see 
The steps would be:
Remark: To update your Home Assistant on your Docker within Qnap NAS, you just remove container and image and do steps again (Don’t remove “config” folder).
### Community Notes 
Note that some users have reported issues creating Home Assistant containers on ARM QNAP systems (e.g., TS-233) with Container Station 3. A possible workaround is the “Docker compose” approach based on a YAML file (see section “Docker compose”). In the QNAP Container Station 3 UI, this can be accessed by going to the “Applications” section and clicking on “Create”. You are then prompted to enter YAML code, which can be copied from that shown in the “Docker compose” section. Take care to modify this code in two ways: firstly, add a first line reading “version: ‘3’”; secondly, replace the text “/PATH_TO_YOUR_CONFIG” by a valid path on your NAS system, e.g., “/share/Container/HomeAssistant/config”.
Once the Home Assistant Container is running Home Assistant should be accessible using http://<host>:8123 (replace  with the hostname or IP of the system). You can continue with onboarding.
### Restart Home Assistant 
If you change the configuration, you have to restart the server. To do that you have 3 options.
  1. In your Home Assistant UI, go to the Settings > System and click the Restart button.
  2. You can go to the Developer Tools > Actions, select homeassistant.restart and select Perform action.
  3. Restart it from a terminal.


Docker CLI
Docker Compose
```
docker restart homeassistant
```

Bash
Copy
```
docker compose restart
```

Bash
Copy
### Docker compose 
Tip
docker compose should on your system. If not, you can install it.
As the Docker command becomes more complex, switching to docker compose can be preferable and support automatically restarting on failure or system restart. Create a compose.yaml file:
```
services:
 homeassistant:
  container_name: homeassistant
  image: "ghcr.io/home-assistant/home-assistant:stable"
  volumes:
   - /PATH_TO_YOUR_CONFIG:/config
   - /etc/localtime:/etc/localtime:ro
   - /run/dbus:/run/dbus:ro
  restart: unless-stopped
  privileged: true
  network_mode: host
  environment:
   TZ: Europe/Amsterdam
```

YAML
Copy
Start it by running:
```
docker compose up -d
```

Bash
Copy
Once the Home Assistant Container is running, Home Assistant should be accessible using http://<host>:8123 (replace  with the hostname or IP of the system). You can continue with onboarding.
### Exposing devices 
In order to use Zigbee or other integrations that require access to devices, you need to map the appropriate device into the container. Ensure the user that is running the container has the correct privileges to access the /dev/tty* file, then add the device mapping to your container instructions:
Docker CLI
Docker Compose
```
docker run ... --device /dev/ttyUSB0:/dev/ttyUSB0 ...
```

Bash
Copy
```
services:
 homeassistant:
  ...
  devices:
   - /dev/ttyUSB0:/dev/ttyUSB0
```

YAML
Copy
### Optimizations 
The Home Assistant Container is using an alternative memory allocation library for better memory management and Python runtime speedup.
As the jemalloc configuration used can cause issues on certain hardware featuring a page size larger than 4K (like some specific ARM64-based SoCs), it can be disabled by passing the environment variable DISABLE_JEMALLOC with any value, for example:
Docker CLI
Docker Compose
```
docker run ... -e "DISABLE_JEMALLOC=true" ...
```

Bash
Copy
```
services:
 homeassistant:
 ...
  environment:
   DISABLE_JEMALLOC: true
```

YAML
Copy
The error message <jemalloc>: Unsupported system page size is one known indicator.
## Community provided guides 
Additional installation guides can be found on our .
These Community Guides are provided as-is. Some of these install methods are more limited than the methods above. Some integrations may not work due to limitations of the platform.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Getting started
#  On this page



## FAQ - Home Assistant

Source: https://www.home-assistant.io/faq/

This is a community curated list of frequently asked questions (FAQ) about the installation, setup, and usage of Home Assistant. If you want to get details about a term, please check the .
## Common 
### Releases 
New versions of Home Assistant are released on the first Wednesday of every month. The exact dates can be seen in the upcoming events calendar on the website.
A list of all releases in our history and their announcement blog posts can be found .
The last week of our release schedule is primarily focused on beta testing. Users who participate in the beta can view the changelog under and get help in the #beta channel of . Testers are also encouraged to .
## Configuration 
### My integration does not show up 
When an integration does not show up, many different things can be the case. Before you try any of these steps, make sure to look at the and see if there are any errors related to your integration you are trying to set up.
If you have incorrect entries in your configuration files you can use the CLI script to check your configuration, each installation type has its own section in the common-tasks about this:


### This entity does not have a unique ID? 
If you try to access the configuration dialog for an entity in your Home Assistant, you might end up seeing this message:
This means that this entity does not have a unique identification, e.g., a serial number or another identifier that is guaranteed to be static and never changes. As a result, the normal editing process that allows you to change various settings through the user interface (such as the entity ID, icon, friendly name, etc.) is not possible here.
Typically, you’ll see this when you create entities manually using YAML, but it can also appear if the integration that provides this entity cannot determine a unique ID. This is not an error, but rather a limitation of the integration you use. A few selected integrations (such as and ) allow you to define a unique ID.
### Used where? 
Unique ID:
  * Only internally in Home Assistant.


Entity ID:
  * Entity with a unique ID: Entity ID only used as a reference, e.g., in automations or dashboards.
  * Entity without a unique ID: Entity ID acts as the replacement for the non-existing unique ID plus as a reference, e.g., in automations or dashboards.


### Can be changed? 
Unique ID:
  * No. It is a static identifier.


Entity ID:
  * Entity with a unique ID: Entity ID can be adjusted freely (as long as it follows the format <domain>.<id> and does not result in duplicates in your Home Assistant). Keep in mind that if you change the entity ID, you also need to update the references, e.g., in automations and dashboards. 
  * Entity without a unique ID: Entity ID is considered a fixed, static identifier and cannot be changed.


In case your entity has no unique ID and therefore cannot be changed through the UI, there are some directly through YAML files.
### Can I add a unique ID myself? 
No, as an end-user, you cannot add a unique ID to an entity that doesn’t have one. Unique IDs are a feature that must be provided by the integration itself. This is because the unique ID needs to be persistent across restarts and should consistently identify the same physical device or service.
If an integration currently doesn’t provide unique IDs for its entities, this means the integration could potentially be modernized to include this capability. However, providing unique IDs is not currently a mandatory requirement for all integrations.
The Home Assistant project always welcomes code contributions to enhance integrations with this capability. If you’re interested in improving an integration to provide unique IDs, you can contribute code to the Home Assistant project. For more information on contributing, please visit the .
In case you want to read more about unique IDs, head over to this .
### Why are you using YAML for the configuration file? 
And not JSON or XML for the ? Because can be written by hand, you don’t have to care about commas or tag and it’s a superset of JSON.
## Documentation 
### Documentation tools 
Why are you not using tools X for the documentation? Because the current solution works for us and we see no additional value in using a separate publishing platform.
### Missing Documentation 
Home Assistant is a FAST moving open source project. This means occasionally the official documentation will not be 100% current or complete. Since this is an open source volunteer project, we would encourage anyone who finds gaps in the documentation to click the EDIT link at the bottom and submit any corrections/enhancements they may find useful. A step-by-step guide on how to contribute to the documentation can be found .
In the absence of information, many users find it beneficial to look at other people’s configurations to find examples of what they want to accomplish in their own configurations. The easiest way to find these configurations is through this .
## Home Assistant 
### 404 Client Error: Not Found (’no such image: homeassistant/…) 
This error indicates the image, whether for updating to Home Assistant or installing or updating an add-on, was not able to be pulled to your system. This is usually a situation where there is not enough space for the image to be downloaded. The first thing to check for is the available space on your system.
Please note, if you are running the operating system as a virtual machine; the default VM image is only about 6GB. Many VM users run into this as they have not allocated enough storage. 32GB is the minimum recommended size.
You will need to explore your own system to determine where space has gone. Using df -h in the SSH add-on console to you can quickly check to see if you have space available.
If there is plenty of space available then you might check to see if you are having network issues that are preventing images from being downloaded.
### Do I need to leave the USB stick connected for Wi-Fi? 
No. The USB “CONFIG” stick is only used to import a network profile to /etc/NetworkManager/system-connections/ and can be removed.
### I’m trying to find my files on the host or SD card. Where are they? 
On a Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. installation, your files are on the data partition within /mnt/data/supervisor/. On the SD itself, this is an EXT4 partition labeled hassos-data.
For information on file access, refer to the section on .
### Is USB Boot for the Raspberry Pi 4 supported? 
Home Assistant offers a data disk feature that offloads all data to an attached USB hard drive. The SD card is still in use but is only used to serve the Home Assistant OS. 
Booting from USB
Due to the complexity of USB and the USB mass storage device class, booting from a USB device is delicate. When booting from a USB drive this process has to be done multiple times (firmware/boot loader and the operating system), and there is a high chance that it doesn’t complete during one of these stages.
That said, booting Home Assistant OS completely from a USB drive (SSD or any other USB mass storage device) works with some USB devices. USB Devices that are known to work with Raspberry Pi OS (check the Raspberry Pi Forum) are more likely to work with Home Assistant OS. However, because Home Assistant OS also has U-Boot in the boot chain, there are devices which are known to work with Raspberry Pi OS but do not work with Home Assistant OS. Finding the right combination of hardware can require experimentation.
### Is the Raspberry Pi 4 with 8GB RAM supported? 
The Raspberry Pi 4 with 8GB RAM is supported with Home Assistant OS 5.5 and later using the 32-bit and 64-bit image. The 64-bit is the better tested option at this point.
### Why does the start button for an add-on flash red when I click it? 
If you are looking for more information about add-ons, which won’t start or install, navigate to in the UI and check the logs.
The logs on this page are the same you would see using su logs in the custom CLI.
## Installation 
### Home Assistant vs. Home Assistant Core 
Home Assistant Core is a Python program, in simple words. It can be run on various operating systems and provide the ability to track, control and automate your devices. When people talking about Home Assistant Core they usually refer to a standalone .
is a combination of Home Assistant Core and tools which allows one to run it easily on a Raspberry Pi and other platforms without setting up an operating system first. Home Assistant is an all-in one-solution and has a management user interface that can be used from the Home Assistant frontend. This interface is not present in a Home Assistant Core setup.
Be aware that add-ons are only available in regular Home Assistant installations.
### No module named pip 
should come bundled with the latest Python 3 but is omitted by some distributions. If you are unable to run python3 -m pip --version you can install pip by and running it with Python 3:
```
python3 get-pip.py

```

### distutils.errors.DistutilsOptionError 
The problem which leads to distutils.errors.DistutilsOptionError: must supply either home or prefix/exec-prefix -- not both is a known issue if you’re on a Mac using Homebrew to install Python. Please follow to resolve it.
### libyaml is not found or a compiler error 
On a Debian system, install the Python 3 YAML library by sudo apt-get install python3-yaml.
### pip3: command not found 
This utility should have been installed as part of the Python 3 installation. Check if Python 3 is installed by running python3 --version. If it is not installed, .
If you are able to successfully run python3 --version but not pip3, install Home Assistant by running the following command instead:
```
python3 -m pip install homeassistant==2025.12.4

```

On a Debian system, you can also install python3 by sudo apt-get install python3 and pip3 by sudo apt-get install python3-pip.
If you run into errors during installation, check that you’ve installed all the necessary prerequisite packages, which include python3-dev, libffi-dev, and libssl-dev. On a Debian-based system, you can install these via apt-get:
```
sudo apt-get install python3-dev libffi-dev libssl-dev

```

## Usage 
### After upgrading, your browser login gets stuck 
After upgrading to a new version, you may notice your browser gets stuck at the “loading data” login screen. Close the window/tab and go into your browser settings and delete all the cookies for your URL. You can then log back in and it should work.
Android Chrome:
chrome -> settings -> site settings -> storage -> search for your URL for Home Assistant-> “clear & reset”
### Connection error 
It can happen that you get a traceback that notify you about connection issues while running Home Assistant. Eg.
```
ConnectionRefusedError: [Errno 111] Connection refused

```

The chance is very high that this is not a bug but an issue with the service/daemon itself. Check your network (DNS, DHCP, uplink, etc.) first and make sure that Home Assistant and the service are properly configured. Keep in mind that webservices can be down.
### Dependencies 
The dependencies which are used by Home Assistant are stored in the folder deps of the directory. After an the dependencies will be upgraded as well.
### Frontend is acting weird 
Close the windows or tab and clear the cache. The frontend is aggressively caching and clearing the cache ensures that the frontend is reloaded when you access it the next time.
### Problems with dependencies 
Almost all integrations have external dependencies to communicate with your devices and services. Sometimes Home Assistant is unable to install the necessary dependencies. If this is the case, it should show up in .
The first step is trying to restart Home Assistant and see if the problem persists. If it does, look at the log to see what the error is. If you can’t figure it out, please so we can investigate what is going on.
### found character ’ ’ that cannot start any token 
This error means you used tabs rather than two spaces in one of your YAML configuration files. Replace the tabs with spaces.
# Entries



## Generic x86-64 - Home Assistant

Source: https://www.home-assistant.io/installation/generic-x86-64

#  On this page
## Install Home Assistant Operating System 
Follow this guide if you want to get started with Home Assistant easily or if you have little to no Linux experience.
Important
Prerequisites
This guide assumes that you have a dedicated Generic x86-64 PC to exclusively run the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users..
  * This is typically an Intel or AMD-based system.
  * The system must be 64-bit capable and be able to boot using UEFI. 
    * Most systems produced in the last 10 years support the UEFI boot mode.


Summary
  1. First, you will need to configure your Generic x86-64 PC to use UEFI boot mode.
  2. Then, write the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. disk image to your boot medium.


## Configure the BIOS on your x86-64 hardware 
To boot Home Assistant OS, the BIOS needs to have UEFI boot mode enabled and Secure Boot disabled. The following screenshots are from a 7th generation Intel NUC system. The BIOS menu will likely look different on your system. However, the options should still be present and named similarly.
  1. To enter the BIOS, start up your x86-64 hardware and repeatedly press the F2 key (on some systems this might be Del, F1 or F10). 
  2. Make sure the UEFI Boot mode is enabled. 
  3. Disable Secure Boot. 
  4. Save your changes and exit.


The BIOS configuration is now complete.
## Write HAOS onto your x86-64 hardware 
Next, you need to write the Home Assistant Operating System image to the boot medium, which is the medium your x86-64 hardware will boot from when it is running Home Assistant.
Note
HAOS has no integrated installer that writes the image automatically. You will write it manually using either the Disks utility from Ubuntu or Balena Etcher.
Typically, an internal medium like S-ATA hard disk, S-ATA SSD, M.2 SSD, or a non-removable eMMC is used for the x86-64 boot medium. Alternatively, an external medium can be used such as a USB SDD, though this is not recommended.
To write the HAOS image to the boot medium on your x86-64 hardware, there are 2 different methods:
Method 1 (recommended): Boot Ubuntu from a USB flash drive and install the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. from there. It also works on laptops and PCs with internal hard disks.
Method 2: With this method, you write the Home Assistant Operating disk image directly onto a boot medium from your regular computer. The steps are a bit more complex. If you have non-removable internal mediums (for example because you are using a laptop) or do not have the necessary adapter (for example an USB to S-ATA adapter) use method 1 instead.
### Method 1: Installing HAOS via Ubuntu booting from a USB flash drive 
#### Required material 
#### To install HAOS via Ubuntu from a USB flash drive 
  1. Notice: This procedure will write the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. onto your device. 
     * This means you will lose all the data as well as the previously installed operating system.
     * Back up your data before carrying out this procedure.
  2. Create a live operating system on a USB flash drive: 
     * Follow the on writing an Ubuntu Desktop iso file onto a USB device.
  3. Insert the USB flash drive into the system on which you want to run Home Assistant. 
     * Boot the live operating system.
     * You might need to adjust boot order or use F10 (might be a different F-key depending on the BIOS) to select the USB flash drive as boot device.
  4. When prompted, make sure to select Try Ubuntu. This runs Ubuntu on the USB flash device. 
     * The system then starts Ubuntu.
     * Connect your system to your network and make sure it has internet access.
  5. In Ubuntu, open a browser and open the current documentation page, so you can follow the steps. 
     * From there, .
  6. In Ubuntu, in the bottom left corner, select Show Applications.
  7. In the applications, search and open Disks and start restoring the HAOS image: 
    1. In Disks, on the left side, select the internal disk device you want to install HAOS onto.
    2. On top of the screen, select the three dots menu and select Restore Disk Image…. 
    3. Select the image you just downloaded. 
    4. Select Start Restoring…. 
    5. Confirm by selecting Restore. 
    6. In the partitions overview, you should now see the restore operation in progress. 
       * The Home Assistant Operating System is now being installed on your system. 
  8. Once the Home Assistant Operating System is installed, shut down the system. 
     * Once Ubuntu has been shut down, remove the USB flash drive (Ubuntu will inform you when this is the case).
     * Your Home Assistant server is now set up and you can start using it.
     * To use it, proceed as described under .


### Method 2: Installing HAOS directly from a boot medium 
Note
Use this method only if Method 1 does not work for you.
#### Required material 
#### Write the image to your boot medium 
  1. Notice: This procedure will write the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. onto your device.
     * This means you will lose all the data as well as the previously installed operating system.
     * Back up your data before continuing with the next step.
  2. Attach the Home Assistant boot medium (storage device) to your computer.
  3. Download and start . You may need to run it with administrator privileges on Windows.
  4. Download the image to your computer.
     * Copy the URL for the image.
     * If there are multiple links below, make sure to select the correct link for your version of Generic x86-64.
```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_generic-x86-64-16.3.img.xz
```

Text
Copy
Select and copy the URL or use the “copy” button that appears when you hover it.
  5. Paste the URL into your browser to start the download.
  6. Extract the file you just downloaded.
  7. Select Flash from file and select the image you just extracted.
     * Do not use Flash from URL. It does not work on some systems. 
  8. Select target. 
  9. Select the boot medium (storage device) you want to use for your installation. 
  10. Select Flash! to start writing the image.
     * If the operation fails, decompress the .xz file and try again. 
     * When Balena Etcher has finished writing the image, you will see a confirmation. 


### Start up your Generic x86-64 
  * If you used method 1 for the installation, make sure the USB flash drive is removed from the system.
  * If you used method 2 for the installation, install the boot medium into your x86-64 hardware.


  1. Plug in an Ethernet cable that is connected to the network and to the internet. 
     * Note: Internet is required because the newly installed Home Assistant OS does not contain all Home Assistant components yet. It downloads the latest version of Home Assistant Core on first start.
  2. Power the system on. If you have a screen connected to the Generic x86-64 system, after a minute or so the Home Assistant welcome banner will appear in the console.


Note
If the machine complains about not being able to find a bootable medium, you might need to specify the EFI entry in your BIOS. This can be accomplished either by using a live operating system (e.g. Ubuntu) and running the following command (replace <drivename> with the appropriate drive name assigned by Linux, typically this will be sda or nvme0n1 on NVMe SSDs):
```
efibootmgr --create --disk /dev/<drivename> --part 1 --label "HAOS" \
  --loader '\EFI\BOOT\bootx64.efi'
```

Text
Copy
The efibootmgr command will only work if you booted the live operating system in UEFI mode, so be sure to boot from your USB flash drive in this mode. Depending on your privileges on the prompt, you may need to run efibootmgr using sudo.
Or else, the BIOS might provide you with a tool to add boot options, there you can specify the path to the EFI file:
```
\EFI\BOOT\bootx64.efi
```

Text
Copy
  1. In the browser of your desktop system, within a few minutes you will be able to reach your new Home Assistant at .


Note
If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your Generic x86-64’s IP address).
With the Home Assistant Operating System installed and accessible, you can continue with onboarding.
## Install Home Assistant Container 
These below instructions are for an installation of Home Assistant ContainerHome Assistant Container is a standalone container-based installation of Home Assistant Core. Any OCI compatible runtime can be used, but the documentation focus is on Docker. [Learn more] running in your own container environment, which you manage yourself. Any compatible runtime can be used, however this guide will focus on installing it with Docker.
Note
This installation type does not have access to add-ons. If you want to use add-ons, you need to use another installation type. The recommended type is Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users.. Checkout the to see the differences.
Important
Prerequisites This guide assumes that you already have an operating system setup and a container runtime installed (like Docker).
If you are using Docker then you need to be on at least version 19.03.9, ideally an even higher version, and libseccomp 2.4.2 or newer. Docker Desktop will not work, you must use Docker Engine.
### Platform installation 
Installation with Docker is straightforward. Adjust the following command so that:
#  Getting started
#  On this page



## Generic x86-64 - Home Assistant

Source: https://www.home-assistant.io/installation/generic-x86-64/

#  On this page
## Install Home Assistant Operating System 
Follow this guide if you want to get started with Home Assistant easily or if you have little to no Linux experience.
Important
Prerequisites
This guide assumes that you have a dedicated Generic x86-64 PC to exclusively run the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users..
  * This is typically an Intel or AMD-based system.
  * The system must be 64-bit capable and be able to boot using UEFI. 
    * Most systems produced in the last 10 years support the UEFI boot mode.


Summary
  1. First, you will need to configure your Generic x86-64 PC to use UEFI boot mode.
  2. Then, write the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. disk image to your boot medium.


## Configure the BIOS on your x86-64 hardware 
To boot Home Assistant OS, the BIOS needs to have UEFI boot mode enabled and Secure Boot disabled. The following screenshots are from a 7th generation Intel NUC system. The BIOS menu will likely look different on your system. However, the options should still be present and named similarly.
  1. To enter the BIOS, start up your x86-64 hardware and repeatedly press the F2 key (on some systems this might be Del, F1 or F10). 
  2. Make sure the UEFI Boot mode is enabled. 
  3. Disable Secure Boot. 
  4. Save your changes and exit.


The BIOS configuration is now complete.
## Write HAOS onto your x86-64 hardware 
Next, you need to write the Home Assistant Operating System image to the boot medium, which is the medium your x86-64 hardware will boot from when it is running Home Assistant.
Note
HAOS has no integrated installer that writes the image automatically. You will write it manually using either the Disks utility from Ubuntu or Balena Etcher.
Typically, an internal medium like S-ATA hard disk, S-ATA SSD, M.2 SSD, or a non-removable eMMC is used for the x86-64 boot medium. Alternatively, an external medium can be used such as a USB SDD, though this is not recommended.
To write the HAOS image to the boot medium on your x86-64 hardware, there are 2 different methods:
Method 1 (recommended): Boot Ubuntu from a USB flash drive and install the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. from there. It also works on laptops and PCs with internal hard disks.
Method 2: With this method, you write the Home Assistant Operating disk image directly onto a boot medium from your regular computer. The steps are a bit more complex. If you have non-removable internal mediums (for example because you are using a laptop) or do not have the necessary adapter (for example an USB to S-ATA adapter) use method 1 instead.
### Method 1: Installing HAOS via Ubuntu booting from a USB flash drive 
#### Required material 
#### To install HAOS via Ubuntu from a USB flash drive 
  1. Notice: This procedure will write the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. onto your device. 
     * This means you will lose all the data as well as the previously installed operating system.
     * Back up your data before carrying out this procedure.
  2. Create a live operating system on a USB flash drive: 
     * Follow the on writing an Ubuntu Desktop iso file onto a USB device.
  3. Insert the USB flash drive into the system on which you want to run Home Assistant. 
     * Boot the live operating system.
     * You might need to adjust boot order or use F10 (might be a different F-key depending on the BIOS) to select the USB flash drive as boot device.
  4. When prompted, make sure to select Try Ubuntu. This runs Ubuntu on the USB flash device. 
     * The system then starts Ubuntu.
     * Connect your system to your network and make sure it has internet access.
  5. In Ubuntu, open a browser and open the current documentation page, so you can follow the steps. 
     * From there, .
  6. In Ubuntu, in the bottom left corner, select Show Applications.
  7. In the applications, search and open Disks and start restoring the HAOS image: 
    1. In Disks, on the left side, select the internal disk device you want to install HAOS onto.
    2. On top of the screen, select the three dots menu and select Restore Disk Image…. 
    3. Select the image you just downloaded. 
    4. Select Start Restoring…. 
    5. Confirm by selecting Restore. 
    6. In the partitions overview, you should now see the restore operation in progress. 
       * The Home Assistant Operating System is now being installed on your system. 
  8. Once the Home Assistant Operating System is installed, shut down the system. 
     * Once Ubuntu has been shut down, remove the USB flash drive (Ubuntu will inform you when this is the case).
     * Your Home Assistant server is now set up and you can start using it.
     * To use it, proceed as described under .


### Method 2: Installing HAOS directly from a boot medium 
Note
Use this method only if Method 1 does not work for you.
#### Required material 
#### Write the image to your boot medium 
  1. Notice: This procedure will write the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. onto your device.
     * This means you will lose all the data as well as the previously installed operating system.
     * Back up your data before continuing with the next step.
  2. Attach the Home Assistant boot medium (storage device) to your computer.
  3. Download and start . You may need to run it with administrator privileges on Windows.
  4. Download the image to your computer.
     * Copy the URL for the image.
     * If there are multiple links below, make sure to select the correct link for your version of Generic x86-64.
```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_generic-x86-64-16.3.img.xz
```

Text
Copy
Select and copy the URL or use the “copy” button that appears when you hover it.
  5. Paste the URL into your browser to start the download.
  6. Extract the file you just downloaded.
  7. Select Flash from file and select the image you just extracted.
     * Do not use Flash from URL. It does not work on some systems. 
  8. Select target. 
  9. Select the boot medium (storage device) you want to use for your installation. 
  10. Select Flash! to start writing the image.
     * If the operation fails, decompress the .xz file and try again. 
     * When Balena Etcher has finished writing the image, you will see a confirmation. 


### Start up your Generic x86-64 
  * If you used method 1 for the installation, make sure the USB flash drive is removed from the system.
  * If you used method 2 for the installation, install the boot medium into your x86-64 hardware.


  1. Plug in an Ethernet cable that is connected to the network and to the internet. 
     * Note: Internet is required because the newly installed Home Assistant OS does not contain all Home Assistant components yet. It downloads the latest version of Home Assistant Core on first start.
  2. Power the system on. If you have a screen connected to the Generic x86-64 system, after a minute or so the Home Assistant welcome banner will appear in the console.


Note
If the machine complains about not being able to find a bootable medium, you might need to specify the EFI entry in your BIOS. This can be accomplished either by using a live operating system (e.g. Ubuntu) and running the following command (replace <drivename> with the appropriate drive name assigned by Linux, typically this will be sda or nvme0n1 on NVMe SSDs):
```
efibootmgr --create --disk /dev/<drivename> --part 1 --label "HAOS" \
  --loader '\EFI\BOOT\bootx64.efi'
```

Text
Copy
The efibootmgr command will only work if you booted the live operating system in UEFI mode, so be sure to boot from your USB flash drive in this mode. Depending on your privileges on the prompt, you may need to run efibootmgr using sudo.
Or else, the BIOS might provide you with a tool to add boot options, there you can specify the path to the EFI file:
```
\EFI\BOOT\bootx64.efi
```

Text
Copy
  1. In the browser of your desktop system, within a few minutes you will be able to reach your new Home Assistant at .


Note
If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your Generic x86-64’s IP address).
With the Home Assistant Operating System installed and accessible, you can continue with onboarding.
## Install Home Assistant Container 
These below instructions are for an installation of Home Assistant ContainerHome Assistant Container is a standalone container-based installation of Home Assistant Core. Any OCI compatible runtime can be used, but the documentation focus is on Docker. [Learn more] running in your own container environment, which you manage yourself. Any compatible runtime can be used, however this guide will focus on installing it with Docker.
Note
This installation type does not have access to add-ons. If you want to use add-ons, you need to use another installation type. The recommended type is Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users.. Checkout the to see the differences.
Important
Prerequisites This guide assumes that you already have an operating system setup and a container runtime installed (like Docker).
If you are using Docker then you need to be on at least version 19.03.9, ideally an even higher version, and libseccomp 2.4.2 or newer. Docker Desktop will not work, you must use Docker Engine.
### Platform installation 
Installation with Docker is straightforward. Adjust the following command so that:
#  Getting started
#  On this page



## Linux - Home Assistant

Source: https://www.home-assistant.io/installation/linux

#  On this page
## Install Home Assistant Operating System 
### Download the appropriate image 
  * (.vdi)
  * (.qcow2)


After downloading, decompress the image. If the image comes in a ZIP file, for example, unzip it.
Follow this guide if you already are running a supported virtual machine hypervisor. If you are not familiar with virtual machines, install Home Assistant OS directly on a , a , or an .
### Create the virtual machine 
Load the appliance image into your virtual machine hypervisor. (Note: You are free to assign as much resources as you wish to the VM, please assign enough based on your add-on needs).
Minimum recommended assignments:
  * 2 GB RAM
  * 32 GB Storage
  * 2vCPU


All these can be extended if your usage calls for more resources.
### Hypervisor specific configuration 
VirtualBox
Unraid
KVM (virt-manager)
KVM (virt-install)
  1. Create a new virtual machine.
  2. Select type Linux, subtype Oracle Linux and version Oracle Linux (64-bit) or Oracle Linux (ARM 64-bit) depending on your hardware.
  3. Under Hardware, select the amount of memory and number of CPUs. Then, select Enable EFI. 
     * Make sure EFI is enabled. If EFI is not enabled, HAOS won’t boot.
  4. Under Hard Disk, select Use an existing virtual hard disk file, select the unzipped VDI file from above.
  5. Then go to Network > Adapter 1. Choose Bridged Adapter and choose your network adapter (i.e. en0:Wi-Fi).
  6. Then go to Audio and choose Intel HD Audio as audio controller.


By default, VirtualBox does not free up unused disk space. To automatically shrink the vdi disk image the discard option must be enabled using your host machine’s terminal:
```
VBoxManage storageattach <VM name> --storagectl "SATA" --port 0 --device 0 --nonrotational on --discard on
```

Bash
Copy
More details can be found about the command can be found .
  1. Download the .qcow2 image above and decompress it. (Extract all in Windows)
  2. Store the image in the isos share on your server.
  3. Make sure under Settings > VM manager, Enable VMs is enabled.
  4. Create a new virtual machine: VMS > Add VM.
  5. Select type Linux and give the VM a name and a description.
  6. Select the CPU cores you want to let the VM use and give it some memory.
  7. Under Primary vDisk Location, select Manual and then select the qcow2 image.
  8. Select your keyboard language under VM Console Keyboard.
  9. Select br0 under Network Source.
  10. Select virtio under Network model.
  11. Select any USB-devices that you want to pass through to Home Assistant, such as Zigbee- or Z-Wave controllers.
  12. Deselect Start VM after creation.
  13. Select Create.
  14. Select the name of your new VM and select the capacity number for your disk. Here, you can expand the disk to whatever your needs are. The default is 32 GB.
  15. Select the icon of your new VM and select start with console (VNC).


  1. Create a new virtual machine in virt-manager.
  2. Select Import existing disk image, provide the path to the QCOW2 image above.
  3. Choose Generic Default for the operating system.
  4. Check the box for Customize configuration before install.
  5. Under Network Selection, select your bridge.
  6. Under customization select Overview > Firmware > UEFI x86_64: …. Make sure to select a non-secureboot version of OVMF (does not contain the word secure, secboot, etc.), e.g., /usr/share/edk2/ovmf/OVMF_CODE.fd.
  7. Click Add Hardware (bottom left), and select Channel.
  8. Select device type: unix.
  9. Select name: org.qemu.guest_agent.0.
  10. Finally, select Begin Installation (upper left corner).


```
virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk <PATH TO QCOW2 FILE>,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi
```

Bash
Copy
If you have a USB dongle to attach, you need to add the option --hostdev busID.deviceId. You can discover these IDs via the lsusb command. As example, if lsusb output is:
```
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 004: ID 30c9:0052 Luxvisions Innotech Limited Integrated RGB Camera
Bus 003 Device 003: ID 1a86:55d4 QinHeng Electronics SONOFF Zigbee 3.0 USB Dongle Plus V2
Bus 003 Device 002: ID 06cb:00fc Synaptics, Inc.
Bus 003 Device 005: ID 8087:0033 Intel Corp.
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

Bash
Copy
You can recognize the Sonoff dongle at Bus 003 Device 003. So the command to install the VM will become:
```
virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk <PATH TO QCOW2 FILE>,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi --hostdev 003.003
```

Bash
Copy
Note that this configuration (bus 003, device 003) is just an example, your dongle could be on another bus and/or with another device ID. Please check the correct IDs of your USB dongle with lsusb.
### Start up your virtual machine 
  1. Start the virtual machine.
  2. Observe the boot process of the Home Assistant Operating System.
  3. Once completed, you will be able to reach Home Assistant on . If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your virtual machine’s IP address).


With the Home Assistant Operating System installed and accessible, you can continue with onboarding.
## Install Home Assistant Container 
These below instructions are for an installation of Home Assistant ContainerHome Assistant Container is a standalone container-based installation of Home Assistant Core. Any OCI compatible runtime can be used, but the documentation focus is on Docker. [Learn more] running in your own container environment, which you manage yourself. Any compatible runtime can be used, however this guide will focus on installing it with Docker.
Note
This installation type does not have access to add-ons. If you want to use add-ons, you need to use another installation type. The recommended type is Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users.. Checkout the to see the differences.
Important
Prerequisites This guide assumes that you already have an operating system setup and a container runtime installed (like Docker).
If you are using Docker then you need to be on at least version 19.03.9, ideally an even higher version, and libseccomp 2.4.2 or newer. Docker Desktop will not work, you must use Docker Engine.
### Platform installation 
Installation with Docker is straightforward. Adjust the following command so that:
#  Getting started
#  On this page



## Raspberry Pi - Home Assistant

Source: https://www.home-assistant.io/installation/raspberrypi

#  On this page
## Suggested hardware 
We will need a few things to get started with installing Home Assistant.
Note
Remember to ensure you’re using an with your Raspberry Pi. Mobile chargers may not be suitable, since some are designed to only provide the full power with that manufacturer’s handsets. USB ports on your computer also will not supply enough power and must not be used.
## Install Home Assistant Operating System 
This guide shows how to install the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. onto your Raspberry Pi using Raspberry Pi Imager.
### Write the image to your SD card 
  1. Download and install the Raspberry Pi Imager on your computer as described under . 
     * Troubleshooting: If Raspberry Pi Imager is not supported by your platform, you can and use another imaging tool, such as Balena Etcher.
  2. Open the Raspberry Pi Imager and select your Raspberry Pi device. 
  3. Choose the operating system: 
    1. Select Choose OS.
    2. Select Other specific-purpose OS > Home assistants and home automation > Home Assistant.
    3. Choose the Home Assistant OS that matches your hardware (RPi 3, RPi 4, or RPi 5). 
  4. Choose the storage: 
    1. Insert the SD card into the computer. Note: the contents of the card will be overwritten.
    2. Select your SD card. 
  5. Write the installer onto the SD card: 
    1. To start the process, select Next.
    2. Wait for the Home Assistant OS to be written to the SD card. 
  6. Eject the SD card.


### Start up your Raspberry Pi 
  1. Insert the SD card into your Raspberry Pi.
  2. Plug in an Ethernet cable and make sure the Raspberry Pi is connected to the same network as your computer and is connected to the internet.
  3. Connect the power supply to start up the device.


### Access Home Assistant 
Within a few minutes after connecting the Raspberry Pi, you will be able to reach your new Home Assistant.
  * In the browser of your desktop system, enter .


Note
If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your Raspberry Pi’s IP address).
Congratulations! You finished the Raspberry Pi setup!
### Downloading the Home Assistant image 
If Raspberry Pi Imager is not supported by your platform, you can download the Home Assistant image and use another imaging tool, such as Balena Etcher.
To download the image to your computer, copy the correct URL for the Raspberry Pi 4 or 5 (Note: there are two different links below!):
Raspberry Pi 5
Raspberry Pi 4
```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_rpi5-64-16.3.img.xz
```

Text
Copy
```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_rpi4-64-16.3.img.xz
```

Text
Copy
With the Home Assistant Operating System installed and accessible, you can now continue with onboarding.
We get commissions for purchases made through links in this post.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Getting started
#  On this page



## Raspberry Pi - Home Assistant

Source: https://www.home-assistant.io/installation/raspberrypi/

#  On this page
## Suggested hardware 
We will need a few things to get started with installing Home Assistant.
Note
Remember to ensure you’re using an with your Raspberry Pi. Mobile chargers may not be suitable, since some are designed to only provide the full power with that manufacturer’s handsets. USB ports on your computer also will not supply enough power and must not be used.
## Install Home Assistant Operating System 
This guide shows how to install the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. onto your Raspberry Pi using Raspberry Pi Imager.
### Write the image to your SD card 
  1. Download and install the Raspberry Pi Imager on your computer as described under . 
     * Troubleshooting: If Raspberry Pi Imager is not supported by your platform, you can and use another imaging tool, such as Balena Etcher.
  2. Open the Raspberry Pi Imager and select your Raspberry Pi device. 
  3. Choose the operating system: 
    1. Select Choose OS.
    2. Select Other specific-purpose OS > Home assistants and home automation > Home Assistant.
    3. Choose the Home Assistant OS that matches your hardware (RPi 3, RPi 4, or RPi 5). 
  4. Choose the storage: 
    1. Insert the SD card into the computer. Note: the contents of the card will be overwritten.
    2. Select your SD card. 
  5. Write the installer onto the SD card: 
    1. To start the process, select Next.
    2. Wait for the Home Assistant OS to be written to the SD card. 
  6. Eject the SD card.


### Start up your Raspberry Pi 
  1. Insert the SD card into your Raspberry Pi.
  2. Plug in an Ethernet cable and make sure the Raspberry Pi is connected to the same network as your computer and is connected to the internet.
  3. Connect the power supply to start up the device.


### Access Home Assistant 
Within a few minutes after connecting the Raspberry Pi, you will be able to reach your new Home Assistant.
  * In the browser of your desktop system, enter .


Note
If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your Raspberry Pi’s IP address).
Congratulations! You finished the Raspberry Pi setup!
### Downloading the Home Assistant image 
If Raspberry Pi Imager is not supported by your platform, you can download the Home Assistant image and use another imaging tool, such as Balena Etcher.
To download the image to your computer, copy the correct URL for the Raspberry Pi 4 or 5 (Note: there are two different links below!):
Raspberry Pi 5
Raspberry Pi 4
```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_rpi5-64-16.3.img.xz
```

Text
Copy
```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_rpi4-64-16.3.img.xz
```

Text
Copy
With the Home Assistant Operating System installed and accessible, you can now continue with onboarding.
We get commissions for purchases made through links in this post.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Getting started
#  On this page



## Advanced Raspberry Pi installation - Home Assistant

Source: https://www.home-assistant.io/installation/raspberrypi-other

#  On this page
While we recommend using the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users., you can also use the Home Assistant ContainerHome Assistant Container is a standalone container-based installation of Home Assistant Core. Any OCI compatible runtime can be used, but the documentation focus is on Docker. [Learn more] method to install Home Assistant. Before you continue, be aware of the limitations and differences compared to the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users.. You can find more information on the . Most notably, are only available with the Home Assistant Operating System.
## Install Home Assistant Container 
These below instructions are for an installation of Home Assistant ContainerHome Assistant Container is a standalone container-based installation of Home Assistant Core. Any OCI compatible runtime can be used, but the documentation focus is on Docker. [Learn more] running in your own container environment, which you manage yourself. Any compatible runtime can be used, however this guide will focus on installing it with Docker.
Note
This installation type does not have access to add-ons. If you want to use add-ons, you need to use another installation type. The recommended type is Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users.. Checkout the to see the differences.
Important
Prerequisites This guide assumes that you already have an operating system setup and a container runtime installed (like Docker).
If you are using Docker then you need to be on at least version 19.03.9, ideally an even higher version, and libseccomp 2.4.2 or newer. Docker Desktop will not work, you must use Docker Engine.
### Platform installation 
Installation with Docker is straightforward. Adjust the following command so that:
#  Getting started
#  On this page



## ODROID - Home Assistant

Source: https://www.home-assistant.io/installation/odroid/

#  On this page
## Install Home Assistant Operating System 
Follow this guide if you want to get started with Home Assistant easily or if you have little to no Linux experience.
## Suggested hardware 
You will need a few things to get started with installing Home Assistant. The links below lead to Ameridroid. If you’re not in the US, you should be able to find these items in web stores in your country.
To get started, we suggest the ODROID-N2+, the board that powers our , or the ODROID-M1.
If unavailable, we also recommend the .
Home Assistant bundles (US market):
The bundles come with Home Assistant pre-installed.
  * ODROID-M1: 4 GB RAM / 256 GB NVMe / or 
  * ODROID-M1: 8 GB RAM / 256 GB NVMe / or 


Variants without pre-installed Home Assistant:
  * ODROID-N2+, or 
  * ODROID-M1S, or 


Related components:
These are affiliated links. We get commissions for purchases made through links in this post.
### Write the image to your boot medium 
  1. Notice: This procedure will write the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. onto your device.
     * This means you will lose all the data as well as the previously installed operating system.
     * Back up your data before continuing with the next step.
  2. Attach the Home Assistant boot medium (eMMC module or SD card) to your computer.
If you are using ODROID-M1, note that booting from NVMe is not supported. If you want to boot from eMMC, before installing the image.
If you are using a or ODROID-N2+, you can .
If you are using an ODROID-M1S, you need to follow this guide to .
  3. Download and start . You may need to run it with administrator privileges on Windows.
  4. Download the image to your computer.
     * Copy the URL for the image.
     * If there are multiple links below, make sure to select the correct link for your version of ODROID.
ODROID-N2
ODROID-N2+
ODROID-C2
ODROID-C4
ODROID-M1
ODROID-M1S
```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_odroid-n2-16.3.img.xz
```

Text
Copy
```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_odroid-n2-16.3.img.xz
```

Text
Copy
```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_odroid-c2-16.3.img.xz
```

Text
Copy
```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_odroid-c4-16.3.img.xz
```

Text
Copy
```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_odroid-m1-16.3.img.xz
```

Text
Copy
```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_odroid-m1s-16.3.img.xz
```

Text
Copy
```
*Select and copy the URL or use the "copy" button that appears when you hover it.*

```

    1. Paste the URL into your browser to start the download.
    2. Extract the file you just downloaded.
    3. Select Flash from file and select the image you just extracted. 
       * Do not use Flash from URL. It does not work on some systems. 
    4. Select target. 
    5. Select the boot medium (eMMC module or SD card) you want to use for your installation. 
    6. Select Flash! to start writing the image. 
       * If the operation fails, decompress the .xz file and try again. 
       * When Balena Etcher has finished writing the image, you will see a confirmation. 
### Start up your ODROID 
    1. Insert the boot medium (eMMC module or SD card) you just created.
    2. Plug in an Ethernet cable that is connected to the network and to the internet and power the system on.
       * Note: Internet is required because the newly installed Home Assistant OS does not contain all Home Assistant components yet. It downloads the latest version of Home Assistant Core on first start.
    3. In the browser of your desktop system, within a few minutes you will be able to reach your new Home Assistant at .
Note
If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your ODROID’s IP address).
With the Home Assistant Operating System installed and accessible, you can continue with onboarding.
## Flashing an ODROID-N2+ 
Home Assistant can be flashed to an ODROID-N2+ by connecting the device directly to your computer via the USB-OTG connection on the front of the board. The device contains the Petitboot bootloader, which allows the ODROID-N2+ storage to show up as it were a USB drive.
All these instructions work the same for the ODROID-N2 (non-plus version).
### What you will need 
To flash your eMMC using Petitboot and OTG-USB, you will need the following items:
### Enabling SPI boot mode 
To enable the SPI boot mode:
    1. Power off the ODROID-N2+ by unplugging the power cable.
    2. Remove the case.
    3. Locate the toggle for boot mode and switch it from MMC to SPI.
    4. Connect the ODROID-N2+ directly to your computer via the USB-OTG port located on the front of the board.
    5. Connect a USB keyboard and a monitor (using HDMI) to your ODROID-N2+.
    6. Plug in the power cable to power on the ODROID-N2+.
### Enabling USB drive mode 
After The ODROID-N2+ is set to SPI boot mode and powered on, it boots into a terminal. To enable the USB drive mode:
    1. Select Exit to shell from the menu.
Note
When using the command line, it may return the following message: can't access tty; job control turned off. You can safely ignore this message and proceed with the installation
    1. Use the following command at the console to confirm the storage device node:
```
ls /dev/mmc*
```

Bash
Copy
    2. Set the storage device on the ODROID-N2+ as a mass storage device using the ums command (USB Mass storage mode). This will configure the ODROID-N2+ and OTG to act as a memory card reader:
```
ums /dev/mmcblk0
```

Bash
Copy
### Flashing Home Assistant 
    1. Connect the ODROID-N2+ to your PC via the micro-USB port at the front of the ODROID-N2+.
    2. When the ODROID-N2 is recognized as a USB connected storage device, you can flash the eMMC with .
       * Use the latest stable version of Home Assistant OS for the (haos_odroid-n2-16.3.img.xz).
       * In Balena, use Flash from file. Flash from URL does not work on all systems.
    3. When the flash process is complete, disconnect the ODROID-N2+ from your PC.
       * Remove the power cable.
       * Remove the USB and HDMI cables.
       * Make sure to toggle the boot mode switch back to MMC.
    4. Put the ODROID back in its case.
    5. Connect your ODROID-N2+ to your network with an Ethernet cable, make sure there is internet access, and plug in power.
    6. If your router supports mDNS, you can reach your installation at http://homeassistant.local:8123.
       * If your network doesn’t support mDNS, you’ll have to use the IP address of your ODROID-N2+ instead of homeassistant.local. For example, http://192.168.0.9:8123.
       * You should be able to find the IP address of your ODROID-N2+ from the admin interface of your router.
    7. Continue with .
## Flashing an ODROID-M1S 
Home Assistant can be flashed to an ODROID-M1S by connecting the device directly to your computer via the USB-OTG connection on the front of the board. Unlike other ODROID boards, the M1S does not have a socket for an optional eMMC module. It also does not have a separate flash chip that holds a dedicated bootloader. Instead, the M1S has a build-in 64GB eMMC soldered directly on the board that holds a bootloader by default. This guide will show you how to install the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. to the built-in eMMC.
Warning: Installing Home Assistant OS replaces the firmware and SPL on the eMMC with the mainline version provided by the Home Assistant OS. As a result, it is not possible to use the SD card with the EMMC2UMS image anymore, because the mainline SPL is not compatible with U-Boot in the EMMC2UMS image at this time (February 2024). This does not pose any problem for standard use, just makes it more complicated in case you want to return to the Hardkernel-provided OS (see ).
### What you will need 
To flash your eMMC using USB-OTG, you will need the following items:
### Boot into mass-storage mode 
(These steps are identical to the official page.)
    1. Download .
    2. Use or another tool to flash the UMS utility onto an SD card. 
       * Use Flash from file. Flash from URL does not work on all systems. (balena Etcher will complain that something went wrong during flashing. You can ignore this message)
    3. Plug-in that SD card to your ODROID-M1S and boot it.
### Flashing Home Assistant M1S 
    1. Download the latest stable version of Home Assistant OS for the .
    2. Apart from the HAOS image to flash (M1S instead of N2+ version), you can follow the N2+ step-by-step flashing guide .
#### HK Recovery 
If you want to restore your M1S back into Hardkernel’s initial state, you will have to restore the HK’s bootloader. A reliable way of reflashing the eMMC with an operating system of your choice is to use Home Assistant OS to flash the EMMC2UMS image which turns the ODROID-M1S into USB Mass Storage device. Once you have flashed the EMMC2UMS image, you can flash any OS again. You will need a micro USB cable to connect ODROID-M1S to PC.
Note: This commands will render your current Home Assistant OS installation unbootable!
Use the local terminal (HDMI/keyboard) to access the system console. On the Home Assistant CLI (command line), enter login to enter the root shell and use curl to download an image and dd it to the eMMC block device:
```
curl -L -A "Mozilla/5.0" https://dn.odroid.com/RK3566/ODROID-M1S/Installer/ODROID-M1S_EMMC2UMS.img | sudo dd of=/dev/mmcblk0 bs=4M status=progress conv=fsync
```

Sh
Copy
This way, the device will start in the UMS mode on the next boot with the SD card removed. Follow the to install a different operating system.
## Install Home Assistant Container 
These below instructions are for an installation of Home Assistant ContainerHome Assistant Container is a standalone container-based installation of Home Assistant Core. Any OCI compatible runtime can be used, but the documentation focus is on Docker. [Learn more] running in your own container environment, which you manage yourself. Any compatible runtime can be used, however this guide will focus on installing it with Docker.
Note
This installation type does not have access to add-ons. If you want to use add-ons, you need to use another installation type. The recommended type is Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users.. Checkout the to see the differences.
Important
Prerequisites This guide assumes that you already have an operating system setup and a container runtime installed (like Docker).
If you are using Docker then you need to be on at least version 19.03.9, ideally an even higher version, and libseccomp 2.4.2 or newer. Docker Desktop will not work, you must use Docker Engine.
### Platform installation 
Installation with Docker is straightforward. Adjust the following command so that:


#  Getting started
#  On this page



## Troubleshooting installation problems - Home Assistant

Source: https://www.home-assistant.io/installation/troubleshooting/

#  On this page
It can happen that you run into trouble while installing and onboarding Home Assistant. This page is here to help you solve the most common problems.
## Can’t access Home Assistant in my browser 
### Symptom: “This site can’t be reached” 
When trying to access Home Assistant in the browser, the browser shows the message “This site can’t be reached”.
### Description 
This means the browser can’t find your Home Assistant installation on the network.
### Resolution 
To resolve this issue, try the following steps:
  1. Make sure your Home Assistant device is powered up (LEDs are on).
  2. Make sure your Home Assistant installation is connected to the internet: 
  3. Make sure the system on which you opened the browser to access Home Assistant is connected to the same network as Home Assistant. 
     * For example, if the system your Browser runs on is using Wi-Fi, make sure it is using the same Wi-Fi Home Assistant is connected to.
  4. Make sure you typed the address correctly. 
     * Especially if the message includes the error code “ERR_CONNECTION_REFUSED”, it is likely that there was a typo in the port part of the URL (:8123).
     * Typically, the URL is .
     * If you are running an older Windows version or have a stricter network configuration, try instead.
  5. The system might still be starting up. Wait for a couple of minutes and refresh the page. 
     * Refreshing might work differently depending on your browser. Look for the refresh icon, or press CTRL+R or CTRL+SHIFT+R.
  6. Check your router’s web interface to see what IP address is assigned to your Home Assistant installation. 
     * Enter this IP address (http://x.x.x.x:8123) directly into your browser.
  7. If you still can’t reach Home Assistant, connect keyboard and monitor to the device Home Assistant is running on to access the console and see where Home Assistant gets stuck. 
     * If you are using a Home Assistant Green, follow these steps .
     * If you are using a Home Assistant Yellow, follow these steps , or .
  8. .


## “Error installing Home Assistant” 
### Symptom: During onboarding, there is an “Error installing Home Assistant” 
You are in the onboarding procedure, but you get the message Error installing Home Assistant.
### Resolution 
  1. Make sure your network has internet access. 
  2. After changing your network environment, wait a few minutes. Home Assistant will try to reconnect.
  3. .


## Stuck at “Preparing Home Assistant” 
### Symptom: Onboarding seems stuck at “Preparing Home Assistant” 
You are in the onboarding procedure, but the process seems stuck at the step Preparing Home Assistant.
### Resolution 
  1. Select Show details to view the log files. 
     * The log files might provide more information on the current status.
  2. Make sure your network has internet access. 
  3. After changing your network environment, wait a few minutes. Home Assistant will try to reconnect.
  4. .


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Getting started
#  On this page



## macOS - Home Assistant

Source: https://www.home-assistant.io/installation/macos

#  On this page
## Install Home Assistant Operating System 
### Download the appropriate image 
  * (.vdi)
  * (.vmdk)


After downloading, decompress the image. If the image comes in a ZIP file, for example, unzip it.
Follow this guide if you already are running a supported virtual machine hypervisor. If you are not familiar with virtual machines, install Home Assistant OS directly on a , a , or an .
  * If VirtualBox is not supported on your Mac, and you have experience using virtual machines, you can try running the Home Assistant Operating System on .


### Create the virtual machine 
Load the appliance image into your virtual machine hypervisor. (Note: You are free to assign as much resources as you wish to the VM, please assign enough based on your add-on needs).
Minimum recommended assignments:
  * 2 GB RAM
  * 32 GB Storage
  * 2vCPU


All these can be extended if your usage calls for more resources.
### Hypervisor specific configuration 
VirtualBox
  1. Create a new virtual machine.
  2. Select type Linux, subtype Oracle Linux and version Oracle Linux (64-bit) or Oracle Linux (ARM 64-bit) depending on your hardware.
  3. Under Hardware, select the amount of memory and number of CPUs. Then, select Enable EFI. 
     * Make sure EFI is enabled. If EFI is not enabled, HAOS won’t boot.
  4. Under Hard Disk, select Use an existing virtual hard disk file, select the unzipped VDI file from above.
  5. Then go to Network > Adapter 1. Choose Bridged Adapter and choose your network adapter (i.e. en0:Wi-Fi).
  6. Then go to Audio and choose Intel HD Audio as audio controller.


By default, VirtualBox does not free up unused disk space. To automatically shrink the vdi disk image the discard option must be enabled using your host machine’s terminal:
```
VBoxManage storageattach <VM name> --storagectl "SATA" --port 0 --device 0 --nonrotational on --discard on
```

Bash
Copy
More details can be found about the command can be found .
### Start up your virtual machine 
  1. Start the virtual machine.
  2. Observe the boot process of the Home Assistant Operating System.
  3. Once completed, you will be able to reach Home Assistant on . If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your virtual machine’s IP address).


With the Home Assistant Operating System installed and accessible, you can continue with onboarding.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Getting started
#  On this page



## macOS - Home Assistant

Source: https://www.home-assistant.io/installation/macos/

#  On this page
## Install Home Assistant Operating System 
### Download the appropriate image 
  * (.vdi)
  * (.vmdk)


After downloading, decompress the image. If the image comes in a ZIP file, for example, unzip it.
Follow this guide if you already are running a supported virtual machine hypervisor. If you are not familiar with virtual machines, install Home Assistant OS directly on a , a , or an .
  * If VirtualBox is not supported on your Mac, and you have experience using virtual machines, you can try running the Home Assistant Operating System on .


### Create the virtual machine 
Load the appliance image into your virtual machine hypervisor. (Note: You are free to assign as much resources as you wish to the VM, please assign enough based on your add-on needs).
Minimum recommended assignments:
  * 2 GB RAM
  * 32 GB Storage
  * 2vCPU


All these can be extended if your usage calls for more resources.
### Hypervisor specific configuration 
VirtualBox
  1. Create a new virtual machine.
  2. Select type Linux, subtype Oracle Linux and version Oracle Linux (64-bit) or Oracle Linux (ARM 64-bit) depending on your hardware.
  3. Under Hardware, select the amount of memory and number of CPUs. Then, select Enable EFI. 
     * Make sure EFI is enabled. If EFI is not enabled, HAOS won’t boot.
  4. Under Hard Disk, select Use an existing virtual hard disk file, select the unzipped VDI file from above.
  5. Then go to Network > Adapter 1. Choose Bridged Adapter and choose your network adapter (i.e. en0:Wi-Fi).
  6. Then go to Audio and choose Intel HD Audio as audio controller.


By default, VirtualBox does not free up unused disk space. To automatically shrink the vdi disk image the discard option must be enabled using your host machine’s terminal:
```
VBoxManage storageattach <VM name> --storagectl "SATA" --port 0 --device 0 --nonrotational on --discard on
```

Bash
Copy
More details can be found about the command can be found .
### Start up your virtual machine 
  1. Start the virtual machine.
  2. Observe the boot process of the Home Assistant Operating System.
  3. Once completed, you will be able to reach Home Assistant on . If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your virtual machine’s IP address).


With the Home Assistant Operating System installed and accessible, you can continue with onboarding.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Getting started
#  On this page



## ODROID - Home Assistant

Source: https://www.home-assistant.io/installation/odroid

#  On this page
## Install Home Assistant Operating System 
Follow this guide if you want to get started with Home Assistant easily or if you have little to no Linux experience.
## Suggested hardware 
You will need a few things to get started with installing Home Assistant. The links below lead to Ameridroid. If you’re not in the US, you should be able to find these items in web stores in your country.
To get started, we suggest the ODROID-N2+, the board that powers our , or the ODROID-M1.
If unavailable, we also recommend the .
Home Assistant bundles (US market):
The bundles come with Home Assistant pre-installed.
  * ODROID-M1: 4 GB RAM / 256 GB NVMe / or 
  * ODROID-M1: 8 GB RAM / 256 GB NVMe / or 


Variants without pre-installed Home Assistant:
  * ODROID-N2+, or 
  * ODROID-M1S, or 


Related components:
These are affiliated links. We get commissions for purchases made through links in this post.
### Write the image to your boot medium 
  1. Notice: This procedure will write the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. onto your device.
     * This means you will lose all the data as well as the previously installed operating system.
     * Back up your data before continuing with the next step.
  2. Attach the Home Assistant boot medium (eMMC module or SD card) to your computer.
If you are using ODROID-M1, note that booting from NVMe is not supported. If you want to boot from eMMC, before installing the image.
If you are using a or ODROID-N2+, you can .
If you are using an ODROID-M1S, you need to follow this guide to .
  3. Download and start . You may need to run it with administrator privileges on Windows.
  4. Download the image to your computer.
     * Copy the URL for the image.
     * If there are multiple links below, make sure to select the correct link for your version of ODROID.
ODROID-N2
ODROID-N2+
ODROID-C2
ODROID-C4
ODROID-M1
ODROID-M1S
```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_odroid-n2-16.3.img.xz

```

```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_odroid-n2-16.3.img.xz

```

```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_odroid-c2-16.3.img.xz

```

```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_odroid-c4-16.3.img.xz

```

```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_odroid-m1-16.3.img.xz

```

```
https://github.com/home-assistant/operating-system/releases/download/16.3/haos_odroid-m1s-16.3.img.xz

```

```
*Select and copy the URL or use the "copy" button that appears when you hover it.*

```

    1. Paste the URL into your browser to start the download.
    2. Extract the file you just downloaded.
    3. Select Flash from file and select the image you just extracted. 
       * Do not use Flash from URL. It does not work on some systems. 
    4. Select target. 
    5. Select the boot medium (eMMC module or SD card) you want to use for your installation. 
    6. Select Flash! to start writing the image. 
       * If the operation fails, decompress the .xz file and try again. 
       * When Balena Etcher has finished writing the image, you will see a confirmation. 
### Start up your ODROID 
    1. Insert the boot medium (eMMC module or SD card) you just created.
    2. Plug in an Ethernet cable that is connected to the network and to the internet and power the system on.
       * Note: Internet is required because the newly installed Home Assistant OS does not contain all Home Assistant components yet. It downloads the latest version of Home Assistant Core on first start.
    3. In the browser of your desktop system, within a few minutes you will be able to reach your new Home Assistant at .
Note
If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your ODROID’s IP address).
With the Home Assistant Operating System installed and accessible, you can continue with onboarding.
## Flashing an ODROID-N2+ 
Home Assistant can be flashed to an ODROID-N2+ by connecting the device directly to your computer via the USB-OTG connection on the front of the board. The device contains the Petitboot bootloader, which allows the ODROID-N2+ storage to show up as it were a USB drive.
All these instructions work the same for the ODROID-N2 (non-plus version).
### What you will need 
To flash your eMMC using Petitboot and OTG-USB, you will need the following items:
### Enabling SPI boot mode 
To enable the SPI boot mode:
    1. Power off the ODROID-N2+ by unplugging the power cable.
    2. Remove the case.
    3. Locate the toggle for boot mode and switch it from MMC to SPI.
    4. Connect the ODROID-N2+ directly to your computer via the USB-OTG port located on the front of the board.
    5. Connect a USB keyboard and a monitor (using HDMI) to your ODROID-N2+.
    6. Plug in the power cable to power on the ODROID-N2+.
### Enabling USB drive mode 
After The ODROID-N2+ is set to SPI boot mode and powered on, it boots into a terminal. To enable the USB drive mode:
    1. Select Exit to shell from the menu.
Note
When using the command line, it may return the following message: can't access tty; job control turned off. You can safely ignore this message and proceed with the installation
    1. Use the following command at the console to confirm the storage device node:
```
ls /dev/mmc*

```

    2. Set the storage device on the ODROID-N2+ as a mass storage device using the ums command (USB Mass storage mode). This will configure the ODROID-N2+ and OTG to act as a memory card reader:
```
ums /dev/mmcblk0

```

### Flashing Home Assistant 
    1. Connect the ODROID-N2+ to your PC via the micro-USB port at the front of the ODROID-N2+.
    2. When the ODROID-N2 is recognized as a USB connected storage device, you can flash the eMMC with .
       * Use the latest stable version of Home Assistant OS for the (haos_odroid-n2-16.3.img.xz).
       * In Balena, use Flash from file. Flash from URL does not work on all systems.
    3. When the flash process is complete, disconnect the ODROID-N2+ from your PC.
       * Remove the power cable.
       * Remove the USB and HDMI cables.
       * Make sure to toggle the boot mode switch back to MMC.
    4. Put the ODROID back in its case.
    5. Connect your ODROID-N2+ to your network with an Ethernet cable, make sure there is internet access, and plug in power.
    6. If your router supports mDNS, you can reach your installation at http://homeassistant.local:8123.
       * If your network doesn’t support mDNS, you’ll have to use the IP address of your ODROID-N2+ instead of homeassistant.local. For example, http://192.168.0.9:8123.
       * You should be able to find the IP address of your ODROID-N2+ from the admin interface of your router.
    7. Continue with .
## Flashing an ODROID-M1S 
Home Assistant can be flashed to an ODROID-M1S by connecting the device directly to your computer via the USB-OTG connection on the front of the board. Unlike other ODROID boards, the M1S does not have a socket for an optional eMMC module. It also does not have a separate flash chip that holds a dedicated bootloader. Instead, the M1S has a build-in 64GB eMMC soldered directly on the board that holds a bootloader by default. This guide will show you how to install the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. to the built-in eMMC.
Warning: Installing Home Assistant OS replaces the firmware and SPL on the eMMC with the mainline version provided by the Home Assistant OS. As a result, it is not possible to use the SD card with the EMMC2UMS image anymore, because the mainline SPL is not compatible with U-Boot in the EMMC2UMS image at this time (February 2024). This does not pose any problem for standard use, just makes it more complicated in case you want to return to the Hardkernel-provided OS (see ).
### What you will need 
To flash your eMMC using USB-OTG, you will need the following items:
### Boot into mass-storage mode 
(These steps are identical to the official page.)
    1. Download .
    2. Use or another tool to flash the UMS utility onto an SD card. 
       * Use Flash from file. Flash from URL does not work on all systems. (balena Etcher will complain that something went wrong during flashing. You can ignore this message)
    3. Plug-in that SD card to your ODROID-M1S and boot it.
### Flashing Home Assistant M1S 
    1. Download the latest stable version of Home Assistant OS for the .
    2. Apart from the HAOS image to flash (M1S instead of N2+ version), you can follow the N2+ step-by-step flashing guide .
#### HK Recovery 
If you want to restore your M1S back into Hardkernel’s initial state, you will have to restore the HK’s bootloader. A reliable way of reflashing the eMMC with an operating system of your choice is to use Home Assistant OS to flash the EMMC2UMS image which turns the ODROID-M1S into USB Mass Storage device. Once you have flashed the EMMC2UMS image, you can flash any OS again. You will need a micro USB cable to connect ODROID-M1S to PC.
Note: This commands will render your current Home Assistant OS installation unbootable!
Use the local terminal (HDMI/keyboard) to access the system console. On the Home Assistant CLI (command line), enter login to enter the root shell and use curl to download an image and dd it to the eMMC block device:
```
curl -L -A "Mozilla/5.0" https://dn.odroid.com/RK3566/ODROID-M1S/Installer/ODROID-M1S_EMMC2UMS.img | sudo dd of=/dev/mmcblk0 bs=4M status=progress conv=fsync

```

This way, the device will start in the UMS mode on the next boot with the SD card removed. Follow the to install a different operating system.
## Install Home Assistant Container 
These below instructions are for an installation of Home Assistant ContainerHome Assistant Container is a standalone container-based installation of Home Assistant Core. Any OCI compatible runtime can be used, but the documentation focus is on Docker. [Learn more] running in your own container environment, which you manage yourself. Any compatible runtime can be used, however this guide will focus on installing it with Docker.
Note
This installation type does not have access to add-ons. If you want to use add-ons, you need to use another installation type. The recommended type is Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users.. Checkout the to see the differences.
Important
Prerequisites This guide assumes that you already have an operating system setup and a container runtime installed (like Docker).
If you are using Docker then you need to be on at least version 19.03.9, ideally an even higher version, and libseccomp 2.4.2 or newer. Docker Desktop will not work, you must use Docker Engine.
### Platform installation 
Installation with Docker is straightforward. Adjust the following command so that:


#  Getting started
#  On this page



## Linux - Home Assistant

Source: https://www.home-assistant.io/installation/linux/

#  On this page
## Install Home Assistant Operating System 
### Download the appropriate image 
  * (.vdi)
  * (.qcow2)


After downloading, decompress the image. If the image comes in a ZIP file, for example, unzip it.
Follow this guide if you already are running a supported virtual machine hypervisor. If you are not familiar with virtual machines, install Home Assistant OS directly on a , a , or an .
### Create the virtual machine 
Load the appliance image into your virtual machine hypervisor. (Note: You are free to assign as much resources as you wish to the VM, please assign enough based on your add-on needs).
Minimum recommended assignments:
  * 2 GB RAM
  * 32 GB Storage
  * 2vCPU


All these can be extended if your usage calls for more resources.
### Hypervisor specific configuration 
VirtualBox
Unraid
KVM (virt-manager)
KVM (virt-install)
  1. Create a new virtual machine.
  2. Select type Linux, subtype Oracle Linux and version Oracle Linux (64-bit) or Oracle Linux (ARM 64-bit) depending on your hardware.
  3. Under Hardware, select the amount of memory and number of CPUs. Then, select Enable EFI. 
     * Make sure EFI is enabled. If EFI is not enabled, HAOS won’t boot.
  4. Under Hard Disk, select Use an existing virtual hard disk file, select the unzipped VDI file from above.
  5. Then go to Network > Adapter 1. Choose Bridged Adapter and choose your network adapter (i.e. en0:Wi-Fi).
  6. Then go to Audio and choose Intel HD Audio as audio controller.


By default, VirtualBox does not free up unused disk space. To automatically shrink the vdi disk image the discard option must be enabled using your host machine’s terminal:
```
VBoxManage storageattach <VM name> --storagectl "SATA" --port 0 --device 0 --nonrotational on --discard on
```

Bash
Copy
More details can be found about the command can be found .
  1. Download the .qcow2 image above and decompress it. (Extract all in Windows)
  2. Store the image in the isos share on your server.
  3. Make sure under Settings > VM manager, Enable VMs is enabled.
  4. Create a new virtual machine: VMS > Add VM.
  5. Select type Linux and give the VM a name and a description.
  6. Select the CPU cores you want to let the VM use and give it some memory.
  7. Under Primary vDisk Location, select Manual and then select the qcow2 image.
  8. Select your keyboard language under VM Console Keyboard.
  9. Select br0 under Network Source.
  10. Select virtio under Network model.
  11. Select any USB-devices that you want to pass through to Home Assistant, such as Zigbee- or Z-Wave controllers.
  12. Deselect Start VM after creation.
  13. Select Create.
  14. Select the name of your new VM and select the capacity number for your disk. Here, you can expand the disk to whatever your needs are. The default is 32 GB.
  15. Select the icon of your new VM and select start with console (VNC).


  1. Create a new virtual machine in virt-manager.
  2. Select Import existing disk image, provide the path to the QCOW2 image above.
  3. Choose Generic Default for the operating system.
  4. Check the box for Customize configuration before install.
  5. Under Network Selection, select your bridge.
  6. Under customization select Overview > Firmware > UEFI x86_64: …. Make sure to select a non-secureboot version of OVMF (does not contain the word secure, secboot, etc.), e.g., /usr/share/edk2/ovmf/OVMF_CODE.fd.
  7. Click Add Hardware (bottom left), and select Channel.
  8. Select device type: unix.
  9. Select name: org.qemu.guest_agent.0.
  10. Finally, select Begin Installation (upper left corner).


```
virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk <PATH TO QCOW2 FILE>,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi
```

Bash
Copy
If you have a USB dongle to attach, you need to add the option --hostdev busID.deviceId. You can discover these IDs via the lsusb command. As example, if lsusb output is:
```
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 004: ID 30c9:0052 Luxvisions Innotech Limited Integrated RGB Camera
Bus 003 Device 003: ID 1a86:55d4 QinHeng Electronics SONOFF Zigbee 3.0 USB Dongle Plus V2
Bus 003 Device 002: ID 06cb:00fc Synaptics, Inc.
Bus 003 Device 005: ID 8087:0033 Intel Corp.
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

Bash
Copy
You can recognize the Sonoff dongle at Bus 003 Device 003. So the command to install the VM will become:
```
virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk <PATH TO QCOW2 FILE>,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi --hostdev 003.003
```

Bash
Copy
Note that this configuration (bus 003, device 003) is just an example, your dongle could be on another bus and/or with another device ID. Please check the correct IDs of your USB dongle with lsusb.
### Start up your virtual machine 
  1. Start the virtual machine.
  2. Observe the boot process of the Home Assistant Operating System.
  3. Once completed, you will be able to reach Home Assistant on . If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your virtual machine’s IP address).


With the Home Assistant Operating System installed and accessible, you can continue with onboarding.
## Install Home Assistant Container 
These below instructions are for an installation of Home Assistant ContainerHome Assistant Container is a standalone container-based installation of Home Assistant Core. Any OCI compatible runtime can be used, but the documentation focus is on Docker. [Learn more] running in your own container environment, which you manage yourself. Any compatible runtime can be used, however this guide will focus on installing it with Docker.
Note
This installation type does not have access to add-ons. If you want to use add-ons, you need to use another installation type. The recommended type is Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users.. Checkout the to see the differences.
Important
Prerequisites This guide assumes that you already have an operating system setup and a container runtime installed (like Docker).
If you are using Docker then you need to be on at least version 19.03.9, ideally an even higher version, and libseccomp 2.4.2 or newer. Docker Desktop will not work, you must use Docker Engine.
### Platform installation 
Installation with Docker is straightforward. Adjust the following command so that:
#  Getting started
#  On this page



## Windows - Home Assistant

Source: https://www.home-assistant.io/installation/windows

#  On this page
## Install Home Assistant Operating System 
### Download the appropriate image 
  * (.vdi)
  * (.vmdk)
  * (.vhdx)


After downloading, decompress the image. If the image comes in a ZIP file, for example, unzip it.
Follow this guide if you already are running a supported virtual machine hypervisor. If you are not familiar with virtual machines, install Home Assistant OS directly on a , a , or an .
### Create the virtual machine 
Load the appliance image into your virtual machine hypervisor. (Note: You are free to assign as much resources as you wish to the VM, please assign enough based on your add-on needs).
Minimum recommended assignments:
  * 2 GB RAM
  * 32 GB Storage
  * 2vCPU


All these can be extended if your usage calls for more resources.
### Hypervisor specific configuration 
VirtualBox
Unraid
KVM (virt-manager)
KVM (virt-install)
VMware Workstation
Hyper-V
  1. Create a new virtual machine.
  2. Select type Linux, subtype Oracle Linux and version Oracle Linux (64-bit) or Oracle Linux (ARM 64-bit) depending on your hardware.
  3. Under Hardware, select the amount of memory and number of CPUs. Then, select Enable EFI. 
     * Make sure EFI is enabled. If EFI is not enabled, HAOS won’t boot.
  4. Under Hard Disk, select Use an existing virtual hard disk file, select the unzipped VDI file from above.
  5. Then go to Network > Adapter 1. Choose Bridged Adapter and choose your network adapter (i.e. en0:Wi-Fi).
  6. Then go to Audio and choose Intel HD Audio as audio controller.


By default, VirtualBox does not free up unused disk space. To automatically shrink the vdi disk image the discard option must be enabled using your host machine’s terminal:
```
VBoxManage storageattach <VM name> --storagectl "SATA" --port 0 --device 0 --nonrotational on --discard on
```

Bash
Copy
More details can be found about the command can be found .
  1. Download the .qcow2 image above and decompress it. (Extract all in Windows)
  2. Store the image in the isos share on your server.
  3. Make sure under Settings > VM manager, Enable VMs is enabled.
  4. Create a new virtual machine: VMS > Add VM.
  5. Select type Linux and give the VM a name and a description.
  6. Select the CPU cores you want to let the VM use and give it some memory.
  7. Under Primary vDisk Location, select Manual and then select the qcow2 image.
  8. Select your keyboard language under VM Console Keyboard.
  9. Select br0 under Network Source.
  10. Select virtio under Network model.
  11. Select any USB-devices that you want to pass through to Home Assistant, such as Zigbee- or Z-Wave controllers.
  12. Deselect Start VM after creation.
  13. Select Create.
  14. Select the name of your new VM and select the capacity number for your disk. Here, you can expand the disk to whatever your needs are. The default is 32 GB.
  15. Select the icon of your new VM and select start with console (VNC).


  1. Create a new virtual machine in virt-manager.
  2. Select Import existing disk image, provide the path to the QCOW2 image above.
  3. Choose Generic Default for the operating system.
  4. Check the box for Customize configuration before install.
  5. Under Network Selection, select your bridge.
  6. Under customization select Overview > Firmware > UEFI x86_64: …. Make sure to select a non-secureboot version of OVMF (does not contain the word secure, secboot, etc.), e.g., /usr/share/edk2/ovmf/OVMF_CODE.fd.
  7. Click Add Hardware (bottom left), and select Channel.
  8. Select device type: unix.
  9. Select name: org.qemu.guest_agent.0.
  10. Finally, select Begin Installation (upper left corner).


```
virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk <PATH TO QCOW2 FILE>,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi
```

Bash
Copy
If you have a USB dongle to attach, you need to add the option --hostdev busID.deviceId. You can discover these IDs via the lsusb command. As example, if lsusb output is:
```
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 004: ID 30c9:0052 Luxvisions Innotech Limited Integrated RGB Camera
Bus 003 Device 003: ID 1a86:55d4 QinHeng Electronics SONOFF Zigbee 3.0 USB Dongle Plus V2
Bus 003 Device 002: ID 06cb:00fc Synaptics, Inc.
Bus 003 Device 005: ID 8087:0033 Intel Corp.
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

Bash
Copy
You can recognize the Sonoff dongle at Bus 003 Device 003. So the command to install the VM will become:
```
virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk <PATH TO QCOW2 FILE>,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi --hostdev 003.003
```

Bash
Copy
Note that this configuration (bus 003, device 003) is just an example, your dongle could be on another bus and/or with another device ID. Please check the correct IDs of your USB dongle with lsusb.
  1. Start VMware Workstation and select Create a New Virtual Machine. 
     * Note: the exact name and location of the settings below depend on the VMware version. This procedure is based on version 17.
  2. Select I will install the operating system later, then select Linux > Other Linux 5.x kernel 64-bit.
  3. Give the VM a name, home-assistant, and define an easy to reach storage location, such as C:\home-assistant.
  4. Specify the disk size and select Store virtual disk as a single file.
  5. Select Customize Hardware.
  6. Define the amount of memory and the number of cores the VM is allowed to use.
  7. Remove the New CD/DVD entry. It will not be used.
  8. Connect an Ethernet cable and make sure it is connected to your network.
  9. Under Network adapter, select Bridged: Connected directly to the physical network. 
  10. At the end of the wizard, select Finish.


## Edit the VM settings 
  1. In Windows Explorer, navigate to the storage location of your newly created VM, for example under C:\home-assistant.
  2. Delete the home-assistant.vmdk file.
  3. In the Downloads folder, find the haos_ova_xx.x.vmdk file. 
     * If you haven’t unzipped the archive, unzip it.
     * Within the folder, find the .vmdk file and rename it to home-assistant.vmdk.
     * Paste the file (not the unzipped folder) into the C:\home-assistant folder.
  4. Right-click the .vmx file and select Open with > Notepad.
  5. Under .encoding, add a line. Enter firmware = "efi".
  6. Now continue with the next step to start your VM. 
     * If you see a message about side channel mitigations, select OK.
     * If you see a message stating that the .vmdk file could not be found, in step 3, you likely pasted the folder, not the file. Repeat step 3.


⚠️ Hyper-V does not have USB support
  1. Create a new virtual machine.
  2. Select Generation 2.
  3. Select Connection > Your Virtual Switch that is bridged.
  4. Select Use an existing virtual hard disk and select the VHDX file from above.


After creation, go to Settings > Security and deselect Enable Secure Boot.
### Start up your virtual machine 
  1. Start the virtual machine.
  2. Observe the boot process of the Home Assistant Operating System.
  3. Once completed, you will be able to reach Home Assistant on . If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your virtual machine’s IP address).


With the Home Assistant Operating System installed and accessible, you can continue with onboarding.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Getting started
#  On this page



## Windows - Home Assistant

Source: https://www.home-assistant.io/installation/windows/

#  On this page
## Install Home Assistant Operating System 
### Download the appropriate image 
  * (.vdi)
  * (.vmdk)
  * (.vhdx)


After downloading, decompress the image. If the image comes in a ZIP file, for example, unzip it.
Follow this guide if you already are running a supported virtual machine hypervisor. If you are not familiar with virtual machines, install Home Assistant OS directly on a , a , or an .
### Create the virtual machine 
Load the appliance image into your virtual machine hypervisor. (Note: You are free to assign as much resources as you wish to the VM, please assign enough based on your add-on needs).
Minimum recommended assignments:
  * 2 GB RAM
  * 32 GB Storage
  * 2vCPU


All these can be extended if your usage calls for more resources.
### Hypervisor specific configuration 
VirtualBox
Unraid
KVM (virt-manager)
KVM (virt-install)
VMware Workstation
Hyper-V
  1. Create a new virtual machine.
  2. Select type Linux, subtype Oracle Linux and version Oracle Linux (64-bit) or Oracle Linux (ARM 64-bit) depending on your hardware.
  3. Under Hardware, select the amount of memory and number of CPUs. Then, select Enable EFI. 
     * Make sure EFI is enabled. If EFI is not enabled, HAOS won’t boot.
  4. Under Hard Disk, select Use an existing virtual hard disk file, select the unzipped VDI file from above.
  5. Then go to Network > Adapter 1. Choose Bridged Adapter and choose your network adapter (i.e. en0:Wi-Fi).
  6. Then go to Audio and choose Intel HD Audio as audio controller.


By default, VirtualBox does not free up unused disk space. To automatically shrink the vdi disk image the discard option must be enabled using your host machine’s terminal:
```
VBoxManage storageattach <VM name> --storagectl "SATA" --port 0 --device 0 --nonrotational on --discard on
```

Bash
Copy
More details can be found about the command can be found .
  1. Download the .qcow2 image above and decompress it. (Extract all in Windows)
  2. Store the image in the isos share on your server.
  3. Make sure under Settings > VM manager, Enable VMs is enabled.
  4. Create a new virtual machine: VMS > Add VM.
  5. Select type Linux and give the VM a name and a description.
  6. Select the CPU cores you want to let the VM use and give it some memory.
  7. Under Primary vDisk Location, select Manual and then select the qcow2 image.
  8. Select your keyboard language under VM Console Keyboard.
  9. Select br0 under Network Source.
  10. Select virtio under Network model.
  11. Select any USB-devices that you want to pass through to Home Assistant, such as Zigbee- or Z-Wave controllers.
  12. Deselect Start VM after creation.
  13. Select Create.
  14. Select the name of your new VM and select the capacity number for your disk. Here, you can expand the disk to whatever your needs are. The default is 32 GB.
  15. Select the icon of your new VM and select start with console (VNC).


  1. Create a new virtual machine in virt-manager.
  2. Select Import existing disk image, provide the path to the QCOW2 image above.
  3. Choose Generic Default for the operating system.
  4. Check the box for Customize configuration before install.
  5. Under Network Selection, select your bridge.
  6. Under customization select Overview > Firmware > UEFI x86_64: …. Make sure to select a non-secureboot version of OVMF (does not contain the word secure, secboot, etc.), e.g., /usr/share/edk2/ovmf/OVMF_CODE.fd.
  7. Click Add Hardware (bottom left), and select Channel.
  8. Select device type: unix.
  9. Select name: org.qemu.guest_agent.0.
  10. Finally, select Begin Installation (upper left corner).


```
virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk <PATH TO QCOW2 FILE>,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi
```

Bash
Copy
If you have a USB dongle to attach, you need to add the option --hostdev busID.deviceId. You can discover these IDs via the lsusb command. As example, if lsusb output is:
```
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 004: ID 30c9:0052 Luxvisions Innotech Limited Integrated RGB Camera
Bus 003 Device 003: ID 1a86:55d4 QinHeng Electronics SONOFF Zigbee 3.0 USB Dongle Plus V2
Bus 003 Device 002: ID 06cb:00fc Synaptics, Inc.
Bus 003 Device 005: ID 8087:0033 Intel Corp.
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

Bash
Copy
You can recognize the Sonoff dongle at Bus 003 Device 003. So the command to install the VM will become:
```
virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk <PATH TO QCOW2 FILE>,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi --hostdev 003.003
```

Bash
Copy
Note that this configuration (bus 003, device 003) is just an example, your dongle could be on another bus and/or with another device ID. Please check the correct IDs of your USB dongle with lsusb.
  1. Start VMware Workstation and select Create a New Virtual Machine. 
     * Note: the exact name and location of the settings below depend on the VMware version. This procedure is based on version 17.
  2. Select I will install the operating system later, then select Linux > Other Linux 5.x kernel 64-bit.
  3. Give the VM a name, home-assistant, and define an easy to reach storage location, such as C:\home-assistant.
  4. Specify the disk size and select Store virtual disk as a single file.
  5. Select Customize Hardware.
  6. Define the amount of memory and the number of cores the VM is allowed to use.
  7. Remove the New CD/DVD entry. It will not be used.
  8. Connect an Ethernet cable and make sure it is connected to your network.
  9. Under Network adapter, select Bridged: Connected directly to the physical network. 
  10. At the end of the wizard, select Finish.


## Edit the VM settings 
  1. In Windows Explorer, navigate to the storage location of your newly created VM, for example under C:\home-assistant.
  2. Delete the home-assistant.vmdk file.
  3. In the Downloads folder, find the haos_ova_xx.x.vmdk file. 
     * If you haven’t unzipped the archive, unzip it.
     * Within the folder, find the .vmdk file and rename it to home-assistant.vmdk.
     * Paste the file (not the unzipped folder) into the C:\home-assistant folder.
  4. Right-click the .vmx file and select Open with > Notepad.
  5. Under .encoding, add a line. Enter firmware = "efi".
  6. Now continue with the next step to start your VM. 
     * If you see a message about side channel mitigations, select OK.
     * If you see a message stating that the .vmdk file could not be found, in step 3, you likely pasted the folder, not the file. Repeat step 3.


⚠️ Hyper-V does not have USB support
  1. Create a new virtual machine.
  2. Select Generation 2.
  3. Select Connection > Your Virtual Switch that is bridged.
  4. Select Use an existing virtual hard disk and select the VHDX file from above.


After creation, go to Settings > Security and deselect Enable Secure Boot.
### Start up your virtual machine 
  1. Start the virtual machine.
  2. Observe the boot process of the Home Assistant Operating System.
  3. Once completed, you will be able to reach Home Assistant on . If you are running an older Windows version or have a stricter network configuration, you might need to access Home Assistant at or http://X.X.X.X:8123 (replace X.X.X.X with your virtual machine’s IP address).


With the Home Assistant Operating System installed and accessible, you can continue with onboarding.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Getting started
#  On this page



## Home Assistant Yellow - Home Assistant

Source: https://www.home-assistant.io/installation/yellow

#  On this page
Our take on Home Automation.
Don't have the hardware yet? Visit the 
# Installation instructions
Already have the hardware?
For installation instructions, check out the 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Getting started
#  On this page



## Getting Started | Home Assistant Companion Docs

Source: https://companion.home-assistant.io/docs

On this page
New onboarding experience
Starting with  app version 2025.11.0, there's a new streamlined onboarding process. .
## Installation
This sections provides the minimal system requirements and installation instructions.
### System Requirements
## Setting Up
  * If your Home Assistant instance is correctly set up for , you should be able set up the Companion App from any location.
  * If you're connected to the same network as your Home Assistant, it will automatically be detected during set up.


  1. Download the Home Assistant Companion App from the or .
  2. When you open the app for the first time, you'll be guided through the process of connecting to your Home Assistant instance. Follow the steps.
     * You are asked to grant the required permissions to integrate your phone with Home Assistant.
     * One of the permissions requested is for location access.
     * If this permission is denied, then you will not get a device_tracker or any sensor entity created for the device.
  3. Once you are done on the first screen, select Continue.
     * The app will start checking your network for Home Assistant instances. 
       * If an instance is found, tap the instance and follow the prompts to connect and log in to your Home Assistant.
       * If you are not connected to the same local network as your Home Assistant instance, tap Enter Address Manually and enter the address you use to remotely connect to your Home Assistant instance (using the Remote UI is recommended but not required).
  4. Once you have connected and logged into your Home Assistant instance, you will be asked to grant permission for the app to work with your iOS device beyond basic browsing of your Home Assistant instance.
  5. Once you have granted or denied permissions, the app will create the required connections to your Home Assistant instance and then take you to your Home Assistant home screen.
     * Depending on the app version, you may see a "What's New" screen in between the end of setup and be taken to your home screen.
     * Once you see the home screen, the installation is complete.
  6. If you have difficulties completing setting up the app, refer to the .


info
Remember to login using your credentials and not to use , if you have that enabled otherwise the app will only work on the trusted network.
## Adding Additional Servers
or 
note
Requires Home Assistant 2021.10 or newer.
Once you have set up your first server, you can add additional Home Assistant instances.
  1. In the Companion app, go to > Companion App.
  2. Select the Add Server option. 
     * Servers on the same local network as your device will be discovered and listed automatically.
  3. If the new server is not listed automatically, enter the address in the same way as setting up the first server.


## TLS Client Authentication
If your Home Assistant requires TLS Client Authentication (because it is behind a reverse proxy configured to perform TLS Client Authentication), the app will ask for a certificate. If no matching certificate is installed or supplied, you might see an error or a blank screen depending on your setup.
Please refer to your device and Android version documentation to install the certificate. Make sure to install the certificate as a "VPN & app user certificate". An example for Pixel phones is available here: .
Wear OS does not support authentication with installed certificates. The app cannot transfer the certificate to the Wear OS app automatically, therefore you are asked to provide a certificate during the Wear OS app onboarding. The certificate and key need to be provided as a single file in PKCS12 format. If that does not work, refer to the .
## New onboarding ( 2025.11.0)
Starting with app version 2025.11.0, the onboarding process has been redesigned to provide a more streamlined setup experience. The new flow includes enhanced security options and clearer permission explanations.
### Step-by-step onboarding process
  1. Welcome screen: When you first open the app, you'll see the Home Assistant Companion app welcome screen with options to Connect to my Home Assistant or Learn more.
  2. Network discovery: The app will search for Home Assistant instances on your network.
     * If found, the app will try to automatically connect your Home Assistant server
     * In case multiple servers were found, you will see a list to choose from
     * If not found or connecting remotely, tap Enter address manually and provide your Home Assistant URL
  3. Login: Enter your Home Assistant credentials to authenticate.
  4. Device naming: Choose a name for your device as it will appear in Home Assistant.
     * This name is used to identify your phone in Home Assistant
  5. Location permission: The app will ask for location access to enable powerful automations and secure connections.
  6. System location permission: Your device will show the standard location permission dialog.
     * Select Allow Once, Allow While Using the App, or Don't Allow
     * For full functionality, including background automations, choose Allow While Using the App, then in the next prompt Allow always
  7. Connection security level: If you plan to use a non-encrypted URL (such as your local IP address), you'll need to choose a security level:
     * Most secure: Only allows non-encrypted connections when you're on your home network (requires location permission)
     * Less secure: Allows non-encrypted connections from any network (not recommended for public networks)
     * You can read more about .
  8. Setup completion: The app will finalize the connection and take you to your Home Assistant dashboard.





## Authentication - Home Assistant

Source: https://www.home-assistant.io/docs/authentication/

#  On this page
The authentication system secures access to Home Assistant.
## Login screen 
You are greeted with a log in screen, asking you for username and password.
## User accounts 
When you start Home Assistant for the first time, the owner user account is created. This account has some special privileges and can:
  * Create and manage other user accounts.
  * Configure integrations and other settings (coming soon).


Warning
For the moment, other user accounts will have the same access as the owner account. In the future, non-owner accounts will be able to have restrictions applied.
Note
If you want to manage users and you’re an owner but you do not see “Users” in your main configuration menu, make sure that Advanced Mode is enabled for your user in your profile.
### Your account profile 
Once you’re logged in, you can see the details of your account on the page by selecting on the circular at the very bottom of the sidebar.
You can:
Note
Unused refresh tokens will be automatically removed. A refresh token is considered unused if it has not been used for a login within 90 days. If you need a permanent token, then we recommend using .
### Securing your login 
Make sure to choose a secure password! At some time in the future, you will probably want to access Home Assistant from outside your local network. This means you are also exposed to random black-hats trying to do the same. Treat the password like the key to your house.
As an extra level of security, you can turn on .
## Adding a person to Home Assistant 
If you have administrator rights, you can and create them a user account.
## Changing display or username 
To learn how to change a display or username, refer to .
## Other authentication techniques 
Home Assistant provides several ways to authenticate. See the section.
## Troubleshooting 
### Authentication failures from 127.0.0.1 
If you’re seeing authentication failures from 127.0.0.1 and you’re using the nmap device tracker, you should from being scanned.
### Bearer token warnings 
Under the new authentication system you’ll see the following warning logged when the is supplied, but not configured in Home Assistant:
```
WARNING (MainThread) [homeassistant.components.http.auth] You need to use a bearer token to access /blah/blah from 192.0.2.4
```

Txt
Copy
If you see this, you need to add an to your http: configuration.
### Bearer token informational messages 
If you see the following, then this is a message for integration developers, to tell them they need to update how they authenticate to Home Assistant. As an end user you don’t need to do anything:
```
INFO (MainThread) [homeassistant.components.http.auth] You need to use a bearer token to access /blah/blah from 192.0.2.4
```

Txt
Copy
### Lost owner password 
If you lose the password associated with the owner account, you need to .
### Error: invalid client id or redirect URL 
You have to use a domain name, not IP address, to remote access Home Assistant otherwise you will get Error: invalid client id or redirect url error on the login form. However, you can use the IP address to access Home Assistant in your home network.
This is because we only allow an IP address as a client ID when your IP address is an internal network address (e.g., 192.168.0.1) or loopback address (e.g., 127.0.0.1).
If you don’t have a valid domain name for your Home Assistant instance, you can modify the hosts file on your computer to fake one. On Linux edit the /etc/hosts file, and add following entry:
```
12.34.56.78 homeassistant.home
```

Text
Copy
Replace 12.34.56.78 with your Home Assistant’s public IP address.
This will allow you to open Home Assistant at http://homeassistant.home:8123/
### Stuck on loading data 
Some ad blocking software, such as Wipr, also blocks WebSockets. If you’re stuck on the Loading data screen, try disabling your ad blocker.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Custom card | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/custom-ui/custom-card/

On this page
are our approach to defining your user interface for Home Assistant. We offer a lot of built-in cards, but you're not just limited to the ones that we decided to include in Home Assistant. You can build and use your own!
## Defining your card
This is a basic example to show what's possible.
Create a new file in your Home Assistant config dir as <config>/www/content-card-example.js and put in the following contents:
```
class ContentCardExample extends HTMLElement { // Whenever the state changes, a new `hass` object is set. Use this to // update your content. set hass(hass) {  // Initialize the content if it's not there yet.  if (!this.content) {   this.innerHTML = `    <ha-card header="Example-card">     <div class="card-content"></div>    </ha-card>   `;   this.content = this.querySelector("div");  }  const entityId = this.config.entity;  const state = hass.states[entityId];  const stateStr = state ? state.state : "unavailable";  this.content.innerHTML = `   The state of ${entityId} is ${stateStr}!   <br><br>   <img src="http://via.placeholder.com/350x150">  `; } // The user supplied configuration. Throw an exception and Home Assistant // will render an error card. setConfig(config) {  if (!config.entity) {   throw new Error("You need to define an entity");  }  this.config = config; } // The height of your card. Home Assistant uses this to automatically // distribute all cards over the available columns in masonry view getCardSize() {  return 3; } // The rules for sizing your card in the grid in sections view getGridOptions() {  return {   rows: 3,   columns: 6,   min_rows: 3,   max_rows: 3,  }; }}customElements.define("content-card-example", ContentCardExample);
```

## Referencing your new card
In our example card we defined a card with the tag content-card-example (see last line), so our card type will be custom:content-card-example. And because you created the file in your <config>/www directory, it will be accessible in your browser via the url /local/ (if you have recently added the www folder you will need to re-start Home Assistant for files to be picked up).
Add a resource to your dashboard configuration with URL /local/content-card-example.js and type module ().
You can then use your card in your dashboard configuration:
```
# Example dashboard configurationviews: - name: Example  cards:   - type: "custom:content-card-example"    entity: input_boolean.switch_tv
```

## API
Custom cards are defined as a . It's up to you to decide how to render your DOM inside your element. You can use Polymer, Angular, Preact or any other popular framework (except for React – ).
### Configuration
Home Assistant will call setConfig(config) when the configuration changes (rare). If you throw an exception if the configuration is invalid, Home Assistant will render an error card to notify the user.
Home Assistant will set when the state of Home Assistant changes (frequent). Whenever the state changes, the component will have to update itself to represent the latest state.
### Sizing in masonry view
Your card can define a getCardSize method that returns the size of your card as a number or a promise that will resolve to a number. A height of 1 is equivalent to 50 pixels. This will help Home Assistant distribute the cards evenly over the columns in the . A card size of 1 will be assumed if the method is not defined.
Since some elements can be lazy loaded, if you want to get the card size of another element, you should first check it is defined.
```
return customElements .whenDefined(element.localName) .then(() => element.getCardSize());
```

### Sizing in sections view
You can define a getGridOptions method that returns the min, max and default number of cells your card will take in the grid if your card is used in the . Each section is divided in 12 columns. If you don't define this method, the card will take 12 columns and will ignore the rows of the grid.
A cell of the grid is defined with the following dimension:
  * width: width of the section divided by 12 (approximately 30px)
  * height: 56px
  * gap between cells: 8px


The different grid options are:
For the number of columns, it's highly recommended to use multiple of 3 for the default value (3, 6, 9 or 12) so your card will have better looking on the dashboard by default.
Example of implementation:
```
public getGridOptions() { return {  rows: 2,  columns: 6,  min_rows: 2, };}
```

In this example, the card will take 6 x 2 cells by default. The height of the card cannot be smaller than 2 rows. According to the cell dimension, the card will have a height of 120px (2 * 56px + 8px).
## Advanced example
Resources to load in dashboards are imported as a JS module import. Below is an example of a custom card using JS modules that does all the fancy things.
Create a new file in your Home Assistant config dir as <config>/www/wired-cards.js and put in the following contents:
```
import "https://unpkg.com/wired-card@0.8.1/wired-card.js?module";import "https://unpkg.com/wired-toggle@0.8.0/wired-toggle.js?module";import { LitElement, html, css,} from "https://unpkg.com/lit-element@2.0.1/lit-element.js?module";function loadCSS(url) { const link = document.createElement("link"); link.type = "text/css"; link.rel = "stylesheet"; link.href = url; document.head.appendChild(link);}loadCSS("https://fonts.googleapis.com/css?family=Gloria+Hallelujah");class WiredToggleCard extends LitElement { static get properties() {  return {   hass: {},   config: {},  }; } render() {  return html`   <wired-card elevation="2">    ${this.config.entities.map((ent) => {     const stateObj = this.hass.states[ent];     return stateObj      ? html`        <div class="state">         ${stateObj.attributes.friendly_name}         <wired-toggle          .checked="${stateObj.state === "on"}"          @change="${(ev) => this._toggle(stateObj)}"         ></wired-toggle>        </div>       `      : html` <div class="not-found">Entity ${ent} not found.</div> `;    })}   </wired-card>  `; } setConfig(config) {  if (!config.entities) {   throw new Error("You need to define entities");  }  this.config = config; } // The height of your card. Home Assistant uses this to automatically // distribute all cards over the available columns. getCardSize() {  return this.config.entities.length + 1; } _toggle(state) {  this.hass.callService("homeassistant", "toggle", {   entity_id: state.entity_id,  }); } static get styles() {  return css`   :host {    font-family: "Gloria Hallelujah", cursive;   }   wired-card {    background-color: white;    padding: 16px;    display: block;    font-size: 18px;   }   .state {    display: flex;    justify-content: space-between;    padding: 8px;    align-items: center;   }   .not-found {    background-color: yellow;    font-family: sans-serif;    font-size: 14px;    padding: 8px;   }   wired-toggle {    margin-left: 8px;   }  `; }}customElements.define("wired-toggle-card", WiredToggleCard);
```

Add a resource to your dashboard config with URL /local/wired-cards.js and type module.
And for your configuration:
```
# Example dashboard configurationviews: - name: Example  cards:   - type: "custom:wired-toggle-card"    entities:     - input_boolean.switch_ac_kitchen     - input_boolean.switch_ac_livingroom     - input_boolean.switch_tv
```

## Graphical card configuration
Your card can define a getConfigElement method that returns a custom element for editing the user configuration. Home Assistant will display this element in the card editor in the dashboard.
Your card can also define a getStubConfig method that returns a default card configuration (without the type: parameter) in json form for use by the card type picker in the dashboard.
Home Assistant will call the setConfig method of the config element on setup. Home Assistant will update the hass property of the config element on state changes, and the lovelace element, which contains information about the dashboard configuration.
Changes to the configuration are communicated back to the dashboard by dispatching a config-changed event with the new configuration in its detail.
To have your card displayed in the card picker dialog in the dashboard, add an object describing it to the array window.customCards. Required properties of the object are type and name (see example below).
```
class ContentCardExample extends HTMLElement { static getConfigElement() {  return document.createElement("content-card-editor"); } static getStubConfig() {  return { entity: "sun.sun" } } ...}customElements.define('content-card-example', ContentCardExample);
```

```
class ContentCardEditor extends LitElement { setConfig(config) {  this._config = config; } configChanged(newConfig) {  const event = new Event("config-changed", {   bubbles: true,   composed: true,  });  event.detail = { config: newConfig };  this.dispatchEvent(event); }}customElements.define("content-card-editor", ContentCardEditor);window.customCards = window.customCards || [];window.customCards.push({ type: "content-card-example", name: "Content Card", preview: false, // Optional - defaults to false description: "A custom card made by me!", // Optional documentationURL:  "https://developers.home-assistant.io/docs/frontend/custom-ui/custom-card", // Adds a help link in the frontend card editor});
```

### Using the built-in form editor
While one way to configure a graphical editor is to supply a custom editor element, another option for cards with relatively simple configuration requirements is to use the built-in frontend form editor. This is done by defining a static getConfigForm function in your card class, that returns a form schema defining the shape of your configuration form.
Example:
```
 static getConfigForm() {  return {   schema: [    { name: "label", selector: { label: {} } },    { name: "entity", required: true, selector: { entity: {} } },    {     type: "grid",     name: "",     schema: [      { name: "name", selector: { text: {} } },      {       name: "icon",       selector: {        icon: {},       },       context: {        icon_entity: "entity",       },      },      {       name: "attribute",       selector: {        attribute: {},       },       context: {        filter_entity: "entity",       },      },      { name: "unit", selector: { text: {} } },      { name: "theme", selector: { theme: {} } },      { name: "state_color", selector: { boolean: {} } },     ],    },   ],   computeLabel: (schema) => {    if (schema.name === "icon") return "Special Icon";    return undefined;   },   computeHelper: (schema) => {    switch (schema.name) {     case "entity":      return "This text describes the function of the entity selector";     case "unit":      return "The unit of measurement for this card";    }    return undefined;   },   assertConfig: (config) => {    if (config.other_option) {     throw new Error("'other_option' is unexpected.");    }   },  }; }
```

From this function, you should return an object with up to 4 keys:
This example then results in the following config form: 
#### Form Schema Elements
The form schema can have individual controls, grids, or expansion panels, configured with the following options:
Controls:
  * name (required): The name of the control.
  * selector (optional): The selector configuration for this control (see for available options)
  * type (optional): If selector is not defined, there are native form types like float and boolean, though using selectors is preferred.


Grids:
Expansion Panel:
This is not an exhaustive list of all options, more configuration options are listed at 



## Multi-factor authentication - Home Assistant

Source: https://www.home-assistant.io/docs/authentication/multi-factor-auth/

#  On this page


The Multi-factor Authentication (MFA) modules require you to solve a second challenge after you provide your password.
A password can be compromised in a number of ways, for example, it can be guessed if it is a simple password. MFA provides a second level of defense by requiring:
  * something you know, like your username and password, and
  * something you have, like a one-time password sent to your phone.


You can use MFA with any of the other authentication providers. If more than one MFA module is enabled, you can choose one when you log in.
You can turn MFA on and off in the for your user account.
## Available MFA modules 
### Time-based One-Time Password MFA module 
(TOTP) is widely adopted in modern authentication systems.
Home Assistant generates a secret key which is synchronized with an app on your phone. Every thirty seconds or so the phone app generates a random six digit number. Because Home Assistant knows the secret key, it knows which number will be generated. If you enter the correct digits, then you’re in.
#### Setting up TOTP 
Enable TOTP in your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] like this:
```
homeassistant:
 auth_mfa_modules:
  - type: totp
```

YAML
Copy
If no auth_mfa_modules configuration section is defined in configuration.yaml a TOTP module named “Authenticator app” will be autoloaded.
You will need an authenticator app on your phone. We recommend either or . Both are available for iOS or Android.
After restarting Home Assistant, go to your and there should be a “Multi-factor Authentication Modules” section.
Click Enable and a new secret key will be generated. Go to your phone app and enter the key, either by scanning the QR code or typing in the key below the QR code manually.
Caution
Please treat the secret key like a password - never expose it to others.
Your phone app will now start generating a different six-digit code every thirty seconds or so. Enter one of these into Home Assistant under the QR code where it asks for a Code. Home Assistant and your phone app are now in sync and you can now use the code displayed in the app to log in.
#### Using TOTP 
Once TOTP is enabled, Home Assistant requires the latest code from your phone app before you can log in.
Note
TOTP is time based so it relies on your Home Assistant clock being accurate. If the verification keeps failing, make sure the clock on Home Assistant is correct.
### Notify multi-factor authentication module 
The Notify MFA module uses the to send you an . It is typically sent to your phone, but can be sent to any destination supported by a notify action. You use this password to log in.
#### Setting up MFA notify 
Add Notify MFA to your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file like this:
```
homeassistant:
 auth_mfa_modules:
  - type: notify
   include:
    - notify_entity
```

YAML
Copy
####  Configuration Variables 
exclude list (Optional) 
The list of notifying entities you want to exclude. 
include list (Optional) 
The list of notifying entities you want to include. 
message template (Optional) 
The message template. 
```
# Example configuration, with a message template.
homeassistant:
 auth_mfa_modules:
  - type: totp
   name: "Authenticator app"
  - type: notify
   message: "I almost forget, to get into my clubhouse, you need to say {}"
```

YAML
Copy
After restarting Home Assistant, go to your and there should be a “Multi-factor Authentication Modules” section. Click Enable on the Notify One-Time Password option.
Try logging out, then logging in again. You will be asked for the six-digit one-time password that was sent to your notify entity. Enter the password to log in.
If the validation failed, a new one-time password will be sent again.
Note
The Notify MFA module can’t tell if the one-time password was delivered successfully. If you don’t get the notification, you won’t be able to log in.
You can disable the Notify MFA module by editing or removing the file [your_config_dir]/.storage/auth_module.notify.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Authentication providers - Home Assistant

Source: https://www.home-assistant.io/docs/authentication/providers/

#  On this page
Caution
This is an advanced feature.
When you log in, an auth provider checks your credentials to make sure you are an authorized user.
## Configuring auth providers 
Warning
Home Assistant automatically configures the standard auth providers so you don’t need to specify auth_providers in your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file unless you are configuring more than one. Specifying auth_providers will disable all auth providers that are not listed, so you could reduce your security or create difficulties logging in if it is not configured correctly.
If you decide to use trusted_networks as your auth_provider there won’t be a way to authenticate for a device outside of your listed trusted network. To overcome this ensure you add the default auth_provider with type: homeassistant back in manually. This will then present you with the default auth login screen when trusted network authentication fails as expected from outside your LAN.
Authentication providers are configured in your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file under the homeassistant: block. If you are moving configuration to packages, this particular configuration must stay within ‘configuration.yaml’. See Issue 16441 in the warning block at the bottom of this page.
You can supply more than one, for example:
```
homeassistant:
 auth_providers:
  - type: homeassistant
  - type: trusted_networks
   trusted_networks:
    - 192.168.0.0/24
```

YAML
Copy
## Available auth providers 
### Home Assistant auth provider 
This is the default auth provider. The first user created is designated as the owner and can create other users.
User details are stored in the [your config]/.storage directory. All passwords are stored hashed and with a salt, making it almost impossible for an attacker to figure out the password even if they have access to the file.
Users can be managed in Home Assistant by the owner. Go to the configuration panel and click on Users.
This is the entry in configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] for Home Assistant auth:
```
homeassistant:
 auth_providers:
  - type: homeassistant
```

YAML
Copy
If you don’t specify any auth_providers section in the configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file then this provider will be set up automatically.
### Trusted networks 
The trusted networks auth provider defines a range of IP addresses for which no authentication will be required (also known as “allowlisting”). For example, you can allowlist your local network so you won’t be prompted for a password if you access Home Assistant from inside your home.
When you log in from one of these networks, you will be asked which user account to use and won’t need to enter a password.
Note
The will not participate in the login process if you are using this auth provider.
Important
You cannot trust a network that you are using in any . The trusted_networks authentication will fail with the message: Your computer is not allowed
Here is an example in configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] to set up Trusted Networks:
```
homeassistant:
 auth_providers:
  - type: trusted_networks
   trusted_networks:
    - 192.168.0.0/24
    - fd00::/8
```

YAML
Copy
####  Configuration Variables 
trusted_networks list Required 
A list of IP addresses or an IP network you want allowlisted. It accepts both IPv4 and IPv6 IP address or network 
trusted_users map (Optional) 
You can also assign which users are available to select when user access login page from certain IP address or network. 
USER_ID list | string (Optional) 
List of user ids available to select on this IP address or network. 
allow_bypass_login boolean (Optional, default: false) 
You can bypass login page if you have only one user available for selection. 
#### Trusted users examples 
```
homeassistant:
 auth_providers:
  - type: trusted_networks
   trusted_networks:
    - 192.168.0.0/24
    - 192.168.10.0/24
    - fd00::/8
   trusted_users:
    192.168.0.1: user1_id
    192.168.0.0/24:
     - user1_id
     - user2_id
    "fd00::/8":
     - user1_id
     - group: system-users
```

YAML
Copy
First note, for trusted_users configuration you need to use user id.
  1. To find the user ID, in your browser, make sure the URL of your Home Assistant ends in config/users/. 
     * For example: homeassistant:8123/config/users.
  2. Select the user from the list, and copy the ID. 
     * For example: acbbff56461748718f3650fb914b88c9.
  3. The trusted_users configuration will not validate the existence of the user, so please make sure you have put in the correct user id.
  4. A trusted user with an IPv6 address must put the IPv6 address in quotes as shown.


In the above example, if user try to access Home Assistant from 192.168.0.1, they will have only one user available to choose. They will have two users available if access from 192.168.0.38 (from 192.168.0.0/24 network). If they access from 192.168.10.0/24 network, they can choose from all available users (non-system and active users).
Specially, you can use group: GROUP_ID to assign all users in certain user group to be available to choose. Group and users can be mix and match.
#### Skip login page examples 
This is a feature to allow you to bring back some of the experience before the user system was implemented. You can directly jump to the main page if you are accessing from trusted networks, the allow_bypass_login is on, and you have ONLY ONE available user to choose from in the login form.
If you allow bypass login then your cookie will not be stored and every time you refresh the page in Home Assistant a new login will be created. This is because bypassing the login does not give you the option to save the login.
```
# assuming you have only one non-system user
homeassistant:
 auth_providers:
  - type: trusted_networks
   trusted_networks:
    - 192.168.0.0/24
    - 127.0.0.1
    - ::1
   allow_bypass_login: true
  - type: homeassistant
```

YAML
Copy
Assuming you have only the owner created though onboarding process, no other users ever created. The above example configuration will allow you directly access Home Assistant main page if you access from your internal network (192.168.0.0/24) or from localhost (127.0.0.1). If you get a login abort error, then you can change to use Home Assistant Authentication Provider to login, if you access your Home Assistant instance from outside network.
### Command line 
The command line auth provider executes a configurable shell command to perform user authentication. Two environment variables, username and password, are passed to the command. Access is granted when the command exits successfully (with exit code 0).
This provider can be used to integrate Home Assistant with arbitrary external authentication services, from plaintext databases over LDAP to RADIUS.
Here is a configuration example:
```
homeassistant:
 auth_providers:
  - type: command_line
   command: /absolute/path/to/command
   # Optionally, define a list of arguments to pass to the command.
   #args: ["--first", "--second"]
   # Uncomment to enable parsing of meta variables (see below).
   #meta: true
```

YAML
Copy
When meta: true is set in the auth provider’s configuration, your command can write some variables to standard output to populate the user account created in Home Assistant with additional data. These variables have to be printed in the form:
```
name = John Doe
group = system-users
local_only = true
```

Txt
Copy
Leading and trailing whitespace, as well as lines starting with # are ignored. The following variables are supported. More may be added in the future.
  * name: The real name of the user to be displayed in their profile.
  * group: The user group uses the value system-admin for administrator (this is the default) or system-users for regular users.
  * local_only: The user can only log in from the local network if you set the value to true. If you do not define this variable, the user can log in from anywhere.


Stderr is not read at all and just passed through to that of the Home Assistant process, hence you can use it for status messages or suchlike.
Note
Any leading and trailing whitespace is stripped from usernames before they’re passed to the configured command. For instance, “ hello “ will be rewritten to just “hello”.
Note
For now, meta variables are only respected the first time a particular user is authenticated. Upon subsequent authentications of the same user, the previously created user object with the old values is reused.
## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Automation conditions - Home Assistant

Source: https://www.home-assistant.io/docs/automation/condition/

#  On this page
Conditions are an optional part of an automation rule. They can be used to prevent the automation’s actions from being run. After a triggerA trigger is a set of values or conditions of a platform that are defined to cause an automation to run. [Learn more] occurred, all conditions will be checked. The automation will be executed if all conditions return true. If any of the conditions returns false, the automation won’t start.
Conditions look very similar to triggers, but they are very different — a trigger will look at events happening in the system, while a condition only looks at how the system looks right now. A trigger can observe that a switch is being turned on. A condition can only see if a switch is currently on or off.
The available conditions for an automation are the same as for the script syntax so see that page for a .
Example of using condition:
```
automation:
 - alias: "Turn on office lights"
  triggers:
   - trigger: state
    entity_id: sensor.office_motion_sensor
    to: "on"
  conditions:
   - or:
    - condition: numeric_state
     entity_id: sun.sun
     attribute: elevation
     below: 4
    - condition: numeric_state
     entity_id: sensor.office_lux_sensor
     below: 10
  actions:
   - action: scene.turn_on
    target:
     entity_id: scene.office_lights
```

YAML
Copy
The condition option of an automation, also accepts a single condition template directly. For example:
```
automation:
 - alias: "Turn on office lights"
  triggers:
   - trigger: state
    entity_id: sensor.office_motion_sensor
    to: "on"
  conditions: "{{ state_attr('sun.sun', 'elevation') < 4 }}"
  actions:
   - action: scene.turn_on
    target:
     entity_id: scene.office_lights
```

YAML
Copy
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Automation editor - Home Assistant

Source: https://www.home-assistant.io/docs/automation/editor/

#  On this page


The automation editor is an easy way of creating and editing automations from the UI.
This tutorial uses the because it generates data (by default, values between 0 and 20). This enables us to walk through the example, even if you do not have any actual sensors connected yet. You could use any other sensor that outputs a numeric value.
  1. Go to and in the lower right corner, select the Create Automation button.
  2. Select Create new automation.
  3. Select Add Trigger, and in the Search trigger field, type “num”.
     * Select Numeric state.
  4. Enter the trigger conditions:
     * Define the sensor: Under Entity, enter “sensor.random_sensor”.
     * If the sensor value is above 10, we want the automation to trigger. 
       * In the Above field, enter “10”.
  5. Define the action that should happen:
     * In the Then do section, select Add Action.
  6. We want to create a .
     * Enter “No” and select Notifications: send a persistent notification.
  7. As the message, we want a simple text that is shown as part of the notification.
```
message: Sensor value greater than 10
```

YAML
Copy
  8. Select Save, give your automation a meaningful name, and Save again.
     * Result: Automations created or edited via the user interface are activated immediately after saving the automation.
     * To learn more about automations, read the documentation for .


## Troubleshooting missing automations 
When you’re creating automations using the GUI and they don’t appear in the UI, make sure that you add back automation: !include automations.yaml from the default configuration to your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more].
## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Automating Home Assistant - Home Assistant

Source: https://www.home-assistant.io/docs/automation

#  On this page


Home Assistant contains information about all your devicesA device is a model representing a physical or logical unit that contains entities. and servicesThe term “service” in Home Assistant is used in the sense of an information service. For example, the municipal waste management service that provides entities for organic, paper, and packaging waste. In terms of functionality, the information service is like a device. It is called service to avoid confusion, as it does not come with a piece of hardware.. This information is available for the user in the dashboard and it can be used to trigger automationsAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more]. And that’s fun!
Automations in Home Assistant allow you to automatically respond to things that happen. You can turn the lights on at sunset or pause the music when you receive a call.
If you are just starting out, we recommend that you start with blueprint automations. These are ready-made automations by the community that you only need to configure.
### 
If you have got the hang of blueprints and would like to explore more, it’s time for the next step. But before you start creating automations, you will need to learn about the automation basics.
### 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Understanding automations - Home Assistant

Source: https://www.home-assistant.io/docs/automation/basics/

#  On this page


All automationsAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] are made up of a triggerA trigger is a set of values or conditions of a platform that are defined to cause an automation to run. [Learn more] and an actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more]. Optionally combined with a conditionConditions are an optional part of an automation that will prevent an action from firing if they are not met. [Learn more]. Take for example the automation:
> When Paulus arrives home and it is after sunset: Turn the lights on in the living room.
We can break up this automation into the following three parts:
```
(trigger)  When Paulus arrives home
(condition) and it is after sunset:
(action)   Turn the lights on in the living room
```

Text
Copy
The first part is the of the automation. Triggers describe eventsEvery time something happens in Home Assistant, an event is fired. There are different types of events, such as state change events, when an action was triggered, or the time changed. All entities produce state change events. Every time a state changes, a state change event is produced. Events can be used to trigger automations or scripts. For example, you can trigger an automation when a light is turned on, then a speaker turns on in that room. Events can also be used to trigger actions in the frontend. For example, you can trigger an action when a button is pressed. [Learn more] that should trigger the automation. In this case, it is a person arriving home, which can be observed in Home Assistant using devicesA device is a model representing a physical or logical unit that contains entities./sensorsSensors return information about a thing, for instance the level of water in a tank. [Learn more] by observing the state of Paulus changing from not_home to home.
The second part is the . Conditions are optional tests that can limit an automation to only work in your specific use cases. A condition will test against the current state of the system. This includes the current time, devices, people and other things like the sun. In this case, we only want to act when the sun has set.
The third part is the , which will be performed when an automation is triggered and all conditions are met. For example, it can turn a light on, set the temperature on your thermostat or activate a scene.
Note
The difference between a trigger and a condition can be confusing as they are very similar.
Triggers require an event to happen for the conditions to be evaluated using current state information.
Event: Arrive home Condition: After Sunset? Action: Turn lights on
## Exploring the internal state 
Automations interact directly with the internal state of Home Assistant, so you’ll need to familiarize yourself with it. Home Assistant exposes its current state via the developer tools. These are available at the bottom of the sidebar in the frontend. Developer Tools > States will show all currently available states. An entity can be anything. A light, a switch, a person and even the sun. A state consists of the following parts:
Name | Description | Example  
---|---|---  
Entity ID | Unique identifier for the entity. | light.living_room  
State | The current state of the device. | off  
Attributes | Extra data related to the device and/or current state. | brightness  
State changes can be used as the source of triggers and the current state can be used in conditions.
To explore the available actions open the . Actions allow changing anything. For example, turn on a light, run a script, or enable a scene. Each action has a domain and a name. For example, the action is capable of turning on any light in your system. Parameters can be passed to an action to indicate, for example, which device to activate or which color to use.
## Creating automations 
Now that you’ve got a sneak peek of what is possible, it’s time to get your feet wet and create your first automation.
### 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Automation actions - Home Assistant

Source: https://www.home-assistant.io/docs/automation/action/

#  On this page
The action of an automation is what is being executed when an automation fires. The action part follows the which can be used to interact with anything via other actions or events.
For actions, you can specify the entity_id that it should apply to and optional parameters (to specify for example the brightness).
You can also perform the action to activate which will allow you to define how you want your devices to be and have Home Assistant perform the right action.
```
automation:
 # Change the light in the kitchen and living room to 150 brightness and color red.
 triggers:
  - trigger: sun
   event: sunset
 actions:
  - action: light.turn_on
   target:
    entity_id:
     - light.kitchen
     - light.living_room
   data:
    brightness: 150
    rgb_color: [255, 0, 0]
automation 2:
 # Notify me on my mobile phone of an event
 triggers:
  - trigger: sun
   event: sunset
   offset: -00:30
 variables:
  notification_action: notify.paulus_iphone
 actions:
  # Actions are scripts so can also be a list of actions
  - action: "{{ notification_action }}"
   data:
    message: "Beautiful sunset!"
  - delay: 0:35
  - action: notify.notify
   data:
    message: "Oh wow you really missed something great."
```

YAML
Copy
Conditions can also be part of an action. You can combine multiple actions and conditions in a single action, and they will be processed in the order you put them in. If the result of a condition is false, the action will stop there so any action after that condition will not be executed.
```
automation:
- alias: "Office at evening"
 triggers:
  - trigger: state
   entity_id: sensor.office_occupancy
   to: "on"
 actions:
  - action: notify.notify
   data:
    message: "Testing conditional actions"
  - condition: or
   conditions:
    - condition: numeric_state
     entity_id: sun.sun
     attribute: elevation
     below: 4
    - condition: state
     entity_id: sensor.office_illuminance
     below: 10
  - action: scene.turn_on
   target:
    entity_id: scene.office_at_evening
  - action: light.turn_on
   target: "{{ {'entity_id': ['light.office', 'light.office_2']} }}"
  - action: switch.turn_on
   target:
    label_id: "{{ ['office_evening', 'office_after_15'] }}"
```

YAML
Copy
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Automation modes - Home Assistant

Source: https://www.home-assistant.io/docs/automation/modes/

#  On this page


An automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] can be triggered while it is already running.
The automation’s mode configuration option controls what happens when the automation is triggered while the actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] are still running from a previous triggerA trigger is a set of values or conditions of a platform that are defined to cause an automation to run. [Learn more].
Mode | Description  
---|---  
single | (Default) Do not start a new run. Issue a warning.  
restart | Start a new run after first stopping the previous run. The automation only restarts if the conditions are met.  
queued | Start a new run after all previous runs complete. Runs are guaranteed to execute in the order they were queued. Note that subsequent queued automations will only join the queue if any conditions it may have are met at the time it is triggered.  
parallel | Start a new, independent run in parallel with previous runs.  
For both queued and parallel modes, configuration option max controls the maximum number of runs that can be executing and/or queued up at a time. The default is 10.
When max is exceeded (which is effectively 1 for single mode) a log message will be emitted to indicate this has happened. Configuration option max_exceeded controls the severity level of that log message. Set it to silent to ignore warnings or set it to a . The default is warning.
## Example throttled automation 
Some automations you only want to run every 5 minutes. This can be achieved using the single mode and silencing the warnings when the automation is triggered while it’s running.
```
automation:
 - mode: single
  max_exceeded: silent
  triggers:
   - ...
  actions:
   - ...
   - delay: 300 # seconds (=5 minutes)
```

YAML
Copy
## Example queued 
Sometimes an automation is doing an action on a device that does not support multiple simultaneous actions. In such cases, a queue can be used. In that case, the automation will be executed once it’s current invocation and queue are done.
```
automation:
 - mode: queued
  max: 25
  triggers:
   - ...
  actions:
   - ...
```

YAML
Copy
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Troubleshooting automations - Home Assistant

Source: https://www.home-assistant.io/docs/automation/troubleshooting/

#  On this page
Automations and scriptsScripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on. [Learn more] can be debugged in a few different ways. You can the full sequence of actions, or test each condition and action separately. let you see details of every step after an automation is run. For complicated automations with templatesA template is an automation definition that can include variables for the action or data from the trigger values. This allows automations to generate dynamic actions. [Learn more], see the section .
## Testing your automation 
Many automations can be tested directly in the automation editor UI.
### Running the entire automation 
In the three dots menu in the automation list or automation editor UI, select the Run actions button. This will execute all of the actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more], while skipping all triggersA trigger is a set of values or conditions of a platform that are defined to cause an automation to run. [Learn more] and conditionsConditions are an optional part of an automation that will prevent an action from firing if they are not met. [Learn more]. This lets you test the full sequence of actions, as if the automation was triggered and all conditions were true. Note that any used in your triggers will not be active when you test this way. The Trigger ID or any data passed by in the trigger data in conditions or actions can’t be tested directly this way.
You can also trigger an automation manually. This can test the conditions as if the automation was triggered by an event. Navigate to . In the Action drop-down, select Automation: Trigger, then Choose entity to select the automation you are testing. Toggle whether to skip the conditions, then Perform action. If needed, additional trigger or other data can be added in the YAML view for testing. The page has more information about data within the trigger.
Testing with complex triggers, conditions, and variables can be difficult. Note that using the Run actions button will skip all triggers and conditions, while Developer Tools can be used with or without checking conditions.
### Running individual actions or conditions 
In the automation editor UI, each conditionConditions are an optional part of an automation that will prevent an action from firing if they are not met. [Learn more] and actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] can be tested individually. Select the three dots menu, then the Test button.
  * Testing a condition will highlight it to show whether the condition passed at the moment it was tested. If all conditions pass, then the automation will run when triggered. Testing building blocks like an and condition will report whether the whole block registers as true or false, or you can test individual conditions within the building block.
  * Testing an action block will run that block immediately.


Note that complex automations that depend on previous blocks, such as trigger IDs, variables in templates, or action calls that return data to use in subsequent blocks, cannot be tested this way.
If you are writing automations in YAML, it is also useful to go to ** and in the Configuration validation section, select the Check configuration button. This is to make sure there are no syntax errors before restarting Home Assistant. In order for Check configuration to be visible, you must enable Advanced Mode on .
## Traces 
When an automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] is run, all steps are recorded and a trace is made. From the UI, open Settings, which is located in the sidebar, then select Automations & Scenes to go to the automation editor or click this button directly: 
From the automation editor UI, or in the automations list in the three dots menu, select Traces. Alternatively, select an automation entry shown under Activity.
The above screenshot shows a previous run of an automation. The automation is displayed using an interactive graph, highlighting which path the automation took. Each node in the graph can be clicked to view the details on what happened with the automation during that specific step. It traces the complete run of an automation.
The right side of the trace screen has tabs with more information:
The top bar shows the date and time the automation was triggered. Use the left and right arrows to view previous runs of the automation.
Automations created in YAML must have an assigned in order for debugging traces to be stored.
### Trace configuration 
The last 5 traces are recorded for all automations. It is possible to change this by adding the following code to your automation.
```
trace:
 stored_traces: 20
```

YAML
Copy
## Testing templates 
If your automation uses in any part, you can do the following to make sure it works as expected:
  1. Go to tab.
  2. Create all variables (sources) required for your template as described at the end of paragraph.
  3. Copy your template code and paste it in Template editor straight after your variables.
  4. If necessary, change your sources’ value and check if the template works as you want and does not generate any errors.


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Automation Templates - Home Assistant

Source: https://www.home-assistant.io/docs/automation/templating/

#  On this page
Automations support the advanced features of in the same way as scripts do. In addition to the available to scripts, the trigger and this template variables are available for automations.
Example of variables used in templates:
  * {{ this.name }} is the name of the automation executing from this trigger
  * {{ trigger.platform }} is the type of trigger object, like calendar 


## Available state data 
The template variable this is an object that contains the of the automation at the moment of triggering the actions and can be used to evaluate declared in the configuration of the active triggerA trigger is a set of values or conditions of a platform that are defined to cause an automation to run. [Learn more]. State objects also contain context data which can be used to identify the user that caused a scriptScripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on. [Learn more] or automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] to execute. Note that this will not change while executing the actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more].
## Available trigger data 
The template variable trigger is an object that contains details about which platformPlatforms are building blocks provided by some integrations to be used by other integrations. [Learn more] triggered the automation. The platform property contains the name of the platformPlatforms are building blocks provided by some integrations to be used by other integrations. [Learn more] whose event triggered the automation.
Templates can use the data to modify the actions performed by the automation or displayed in a message. For example, you could create an automation that multiple sensors can trigger and then use the sensor’s location to specify a light to activate; or you could send a notification containing the friendly name of the sensor that triggered it.
Each platform includes additional data specific to that platformPlatforms are building blocks provided by some integrations to be used by other integrations. [Learn more].
### All 
Triggers from all platforms will include the following properties.
Template variable | Data  
---|---  
trigger.platform | Trigger object type.  
trigger.alias | Alias of the trigger.  
trigger.id | The .  
trigger.idx | Index of the trigger. (The first trigger idx is 0.)  
### Calendar 
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: calendar   
trigger.event | The trigger event type, either start or end.  
trigger.calendar_event | The calendar event object matched.  
trigger.calendar_event.summary | The title or summary of the calendar event.  
trigger.calendar_event.start | String representation of the start date or date time of the calendar event e.g. 2022-04-10, or 2022-04-10 11:30:00-07:00   
trigger.calendar_event.end | String representation of the end time of date time the calendar event in UTC e.g. 2022-04-11, or 2022-04-10 11:45:00-07:00   
trigger.calendar_event.all_day | Indicates the event spans the entire day.  
trigger.calendar_event.description | A detailed description of the calendar event, if available.  
trigger.calendar_event.location | Location information for the calendar event, if available.  
trigger.offset | Timedelta object with offset to the event, if any.  
### Device 
These are the properties available for a .
Inherits template variables from or template based on the type of trigger selected for the device.
Template variable | Data  
---|---  
trigger.platform | Hardcoded: device   
### Event 
An trigger is fired each time an entityAn entity represents a sensor, actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a device or a service. [Learn more] state changes or an event matching the configured event_type occurs.
These are the properties available for an .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: event   
trigger.event | Event object that matched.  
trigger.event.event_type | Event type.  
trigger.event.data | Optional event data.  
### Geolocation 
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: geo_location   
trigger.event | The trigger event type, either enter or leave.  
trigger.source | The Geolocation platform creating the trigger event.  
trigger.zone | State object of the zone.  
### Home Assistant 
The Home Assistant trigger is recommended for automations instead of .
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: homeassistant   
trigger.event | The trigger event type, either start or shutdown.  
### MQTT 
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: mqtt   
trigger.topic | Topic that received payload.  
trigger.payload | Payload.  
trigger.payload_json | Dictionary of the JSON parsed payload.  
trigger.qos | QOS of payload.  
### Numeric state 
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: numeric_state   
trigger.entity_id | Entity ID that we observe.  
trigger.below | The below threshold, if any.  
trigger.above | The above threshold, if any.  
trigger.from_state | The previous of the entity.  
trigger.to_state | The new that triggered trigger.  
trigger.for | Timedelta object how long state has met above/below criteria, if any.  
### Sentence 
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: conversation   
trigger.sentence | Text of the sentence that was matched.  
trigger.slots | Object with matched slot values.  
trigger.details | Object with matched slot details by name, such as . Each detail contains: 
  * name - name of the slot
  * text - matched text
  * value - output value (see )

.  
trigger.device_id | The device ID that captured the command, if any.  
trigger.satellite_id | The entity ID of the satellite that captured the command, if any.  
### State 
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: state   
trigger.entity_id | Entity ID that we observe.  
trigger.from_state | The previous of the entity.  
trigger.to_state | The new that triggered trigger.  
trigger.for | Timedelta object how long state has been to state, if any.  
### Sun 
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: sun   
trigger.event | The event that just happened: sunset or sunrise.  
trigger.offset | Timedelta object with offset to the event, if any.  
### Tag 
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: tag   
trigger.tag_id | The tag ID captured.  
trigger.device_id | Optional device ID that captured the tag.  
### Template 
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: template   
trigger.entity_id | Entity ID that caused change.  
trigger.from_state | Previous of entity that caused change.  
trigger.to_state | New of entity that caused template to change.  
trigger.for | Timedelta object how long state has been to state, if any.  
### Time 
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: time   
trigger.now | DateTime object that triggered the time trigger.  
### Time pattern 
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: time_pattern   
trigger.now | DateTime object that triggered the time_pattern trigger.  
### Persistent notification 
These properties are available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: persistent_notification   
trigger.update_type | Type of persistent notification update added, removed, current, or updated.  
trigger.notification | Notification object that triggered the persistent notification trigger.  
trigger.notification.notification_id | The notification ID.  
trigger.notification.title | Title of the notification.  
trigger.notification.message | Message of the notification.  
trigger.notification.created_at | DateTime object indicating when the notification was created.  
### Webhook 
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: webhook   
trigger.webhook_id | The webhook ID that was triggered.  
trigger.json | The JSON data of the request (if it had a JSON content type) as a mapping.  
trigger.data | The form data of the request (if it had a form data content type).  
trigger.query | The URL query parameters of the request (if provided).  
### Zone 
These are the properties available for a .
Template variable | Data  
---|---  
trigger.platform | Hardcoded: zone   
trigger.entity_id | Entity ID that we are observing.  
trigger.from_state | Previous of the entity.  
trigger.to_state | New of the entity.  
trigger.zone | State object of the zone.  
trigger.event | Event that trigger observed: enter or leave.  
## Examples 
```
# Example configuration.yaml entries
automation:
 triggers:
  - trigger: state
   entity_id: device_tracker.paulus
   id: paulus_device
 actions:
  - action: notify.notify
   data:
    message: >
     Paulus just changed from {{ trigger.from_state.state }}
     to {{ trigger.to_state.state }}
     This was triggered by {{ trigger.id }}
automation 2:
 triggers:
  - trigger: mqtt
   topic: "/notify/+"
 actions:
  - action: >
    notify.{{ trigger.topic.split('/')[-1] }}
   data:
    message: "{{ trigger.payload }}"
automation 3:
 triggers:
  # Multiple entities for which you want to perform the same action.
  - trigger: state
   entity_id:
    - light.bedroom_closet
    - light.kiddos_closet
    - light.linen_closet
   to: "on"
   # Trigger when someone leaves one of those lights on for 10 minutes.
   for: "00:10:00"
 actions:
  - action: light.turn_off
   target:
    # Turn off whichever entity triggered the automation.
    entity_id: "{{ trigger.entity_id }}"
automation 4:
 triggers:
  # When an NFC tag is scanned by Home Assistant...
  - trigger: event
   event_type: tag_scanned
   # ...By certain people
   context:
    user_id:
     - 06cbf6deafc54cf0b2ffa49552a396ba
     - 2df8a2a6e0be4d5d962aad2d39ed4c9c
 conditions:
  # Check NFC tag (ID) is the one by the front door
  - condition: template
   value_template: "{{ trigger.event.data.tag_id == '8b6d6755-b4d5-4c23-818b-cf224d221ab7'}}"
 actions:
  # Turn off various lights
  - action: light.turn_off
   target:
    entity_id:
     - light.kitchen
     - light.bedroom
     - light.living_room
```

YAML
Copy
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Automation actions - Home Assistant

Source: https://www.home-assistant.io/docs/automation/services/

#  On this page
The automation integration has actions to control automations, like turning automations on and off. This can be useful if you want to disable an automation from another automation.
## Action 
This action enables the automation’s triggersA trigger is a set of values or conditions of a platform that are defined to cause an automation to run. [Learn more].
Data attribute | Optional | Description  
---|---|---  
entity_id | no | Entity ID of automation to turn on. Can be a list. none or all are also accepted.  
## Action 
This action disables the automation’s triggersA trigger is a set of values or conditions of a platform that are defined to cause an automation to run. [Learn more], and optionally stops any currently active actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more].
Data attribute | Optional | Description  
---|---|---  
entity_id | no | Entity ID of automation to turn off. Can be a list. none or all are also accepted.  
stop_actions | yes | Stop any currently active actions (defaults to true).  
## Action 
This action enables the automation’s triggers if they were disabled, or disables the automation’s triggers, and stops any currently active actions, if the triggers were enabled.
Data attribute | Optional | Description  
---|---|---  
entity_id | no | Entity ID of automation to turn on. Can be a list. none or all are also accepted.  
## Action 
This action will trigger the actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] of an automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more]. By default it bypasses any conditions, though that can be changed via the skip_condition attribute.
Data attribute | Optional | Description  
---|---|---  
entity_id | no | Entity ID of automation to trigger. Can be a list. none or all are also accepted.  
skip_condition | yes | Whether or not the condition will be skipped (defaults to true).  
## Action 
This action is only required if you create/edit automations in YAML. Automations via the UI do this automatically.
This action reloads all automations, stopping all currently active automation actions.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Automation Trigger - Home Assistant

Source: https://www.home-assistant.io/docs/automation/trigger/

#  On this page
Triggers are what starts the processing of an automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] rule. When any of the automation’s triggers becomes true (trigger fires), Home Assistant will validate the , if any, and call the .
An automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] can be triggered by an eventEvery time something happens in Home Assistant, an event is fired. There are different types of events, such as state change events, when an action was triggered, or the time changed. All entities produce state change events. Every time a state changes, a state change event is produced. Events can be used to trigger automations or scripts. For example, you can trigger an automation when a light is turned on, then a speaker turns on in that room. Events can also be used to trigger actions in the frontend. For example, you can trigger an action when a button is pressed. [Learn more], a certain entityAn entity represents a sensor, actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a device or a service. [Learn more] stateThe state holds the information of interest of an entity, for example, if a light is on or off. Each entity has exactly one state and the state only holds one value at a time. However, entities can store attributes related to that state such as brightness, color, or a unit of measurement. [Learn more], at a given time, and more. These can be specified directly or more flexible via templates. It is also possible to specify multiple triggers for one automation.
## Trigger ID 
All triggers can be assigned an optional id. If the ID is omitted, it will instead be set to the index of the trigger. The id can be referenced from . The id does not have to be unique for each trigger, and it can be used to group similar triggers for use later in the automation (i.e., several triggers of different types that should all turn some entity on).
### Video tutorial 
This video tutorial explains how trigger IDs work.
```
automation:
 triggers:
  - trigger: event
   event_type: "MY_CUSTOM_EVENT"
   id: "custom_event"
  - trigger: mqtt
   topic: "living_room/switch/ac"
   id: "ac_on"
  - trigger: state # This trigger will be assigned id="2"
   entity_id:
    - device_tracker.paulus
    - device_tracker.anne_therese
   to: "home"
```

YAML
Copy
## Trigger variables 
There are two different types of variables available for triggers. Both work like .
The first variant allows you to define variables that will be set when the trigger fires. The variables will be able to use templates and have access to .
The second variant is setting variables that are available when attaching a trigger when the trigger can contain templated values. These are defined using the trigger_variables key at an automation level. These variables can only contain . The triggers will not re-apply if the value of the template changes. Trigger variables are a feature meant to support using blueprint inputs in triggers.
```
automation:
 trigger_variables:
  my_event: example_event
 triggers:
  - trigger: event
   # Able to use `trigger_variables`
   event_type: "{{ my_event }}"
   # These variables are evaluated and set when this trigger is triggered
   variables:
    name: "{{ trigger.event.data.name }}"
```

YAML
Copy
## Event trigger 
An event trigger fires when an is being received. Events are the raw building blocks of Home Assistant. You can match events on just the event name or also require specific event data or context to be present.
Events can be fired by integrations or via the API. There is no limitation to the types. A list of built-in events can be found .
```
automation:
 triggers:
  - trigger: event
   event_type: "MY_CUSTOM_EVENT"
   # optional
   event_data:
    mood: happy
   context:
    user_id:
    # any of these will match
     - "MY_USER_ID"
     - "ANOTHER_USER_ID"
```

YAML
Copy
It is also possible to listen for multiple events at once. This is useful for event that contain no, or similar, data and contexts.
```
automation:
 triggers:
  - trigger: event
   event_type:
    - automation_reloaded
    - scene_reloaded
```

YAML
Copy
It’s also possible to use in the event_type, event_data and context options.
Important
The event_type, event_data and context templates are only evaluated when setting up the trigger, they will not be reevaluated for every event.
```
automation:
 trigger_variables:
  sub_event: ABC
  node: ac
  value: on
 triggers:
  - trigger: event
   event_type: "{{ 'MY_CUSTOM_EVENT_' ~ sub_event }}"
```

YAML
Copy
## Home Assistant trigger 
Fires when Home Assistant starts up or shuts down.
```
automation:
 triggers:
  - trigger: homeassistant
   # Event can also be 'shutdown'
   event: start
```

YAML
Copy
Note
Automations triggered by the shutdown event have 20 seconds to run, after which they are stopped to continue with the shutdown.
## MQTT trigger 
Fires when a specific message is received on given MQTT topic. Optionally can match on the payload being sent over the topic. The default payload encoding is ‘utf-8’. For images and other byte payloads use encoding: '' to disable payload decoding completely.
```
automation:
 triggers:
  - trigger: mqtt
   topic: "living_room/switch/ac"
   # Optional
   payload: "on"
   encoding: "utf-8"
```

YAML
Copy
The payload option can be combined with a value_template to process the message received on the given MQTT topic before matching it with the payload. The trigger in the example below will trigger only when the message received on living_room/switch/ac is valid JSON, with a key state which has the value "on".
```
automation:
 triggers:
  - trigger: mqtt
   topic: "living_room/switch/ac"
   payload: "on"
   value_template: "{{ value_json.state }}"
```

YAML
Copy
It’s also possible to use in the topic and payload options.
Note
The topic and payload templates are only evaluated when setting up the trigger, they will not be re-evaluated for every incoming MQTT message.
```
automation:
 trigger_variables:
  room: "living_room"
  node: "ac"
  value: "on"
 triggers:
  - trigger: mqtt
   topic: "{{ room ~ '/switch/' ~ node}}"
   # Optional
   payload: "{{ 'state:' ~ value }}"
   encoding: "utf-8"
```

YAML
Copy
## Numeric state trigger 
Fires when the numeric value of an entity’s state (or attribute’s value if using the attribute property, or the calculated value if using the value_template property) crosses a given threshold (equal excluded). On state change of a specified entity, attempts to parse the state as a number and fires if the value is changing from above to below or from below to above the given threshold (equal excluded).
Note
Crossing the threshold means that the trigger only fires if the state wasn’t previously within the threshold. If the current state of your entity is 50 and you set the threshold to below: 75, the trigger would not fire if the state changed to e.g. 49 or 72 because the threshold was never crossed. The state would first have to change to e.g. 76 and then to e.g. 74 for the trigger to fire.
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id: sensor.temperature
   # If given, will trigger when the value of the given attribute for the given entity changes..
   attribute: attribute_name
   # ..or alternatively, will trigger when the value given by this evaluated template changes.
   value_template: "{{ state.attributes.value - 5 }}"
   # At least one of the following required
   above: 17
   below: 25
   # If given, will trigger when the condition has been true for X time; you can also use days and milliseconds.
   for:
    hours: 1
    minutes: 10
    seconds: 5
```

YAML
Copy
Note
Listing above and below together means the numeric_state has to be between the two values. In the example above, the trigger would fire a single time if a numeric_state goes into the 17.1-24.9 range (above 17 and below 25). It will only fire again, once it has left the defined range and enters it again.
When the attribute option is specified the trigger is compared to the given attribute instead of the state of the entity.
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id: climate.kitchen
   attribute: current_temperature
   above: 23
```

YAML
Copy
More dynamic and complex calculations can be done with value_template. The variable ‘state’ is the of the entity specified by entity_id.
The state of the entity can be referenced like this:
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id: sensor.temperature
   value_template: "{{ state.state | float * 9 / 5 + 32 }}"
   above: 70
```

YAML
Copy
Attributes of the entity can be referenced like this:
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id: climate.kitchen
   value_template: "{{ state.attributes.current_temperature - state.attributes.temperature_set_point }}"
   above: 3
```

YAML
Copy
Number helpers (input_number entities), number, sensor, and zone entities that contain a numeric value, can be used in the above and below thresholds. However, the comparison will only be made when the entity specified in the trigger is updated. This would look like:
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id: sensor.outside_temperature
   # Other entity ids can be specified for above and/or below thresholds
   above: sensor.inside_temperature
```

YAML
Copy
The for: can also be specified as HH:MM:SS like this:
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id: sensor.temperature
   # At least one of the following required
   above: 17
   below: 25
   # If given, will trigger when condition has been for X time.
   for: "01:10:05"
```

YAML
Copy
You can also use templates in the for option.
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id:
    - sensor.temperature_1
    - sensor.temperature_2
   above: 80
   for:
    minutes: "{{ states('input_number.high_temp_min')|int }}"
    seconds: "{{ states('input_number.high_temp_sec')|int }}"
 actions:
  - action: persistent_notification.create
   data:
    message: >
     {{ trigger.to_state.name }} too high for {{ trigger.for }}!
```

YAML
Copy
The for template(s) will be evaluated when an entity changes as specified.
Important
Use of the for option will not survive Home Assistant restart or the reload of automations. During restart or reload, automations that were awaiting for the trigger to pass, are reset.
If for your use case this is undesired, you could consider using the automation to set an to the desired time and then use that as an automation trigger to perform the desired actions at the set time.
## State trigger 
In general, the state trigger fires when the state of any of given entities changes. The behavior is as follows:
Tip
The values you see in your overview will often not be the same as the actual state of the entity. For instance, the overview may show Connected when the underlying entity is actually on. You should check the state of the entity by checking the states in the developer tool, under .
### Examples 
This automation triggers if either Paulus or Anne-Therese are home for one minute.
```
automation:
 triggers:
  - trigger: state
   entity_id:
    - device_tracker.paulus
    - device_tracker.anne_therese
   # Optional
   from: "not_home"
   # Optional
   to: "home"
   # If given, will trigger when the condition has been true for X time; you can also use days and milliseconds.
   for:
    hours: 0
    minutes: 1
    seconds: 0
```

YAML
Copy
It’s possible to give a list of from states or to states:
```
automation:
 triggers:
  - trigger: state
   entity_id: vacuum.test
   from:
    - "cleaning"
    - "returning"
   to: "error"
```

YAML
Copy
If you want to trigger on all state changes, but not on attribute changes, you can to to null (this would also work by setting from, not_from, or not_to to null):
```
automation:
 triggers:
  - trigger: state
   entity_id: vacuum.test
   to:
```

YAML
Copy
If you want to trigger on all state changes except specific ones, use not_from or not_to The not_from and not_to options are the counter parts of from and to. They can be used to trigger on state changes that are not the specified state.
```
automation:
 triggers:
  - trigger: state
   entity_id: vacuum.test
   not_from:
    - "unknown"
    - "unavailable"
   to: "on"
```

YAML
Copy
You cannot use from and not_from at the same time. The same applies to to and not_to.
### Triggering on attribute changes 
When the attribute option is specified, the trigger only fires when the specified attribute changes. Changes to other attributes or state changes are ignored.
For example, this trigger only fires when the boiler has been heating for 10 minutes:
```
automation:
 triggers:
  - trigger: state
   entity_id: climate.living_room
   attribute: hvac_action
   to: "heating"
   for: "00:10:00"
```

YAML
Copy
This trigger fires whenever the boiler’s hvac_action attribute changes:
```
automation:
 triggers:
  - trigger: state
   entity_id: climate.living_room
   attribute: hvac_action
```

YAML
Copy
### Holding a state or attribute 
You can use for to have the state trigger only fire if the state holds for some time.
This example fires, when the entity state changed to "on" and holds that state for 30 seconds:
```
automation:
 triggers:
  - trigger: state
   entity_id: light.office
   # Must stay "on" for 30 seconds
   to: "on"
   for: "00:00:30"
```

YAML
Copy
When holding a state, changes to attributes are ignored. Changes to attributes don’t cancel the hold time.
You can also fire the trigger when the state value changed from a specific state, but hasn’t returned to that state value for the specified time.
This can be useful, e.g., checking if a media player hasn’t turned “off” for the time specified, but doesn’t care about “playing” or “paused”.
```
automation:
 triggers:
  - trigger: state
   entity_id: media_player.kitchen
   # Not "off" for 30 minutes
   from: "off"
   for: "00:30:00"
```

YAML
Copy
Please note, that when using from, to and for, only the value of the to option is considered for the time specified.
In this example, the trigger fires if the state value of the entity remains the same for for the time specified, regardless of the current state value.
```
automation:
 triggers:
  - trigger: state
   entity_id: media_player.kitchen
   # The media player remained in its current state for 1 hour
   for: "01:00:00"
```

YAML
Copy
You can also use templates in the for option.
```
automation:
 triggers:
  - trigger: state
   entity_id:
    - device_tracker.paulus
    - device_tracker.anne_therese
   to: "home"
   for:
    minutes: "{{ states('input_number.lock_min')|int }}"
    seconds: "{{ states('input_number.lock_sec')|int }}"
 actions:
  - action: lock.lock
   target:
    entity_id: lock.my_place
```

YAML
Copy
The for template(s) will be evaluated when an entity changes as specified.
Tip
Use quotes around your values for from and to to avoid the YAML parser from interpreting values as booleans.
## Sun trigger 
### Sunset / Sunrise trigger 
Fires when the sun is setting or rising, i.e., when the sun elevation reaches 0°.
An optional time offset can be given to have it fire a set time before or after the sun event (e.g., 45 minutes before sunset). A negative value makes it fire before sunrise or sunset, a positive value afterwards. The offset needs to be specified in number of seconds, or in a hh:mm:ss format.
Tip
Since the duration of twilight is different throughout the year, it is recommended to use instead of sunset or sunrise with a time offset to trigger automations during dusk or dawn.
```
automation:
 triggers:
  - trigger: sun
   # Possible values: sunset, sunrise
   event: sunset
   # Optional time offset. This example will trigger 45 minutes before sunset.
   offset: "-00:45:00"
```

YAML
Copy
### Sun elevation trigger 
Sometimes you may want more granular control over an automation than simply sunset or sunrise and specify an exact elevation of the sun. This can be used to layer automations to occur as the sun lowers on the horizon or even after it is below the horizon. This is also useful when the “sunset” event is not dark enough outside and you would like the automation to run later at a precise solar angle instead of the time offset such as turning on exterior lighting. For most automations intended to run during dusk or dawn, a number between 0° and -6° is suitable; -4° is used in this example:
```
automation:
 - alias: "Exterior Lighting on when dark outside"
  triggers:
   - trigger: numeric_state
    entity_id: sun.sun
    attribute: elevation
    # Can be a positive or negative number
    below: -4.0
  actions:
   - action: switch.turn_on
    target:
     entity_id: switch.exterior_lighting
```

YAML
Copy
If you want to get more precise, you can use this , which will help you estimate what the solar elevation will be at any specific time. Then from this, you can select from the defined twilight numbers.
Although the actual amount of light depends on weather, topography and land cover, they are defined as:
  * Civil twilight: 0° > Solar angle > -6°
This is what is meant by twilight for the average person: Under clear weather conditions, civil twilight approximates the limit at which solar illumination suffices for the human eye to clearly distinguish terrestrial objects. Enough illumination renders artificial sources unnecessary for most outdoor activities.
  * Nautical twilight: -6° > Solar angle > -12°
  * Astronomical twilight: -12° > Solar angle > -18°


A very thorough explanation of this is available in the Wikipedia article about the .
## Tag trigger 
Fires when a is scanned. For example, a NFC tag is scanned using the Home Assistant Companion mobile application.
```
automation:
 triggers:
  - trigger: tag
   tag_id: A7-6B-90-5F
```

YAML
Copy
Additionally, you can also only trigger if a card is scanned by a specific device/scanner by setting the device_id:
```
automation:
 triggers:
  - trigger: tag
   tag_id: A7-6B-90-5F
   device_id: 0e19cd3cf2b311ea88f469a7512c307d
```

YAML
Copy
Or trigger on multiple possible devices for multiple tags:
```
automation:
 triggers:
  - trigger: tag
   tag_id:
    - "A7-6B-90-5F"
    - "A7-6B-15-AC"
   device_id:
    - 0e19cd3cf2b311ea88f469a7512c307d
    - d0609cb25f4a13922bb27d8f86e4c821
```

YAML
Copy
## Template trigger 
Template triggers work by evaluating a when any of the recognized entities change state. The trigger will fire if the state change caused the template to render ‘true’ (a non-zero number or any of the strings true, yes, on, enable) when it was previously ‘false’ (anything else).
This is achieved by having the template result in a true boolean expression (for example {{ is_state('device_tracker.paulus', 'home') }}) or by having the template render true (example below).
With template triggers you can also evaluate attribute changes by using is_state_attr (like {{ is_state_attr('climate.living_room', 'away_mode', 'off') }})
```
automation:
 triggers:
  - trigger: template
   value_template: "{% if is_state('device_tracker.paulus', 'home') %}true{% endif %}"
   # If given, will trigger when template remains true for X time.
   for: "00:01:00"
```

YAML
Copy
You can also use templates in the for option.
```
automation:
 triggers:
  - trigger: template
   value_template: "{{ is_state('device_tracker.paulus', 'home') }}"
   for:
    minutes: "{{ states('input_number.minutes')|int(0) }}"
```

YAML
Copy
The for template(s) will be evaluated when the value_template becomes ‘true’.
Templates that do not contain an entity will be rendered once per minute.
Important
Use of the for option will not survive Home Assistant restart or the reload of automations. During restart or reload, automations that were awaiting for the trigger to pass, are reset.
If for your use case this is undesired, you could consider using the automation to set an to the desired time and then use that as an automation trigger to perform the desired actions at the set time.
## Time trigger 
The time trigger is configured to fire once a day at a specific time, or at a specific time on a specific date. There are three allowed formats:
### Time string 
A string that represents a time to fire on each day. Can be specified as HH:MM or HH:MM:SS. If the seconds are not specified, :00 will be used.
```
automation:
 - triggers:
  - trigger: time
   # 24-hour time format. This trigger will fire at 3:32 PM
   at: "15:32:00"
```

YAML
Copy
### Input datetime 
The entity ID of an .
has_date | has_time | Description  
---|---|---  
true | true | Will fire at specified date & time.  
true | false | Will fire at midnight on specified date.  
false | true | Will fire once a day at specified time.  
```
automation:
 - triggers:
   - trigger: state
    entity_id: binary_sensor.motion
    to: "on"
  actions:
   - action: climate.turn_on
    target:
     entity_id: climate.office
   - action: input_datetime.set_datetime
    target:
     entity_id: input_datetime.turn_off_ac
    data:
     datetime: >
      {{ (now().timestamp() + 2*60*60)
        | timestamp_custom('%Y-%m-%d %H:%M:%S') }}
 - triggers:
   - trigger: time
    at: input_datetime.turn_off_ac
  actions:
   - action: climate.turn_off
    target:
     entity_id: climate.office
```

YAML
Copy
### Sensors of datetime device class 
The Entity ID of a with the “timestamp” device class.
```
automation:
 - triggers:
   - trigger: time
    at: sensor.phone_next_alarm
  actions:
   - action: light.turn_on
    target:
     entity_id: light.bedroom
```

YAML
Copy
### Sensors of datetime device class with offsets 
When the time is provided using a sensor of the timestamp device class, an offset can be provided. This offset will be added to (or subtracted from when negative) the sensor value.
For example, this trigger fires 5 minutes before the phone alarm goes off.
```
automation:
 - triggers:
   - trigger: time
    at:
     entity_id: sensor.phone_next_alarm
     offset: -00:05:00
  actions:
   - action: light.turn_on
    target:
     entity_id: light.bedroom
```

YAML
Copy
Important
When using a positive offset the trigger might never fire. This is due to the sensor changing before the offset is reached. For example, when using a phone alarm as a trigger, the sensor value will change to the new alarm time when the alarm goes off, which means this trigger will change to the new time as well.
### Multiple times 
Multiple times can be provided in a list. All formats can be intermixed.
```
automation:
 triggers:
  - trigger: time
   at:
    - input_datetime.leave_for_work
    - "18:30:00"
    - entity_id: sensor.bus_arrival
     offset: "-00:10:00"
```

YAML
Copy
### Limited templates 
It’s also possible to use for times.
```
blueprint:
 input:
  alarm:
   name: Alarm
   selector:
    text:
  hour:
   name: Hour
   selector:
    number:
     min: 0
     max: 24
 trigger_variables:
  my_alarm: !input alarm
  my_hour: !input hour
 trigger:
  - platform: time
   at:
   - "sensor.{{ my_alarm | slugify }}_time"
   - "{{ my_hour }}:30:00"
```

YAML
Copy
### Weekday filtering 
Time triggers can be filtered to fire only on specific days of the week using the weekday option. This allows you to create automations that only run on certain days, such as weekdays or weekends.
The weekday option accepts:
  * A single weekday as a string: "mon", "tue", "wed", "thu", "fri", "sat", "sun" 
  * A list of weekdays using the expanded format


#### Single weekday 
This example will turn on the lights only on Mondays at 8:00 AM:
```
automation:
 - triggers:
   - trigger: time
    at: "08:00:00"
    weekday: "mon"
  actions:
   - action: light.turn_on
    target:
     entity_id: light.bedroom
```

YAML
Copy
#### Multiple weekdays 
This example will run a morning routine only on weekdays (Monday through Friday) at 6:30 AM:
```
automation:
 - triggers:
   - trigger: time
    at: "06:30:00"
    weekday:
     - "mon"
     - "tue"
     - "wed"
     - "thu"
     - "fri"
  actions:
   - action: script.morning_routine
```

YAML
Copy
#### Weekend example 
This example demonstrates a different wake-up time for weekends:
```
automation:
 - alias: "Weekday alarm"
  triggers:
   - trigger: time
    at: "06:30:00"
    weekday:
     - "mon"
     - "tue"
     - "wed"
     - "thu"
     - "fri"
  actions:
   - action: script.weekday_morning
 - alias: "Weekend alarm"
  triggers:
   - trigger: time
    at: "08:00:00"
    weekday:
     - "sat"
     - "sun"
  actions:
   - action: script.weekend_morning
```

YAML
Copy
#### Combined with input datetime 
The weekday option works with all time formats, including input datetime entities:
```
automation:
 - triggers:
   - trigger: time
    at: input_datetime.work_start_time
    weekday:
     - "mon"
     - "tue"
     - "wed"
     - "thu"
     - "fri"
  actions:
   - action: notify.mobile_app
    data:
     title: "Work Day!"
     message: "Time to start working"
```

YAML
Copy
## Time pattern trigger 
With the time pattern trigger, you can match if the hour, minute or second of the current time matches a specific value. You can prefix the value with a / to match whenever the value is divisible by that number. You can specify * to match any value.
```
automation:
 triggers:
  - trigger: time_pattern
   # Matches every hour at 5 minutes past whole
   minutes: 5
automation 2:
 triggers:
  - trigger: time_pattern
   # Trigger once per minute during the hour of 3
   hours: "3"
   minutes: "*"
automation 3:
 triggers:
  - trigger: time_pattern
   # You can also match on interval. This will match every 5 minutes
   minutes: "/5"
```

YAML
Copy
Note
Do not prefix numbers with a zero - using '01' instead of '1' for example will result in errors.
## Persistent notification trigger 
Persistent notification triggers are fired when a persistent_notification is added or removed that matches the configuration options.
```
automation:
 triggers:
  - trigger: persistent_notification
   update_type:
    - added
    - removed
   notification_id: invalid_config
```

YAML
Copy
See the integration for more details on event triggers and the additional event data available for use by an automation.
## Webhook trigger 
Webhook trigger fires when a web request is made to the webhook endpoint: /api/webhook/<webhook_id>. The webhook endpoint is created automatically when you set it as the webhook_id in an automation trigger. The webhook_id can either be a static value or computed using .
Note
The webhook_id template is only evaluated when setting up the trigger, they will not be re-evaluated for incoming webhook triggers.
```
automation:
 trigger_variables:
  webhook_id_variable: "template_webhook_id"
 triggers:
  - trigger: webhook
   webhook_id: "some_hook_id"
   allowed_methods:
    - POST
    - PUT
   local_only: true
  - trigger: webhook
   webhook_id: ""
   allowed_methods:
    - POST
```

YAML
Copy
You can run this automation by sending an HTTP POST request to http://your-home-assistant:8123/api/webhook/some_hook_id. Here is an example using the curl command line program, with an example form data payload:
```
curl -X POST -d 'key=value&key2=value2' https://your-home-assistant:8123/api/webhook/some_hook_id
```

Bash
Copy
Webhooks support HTTP POST, PUT, HEAD, and GET requests; PUT requests are recommended. HTTP GET and HEAD requests are not enabled by default but can be enabled by adding them to the allowed_methods option. The request methods can also be configured in the UI by clicking the settings gear menu button beside the Webhook ID.
By default, webhook triggers can only be accessed from devices on the same network as Home Assistant or via . The local_only option should be set to false to allow webhooks to be triggered directly via the internet. This option can also be configured in the UI by clicking the settings gear menu button beside the Webhook ID.
Remember to use an HTTPS URL if you’ve secured your Home Assistant installation with SSL/TLS.
Note that a given webhook can only be used in one automation at a time. That is, only one automation trigger can use a specific webhook ID.
### Webhook data 
Payloads may either be encoded as form data or JSON. Depending on that, its data will be available in an automation template as either trigger.data or trigger.json. URL query parameters are also available in the template as trigger.query.
Note that to use JSON encoded payloads, the Content-Type header must be set to application/json, e.g.:
```
curl -X POST -H "Content-Type: application/json" -d '{ "key": "value" }' https://your-home-assistant:8123/api/webhook/some_hook_id
```

Bash
Copy
### Webhook security 
Webhook endpoints don’t require authentication, other than knowing a valid webhook ID. Security best practices for webhooks include:
## Zone trigger 
Zone trigger fires when an entity is entering or leaving the zone. The entity can be either a person, or a device_tracker. For zone automation to work, you need to have setup a device tracker platform that supports reporting GPS coordinates. This includes , the and the .
```
automation:
 triggers:
  - trigger: zone
   entity_id: person.paulus
   zone: zone.home
   # Event is either enter or leave
   event: enter # or "leave"
```

YAML
Copy
## Geolocation trigger 
Geolocation trigger fires when an entity is appearing in or disappearing from a zone. Entities that are created by a platform support reporting GPS coordinates. Because entities are generated and removed by these platforms automatically, the entity ID normally cannot be predicted. Instead, this trigger requires the definition of a source, which is directly linked to one of the Geolocation platforms.
Tip
This isn’t for use with device_tracker entities. For those look above at the zone trigger.
```
automation:
 triggers:
  - trigger: geo_location
   source: nsw_rural_fire_service_feed
   zone: zone.bushfire_alert_zone
   # Event is either enter or leave
   event: enter # or "leave"
```

YAML
Copy
## Device triggers 
Device triggers encompass a set of events that are defined by an integration. This includes, for example, state changes of sensors as well as button events from remotes. are set up through autodiscovery.
In contrast to state triggers, device triggers are tied to a device and not necessarily an entity. To use a device trigger, set up an automation through the browser frontend. If you would like to use a device trigger for an automation that is not managed through the browser frontend, you can copy the YAML from the trigger widget in the frontend and paste it into your automation’s trigger list.
## Calendar trigger 
Calendar trigger fires when a event starts or ends, allowing for much more flexible automations than using the Calendar entity state which only supports a single event start at a time.
An optional time offset can be given to have it fire a set time before or after the calendar event (e.g., 5 minutes before event start).
```
automation:
 triggers:
  - trigger: calendar
   # Possible values: start, end
   event: start
   # The calendar entity_id
   entity_id: calendar.light_schedule
   # Optional time offset
   offset: "-00:05:00"
```

YAML
Copy
See the integration for more details on event triggers and the additional event data available for use by an automation.
## Sentence trigger 
A sentence trigger fires when matches a sentence from a voice assistant using the default . Sentence triggers work with Home Assistant Assist. They will not work with external conversation agents such as OpenAI or Google Generative AI unless “Prefer handling commands locally” is enabled in the conversation agent settings.
Sentences are allowed to use some basic like optional and alternative words. For example, [it's ]party time will match both “party time” and “it’s party time”.
```
automation:
 triggers:
  - trigger: conversation
   command:
    - "[it's ]party time"
    - "happy (new year|birthday)"
```

YAML
Copy
The sentences matched by this trigger will be:
Punctuation and casing are ignored, so “It’s PARTY TIME!!!” will also match.
### Related topic 


### Sentence wildcards 
Adding one or more {lists} to your trigger sentences will capture any text at that point in the sentence. A slots object will be . This allows you to match sentences with variable parts, such as album/artist names or a description of a picture.
For example, the sentence play {album} by {artist} will match “play the white album by the beatles” and have the following variables available in the action templates:
  * {{ trigger.slots.album }} - “the white album”
  * {{ trigger.slots.artist }} - “the beatles”


Wildcards will match as much text as possible, which may lead to surprises: “play day by day by taken by trees” will match album as “day” and artist as “day by taken by trees”. Including extra words in your template can help: play {album} by artist {artist} can now correctly match “play day by day by artist taken by trees”.
## Multiple triggers 
It is possible to specify multiple triggers for the same rule. To do so just prefix the first line of each trigger with a dash (-) and indent the next lines accordingly. Whenever one of the triggers fires, processing of your automation rule begins.
```
automation:
 triggers:
  # first trigger
  - trigger: time_pattern
   minutes: 5
   # our second trigger is the sunset
  - trigger: sun
   event: sunset
```

YAML
Copy
## Multiple entity IDs for the same trigger 
It is possible to specify multiple entities for the same trigger. To do so add multiple entities using a nested list. The trigger will fire and start, processing your automation each time the trigger is true for any entity listed.
```
automation:
 triggers:
  - trigger: state
   entity_id:
    - sensor.one
    - sensor.two
    - sensor.three
```

YAML
Copy
## Disabling a trigger 
Every individual trigger in an automation can be disabled, without removing it. To do so, add enabled: false to the trigger. For example:
```
# Example script with a disabled trigger
automation:
 triggers:
  # This trigger will not trigger, as it is disabled.
  # This automation does not run when the sun is set.
  - enabled: false
   trigger: sun
   event: sunset
  # This trigger will fire, as it is not disabled.
  - trigger: time
   at: "15:32:00"
```

YAML
Copy
Triggers can also be disabled based on limited templates or blueprint inputs. These are only evaluated once when the automation is loaded.
```
blueprint:
 input:
  input_boolean:
   name: Boolean
   selector:
    boolean:
  input_number:
   name: Number
   selector:
    number:
     min: 0
     max: 100
 trigger_variables:
  _enable_number: !input input_number
 triggers:
  - trigger: sun
   event_type: sunrise
   enabled: !input input_boolean
  - trigger: sun
   event_type: sunset
   enabled: "{{ _enable_number < 50 }}"
```

YAML
Copy
## Merging lists of triggers 
Caution
This feature requires Home Assistant version 2024.10 or later. If using this in a blueprint, set the min_version for the blueprint to at least this version. See the for more details.
In some advanced cases (like for blueprints with trigger selectors), it may be necessary to insert a second list of triggers into the main trigger list. This can be done by adding a dictionary in the main trigger list with the sole key triggers, and the value for that key contains a second list of triggers. These will then be flattened into a single list of triggers. For example:
```
blueprint:
 name: Nested Trigger Blueprint
 domain: automation
 input:
  usertrigger:
   selector:
    trigger:
triggers:
 - trigger: event
  event_type: manual_event
 - triggers: !input usertrigger
```

YAML
Copy
This blueprint automation can then be triggered either by the fixed manual_event trigger, or additionally by any triggers selected in the trigger selector. This is also applicable for wait_for_trigger action.
## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Using automation blueprints - Home Assistant

Source: https://www.home-assistant.io/docs/automation/using_blueprints/

#  On this page
Automation blueprints are pre-made automationsAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] that you can easily add to your Home Assistant instance. Each blueprint can be added as many times as you want.
Quick links:


## Blueprint automations 
Automations based on a blueprint need to be configured. What needs to be configured differs by blueprint.
  1. To create your first automation based on a blueprint, go to Settings > Automations & Scenes > Blueprints.
  2. Find the blueprint that you want to use and select Create Automation. 
     * This opens the automation editor with the blueprint selected.
  3. Give it a name and configure the blueprint.
  4. Select the blue Save Automation button in the bottom right corner.


Done! If you want to revisit the configuration values, go to Settings > Automations & Scenes > Blueprints.
## Importing blueprints 
Home Assistant can import blueprints from the Home Assistant forums, GitHub, and GitHub gists.
  1. To import a blueprint, first .
     * If you just want to practice importing, you can use this URL:
```
https://github.com/home-assistant/core/blob/dev/homeassistant/components/automation/blueprints/motion_light.yaml
```

Text
Copy
  2. Go to Settings > Automations & Scenes > Blueprints.
  3. Select the blue Import Blueprint button in the bottom right.
     * A new dialog will pop-up asking you for the URL.
  4. Enter the URL and select Preview.
     * This will load the blueprint and show a preview in the import dialog.
     * You can change the name and finish the import.


The blueprint can now be used for creating automations.
## Editing an imported blueprint 
You can tweak an imported blueprint by “taking control” of this blueprint. Home Assistant then converts the blueprint automation into a regular automation, allowing you to make any tweak without having to fully re-invent the wheel.
To edit an imported blueprint, follow these steps:
  1. Go to Settings > Automations & Scenes > Blueprints.
  2. Select the blueprint from the list.
  3. Select the and select Take control.
  4. A preview of the automation is shown.
     * Info: By taking control, the blueprint is converted into an automation. You won’t be able to convert this back into a blueprint.
     * To convert it into an automation and take control, select Yes.
     * If you change your mind and want to keep the blueprint, select No.


## Re-importing a blueprint 
Blueprints created by the community may go through multiple revisions. Sometimes a user creates a blueprint, the community provides feedback, new functionality is added.
The quickest way to get these changes, is by re-importing the blueprint. This will overwrite the blueprint you currently have.
Caution
Before you do this: If the re-imported blueprint is not compatible, it can break your automations.
  * In this case, you will need to manually adjust your automations.


### To re-import a blueprint 
  1. Go to Settings > Automations & Scenes > Blueprints.
  2. On the blueprint that you want to re-import, select the three dots menu, and select Re-import blueprint.


## Updating an imported blueprint in YAML 
Blueprints created by the community may go through multiple revisions. Sometimes a user creates a blueprint, the community provides feedback, new functionality is added.
If you do not want to for some reason, you can manually edit its YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] content to keep it up to date:
  1. Navigate to the blueprints directory (blueprints/automation/). The location of this directory depends on the installation type. It’s similar to how you find .
  2. Next, you must find the blueprint to update. The path name of a blueprint consists of: 
     * The username of the user that created it. The name depends on the source of the blueprint: the forum, or GitHub.
     * The name of the YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] file. For the forum it’s the title of the topic in the URL, for GitHub it’s the name of the YAML file.
  3. Open the YAML file with your editor and update its contents.
  4. Reload the automations for the changes to take effect.


The new changes will appear to your existing automations as well.
## Finding new blueprints 
The Home Assistant Community forums have a specific tag for blueprints. This tag is used to collect all blueprints.
## Creating new blueprints 
Using blueprints is nice and easy, but what if you could create that one missing blueprint that our community definitely needs?
Learn more about blueprints by .
## Troubleshooting missing automations 
When you’re creating automations using blueprints and they don’t appear in the UI, make sure that you add back automation: !include automations.yaml from the default configuration to your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more].
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Backend of Home Assistant - Home Assistant

Source: https://www.home-assistant.io/docs/backend/

#  On this page
The backend of Home Assistant is running with .
The show the details about the elements running in the background of Home Assistant.
To implement a new platform or component, please refer to the .
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Database - Home Assistant

Source: https://www.home-assistant.io/docs/backend/database/

#  On this page


Home Assistant uses databases to store eventsEvery time something happens in Home Assistant, an event is fired. There are different types of events, such as state change events, when an action was triggered, or the time changed. All entities produce state change events. Every time a state changes, a state change event is produced. Events can be used to trigger automations or scripts. For example, you can trigger an automation when a light is turned on, then a speaker turns on in that room. Events can also be used to trigger actions in the frontend. For example, you can trigger an action when a button is pressed. [Learn more] and parameters for history and tracking. The default database used is .
The database file is stored in your (e.g., <path to config dir>/home-assistant_v2.db); however, other databases can be used. If you prefer to run a database server (e.g., PostgreSQL), use the integration.
To work with SQLite database manually from the command-line, you will need an of sqlite3. Alternatively provides a viewer for exploring the database data and an editor for executing SQL commands. First load your database with sqlite3:
```
$ sqlite3 home-assistant_v2.db
SQLite version 3.13.0 2016-05-18 10:57:30
Enter ".help" for usage hints.
sqlite>
```

Bash
Copy
It helps to set some options to make the output more readable:
```
sqlite> .header on
sqlite> .mode column
```

Bash
Copy
You could also start sqlite3 and attach the database later. Not sure what database you are working with? Check it, especially if you are going to delete data.
```
sqlite> .databases
seq name       file
--- --------------- ----------------------------------------------------------
0  main       /home/fab/.homeassistant/home-assistant_v2.db
```

Bash
Copy
### Schema 
Get all available tables from your current Home Assistant database:
```
sqlite> SELECT sql FROM sqlite_master;
-------------------------------------------------------------------------------------
CREATE TABLE event_data (
    data_id INTEGER NOT NULL,
    hash BIGINT,
    shared_data TEXT,
    PRIMARY KEY (data_id)
)
CREATE TABLE event_types (
    event_type_id INTEGER NOT NULL,
    event_type VARCHAR(64),
    PRIMARY KEY (event_type_id)
)
CREATE TABLE state_attributes (
    attributes_id INTEGER NOT NULL,
    hash BIGINT,
    shared_attrs TEXT,
    PRIMARY KEY (attributes_id)
)
CREATE TABLE states_meta (
    metadata_id INTEGER NOT NULL,
    entity_id VARCHAR(255),
    PRIMARY KEY (metadata_id)
)
CREATE TABLE statistics_meta (
    id INTEGER NOT NULL,
    statistic_id VARCHAR(255),
    source VARCHAR(32),
    unit_of_measurement VARCHAR(255),
    has_mean BOOLEAN,
    has_sum BOOLEAN,
    name VARCHAR(255), mean_type INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
)
CREATE TABLE recorder_runs (
    run_id INTEGER NOT NULL,
    start DATETIME NOT NULL,
    "end" DATETIME,
    closed_incorrect BOOLEAN NOT NULL,
    created DATETIME NOT NULL,
    PRIMARY KEY (run_id)
)
CREATE TABLE schema_changes (
    change_id INTEGER NOT NULL,
    schema_version INTEGER,
    changed DATETIME NOT NULL,
    PRIMARY KEY (change_id)
)
CREATE TABLE statistics_runs (
    run_id INTEGER NOT NULL,
    start DATETIME NOT NULL,
    PRIMARY KEY (run_id)
)
CREATE TABLE events (
    event_id INTEGER NOT NULL,
    event_type CHAR(0),
    event_data CHAR(0),
    origin CHAR(0),
    origin_idx SMALLINT,
    time_fired CHAR(0),
    time_fired_ts FLOAT,
    context_id CHAR(0),
    context_user_id CHAR(0),
    context_parent_id CHAR(0),
    data_id INTEGER,
    context_id_bin BLOB,
    context_user_id_bin BLOB,
    context_parent_id_bin BLOB,
    event_type_id INTEGER,
    PRIMARY KEY (event_id),
    FOREIGN KEY(data_id) REFERENCES event_data (data_id),
    FOREIGN KEY(event_type_id) REFERENCES event_types (event_type_id)
)
CREATE TABLE states (
    state_id INTEGER NOT NULL,
    entity_id CHAR(0),
    state VARCHAR(255),
    attributes CHAR(0),
    event_id SMALLINT,
    last_changed CHAR(0),
    last_changed_ts FLOAT,
    last_updated CHAR(0),
    last_updated_ts FLOAT,
    old_state_id INTEGER,
    attributes_id INTEGER,
    context_id CHAR(0),
    context_user_id CHAR(0),
    context_parent_id CHAR(0),
    origin_idx SMALLINT,
    context_id_bin BLOB,
    context_user_id_bin BLOB,
    context_parent_id_bin BLOB,
    metadata_id INTEGER, last_reported_ts FLOAT,
    PRIMARY KEY (state_id),
    FOREIGN KEY(old_state_id) REFERENCES states (state_id),
    FOREIGN KEY(attributes_id) REFERENCES state_attributes (attributes_id),
    FOREIGN KEY(metadata_id) REFERENCES states_meta (metadata_id)
)
CREATE TABLE statistics (
    id INTEGER NOT NULL,
    created CHAR(0),
    created_ts FLOAT,
    metadata_id INTEGER,
    start CHAR(0),
    start_ts FLOAT,
    mean FLOAT,
    min FLOAT,
    max FLOAT,
    last_reset CHAR(0),
    last_reset_ts FLOAT,
    state FLOAT,
    sum FLOAT, mean_weight FLOAT,
    PRIMARY KEY (id),
    FOREIGN KEY(metadata_id) REFERENCES statistics_meta (id) ON DELETE CASCADE
)
CREATE TABLE statistics_short_term (
    id INTEGER NOT NULL,
    created CHAR(0),
    created_ts FLOAT,
    metadata_id INTEGER,
    start CHAR(0),
    start_ts FLOAT,
    mean FLOAT,
    min FLOAT,
    max FLOAT,
    last_reset CHAR(0),
    last_reset_ts FLOAT,
    state FLOAT,
    sum FLOAT, mean_weight FLOAT,
    PRIMARY KEY (id),
    FOREIGN KEY(metadata_id) REFERENCES statistics_meta (id) ON DELETE CASCADE
)
CREATE TABLE sqlite_stat1(tbl,idx,stat)
CREATE INDEX ix_event_data_hash ON event_data (hash)
CREATE UNIQUE INDEX ix_event_types_event_type ON event_types (event_type)
CREATE INDEX ix_state_attributes_hash ON state_attributes (hash)
CREATE UNIQUE INDEX ix_states_meta_entity_id ON states_meta (entity_id)
CREATE UNIQUE INDEX ix_statistics_meta_statistic_id ON statistics_meta (statistic_id)
CREATE INDEX ix_recorder_runs_start_end ON recorder_runs (start, "end")
CREATE INDEX ix_statistics_runs_start ON statistics_runs (start)
CREATE INDEX ix_events_data_id ON events (data_id)
CREATE INDEX ix_events_event_type_id_time_fired_ts ON events (event_type_id, time_fired_ts)
CREATE INDEX ix_events_time_fired_ts ON events (time_fired_ts)
CREATE INDEX ix_events_context_id_bin ON events (context_id_bin)
CREATE INDEX ix_states_context_id_bin ON states (context_id_bin)
CREATE INDEX ix_states_attributes_id ON states (attributes_id)
CREATE INDEX ix_states_last_updated_ts ON states (last_updated_ts)
CREATE INDEX ix_states_metadata_id_last_updated_ts ON states (metadata_id, last_updated_ts)
CREATE INDEX ix_states_old_state_id ON states (old_state_id)
CREATE INDEX ix_statistics_start_ts ON statistics (start_ts)
CREATE UNIQUE INDEX ix_statistics_statistic_id_start_ts ON statistics (metadata_id, start_ts)
CREATE UNIQUE INDEX ix_statistics_short_term_statistic_id_start_ts ON statistics_short_term (metadata_id, start_ts)
CREATE INDEX ix_statistics_short_term_start_ts ON statistics_short_term (start_ts)
CREATE TABLE migration_changes (
    migration_id VARCHAR(255) NOT NULL,
    version SMALLINT NOT NULL,
    PRIMARY KEY (migration_id)
)
```

Bash
Copy
To only show the details about the states table (since we are using that one in the next examples):
```
sqlite> SELECT sql FROM sqlite_master WHERE type = 'table' AND tbl_name = 'states';
```

Bash
Copy
### Query 
The identification of the available columns in the table is done and we are now able to create a query. Let’s list your Top 10 entities:
```
sqlite> .width 30, 10,
sqlite> SELECT states_meta.entity_id, COUNT(*) as count FROM states INNER JOIN states_meta ON states.metadata_id = states_meta.metadata_id GROUP BY states_meta.entity_id ORDER BY count DESC LIMIT 10;
entity_id            count
------------------------------ ----------
sensor.cpu           28874
sun.sun             21238
sensor.time           18415
sensor.new_york         18393
cover.kitchen_cover       17811
switch.mystrom_switch      14101
sensor.internet_time      12963
sensor.solar_angle1       11397
sensor.solar_angle       10440
group.all_switches       8018
```

Bash
Copy
### Delete 
If you don’t want to keep certain entities, you can delete them permanently by using the .
For a more interactive way of working with the database, check the .
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Automation YAML - Home Assistant

Source: https://www.home-assistant.io/docs/automation/yaml/

#  On this page
Automations are created in Home Assistant via the UI, but are stored in a YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] format. If you want to edit the YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] of an automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more], select the automation, click on the menu button in the top right then on Edit in YAML.
The UI will write your automations to automations.yaml. This file is managed by the UI and should not be edited manually.
It is also possible to write your automations directly inside configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] or other YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] files. You can do this by adding a labeled automation block to your configuration.yaml:
```
# The configuration required for the UI to work
automation: !include automations.yaml
# Labeled automation block
automation kitchen:
 - triggers:
   - trigger: ...
```

YAML
Copy
You can add as many labeled automation blocks as you want.
####  Configuration Variables 
alias string (Optional) 
Friendly name for the automation. 
id string (Optional) 
A unique id for your automation, will allow you to make changes to the name and entity_id in the UI, and will enable debug traces. 
description string (Optional) 
A description of the automation. 
initial_state boolean (Optional, default: Restored from last run) 
Used to define the state of your automation at startup. When not set, the state will be restored from the last run. See Automation initial state. 
trace map (Optional, default: {}) 
Configuration values for the traces stored, currently only stored_traces can be configured. 
stored_traces integer (Optional, default: 5) 
The number of traces which will be stored. See Number of debug traces stored. 
variables map (Optional, default: {}) 
Variables that will be available inside your templates, both in conditions and actions. 
PARAMETER_NAME any 
The value of the variable. Any YAML is valid. Templates can also be used to pass a value to the variable. 
trigger_variables map (Optional, default: {}) 
Variables that will be available inside your templates triggers. 
PARAMETER_NAME any 
The value of the variable. Any YAML is valid. Only limited templates can be used. 
mode string (Optional, default: single) 
Controls what happens when the automation is invoked while it is still running from one or more previous invocations. See Automation modes. 
max integer (Optional, default: 10) 
Controls maximum number of runs executing and/or queued up to run at a time. Only valid with modes queued and parallel. 
max_exceeded string (Optional, default: warning) 
When max is exceeded (which is effectively 1 for single mode) a log message will be emitted to indicate this has happened. This option controls the severity level of that log message. See Log Levels for a list of valid options. Or silent may be specified to suppress the message from being emitted. 
triggers list Required 
The trigger(s) which will start the automation. Multiple triggers can be added and the automation will start when any of these triggers trigger. 
id string (Optional) 
An ID that can be used in the automation to determine which trigger caused the automation to start. 
variables map (Optional, default: {}) 
Variables that will be available in the conditions and action sequence. 
PARAMETER_NAME any 
The value of the variable. Any YAML is valid. Templates can also be used to pass a value to the variable. 
conditions list (Optional) 
Conditions that have to be true to start the automation. By default all conditions listed have to be true, you can use logical conditions to change this default behavior. 
actions list Required 
The sequence of actions to be performed in the script. 
### Automation modes 
Mode | Description  
---|---  
single | Do not start a new run. Issue a warning.  
restart | Start a new run after first stopping previous run.  
queued | Start a new run after all previous runs complete. Runs are guaranteed to execute in the order they were queued.  
parallel | Start a new, independent run in parallel with previous runs.  
## YAML example 
Example of a YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] based automation that you can add to configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more].
```
# Example of entry in configuration.yaml
automation my_lights:
 # Turns on lights 1 hour before sunset if people are home
 # and if people get home between 16:00-23:00
 - alias: "Rule 1 Light on in the evening"
  triggers:
   # Prefix the first line of each trigger configuration
   # with a '-' to enter multiple
   - trigger: sun
    event: sunset
    offset: "-01:00:00"
   - trigger: state
    entity_id: all
    to: "home"
  conditions:
   # Prefix the first line of each condition configuration
   # with a '-'' to enter multiple
   - condition: state
    entity_id: all
    state: "home"
   - condition: time
    after: "16:00:00"
    before: "23:00:00"
  actions:
   # With a single action entry, we don't need a '-' before action - though you can if you want to
   - action: homeassistant.turn_on
    target:
     entity_id: group.living_room
 # Turn off lights when everybody leaves the house
 - alias: "Rule 2 - Away Mode"
  triggers:
   - trigger: state
    entity_id: all
    to: "not_home"
  actions:
   - action: light.turn_off
    target:
     entity_id: all
 # Notify when Paulus leaves the house in the evening
 - alias: "Leave Home notification"
  triggers:
   - trigger: zone
    event: leave
    zone: zone.home
    entity_id: device_tracker.paulus
  conditions:
   - condition: time
    after: "20:00"
  actions:
   - action: notify.notify
    data:
     message: "Paulus left the house"
 # Send a notification via Pushover with the event of a Xiaomi cube. Custom event from the Xiaomi integration.
 - alias: "Xiaomi Cube Action"
  initial_state: false
  triggers:
   - trigger: event
    event_type: cube_action
    event_data:
     entity_id: binary_sensor.cube_158d000103a3de
  actions:
   - action: notify.pushover
    data:
     title: "Cube event detected"
     message: "Cube has triggered this event: {{ trigger.event }}"
```

YAML
Copy
## Extra options 
When writing automations directly in YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more], you will have access to advanced options that are not available in the user interface.
### Automation initial state 
At startup, automations by default restore their last state of when Home Assistant ran. This can be controlled with the initial_state option. Set it to false or true to force initial state to be off or on.
```
automation:
 - alias: "Automation Name"
  initial_state: false
  triggers:
   - trigger: ...
```

YAML
Copy
### Number of debug traces stored 
When using YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] you can configure the number of debugging traces stored for an automation. This is controlled with the stored_traces option under trace. Set stored_traces to the number of traces you wish to store for the particular automation. If not specified the default value of 5 will be used.
```
automation:
 - alias: "Automation Name"
  trace:
   stored_traces: 10
  triggers:
   - trigger: ...
```

YAML
Copy
## Migrating your YAML automations to automations.yaml 
If you want to migrate your manual automations to use the editor, you’ll have to copy them to automations.yaml. Make sure that automations.yaml remains a list! For each automation that you copy over, you’ll have to add an id. This can be any string as long as it’s unique.
```
# Example automations.yaml entry. Note, automations.yaml is always a list!
- id: my_unique_id # <-- Required for editor to work, for automations created with the editor the id will be automatically generated.
 alias: "Hello world"
 triggers:
  - trigger: state
   entity_id: sun.sun
   from: below_horizon
   to: above_horizon
 conditions:
  - condition: numeric_state
   entity_id: sensor.temperature
   above: 17
   below: 25
   value_template: "{{ float(state.state) + 2 }}"
 actions:
  - action: light.turn_on
```

YAML
Copy
### Deleting automations 
When automations remain visible in the Home Assistant dashboard, even after having deleted in the YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] file, you have to delete them in the UI.
To delete them completely, go to UI and find the automation in the search field or by scrolling down.
Check the square box aside of the automation you wish to delete and from the top-right of your screen, select ‘REMOVE SELECTED’.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## About blueprints - Home Assistant

Source: https://www.home-assistant.io/docs/blueprint

#  On this page


This section gives a high-level introduction to blueprints. To view a description of the YAML-schema used to create a valid blueprint, refer to the section .
## What is a blueprint? 
A blueprint is a scriptScripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on. [Learn more], automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] or configuration with certain parts marked as configurable. This allows you to create different scripts, automations or template entities based on the same blueprint.
Imagine you want to control lights based on motion. A blueprint provides the generic automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] framework, while letting you select one specific motion sensor as a triggerA trigger is a set of values or conditions of a platform that are defined to cause an automation to run. [Learn more], and the exact light to control. This blueprint makes it possible to create two automations. Each automation has their own configuration and act completely independently. Yet, they share some basic automation configuration so that you do not have to set this up every time.
Automations inherit from blueprints, which means that changes made to a blueprint will be reflected in all automations based on that blueprint the next time the automations are reloaded. This occurs as part of Home Assistant starting. To manually reload the automations, go to and reload the automations.
Blueprints are shared by the community in the .
## Related topics 
## Related links 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## About blueprints - Home Assistant

Source: https://www.home-assistant.io/docs/blueprint/

#  On this page


This section gives a high-level introduction to blueprints. To view a description of the YAML-schema used to create a valid blueprint, refer to the section .
## What is a blueprint? 
A blueprint is a scriptScripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on. [Learn more], automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] or configuration with certain parts marked as configurable. This allows you to create different scripts, automations or template entities based on the same blueprint.
Imagine you want to control lights based on motion. A blueprint provides the generic automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] framework, while letting you select one specific motion sensor as a triggerA trigger is a set of values or conditions of a platform that are defined to cause an automation to run. [Learn more], and the exact light to control. This blueprint makes it possible to create two automations. Each automation has their own configuration and act completely independently. Yet, they share some basic automation configuration so that you do not have to set this up every time.
Automations inherit from blueprints, which means that changes made to a blueprint will be reflected in all automations based on that blueprint the next time the automations are reloaded. This occurs as part of Home Assistant starting. To manually reload the automations, go to and reload the automations.
Blueprints are shared by the community in the .
## Related topics 
## Related links 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Customizing entities - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/customizing-devices/

#  On this page


After adding a new device, you might find the automatically assigned entity ID too technical and the entity lacking a friendly name. You can personalize these elements to better fit your naming conventions or modify other attributes like the icon.
To change entity attributes, follow these steps:
  1. Go to and select the entity from the list.
  2. In the top-right corner, select the cog icon.
  3. Enter or edit the attributes:
  4. To apply the changes, select Update.
  5. If you have used this entity in automations and scripts, you need to rename the entity ID there, too.
     * Go to open the respective tab and find your automation or script.


### Customizing an entity in YAML 
If your entity is not supported, or you could not customize what you need via the user interface, you need to edit the settings in your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file. For a detailed description of the entity configuration variables and information, refer to the .
## Related topics 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Setup basic information - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/basic/

#  On this page
As part of the default onboarding process, Home Assistant can detect your location from IP address geolocation. Home Assistant will automatically select a unit system and time zone based on this location. If you didn’t adjust this directly during onboarding, you can do it later.
Screenshot showing the General settings page. 
The general settings described here are managed by the . If you are interested in the actions offered by this integration, check out the integration documentation.
## Editing the general settings 
To change the general settings that were defined during onboarding, follow these steps:
  1. Go to .
  2. To change network-related configuration, such as the network name, go to .
  3. If some of the settings are not visible, you may need to enable Advanced mode.
     * In the bottom left, select your username to go to your , and enable Advanced mode.
  4. Troubleshooting: If any of the settings are grayed out and can’t be edited, this is because they are defined in the configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file.
     * If you prefer editing the settings in the UI, you have to delete these entries from the configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file.
     * For more information about the general settings in YAML, refer to the .
  5. To apply the changes, follow the steps on .


## Changing a person’s display name 
The display name is the name that is shown in Home Assistant. It can differ from the username, which is the name used to log in.
### Prerequisites 
  * You need administrator rights to change a display name.


## To change a display name 
  1. To edit the display name of a person using Home Assistant, go to and select the person for which you want to change the display name.
  2. Change the display name and select Update to save the change.


## Changing a username 
The username is the name that is used to log in. It can differ from the display name.
### Prerequisites 
  * You need owner rights to change a username.


### To change a username 
  1. To edit the username of a person using Home Assistant, go to and select the person for which you want to change the display name.
  2. Change the username and select Update to save the change. 
     * It must be lowercase and contain no spaces.
     * The log in is case-sensitive.


## Changing authentication settings 
To learn how to edit authentication settings such as password or multi-factor authentication, refer to the following topics:


## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Entities and domains - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/entities_domains/

#  On this page


Your devices are represented in Home Assistant as entities. Entities are the basic building blocks to hold data in Home Assistant. An entity represents a sensorSensors return information about a thing, for instance the level of water in a tank. [Learn more], actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a deviceA device is a model representing a physical or logical unit that contains entities. or a serviceThe term “service” in Home Assistant is used in the sense of an information service. For example, the municipal waste management service that provides entities for organic, paper, and packaging waste. In terms of functionality, the information service is like a device. It is called service to avoid confusion, as it does not come with a piece of hardware.. Entities have and .
All your entities are listed in the entities table, under .
Screenshot of the Entities table. Each line represents an entity.
## Domains 
Each integration in Home Assistant has a unique identifier: a domain. All entities and actions available in Home Assistant are provided by integrations and thus belong to such a domain. The first part of the entity or action, before the . shows the domain they belong to. For example, light.bed_light is an entity in the light domain. bed_light is the ID of the entity.
The domain provides entities, services, and other functionality that other integrations can use. For example, IKEA and Philips Hue both use functionalities provided by the light integration. This is why the look and feel and behavior is similar in Home Assistant.
There are different types of domains: integration domains and entity domains:
  * Integration domains provide functionality primarily for itself: examples are Hue, Matter, or Zigbee.
  * Entity domains don’t use their own functionality as such. But they provide it for other integrations to use.


The integrations listed below are used as entity domains. They are also referred to as building block integrations or entity integrations:
## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Selectors - Home Assistant

Source: https://www.home-assistant.io/docs/blueprint/selectors/

#  On this page
Selectors can be used to specify what values are accepted for a blueprint input. The selector also defines how the input is shown in the user interface.
Some selectors can, for example, show a toggle button to turn something on or off, while another select can filter a list of devices to show only devices that have motion-sensing capabilities.
Having good selectors set on your blueprint automation inputs makes a blueprint easier to use from the UI.
The following selectors are currently available:
Interactive demos of each of these selectors can be found on the .
If no selector is defined, a text input for a single line will be shown.
## Action selector 
The action selector allows the user to input one or more sequences of actions. On the user interface, the action part of the automation editor will be shown. The value of the input will contain a list of actions to perform.
This selector does not have any other options; therefore, it only has its key.
```
action:
```

YAML
Copy
The output of this selector is a list of actions. For example:
```
# Example action selector output result
- action: scene.turn_on
 target:
  entity_id: scene.watching_movies
 metadata: {}
```

YAML
Copy
## Add-on selector 
This can only be used on a Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. installation. For Home Assistant ContainerHome Assistant Container is a standalone container-based installation of Home Assistant Core. Any OCI compatible runtime can be used, but the documentation focus is on Docker. [Learn more] installations, an error will be displayed.
The add-on selector allows the user to input an add-on slug. On the user interface, it will list all installed add-ons and use the slug of the selected add-on.
This selector does not have any other options; therefore, it only has its key.
```
# Example add-on selector
addon:
```

YAML
Copy
The output of this selector is the slug of the selected add-on. For example: core_ssh.
## Area selector 
The area selector shows an area finder that can pick a single or multiple areas based on the selector configuration. The value of the input will be the area ID, or a list of area IDs, based on if multiple is set to true.
An area selector can filter the list of areas, based on properties of the devices and entities that are assigned to those areas. For example, the areas list could be limited to areas with entities provided by the integration.
In its most basic form, this selector doesn’t require any options, which will show all areas.
```
area:
```

YAML
Copy
####  Configuration Variables 
device list (Optional) 
When device options are provided, the list of areas is filtered by areas that at least provide one device that matches the given conditions. Can be either a object or a list of object. 
integration string (Optional) 
Can be set to an integration domain. Limits the list of areas that provide devices by the set integration domain, for example, zha. 
manufacturer string (Optional) 
When set, it limits the list of areas that provide devices by the set manufacturer name. 
model string (Optional) 
When set, it limits the list of areas that provide devices that have the set model. 
model_id string (Optional) 
When set, the list of areas is limited to areas with devices that have the set model ID. 
entity list (Optional) 
When entity options are provided, the list of areas is filtered by areas that at least provide one entity that matches the given conditions. Can be either a object or a list of object. 
integration string (Optional) 
Can be set to an integration domain. Limits the list of areas that provide entities by the set integration domain, for example, zha. 
domain string | list (Optional) 
Limits the list of areas that provide entities of a certain domain(s), for example, light or binary_sensor. Can be either a string with a single domain, or a list of string domains to limit the selection to. 
device_class device_class | list (Optional) 
Limits the list of areas to areas that have entities with a certain device class(es), for example, motion or window. Can be either a string with a single device_class, or a list of string device_class to limit the selection to. 
supported_features list (Optional) 
Limits the list of areas to areas that have entities with a certain supported feature, for example, light.LightEntityFeature.TRANSITION or climate.ClimateEntityFeature.TARGET_TEMPERATURE. Should be a list of features. For a list of supported features for each entity type, refer to the entity documentation. 
multiple boolean (Optional, default: false) 
Allows selecting multiple areas. If set to true, the resulting value of this selector will be a list instead of a single string value. 
The output of this selector is the area ID, or (in case multiple is set to true) a list of area IDs.
```
# Example area selector output result, when multiple is set to false
living_room
# Example area selector output result, when multiple is set to true
- living_room
- kitchen
```

YAML
Copy
### Example area selectors 
An example area selector only shows areas that provide one or more lights or switches provided by the integration.
```
area:
 entity:
  integration: zha
  domain:
   - light
   - switch
```

YAML
Copy
Another example uses the area selector, which only shows areas that provide one or more remote controls provided by the integration. Multiple areas can be selected.
```
area:
 multiple: true
 device:
  - integration: deconz
   manufacturer: IKEA of Sweden
   model: TRADFRI remote control
```

YAML
Copy
## Attribute selector 
The attributes selector shows a list of state attributes from a provided entity of which one can be selected.
This allows for selecting, e.g., the “Effect” attribute from a light entity, or the “Next dawn” attribute from the sun entity.
####  Configuration Variables 
entity_id string Required 
The entity ID of which an state attribute can be selected from. 
The output of this selector is the selected attribute key (not the translated or prettified name shown in the frontend). For example: next_dawn.
## Assist pipeline selector 
The assist pipeline selector shows all available assist pipelines (assistants) of which one can be selected.
This selector does not have any other options; therefore, it only has its key.
```
assist_pipeline:
```

YAML
Copy
## Backup location selector 
This can only be used on an installation with a Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users.. For Home Assistant ContainerHome Assistant Container is a standalone container-based installation of Home Assistant Core. Any OCI compatible runtime can be used, but the documentation focus is on Docker. [Learn more] installations, an error
will be displayed.
The backup location selector shows a list of places a backup could go, depending on what you have configured in .
The output of this selector is the name of the selected network storage. It may also be the value /backup, if the user chooses to use the local data disk option instead of one of the configured network storage locations.
```
backup_location:
```

YAML
Copy
## Boolean selector 
The boolean selector shows a toggle that allows the user to turn on or off the selected option.
The boolean selector is suitable for adding feature switches to, for example, blueprints.
This selector does not have any other options; therefore, it only has its key.
```
boolean:
```

YAML
Copy
The output of this selector is true when the toggle is on, false otherwise.
## Color temperature selector 
The color temperature selector allows you to select a color temperature from a gradient using a slider.
```
color_temp:
```

YAML
Copy
####  Configuration Variables 
unit string (Optional, default: mired) 
The chosen unit for the color temperature. This can be either kelvin or mired. mired is the default for historical reasons. 
min integer (Optional) 
The minimum color temperature in the chosen unit. 
Default: 
2700 for kelvin 153 for mired
max integer (Optional) 
The maximum color temperature in the chosen unit. 
Default: 
6500 for kelvin 500 for mired
The output of this selector is the number representing the chosen color temperature for the unit used.
## Condition selector 
The condition selector allows the user to input one or more conditions. On the user interface, the condition part of the automation editor will be shown. The value of the input will contain a list of conditions.
This selector does not have any other options; therefore, it only has its key.
```
condition:
```

YAML
Copy
The output of this selector is a list of conditions. For example:
```
# Example condition selector output result
- condition: numeric_state
 entity_id: "sensor.outside_temperature"
 below: 20
```

YAML
Copy
## Config entry selector 
The config entry selector allows the user to select an integration configuration entry. The selector returns the entry ID of the selected integration configuration entry.
```
config_entry:
```

YAML
Copy
####  Configuration Variables 
integration string (Optional) 
Limits the list of selectable configuration entries to a single integration domain. 
The output of this selector is the entry ID of the config entry, for example, 6b68b250388cbe0d620c92dd3acc93ec.
## Constant selector 
The constant selector shows a toggle that allows the user to enable the selected option. This is similar to the , the difference is that the constant selector has no value when it’s not enabled.
The selector’s value must be configured, and optionally, a label.
```
constant:
 value: true
 label: Enabled
```

YAML
Copy
The output of this selector is the configured value when the toggle is on, it has no output otherwise.
## Conversation agent selector 
The conversation agent selector allows picking a conversation agent.
The selector has 1 option, language. This filters the conversation agents shown, depending on the language.
```
conversation_agent:
 language: en
```

YAML
Copy
####  Configuration Variables 
language string (Optional) 
Limits the list of conversation agents to those supporting the specified language. 
The output of this selector is the ID of the conversation agent.
## Country selector 
The country selector allows a user to pick a country from a list of countries.
```
country:
```

YAML
Copy
####  Configuration Variables 
countries list (Optional) 
A list of countries to pick from, this should be ISO 3166 country codes. 
Default: 
The available countries in the Home Assistant frontend
no_sort boolean (Optional, default: false) 
Should the options be sorted by name, if set to true, the order of the provided countries is kept. 
The output of this selector is an ISO 3166 country code.
## Date selector 
The date selector shows a date input that allows the user to specify a date.
This selector does not have any other options; therefore, it only has its key.
```
date:
```

YAML
Copy
The output of this selector will contain the date in Year-Month-Day (YYYY-MM-DD) format, for example, 2022-02-22.
## Date & time selector 
The date selector shows a date and time input that allows the user to specify a date with a specific time.
This selector does not have any other options; therefore, it only has its key.
```
datetime:
```

YAML
Copy
The output of this selector will contain the date in Year-Month-Day (YYYY-MM-DD) format and the time in 24-hour format, for example: 2022-02-22 13:30:00.
## Device selector 
The device selector shows a device finder that can pick a single or multiple devices based on the selector configuration. The value of the input will contain the device ID or a list of device IDs, based on if multiple is set to true.
A device selector can filter the list of devices, based on things like the manufacturer, model, or model ID of the device, the entities the device provides or based on the domain that provided the device.
In its most basic form, this selector doesn’t require any options, which will show all devices.
```
device:
```

YAML
Copy
####  Configuration Variables 
entity list (Optional) 
When entity options are provided, the list of devices is filtered by devices that at least provide one entity that matches the given conditions. Can be either a object or a list of object. 
integration string (Optional) 
Can be set to an integration domain. Limits the list of devices that provide entities by the set integration domain, for example, zha. 
domain string (Optional) 
Limits the list of devices that provide entities of a certain domain(s), for example, light or binary_sensor. Can be either a string with a single domain, or a list of string domains to limit the selection to. 
device_class device_class | list (Optional) 
Limits the list of devices to devices that have entities with a certain device class(es), for example, motion or window. Can be either a string with a single device_class, or a list of string device_class to limit the selection to. 
supported_features list (Optional) 
Limits the list of devices to devices that have entities with a certain supported feature, for example, light.LightEntityFeature.TRANSITION or climate.ClimateEntityFeature.TARGET_TEMPERATURE. Should be a list of features. For a list of supported features for each entity type, refer to the entity documentation. 
filter list (Optional) 
When filter options are provided, the list of devices is filtered by devices that at least provide one entity that matches the given conditions. Can be either a object or a list of object. 
integration string (Optional) 
Can be set to an integration domain. Limits the list of devices to devices provided by the set integration domain. 
manufacturer string (Optional) 
When set, it limits the list of devices to devices provided by the set manufacturer name. 
model string (Optional) 
When set, it limits the list of devices to devices that have the set model. 
model_id string (Optional) 
When set, the list of devices is limited to devices that have the set model ID. 
multiple boolean (Optional, default: false) 
Allows selecting multiple devices. If set to true, the resulting value of this selector will be a list instead of a single string value. 
The output of this selector is the device ID, or (in case multiple is set to true) a list of devices IDs.
```
# Example device selector output result, when multiple is set to false
faadde5365842003e8ca55267fe9d1f4
# Example device selector output result, when multiple is set to true
- faadde5365842003e8ca55267fe9d1f4
- 3da77cb054352848b9544d40e19de562
```

YAML
Copy
### Example device selector 
An example entity selector that, will only show devices that are:
  * Provided by the integration.
  * Are a Philips Hue Remote of Model RWL021.
  * Provide a battery .


And this is what is looks like in YAML:
```
device:
 filter:
  - integration: deconz
   manufacturer: Philips
   model: RWL021
 entity:
  - domain: sensor
   device_class: battery
```

YAML
Copy
## Duration selector 
The duration select allow the user to select a time duration. This can be helpful for, e.g., delays or offsets.
```
duration:
```

YAML
Copy
####  Configuration Variables 
enable_day boolean (Optional, default: false) 
When true, the duration selector will allow selecting days. 
enable_millisecond boolean (Optional, default: false) 
When true, the duration selector will allow selecting milliseconds. 
The output of this selector is a mapping of the time values the user selected. For example:
```
days: 1 # Only when enable_day was set to true
hours: 12
minutes: 30
seconds: 15
milliseconds: 500 # Only when enable_millisecond was set to true
```

YAML
Copy
## Entity selector 
The entity selector shows an entity finder that can pick a single entity or a list of entities based on the selector configuration. The value of the input will contain the entity ID, or list of entity IDs, based on if multiple is set to true.
An entity selector can filter the list of entities, based on things like the class of the device, the domain of the entity or the domain that provided the entity.
In its most basic form, this selector doesn’t require any options, which will show all entities.
```
entity:
```

YAML
Copy
####  Configuration Variables 
exclude_entities list (Optional) 
List of entity IDs to exclude from the selectable list. 
include_entities list (Optional) 
List of entity IDs to limit the selectable list to. 
filter list (Optional) 
When filter options are provided, the entities are limited by entities that at least match the given conditions. Can be either an object or a list of objects. 
integration string (Optional) 
Can be set to an integration domain. Limits the list of entities to entities provided by the set integration domain, for example, zha. 
domain string | list (Optional) 
Limits the list of entities to entities of a certain domain(s), for example, light or binary_sensor. Can be either a string with a single domain, or a list of string domains to limit the selection to. 
device_class device_class | list (Optional) 
Limits the list of entities to entities that have a certain device class(es), for example, motion or window. Can be either a string with a single device_class, or a list of string device_class to limit the selection to. 
supported_features list (Optional) 
Limits the list of entities to entities that have a certain supported feature, for example, light.LightEntityFeature.TRANSITION or climate.ClimateEntityFeature.TARGET_TEMPERATURE. Should be a list of features. 
multiple boolean (Optional, default: false) 
Allows selecting multiple entities. If set to true, the resulting value of this selector will be a list instead of a single string value. 
reorder boolean (Optional, default: false) 
Allows reordering of entities (only applies if multiple is set to true). 
The output of this selector is the entity ID, or (in case multiple is set to true) a list of entity IDs.
```
# Example entity selector output result, when multiple is set to false
light.living_room
# Example entity selector output result, when multiple is set to true
- light.living_room
- light.kitchen
```

YAML
Copy
### Example entity selector 
An example entity selector that, will only show entities that are:
And this is what it looks like in YAML:
```
entity:
 multiple: true
 filter:
  - integration: zha
   domain: binary_sensor
   device_class: motion
```

YAML
Copy
## Floor selector 
The floor selector shows a floor finder that can pick floors based on the selector configuration. The value of the input will be the floor ID. If multiple is set to true, the value is a list of floor IDs.
A floor selector can filter the list of floors based on the properties of the devices and entities assigned to the areas on those floors. For example, the floor list could be limited to floors with entities provided by the integration, based on the areas they are in.
In its most basic form, this selector doesn’t require any options. It will show all floors.
```
floor:
```

YAML
Copy
####  Configuration Variables 
device list (Optional) 
When device options are provided, the list of floors is filtered by floors that have at least one device matching the given conditions. Can be either an object or a list of objects. 
integration string (Optional) 
Can be set to an integration domain. Limits the list of floors that have devices by this integration domain. For example, zha. 
manufacturer string (Optional) 
When set, the list only includes floors that have devices by the set manufacturer name. 
model string (Optional) 
When set, the list only includes floors that have devices which have the set model. 
model_id string (Optional) 
When set, the list only includes floors with devices that have the set model ID. 
entity list (Optional) 
When entity options are provided, the list only includes floors that at least have one entity that matches the given conditions. Can be either an object or a list of objects. 
integration string (Optional) 
Can be set to an integration domain. Limits the list of floors that have entities by the set integration domain. For example, zha. 
domain string | list (Optional) 
When set, the list only includes floors that have entities of certain domains, for example, light or binary_sensor. Can be either a string with a single domain, or a list of string domains to limit the selection to. 
device_class device_class | list (Optional) 
When set, the list only includes floors that have entities with a certain device class, for example, motion or window. Can be either a string with a single device_class, or a list of string device_class to limit the selection. 
supported_features list (Optional) 
When set, the list only includes floors that have entities with a certain supported feature, for example, light.LightEntityFeature.TRANSITION or climate.ClimateEntityFeature.TARGET_TEMPERATURE. Should be a list of features. 
multiple boolean (Optional, default: false) 
Allows selecting multiple floors. If set to true, the resulting value of this selector will be a list instead of a single string value. 
The output of this selector is the floor ID, or (in case multiple is set to true) a list of floor IDs.
```
# Example floor selector output result, when multiple is set to false
first_floor
# Example floor selector output result, when multiple is set to true
- first_floor
- second_floor
```

YAML
Copy
### Example floor selectors 
An example floor selector only shows floors that have one or more lights or switches provided by the integration.
```
floor:
 entity:
  integration: zha
  domain:
   - light
   - switch
```

YAML
Copy
Another example using the floor selector, which only shows floors that have one or more remote controls provided by the integration. Multiple floors can be selected.
```
floor:
 multiple: true
 device:
  - integration: deconz
   manufacturer: IKEA of Sweden
   model: TRADFRI remote control
```

YAML
Copy
## Icon selector 
The icon selector shows an icon picker that allows the user to select an icon.
```
icon:
```

YAML
Copy
####  Configuration Variables 
placeholder string (Optional) 
Placeholder icon to show, when no icon is selected. 
The output of this selector is a string containing the selected icon, for example: mdi:bell.
## Label selector 
The label selector shows a label finder that can pick labels. The value of the input is the label ID. If multiple is set to true, the value is a list of label IDs.
In its most basic form, this selector doesn’t require any options. It will show all labels.
```
label:
```

YAML
Copy
####  Configuration Variables 
multiple boolean (Optional, default: false) 
Allows selecting multiple labels. If set to true, the resulting value of this selector will be a list instead of a single string value. 
The output of this selector is the label ID, or (in case multiple is set to true) a list of label IDs.
```
# Example label selector output result, when multiple is set to false
energy_saving
# Example label selector output result, when multiple is set to true
- energy_saving
- christmas_decorations
```

YAML
Copy
## Language selector 
The language selector allows a user to pick a language from a list of languages.
```
language:
```

YAML
Copy
####  Configuration Variables 
languages list (Optional) 
A list of languages to pick from, this should be RFC 5646 languages codes. 
Default: 
The available languages in the Home Assistant frontend
native_name boolean (Optional, default: false) 
Should the name of the languages be shown in the language of the user, or in the language itself. 
no_sort boolean (Optional, default: false) 
Should the options be sorted by name, if set to true, the order of the provided languages is kept. 
The output of this selector is a RFC 5646 language code.
## Location selector 
The location selector allow a user to pick a location from a map and returns the matching longitude and latitude coordinators. Optionally it supports selecting the radius of the location.
```
location:
```

YAML
Copy
####  Configuration Variables 
icon string (Optional) 
An optional icon to show on the map. 
radius boolean (Optional, default: false) 
Allow selecting the radius of the location. If enabled, the radius will be returned in meters. 
The output of this selector is a mapping containing the latitude and longitude of the selected location, and, if enabled, the radius. For example:
```
latitude: 50.935
longitude: 6.95
radius: 500 # Only provided when radius was set to true.
```

YAML
Copy
## Media selector 
The media selector is a powerful selector that allows a user to easily select media to play on a media device. Media can be a lot of things, for example, cameras, local media, text-to-speech, Home Assistant Dashboards, and many more.
You are prompted to select the device used to play media. Once the device is selected, the media selector only shows media that is suitable for this device.
To ask the user to select a media device and suitable media, you can use the media selector without any options:
```
media:
```

YAML
Copy
You can also use the media selector with an optional accept filter to limit the media types that can be selected. The user will not be asked to pick a device.
```
media:
 accept:
  - image/*
```

YAML
Copy
####  Configuration Variables 
accept list (Optional) 
List of media types the user is allowed to select. 
multiple boolean (Optional, default: false) 
Allows selecting multiple media items. If set to true, the resulting value of this selector will be a list instead of a single object. 
The output of the media selector, is an mapping with information about the selected media device and the selected media to play. There is also metadata, which is used by the frontend and should not be used in the backend.
Example output:
```
entity_id: media_player.living_room
media_content_id: media-source://tts/cloud?message=TTS+Message&language=en-US&gender=female
media_content_type: provider
metadata:
 title: TTS Message
 thumbnail: https://brands.home-assistant.io/_/cloud/logo.png
 media_class: app
 children_media_class: null
 navigateIds:
  - {}
  - media_content_type: app
   media_content_id: media-source://tts
  - media_content_type: provider
   media_content_id: >-
    media-source://tts/cloud?message=TTS+Message&language=en-US&gender=female
```

YAML
Copy
Example output if accept filter is used. Note that the entity_id is not present:
```
media_content_id: media-source://tts/cloud?message=TTS+Message&language=en-US&gender=female
media_content_type: provider
metadata:
 title: TTS Message
 thumbnail: https://brands.home-assistant.io/_/cloud/logo.png
 media_class: app
 children_media_class: null
 navigateIds:
  - {}
  - media_content_type: app
   media_content_id: media-source://tts
  - media_content_type: provider
   media_content_id: >-
    media-source://tts/cloud?message=TTS+Message&language=en-US&gender=female
```

YAML
Copy
Example output when multiple is set to true (a list of media objects):
```
- media_content_id: media-source://media_source/local/image1.jpg
 media_content_type: image/jpeg
 metadata:
  title: image1.jpg
- media_content_id: media-source://media_source/local/image2.jpg
 media_content_type: image/jpeg
 metadata:
  title: image2.jpg
```

YAML
Copy
## Number selector 
The number selector shows either a number input or a slider input, that allows the user to specify a numeric value. The value of the input will contain the select value.
On the user interface, the input can either be in a slider or number mode. Both modes limit the user input by a minimum and maximum value, and can have a unit of measurement to go with it.
In its most basic form, this selector requires a minimum and maximum value:
```
number:
 min: 0
 max: 100
```

YAML
Copy
####  Configuration Variables 
min integer | float (Optional) 
The minimum user-settable number value. 
max integer | float (Optional) 
The maximum user-settable number value. 
step integer | float | any (Optional, default: 1) 
The step size of the number value. Set to "any" to allow any number. 
unit_of_measurement string (Optional) 
Unit of measurement in which the number value is expressed in. 
mode string (Optional) 
This can be either box or slider mode. 
Default: 
slider if min and max are set, otherwise box
translation_key string (Optional) 
Allows translations provided by an integration where translation_key is the translation key that is providing the unit_of_measurement string translation. See the documentation on Backend Localization for more information. 
The output of this selector is a number, for example: 42
### Example number selectors 
An example number selector that allows a user a percentage, directly in a regular number input box.
```
number:
 min: 0
 max: 100
 unit_of_measurement: "%"
```

YAML
Copy
A more visual variant of this example could be achieved using a slider. This can be helpful for things like allowing the user to select a brightness level of lights. Additionally, this example changes the brightness in incremental steps of 10%.
```
number:
 min: 0
 max: 100
 step: 10
 unit_of_measurement: "%"
 mode: slider
```

YAML
Copy
## Object selector 
The object selector can be used to input arbitrary data in YAML form. This is useful for e.g. lists and dictionaries containing data for actions. The value of the input will contain the provided data.
When used without options, the selector will accept any valid YAML content, such as objects, arrays, strings, or other YAML types. The input box is displayed as an editor with syntax highlighting.
```
object:
```

YAML
Copy
When used with fields specified, the selector will force the object to be in this format by displaying a form.
```
object:
 label_field: name
 description_field: percentage
 multiple: true
 fields:
  name:
   label: Name
   selector:
    text:
  percentage:
   label: Percentage
   selector:
    number:
     unit_of_measurement: "%"
```

YAML
Copy
The output of this selector is a YAML object.
####  Configuration Variables 
fields map (Optional) 
List of fields of the object. 
label string (Optional) 
The label of the field 
required boolean (Optional, default: false) 
If set to true, the field must be present. 
selector string Required 
The selector to use for this field. It can be any available selector. 
label_field string (Optional) 
The field to use as a label. By default, it will be the first field defined. This option is only used if fields option set. 
description_field string (Optional) 
The field to use as a description. This option is only used if fields option set. 
translation_key string (Optional) 
Allows translations provided by an integration where translation_key is the translation key that is providing the selector option strings translation. See the documentation on Backend Localization for more information. 
multiple boolean (Optional, default: false) 
Allows adding multiple objects. If set to true, the resulting value of this selector will be a list instead of a single YAML object. This option is only used if fields option set. 
## QR code selector 
The QR code selector shows a QR code. It has no return value.
The QR code’s data must be configured, and optionally, the scale, and error correction level can be set. The scale makes the QR code bigger or smaller.
####  Configuration Variables 
data any Required 
The data that should be represented in the QR code. 
scale integer (Optional, default: 4) 
The scale factor to use, this will make the QR code bigger or smaller. 
error_correction_level string (Optional, default: medium) 
The error correction level of the QR code, with a higher error correction level the QR code can be scanned even when some pieces are missing. Can be “low”, “medium”, “quartile” or “high”. 
```
qr_code:
 data: "https://home-assistant.io"
 scale: 5
 error_correction_level: quartile
```

YAML
Copy
## RGB color selector 
The RGB color selector allows the user to select an color from a color picker from the user interface, and returns the RGB color value.
```
color_rgb:
```

YAML
Copy
This selector does not have any other options; therefore, it only has its key.
The output of this selector is a list with the three (RGB) color value, for example: [255, 0, 0].
## Select selector 
The select selector shows a list of available options from which the user can choose. The value of the input contains the value of the selected option. Only a single option can be selected at a time.
The selector requires a list of options that the user can choose from.
```
select:
 options:
  - Red
  - Green
  - Blue
```

YAML
Copy
####  Configuration Variables 
options list Required 
List of options that the user can choose from. Small lists (5 items or less), are displayed as radio buttons. When more items are added, a dropdown list is used. 
multiple boolean (Optional, default: false) 
Allows selecting multiple options. If set to true, the resulting value of this selector will be a list instead of a single string value. 
custom_value boolean (Optional, default: false) 
Allows the user to enter and select a custom value (or multiple custom values in addition to the listed options if multiple is set to true). 
mode string (Optional) 
This can be either list (radio buttons) or dropdown (combobox) mode. When not specified, small lists (5 items or less), are displayed as radio buttons. When more items are added, a dropdown list is used. If custom_value is true, this setting will be ignored and the frontend will use a dropdown input. 
translation_key string (Optional) 
Allows translations provided by an integration where translation_key is the translation key that is providing the selector option strings translation. See the documentation on Backend Localization for more information. 
sort boolean (Optional, default: false) 
Display options in alphabetical order. 
Alternatively, a mapping can be used for the options. When you want to return a different value compared to how it is displayed to the user.
```
select:
 options:
  - label: Red
   value: r
  - label: Green
   value: g
  - label: Blue
   value: b
```

YAML
Copy
####  Configuration Variables 
options map Required 
List of options that the user can choose from. Small lists (5 items or less), are displayed as radio buttons. When more items are added, a dropdown list is used. 
label string Required 
The description to show in the UI for this item. 
value string Required 
The value to return when this label is selected. 
When multiple is false, the output of this selector is the string of the selected option value. When selecting Green in the last example, it returns: g, in the first example it would return Green.
When multiple is true, the output of this selector is the list of selected option values. In this case, if Green was selected, in the first example it would return [“Green”] and in the last example it returns [“g”].
## State selector 
The state selector shows a list of states for a provided entity of which one or more can be selected.
####  Configuration Variables 
entity_id string (Optional) 
The entity ID of which an state can be selected from. 
hide_states list (Optional) 
The states to exclude from the list of options 
multiple boolean 
Allows selecting multiple states. If set to true, the resulting value of this selector will be a list instead of a single string value. 
The output of this selector is the select state (not the translated or prettified name shown in the frontend), or a list of states if multiple is true.
For example: heat_cool.
## Statistic selector 
The statistic selector selects the statistic ID of an entity that records Long-term statisticsHome Assistant saves long-term statistics for a sensor if the entity has a state_class of measurement, total, or total_increasing. For short-term statistics, a snapshot is taken every 5 minutes. For long-term statistics, an hourly aggregate is stored of the short-term statistics. Short-term statistics are automatically purged after a predefined period (default is 10 days). Long-term statistics are never purged. [Learn more]. It may resemble an entity ID (like sensor.temperature), or an external statistic ID (like external:temperature).
####  Configuration Variables 
multiple boolean (Optional, default: false) 
If set to true, the selector returns a list of statistic IDs. 
The output of this selector is a string representing a statistic ID, or a list of statistic IDs if multiple is set to true.
## Target selector 
The target selector is a rather special selector, allowing the user to select targeted entities, devices, or areas for actions. The value of the input will contain a special target format, that is accepted by actions.
The selectable targets can be filtered, based on entity or device properties. Areas are only selectable as a target, if some entities or devices match those properties in those areas.
In its most basic form, this selector does not require any options, which will allow the user to target any entity, device or area available in the system.
```
target:
```

YAML
Copy
####  Configuration Variables 
entity list (Optional) 
When entity options are provided, the targets are limited by entities that at least match the given conditions. Can be either a object or a list of object. 
integration string (Optional) 
Can be set to an integration domain. Limits targets to entities provided by the set integration domain, for example, zha. 
domain string | list (Optional) 
Limits the targets to entities of a certain domain(s), for example, light or binary_sensor. Can be either a with a single domain, or a list of string domains to limit the selection to. 
device_class device_class | list (Optional) 
Limits the targets to entities with a certain device class(es), for example, motion or window. Can be either a string with a single device_class, or a list of string device_class to limit the selection to. 
supported_features list (Optional) 
Limits the targets to entities with a certain supported feature, for example, light.LightEntityFeature.TRANSITION or climate.ClimateEntityFeature.TARGET_TEMPERATURE. Should be a list of features. For a list of supported features for each entity type, refer to the entity documentation. 
Important
Targets are meant to be used with the target property of an action in a script sequence. For example:
```
actions:
 - action: light.turn_on
  target: !input lights
```

YAML
Copy
### Example target selectors 
An example target selector that only shows targets that at least provide one or more lights, provided by the integration.
```
target:
 entity:
  - integration: zha
   domain: light
```

YAML
Copy
## Template selector 
The template selector can be used to input a Jinja2 template. This is useful for allowing more advanced user-input that use Jinja2 templates.
This selector does not have any other options; therefore, it only has its key.
```
template:
```

YAML
Copy
The output of this selector is a template string.
## Text selector 
The text selector can be used to enter a text string. It can also be used to enter a list of text strings; if multiple is set to true. The value of the input will contain the selected text. This can be used in shopping lists, for example.
Unless multiline is set to true, this selector behaves exactly like if no selector at all was specified, and will display a single line text input box on the user interface.
```
text:
```

YAML
Copy
####  Configuration Variables 
multiline boolean (Optional, default: false) 
Set to true to display the input as a multi-line text box on the user interface. 
prefix string (Optional) 
An optional prefix to show before the text input box. 
suffix string (Optional) 
An optional suffix to show after the text input box. 
type string (Optional, default: text) 
The type of input. This supplies the HTML type attribute, which controls how the browser displays and validates the field. A subset of types available to the attribute are supported, since some are handled by other selectors. Possible types are: color, date, datetime-local, email, month, number, password, search, tel, text, time, url, week. 
autocomplete string (Optional) 
Guides the browser on the type of information which should automatically fill the field. This supplies the HTML autocomplete attribute. Any value supported by the HTML attribute is valid. 
multiple boolean (Optional, default: false) 
Allows adding list of text strings. If set to true, the resulting value of this selector will be a list instead of a single string value. 
The output of this selector is a single string value.
## Theme selector 
The theme selector allows for selecting a theme from the available themes installed in Home Assistant.
```
theme:
```

YAML
Copy
####  Configuration Variables 
include_default boolean (Optional, default: false) 
Includes Home Assistant default theme in the list. 
The output of this selector will contain the selected theme, for example: waves_dark.
## Time selector 
The time selector shows a time input that allows the user to specify a time of the day.
This selector does not have any other options; therefore, it only has its key.
```
time:
```

YAML
Copy
The output of this selector will contain the time in 24-hour format, for example, 23:59:59.
## Trigger selector 
The triggers selector allows the user to input one or more triggers. On the user interface, the trigger part of the automation editor is shown. The value of the input contains a list of triggers.
This selector does not have any other options; therefore, it only has its key.
```
trigger:
```

YAML
Copy
The output of this selector is a list of triggers. For example:
```
# Example trigger selector output result
- trigger: numeric_state
 entity_id: "sensor.outside_temperature"
 below: 20
```

YAML
Copy
### Example - Merging with existing triggers 
If the trigger(s) should exist within a blueprint that already has some default triggers defined, and an additional customizable trigger should be merged, you need to use the - triggers syntax in the blueprint.
```
# Example trigger selector
input:
 my_trigger_input:
  selector:
   trigger:
triggers:
 - triggers: !input my_trigger_input
 - platform: numeric_state
 [...]
```

YAML
Copy
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## About the blueprint schema - Home Assistant

Source: https://www.home-assistant.io/docs/blueprint/schema/

#  On this page
## The blueprint schema 
Blueprint schemas currently supports three types of schema depending on its domain: ; script; and .
The configuration schema of a blueprint consists of 2 parts:
  1. The blueprint’s high-level metadata: name, domain and, optionally, any input required from the user.
  2. The schema for the blueprint domain it describes.


The first part is referred to as the blueprint schema. It contains the blueprint’s metadata.
Minimum required metadata for a blueprint is its name and domain. In its most basic form, a blueprint looks like:
```
blueprint:
 name: Example blueprint
 domain: automation
```

YAML
Copy
Although this is a valid blueprint, it is not very useful.
The second part depends on its domain, the type of blueprint. For example, when creating a blueprint for an automation, the full schema for an applies.
This is the full blueprint schema:
####  Configuration Variables 
name string Required 
The name of the blueprint. Keep this short and descriptive. 
description string (Optional) 
The description of the blueprint. While optional, this field is highly recommended. Describe what the blueprint does and describe the inputs the blueprint requires. The description can include Markdown. 
domain string Required 
The domain in which this blueprint is used. Currently, only three types, automation, script and template are supported. 
author string (Optional) 
The name of the blueprint author. 
homeassistant map (Optional) 
Home Assistant version required for the blueprint to work successfully. 
min_version string (Optional) 
Minimum required version of Home Assistant to use the blueprint in the format of major.minor.patch (all parts are required). For example, 2022.4.0. It is important to set this if the blueprint uses any features introduced in recent releases to head off issues. 
input map (Optional) 
A dictionary of defined user inputs or sections. These are the input fields that the consumer of your blueprint can provide using YAML definition, or via a configuration form in the UI. Sections provide a way to visually group a set of related inputs (see below). 
### Blueprint inputs 
A blueprint can accept one or multiple inputs from the user, but does not require any input.
These inputs can be of any type (string, boolean, list, map). They can have a default value and also provide a that ensures a matching input field in the user interface.
A blueprint input has the following configuration:
####  Configuration Variables 
name string (Optional) 
The name of the input field. 
description string (Optional) 
A short description of the input field. Keep this short and descriptive. The description can include Markdown. 
selector selector (Optional) 
The selector to use for this input. A selector defines how the input is displayed in the frontend UI. 
default any (Optional) 
The default value of this input, in case the input is not provided by the user of this blueprint. 
Each input field can be referred to, outside of the blueprint metadata, using the !input custom YAML tag before its name.
The following example shows a minimal blueprint schema with a single input:
```
blueprint:
 name: Example blueprint
 description: Example showing an input
 domain: automation
 input:
  my_input:
   name: Example input
```

YAML
Copy
In the above example, my_input is the identifier of the input. It can be referenced by using the !input my_input custom tag.
In this example, no was provided. In the user interface, a text input field would be shown to the user. It is then up to the user to find out what to enter there. Blueprints that come with are easier to use.
A blueprint can have as many inputs as you like.
### Blueprint input sections 
One or more input sections can be added under the main input key. Each section visually groups the inputs in that section, allows an optional description, and optionally allows for collapsing those inputs. Note that the section only impacts how inputs are displayed to the user when they fill in the blueprint. Inputs must have unique names and be referenced directly by their name; not by section and name.
A section is differentiated from an input by the presence of an additional input key within that section.
Caution
Input sections are a new feature in version 2024.6.0. Set the min_version for the blueprint to at least this version if using input sections. Otherwise, the blueprint will generate errors on older versions. See for more details.
The full configuration for an input section is below:
####  Configuration Variables 
name string (Optional) 
A name for the section. If omitted the key of the section is used. 
icon string (Optional) 
An icon to display next to the name of the section. 
description string (Optional) 
An optional description of this section, which will be displayed at the top of the section. The description can include Markdown. 
collapsed boolean (Optional, default: false) 
If true, the section will be collapsed by default. Useful for optional or less important inputs. All collapsed inputs must also have a defined default before they can be hidden. 
input map Required 
A dictionary of defined user inputs within this section. 
The following example shows a blueprint schema with some inputs in a section:
```
blueprint:
 name: Example sections blueprint
 description: Example showing a section
 input:
  base_input:
   name: An input not in the section
  my_section:
   name: My Section
   icon: mdi:cog
   description: These options control a specific feature of this blueprint
   input:
    my_input:
     name: Example input
    my_input_2:
     name: 2nd example input
```

YAML
Copy
### Blueprint inputs in templates 
The inputs are available as custom YAML tags, but not as template variables. To use a blueprint input in a template, it first needs to be exposed as either a or in a .
```
variables:
 # Make input my_input available as a script level variable
 my_input: !input my_input
```

YAML
Copy
### Example blueprints 
The are great examples to get a bit of a feeling of how blueprints work.
Here is the built-in motion light automation blueprint. Note the blueprint schema under the blueprint key is followed by its domain schema. In this example, an automation schema.
```
blueprint:
 name: Motion-activated Light
 description: Turn on a light when motion is detected.
 domain: automation
 input:
  motion_entity:
   name: Motion Sensor
   selector:
    entity:
     filter:
      device_class: motion
      domain: binary_sensor
  light_target:
   name: Light
   selector:
    target:
     entity:
      domain: light
  no_motion_wait:
   name: Wait time
   description: Time to leave the light on after last motion is detected.
   default: 120
   selector:
    number:
     min: 0
     max: 3600
     unit_of_measurement: seconds
# If motion is detected within the delay,
# we restart the script.
mode: restart
max_exceeded: silent
triggers:
 - trigger: state
  entity_id: !input motion_entity
  from: "off"
  to: "on"
actions:
 - action: light.turn_on
  target: !input light_target
 - wait_for_trigger:
   - trigger: state
    entity_id: !input motion_entity
    from: "on"
    to: "off"
 - delay: !input no_motion_wait
 - action: light.turn_off
  target: !input light_target
```

YAML
Copy
## Related topics 
## Related links 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Events - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/events/

#  On this page
The core of Home Assistant is the event bus. The event bus allows any integration to fire or listen for events.
## Events and state changes 
All entitiesAn entity represents a sensor, actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a device or a service. [Learn more] produce state change events. Every time a stateThe state holds the information of interest of an entity, for example, if a light is on or off. Each entity has exactly one state and the state only holds one value at a time. However, entities can store attributes related to that state such as brightness, color, or a unit of measurement. [Learn more] changes, a state change event is produced. State change events are just one type of event on the event bus, but there are other kinds of events, such as the that are used to coordinate between various integrations.
### State change events versus event entity 
State change events are not to be confused with the . The event entity is a specific type of entity that itself produces event state changes, just like all other entities.
Any state change will be announced on the event bus as a state_changed event, containing the previous and the new state of an entity.
## Common fields 
All events share these basic fields.
Field | Description  
---|---  
event_type | Type of the event. Example: call_service.  
origin | Origin of the event. REMOTE (coming in from the API, e.g. a webhook) or LOCAL (everything else).  
time_fired | When the event was fired. Example: 2022-01-28T12:19:53.736380+00:00.  
context | Dictionary with the . Example: { 'id': '123', "parent_id": null, 'user_id': 'abc'}.  
In addition, all events contain a data dictionary with event-specific information. These are described below.
## Built-in Events (core) 
### call_service 
This event is fired when an service action is performed
Field | Description  
---|---  
domain | Domain of the action. Example: light.  
service | The service action that is performed. Example: turn_on   
service_data | Dictionary with the call parameters. Example: { 'brightness': 120 }.  
service_call_id | String with a unique call id. Example: 23123-4.  
### component_loaded 
This event is fired when a new integration has been loaded and initialized.
Please note that while this event is fired for each loaded integration during Home Assistant startup, the automation engine of Home Assistant is started last. Thus this event can not be used to run automations during startup as it would have missed these events.
Field | Description  
---|---  
component | Domain of the integration that has just been initialized. Example: light.  
### core_config_updated 
This event is fired when the core configuration is updated, for example when the location has been changed.
It contains no additional data.
### data_entry_flow_progressed 
This event is fired when a data entry flow has changed and is used by the frontend to reload the flow state.
Field | Description  
---|---  
handler | The flow handler.  
flow_id | Identification of the flow.  
### homeassistant_start, homeassistant_started 
These events are fired during the startup of Home Assistant, in the following order:
  1. homeassistant_start
  2. homeassistant_started


These events contain no additional data.
If you want to trigger automation on a Home Assistant start event, we recommend using the special instead of listening to these events.
### homeassistant_stop, homeassistant_final_write, homeassistant_close 
These events are fired during the shutdown of Home Assistant, in the following order:
  1. homeassistant_stop
  2. homeassistant_final_write
  3. homeassistant_close


These events contain no additional data.
Please note that homeassistant_final_write and homeassistant_close, cannot be used with automations, as the automation engine would already have been stopped when those are fired.
If you want to trigger automation on a Home Assistant stop event, we recommend using the special instead of listening to these events.
### logbook_entry 
Field | Description  
---|---  
name | Name of the entity. Example: Kitchen light.  
message | Message. Example: was turned on   
domain | Optional, domain of the entry. Example: light   
entity_id | Optional, identifier of the entity that was logged.  
### service_registered 
This event is fired when a new service action has been registered within Home Assistant.
Field | Description  
---|---  
domain | The domain of the integration that offers this action. Example: light.  
service | The name of the service action. Example: turn_on   
### service_removed 
This event is fired when a service action has been removed from Home Assistant.
Field | Description  
---|---  
domain | The domain of the integration that offers this action. Example: light.  
service | The name of the service action. Example: turn_on   
### state_changed 
This event is fired when a state has changed. It contains the entity identifier and both the new_state and old_state of the entity as .
Field | Description  
---|---  
entity_id | Identifier of the entity that has changed. Example: light.kitchen   
old_state | The previous state of the entity before it changed. Omitted if the state is set for the first time.  
new_state | The new state of the entity. Omitted if the state has been removed.  
### themes_updated 
This event is fired after a theme has been set or reloaded. It contains no additional data.
### user_added 
This event is fired when a user has been added.
Field | Description  
---|---  
user_id | Identification of the new user.  
### user_removed 
This event is fired when a user has been removed.
Field | Description  
---|---  
user_id | Identification of the removed user.  
## Built-in events (default integrations) 
### automation_reloaded 
Integration: 
This event is fired when automations have been reloaded and thus might have changed.
This event contains no additional data.
### automation_triggered 
Integration: 
This event is fired when an automation is triggered.
Field | Description  
---|---  
name | The name of the automation.  
entity_id | The identifier of the automation.  
### scene_reloaded 
Integration: 
This event is fired when scenes have been reloaded and thus might have changed.
This event contains no additional data.
### script_started 
Integration: 
This event is fired when a script is run. A script can be invoked by a user or triggered by an automation. The resulting changes can be tracked because all related events will share the same context as this event.
Field | Description  
---|---  
name | Name of the script that was run.  
entity_id | Identifier of the script that was run.  
## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Entity integration platform options - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/platform_options/

#  On this page


Important
These options are being phased out and are only available for single platform integrations.
Some integrations or platforms (those that are based on the class) allow various extra options to be set.
## Entity namespace 
By setting an entity namespace, all entities will be prefixed with that namespace. That way, light.bathroom can become light.holiday_house_bathroom.
```
# Example configuration.yaml entry
light:
 - platform: your_lights
  entity_namespace: holiday_house
```

YAML
Copy
## Scan interval 
Platforms that require polling will be polled in an interval specified by the main integration. For example, a light will check every 30 seconds for a changed state. It is possible to overwrite this scanning interval for any platform that is being polled by specifying a scan_interval configuration key. In the example below, we set up the your_lights platform but tell Home Assistant to poll the devices every 10 seconds instead of the default 30 seconds.
```
# Example configuration.yaml entry to poll your_lights every 10 seconds.
light:
 - platform: your_lights
  scan_interval: 10
```

YAML
Copy
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Packages - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/packages/

#  On this page


Packages in Home Assistant provide a way to bundle configurations from multiple integrations. With packages, we have a way to include multiple integrations, or parts of integrations using any of the !include directives introduced in .
Packages are configured under the core homeassistant/packages in the configuration and take the format of a package name (no spaces, all lower case) followed by a dictionary with the package configuration. For example, package pack_1 would be created as:
```
homeassistant:
 ...
 packages:
  pack_1:
   ...package configuration here...
```

YAML
Copy
The package configuration can include: switch, light, automation, groups, or most other Home Assistant integrations including hardware platforms.
It can be specified inline or in a separate YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] file using !include.
Inline example, main configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more]:
```
homeassistant:
 ...
 packages:
  pack_1:
   switch:
    - platform: rest
     ...
   light:
    - platform: rpi
     ...
```

YAML
Copy
Include example, main configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more]:
```
homeassistant:
 ...
 packages:
  pack_1: !include my_package.yaml
```

YAML
Copy
The file my_package.yaml contains the “top-level” configuration:
```
switch:
 - platform: rest
  ...
light:
 - platform: rpi
  ...
```

YAML
Copy
There are some rules for packages that will be merged:
  1. Platform based integrations (light, switch, etc) can always be merged.
  2. Integrations where entities are identified by a key that will represent the entity_id ({key: config}) need to have unique ‘keys’ between packages and the main configuration file.
For example if we have the following in the main configuration. You are not allowed to re-use “my_input” again for input_boolean in a package:
```
input_boolean:
 my_input:
```

YAML
Copy
  3. Any integration that is not a platform [1], or dictionaries with Entity ID keys [2] can only be merged if its keys, except those for lists, are solely defined once.


Tip
Integrations inside packages can only specify platform entries using configuration style 1, where all the platforms are grouped under the integration name.
## Create a packages folder 
One way to organize packages is to create a folder named “packages” in your Home Assistant configuration directory. In the packages directory, you can store any number of packages in a YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] file. This entry in your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] will load all YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more]-files in this packages folder and its subfolders:
```
homeassistant:
 packages: !include_dir_named packages
```

YAML
Copy
The benefit of this approach is to pull all configurations required to integrate a system into one file—rather than keeping them spread across several files. You can use other !include methods for packages; for example !include_dir_merge_named. However, unlike !include_dir_merge_named, the !include_dir_named method uses the same indentation as the ‘configuration.yaml’. This means that you can copy and paste elements from the config file. With !include_dir_named, the file name is used as the package name. File names must be unique.
With the !include_dir_merge_named method, the package name has to be included in the file. The configuration below then needs to be indented accordingly. This means you cannot directly copy and paste from the configuration file.
```
homeassistant:
 packages: !include_dir_merge_named packages/
```

YAML
Copy
and in packages/subsystem1/functionality1.yaml:
```
subsystem1_functionality1:
 input_boolean:
 ...
 binary_sensor:
 ...
 automation:
```

YAML
Copy
## Customizing entities with packages 
It is possible to within packages. Just create your customization entries under:
```
homeassistant:
 customize:
```

YAML
Copy
Important
If you are moving configuration to packages, auth_providers must stay within ‘configuration.yaml’. See the general documentation for .
This is because Home Assistant processes the authentication provided early in the start-up process, even before packages are processed.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Remote access - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/remote/

#  On this page
If you’re interested in logging in to Home Assistant while away, you’ll have to make your instance remotely accessible. Below are a few options to do this.
Tip
Remember to follow the before doing this.
## Home Assistant Cloud 
Users of can use the feature without requiring any configuration.
A unique remote URL will be generated and given to you along with a certificate so all your traffic to Home Assistant is encrypted automatically.
## VPN 
A secure way to remotely access your Home Assistant is to use a Virtual Private Network (VPN) service such as or .
A VPN connection needs to be established before you can connect to your Home Assistant from outside your local network. The VPN makes this connection secure. When using the Home Assistant Companion app (such as on a mobile device), without this connection, your sensors will not update in Home Assistant.
## Port forwarding 
Set up port forwarding (for any port) from your router to port 8123 on the computer that is hosting Home Assistant. General instructions on how to do this can be found by searching <router model> port forwarding instructions. You can use any free port on your router and forward that to port 8123.
A problem with making a port accessible is that some Internet Service Providers only offer dynamic IPs. This can cause you to lose access to Home Assistant while away. You can solve this by using a free Dynamic DNS service like .
If you cannot access your Home Assistant installation remotely, remember to check if your ISP provides you with a dedicated IP, instead of one shared with other users via a . This is becoming fairly common nowadays due to the shortage of IPv4 addresses. Some, if not most ISPs will require you to pay an extra fee to be assigned a dedicated IPv4 address.
Caution
Just putting a port up is not secure. You should definitely consider encrypting your traffic if you are accessing your Home Assistant installation remotely. For details, please check the blog post or this to using Let’s Encrypt with Home Assistant.
## Adding a remote URL to Home Assistant 
To set the URL under which your Home Assistant can be accessed from outside your local network, follow these steps:
  1. In the bottom left, select your username to go to your , and make sure Advanced mode is enabled.
  2. Go to .
  3. Under Home Assistant URL, enter the external URL that you previously set up for your instance.


## Related topics 


## Related links 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Storing secrets - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/secrets/

#  On this page


The configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file is a plain-text file, thus it is readable by anyone who has access to the file. The file contains passwords and API tokens which need to be redacted if you want to share your configuration.
By using !secret you can remove any private information from your configuration files. This separation can also help you to keep easier track of your passwords and API keys, as they are all stored at one place and no longer spread across the configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file or even multiple YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] files if you .
## Using secrets.yaml 
The workflow for moving private information to secrets.yaml is very similar to the . Create a secrets.yaml file in your Home Assistant .
The entries for password and API keys in the configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file usually looks like the example below.
```
rest:
 - authentication: basic
  username: "admin"
  password: "YOUR_PASSWORD"
  ...
```

YAML
Copy
Those entries need to be replaced with !secret and an identifier.
```
rest:
 - authentication: basic
  username: "admin"
  password: !secret rest_password
  ...
```

YAML
Copy
The secrets.yaml file contains the corresponding password assigned to the identifier.
```
rest_password: "YOUR_PASSWORD"
```

YAML
Copy
## Debugging secrets 
When you start splitting your configuration into multiple files, you might end up with configuration in sub folders. Secrets will be resolved in this order:
  * A secrets.yaml located in the same folder as the YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] file referencing the secret,
  * next, parent folders will be searched for a secrets.yaml file with the secret, stopping at the folder with the main configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more].


To see where secrets are being loaded from, you can add an option to your secrets.yaml file.
Print where secrets are retrieved from to the Home Assistant log by adding the following to secrets.yaml:
```
logger: debug
```

YAML
Copy
This will not print the actual secret’s value to the log.
## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Securing - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/securing/

#  On this page
One major advantage of Home Assistant is that it is not dependent on cloud services. Even if you are only using Home Assistant on a local network, you should take steps to secure your instance.
## Checklist 
Here’s the summary of what you must do to secure your Home Assistant system:
  * Centralize sensitive data in (but do remember to back them up). 
    * Note: Storing secrets in secrets.yaml does not encrypt them.
  * Regularly keep the system up to date.


## Remote access 
If you want secure remote access, the easiest option is to use by which you also support the , which develops Home Assistant, ESPHome and much more.
Another option is to use TLS/SSL via the add-on integrating Let’s Encrypt.
To expose your instance to the internet, use a , or an . Make sure to expose the used port in your router.
### Extras for manual installations 
Besides the above, we advise that you consider the following to improve security:
## Related topics 


## Related links 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## State and state object - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/state_object/

#  On this page
Devices are represented in Home Assistant as entitiesAn entity represents a sensor, actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a device or a service. [Learn more]. The state of an entity (for example, if a light is on, at 50% brightness in orange) can be shown on the dashboard or be used in automations. This page looks at the concepts state, state object, and entity state attribute.
## State versus state object 
In Home Assistant, the state object is the current representation of the entityAn entity represents a sensor, actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a device or a service. [Learn more] with all its attributes at a given moment in time. This state is recorded as a state object. Entities constantly keep track of their state and write it into a state object, so that other entities/templates/frontend can access it. In the example—the light is on, at 50% brightness in orange—on is the actual state of the light. 50% brightness and the color are entity state attributes.
### About the state object 
The state object represents the state of an entity with its attributes at a specific point in time. All state objects will always have an entity id, a state, and timestamps when last updated, last changed, and last reported. The state prefix indicates that this information is part of the state object (which is related to the entity). For example, state.state is the state of the entity at a given time.
Field | Description  
---|---  
state.state | String representation of the current state of the entity. Example off.  
state.entity_id | Entity ID. Format: <domain>.<object_id>. Example: light.kitchen.  
state.domain | Domain of the entity. Example: light.  
state.object_id | Object ID of entity. Example: kitchen.  
state.name | Name of the entity. Based on friendly_name attribute with fall back to object ID. Example: Kitchen ceiling.  
state.last_changed | Time the state changed in the state machine in UTC time. This is not updated if only state attributes change. Example: 2013-09-17 07:32:51.715874+00:00.  
state.last_reported | Time the state was written to the state machine in UTC time. This timestamp is updated regardless of any changes to the state or state attributes. Example: 2013-09-17 07:32:51.715874+00:00.  
state.last_updated | Time the state or state attributes changed in the state machine in UTC time. This is not updated if neither state nor state attributes changed. Example: 2013-09-17 07:32:51.715874+00:00.  
state.attributes | A dictionary with extra attributes related to the current state.  
state.context | A dictionary with extra attributes related to the context of the state.  
### About the state 
The screenshot of the Developer Tools States page shows three lights in different states (the state.state): on, off, and unavailable. Each light comes with its own entity state attributes such as supported_color_modes, supported_features. These attributes have their own state: the state of the supported_color_modes attribute is color_temp and hs, the state of the supported_features attribute is 4.
Three lights with different states: `on`, `off`, or `unavailable`. 
The state.state is the heart of the . State holds the information of interest of an entity. For example, if a light is on or off, the current temperature, or the amount of energy used. The state object stores 3 timestamps related to the state: last_updated, last_changed, and last_reported. Each entity has exactly one state, and the state only holds one value at a time.
### About entity state attributes 
The state only holds one value at a time. However, entities can store related entity state attributes in the state object. For example, the state of a light is on, and the related attributes could be its current brightness and color values. can be used as triggers. The current state can be used in . The example below shows three lights with different entity state attributes.
Example showing three lights with different entity state attributes. 
Entities have some attributes that are not related to its state, such as friendly_name. A few attributes are available on all entities, such as friendly_name or icon. In addition to those, each integration has its own attributes to represent extra state data about the entity. For example, the light integration has attributes for the current brightness and color of the light. When an attribute is not available, Home Assistant will not write it to the state. Entity attributes are optional.
When using templates, attributes will be available by their name. For example state.attributes.assumed_state.
The table lists common state attributes that may be present, depending on the entity domain.
Attribute | Description  
---|---  
friendly_name | Name of the entity. Example: Kitchen Ceiling.  
icon | Icon to use for the entity in the frontend. Example: mdi:home.  
entity_picture | URL to a picture that should be used instead of showing the domain icon. Example: http://example.com/picture.jpg.  
assumed_state | Boolean if the current state is an assumption. Example: True.  
unit_of_measurement | The unit of measurement the state is expressed in. Used for grouping graphs or understanding the entity. Example: °C.  
attribution | The provider of the data. For example, “Data provided by rejseplanen.dk”, “Data provided by openSenseMap”  
device_class | The type of device that an entity represents. Used to display device specific information in the UI.  
supported_features | The features an entity supports. For covers, for example, it might list opening, closing, stopping, setting position. For media players, it might list play, pause, stop, and volume control   
When an attribute contains spaces, you can retrieve it like this: state_attr('sensor.livingroom', 'Battery numeric').
## Context 
Context is a property used in state objects and events. It ties eventsEvery time something happens in Home Assistant, an event is fired. There are different types of events, such as state change events, when an action was triggered, or the time changed. All entities produce state change events. Every time a state changes, a state change event is produced. Events can be used to trigger automations or scripts. For example, you can trigger an automation when a light is turned on, then a speaker turns on in that room. Events can also be used to trigger actions in the frontend. For example, you can trigger an action when a button is pressed. [Learn more] and statesThe state holds the information of interest of an entity, for example, if a light is on or off. Each entity has exactly one state and the state only holds one value at a time. However, entities can store attributes related to that state such as brightness, color, or a unit of measurement. [Learn more] together in Home Assistant. Whenever an automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] or user interaction causes a state to change, a new context is assigned in the state object. This context will be attached to all events and states that happen as a result of the change.
Field | Description  
---|---  
id | Unique identifier for the context.  
user_id | Unique identifier of the user that started the change. Will be None if the action was not started by a user (for example, started by an automation).  
parent_id | Unique identifier of the parent context that started the change, if available. For example, if an automation is triggered, the context of the trigger will be set as parent.  
## Examples 
  * Evaluate the state.last_changed of a switch entity:
```
{{ states.switch.my_switch.last_changed }}
```

Jinja
Copy
result type: string representing a datetime object e.g. 2025-11-11 12:56:10.244125+00:00


  * Evaluate the state.context.id of this switch:
```
{{ states.switch.my_switch.context.id }}
```

Jinja
Copy
result type: string representing an id code e.g. 01K9SF2R36KRV5N4PTC38S6KJ2F


  * Evaluate the state.context.user_id of this switch:
```
{{ states.switch.my_switch.context.user_id }}
```

Jinja
Copy
result type: string representing an user id code e.g. 01K9SF2R36KRV5N4PTC38SKS4LW6


## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Splitting up the configuration - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/splitting_configuration/

#  On this page
So you’ve been using Home Assistant for a while now and your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file brings people to tears because it has become so large. Or, you simply want to start off with the distributed approach. Here’s how to split the configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] into more manageable (read: human-readable) pieces.
## Example configuration files for inspiration 
First off, several community members have sanitized (read: without API keys/passwords) versions of their configurations available for viewing. You can see a .
As commenting code doesn’t always happen, please read on to learn in detail how configuration files can be structured.
## Analyzing the configuration files 
In this section, we are going use some example configuration files and look at their structure and format in more detail.
Now you might think that the configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] will be replaced during the splitting process. However, it will in fact remain, albeit in a much less cluttered form.
### The core configuration file 
In this lighter version, we will still need what could be called the core snippet:
```
homeassistant:
 # Name of the location where Home Assistant is running
 name: "My Home Assistant Instance"
 # Location required to calculate the time the sun rises and sets
 latitude: 37
 longitude: -121
 # 'metric' for Metric, 'us_customary' for US Customary
 unit_system: us_customary
 # Pick yours from here: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
 time_zone: "America/Los_Angeles"
 customize: !include customize.yaml
```

YAML
Copy
### Indentation, includes, comments, and modularization 
Note that each line after homeassistant: is indented two (2) spaces. Since the configuration files in Home Assistant are based on the YAML language, indentation and spacing are important. Also note that seemingly strange entry under customize:.
!include customize.yaml is the statement that tells Home Assistant to insert the parsed contents of customize.yaml at that point. The contents of the included file must be yaml data that is valid at the location it is included. This is how we are going to break a monolithic and hard to read file (when it gets big) into more manageable chunks.
Now before we start splitting out the different components, let’s look at the other integrations (in our example) that will stay in the base file:
```
history:
frontend:
logbook:
http:
 api_password: "ImNotTelling!"
ifttt:
 key: ["nope"]
mqtt:
 sensor:
  - name: "test sensor 1"
   state_topic: "test/some_topic1"
  - name: "test sensor 2"
   state_topic: "test/some_topic2"
```

YAML
Copy
As with the core snippet, indentation makes a difference:
#### Comments 
The # symbol (hash/pound) represents a “comment” as far as the commands are interpreted. Put another way, any line prefixed with a # will be ignored by the software. It is for humans only. Comments allow breaking up files for readability, as well as turning off features while leaving the entry intact.
#### Modularization and granularity 
While some of these integrations could technically be moved to a separate file, they are so small or “one off’s” where splitting them off is superfluous.
Now, lets assume that a blank file has been created in the Home Assistant configuration directory for each of the following:
```
automation.yaml
zone.yaml
sensor.yaml
switch.yaml
device_tracker.yaml
customize.yaml
```

Text
Copy
automation.yaml will hold all the automation integration details. zone.yaml will hold the zone integration details and so forth. These files can be called anything but giving them names that match their function will make things easier to keep track of.
Inside the base configuration file, add the following entries:
```
automation: !include automation.yaml
zone: !include zone.yaml
sensor: !include sensor.yaml
switch: !include switch.yaml
device_tracker: !include device_tracker.yaml
```

YAML
Copy
#### Include statements and packages to split files 
Nesting !include statements (having an !include within a file that is itself !included) will also work.
Some integrations support multiple top-level !include statements. This includes integrations defining an IoT domain. For example, light, switch, or sensor; as well as the automation, script, and template integrations, if you give a different label to each one.
Configuration for other integrations can instead be split up by using packages. To learn more about packages, see the page.
#### Top level keys 
Example of multiple top-level keys for the light platform.
```
light:
- platform: group
 name: "Bedside Lights"
 entities:
  - light.left_bedside_light
  - light.right_bedside_light
# define more light groups in a separate file
light groups: !include light-groups.yaml
# define some light switch mappings in a different file
light switches: !include light-switches.yaml
```

YAML
Copy
where light-groups.yaml might look like:
```
- platform: group
 name: "Outside Lights"
 entities:
  - light.porch_lights
  - light.patio_lights
```

YAML
Copy
with light-switches.yaml containing:
```
- platform: switch
 name: "Patio Lights"
 entity_id: switch.patio_lights
- platform: switch
 name: "Floor Lamp"
 entity_id: switch.floor_lamp_plug
```

YAML
Copy
Alright, so we’ve got the single integrations and the include statements in the base file, what goes in those extra files?
Let’s look at the device_tracker.yaml file from our example:
```
- platform: owntracks
- platform: nmap_tracker
 home_interval: 3
 hosts: 192.168.2.0/24
 track_new_devices: true
 interval_seconds: 40
 consider_home: 120
```

YAML
Copy
This small example illustrates how the “split” files work. In this case, we start with two (2) device tracker entries (owntracks and nmap). These files follow that is to say a fully left aligned leading entry (- platform: owntracks) followed by the parameter entries indented two (2) spaces.
This (large) sensor configuration gives us another example:
```
### sensor.yaml
### METEOBRIDGE #############################################
- platform: tcp
 name: "Outdoor Temp (Meteobridge)"
 host: 192.168.2.82
 timeout: 6
 payload: "Content-type: text/xml; charset=UTF-8\n\n"
 value_template: "{{value.split (' ')[2]}}"
 unit: C
- platform: tcp
 name: "Outdoor Humidity (Meteobridge)"
 host: 192.168.2.82
 port: 5556
 timeout: 6
 payload: "Content-type: text/xml; charset=UTF-8\n\n"
 value_template: "{{value.split (' ')[3]}}"
 unit: Percent
#### STEAM FRIENDS ##################################
- platform: steam_online
 api_key: ["not telling"]
 accounts:
  - 76561198012067051
#### TIME/DATE ##################################
- platform: time_date
 display_options:
  - "time"
  - "date"
- platform: worldclock
 time_zone: Etc/UTC
 name: "UTC"
- platform: worldclock
 time_zone: America/New_York
 name: "Ann Arbor"
```

YAML
Copy
You’ll notice that this example includes a secondary parameter section (under the steam section) as well as a better example of the way comments can be used to break down files into sections.
All of the above can be applied when splitting up files using packages. To learn more about packages, see the page.
That about wraps it up.
If you have issues, check the file indentations and check . If all else fails, head over to our and ask away.
## Debugging configuration files 
If you have many configuration files, Home Assistant provides a CLI that allows you to see how it interprets them. Each installation type has its own section in the common-tasks about this:


## Advanced usage 
We offer four advanced options to include whole directories at once. Please note that your files must have the .yaml file extension; .yml is not supported.
This will allow you to !include files with .yml extensions from within the .yaml files; without those .yml files being imported by the following commands themselves.
These work recursively. As an example using !include_dir_list automation, will include all 6 files shown below:
```
.
└── .homeassistant
  ├── automation
  │  ├── lights
  │  │  ├── turn_light_off_bedroom.yaml
  │  │  ├── turn_light_off_lounge.yaml
  │  │  ├── turn_light_on_bedroom.yaml
  │  │  └── turn_light_on_lounge.yaml
  │  ├── say_hello.yaml
  │  └── sensors
  │    └── react.yaml
  └── configuration.yaml (not included)
```

Bash
Copy
### Example: !include_dir_list 
configuration.yaml
```
automation:
 - alias: "Automation 1"
  triggers:
   - trigger: state
    entity_id: device_tracker.iphone
    to: "home"
  actions:
   - action: light.turn_on
    target:
     entity_id: light.entryway
 - alias: "Automation 2"
  triggers:
   - trigger: state
    entity_id: device_tracker.iphone
    from: "home"
  actions:
   - action: light.turn_off
    target:
     entity_id: light.entryway
```

YAML
Copy
can be turned into:
configuration.yaml
```
automation: !include_dir_list automation/presence/
```

YAML
Copy
automation/presence/automation1.yaml
```
alias: "Automation 1"
triggers:
 - trigger: state
  entity_id: device_tracker.iphone
  to: "home"
actions:
 - action: light.turn_on
  target:
   entity_id: light.entryway
```

YAML
Copy
automation/presence/automation2.yaml
```
alias: "Automation 2"
triggers:
 - trigger: state
  entity_id: device_tracker.iphone
  from: "home"
actions:
 - action: light.turn_off
  target:
   entity_id: light.entryway
```

YAML
Copy
It is important to note that each file must contain only one entry when using !include_dir_list.
### Example: !include_dir_named 
configuration.yaml
```
alexa:
 intents:
  LocateIntent:
   actions:
    action: notify.pushover
    data:
     message: "Your location has been queried via Alexa."
   speech:
    type: plaintext
    text: >
     {%- for state in states.device_tracker -%}
      {%- if state.name.lower() == User.lower() -%}
       {{ state.name }} is at {{ state.state }}
      {%- endif -%}
     {%- else -%}
      I am sorry. Pootie! I do not know where {{User}} is.
     {%- endfor -%}
  WhereAreWeIntent:
   speech:
    type: plaintext
    text: >
     {%- if is_state('device_tracker.iphone', 'home') -%}
      iPhone is home.
     {%- else -%}
      iPhone is not home.
     {% endif %}
```

YAML
Copy
can be turned into:
configuration.yaml
```
alexa:
 intents: !include_dir_named alexa/
```

YAML
Copy
alexa/LocateIntent.yaml
```
actions:
 action: notify.pushover
 data:
  message: "Your location has been queried via Alexa."
speech:
 type: plaintext
 text: >
  {%- for state in states.device_tracker -%}
   {%- if state.name.lower() == User.lower() -%}
    {{ state.name }} is at {{ state.state }}
   {%- endif -%}
  {%- else -%}
   I am sorry. Pootie! I do not know where {{User}} is.
  {%- endfor -%}
```

YAML
Copy
alexa/WhereAreWeIntent.yaml
```
speech:
 type: plaintext
 text: >
  {%- if is_state('device_tracker.iphone', 'home') -%}
   iPhone is home.
  {%- else -%}
   iPhone is not home.
  {% endif %}
```

YAML
Copy
### Example: !include_dir_merge_list 
configuration.yaml
```
automation:
 - alias: "Automation 1"
  triggers:
   - trigger: state
    entity_id: device_tracker.iphone
    to: "home"
  actions:
   - action: light.turn_on
    target:
     entity_id: light.entryway
 - alias: "Automation 2"
  triggers:
   - trigger: state
    entity_id: device_tracker.iphone
    from: "home"
  actions:
   - action: light.turn_off
    target:
     entity_id: light.entryway
```

YAML
Copy
can be turned into:
configuration.yaml
```
automation: !include_dir_merge_list automation/
```

YAML
Copy
automation/presence.yaml
```
- alias: "Automation 1"
 triggers:
  - trigger: state
   entity_id: device_tracker.iphone
   to: "home"
 actions:
  - action: light.turn_on
   target:
    entity_id: light.entryway
- alias: "Automation 2"
 triggers:
  - trigger: state
   entity_id: device_tracker.iphone
   from: "home"
 actions:
  - action: light.turn_off
   target:
    entity_id: light.entryway
```

YAML
Copy
It is important to note that when using !include_dir_merge_list, you must include a list in each file (each list item is denoted with a hyphen [-]). Each file may contain one or more entries.
### Example: !include_dir_merge_named 
configuration.yaml
```
group:
 bedroom:
  name: "Bedroom"
  entities:
   - light.bedroom_lamp
   - light.bedroom_overhead
 hallway:
  name: "Hallway"
  entities:
   - light.hallway
   - thermostat.home
 front_yard:
  name: "Front Yard"
  entities:
   - light.front_porch
   - light.security
   - light.pathway
   - sensor.mailbox
   - camera.front_porch
```

YAML
Copy
can be turned into:
configuration.yaml
```
group: !include_dir_merge_named group/
```

YAML
Copy
group/interior.yaml
```
bedroom:
 name: "Bedroom"
 entities:
  - light.bedroom_lamp
  - light.bedroom_overhead
hallway:
 name: Hallway
 entities:
  - light.hallway
  - thermostat.home
```

YAML
Copy
group/exterior.yaml
```
front_yard:
 name: "Front Yard"
 entities:
  - light.front_porch
  - light.security
  - light.pathway
  - sensor.mailbox
  - camera.front_porch
```

YAML
Copy
### Example: Combine !include_dir_merge_list with automations.yaml 
You want to go the advanced route and split your automations, but still want to be able to create ? In a chapter above we write about nesting !includes. Here is how we can do that for automations.
Using labels like manual or ui allows for using multiple keys in the config:
configuration.yaml
```
# My own handmade automations
automation manual: !include_dir_merge_list automations/
# Automations I create in the UI
automation ui: !include automations.yaml
```

YAML
Copy
## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Templating - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/templating/

#  On this page
This is an advanced feature of Home Assistant. You’ll need a basic understanding of:
  * , especially states.
  * The .


Templating is a powerful feature that allows you to control information going into and out of the system. It is used for:
  * Formatting outgoing messages in, for example, the platforms and integration.
  * Process incoming data from sources that provide raw data, like , or the .
  * .


## Building templates 
Templating in Home Assistant is powered by the templating engine. This means that we are using their syntax and make some custom Home Assistant variables available to templates during rendering. Jinja2 supports a wide variety of operations:
We will not go over the basics of the syntax, as Jinja2 does a great job of this in their .
The frontend has a to help develop and debug templates. Navigate to , create your template in the Template editor and check the results on the right.
Templates can get big pretty fast. To keep a clear overview, consider using YAML multiline strings to define your templates:
```
script:
 msg_who_is_home:
  sequence:
   - action: notify.notify
    data:
     message: >
      {% if is_state('device_tracker.paulus', 'home') %}
       Ha, Paulus is home!
      {% else %}
       Paulus is at {{ states('device_tracker.paulus') }}.
      {% endif %}
```

YAML
Copy
### Important template rules 
There are a few very important rules to remember when adding templates to YAML:
  1. You must surround single-line templates with double quotes (") or single quotes (').
  2. It is advised that you prepare for undefined variables by using if ... is not none or the , or both.
  3. It is advised that when comparing numbers, you convert the number(s) to a or an by using the respective .
  4. While the and filters do allow a default fallback value if the conversion is unsuccessful, they do not provide the ability to catch undefined variables.


Remembering these simple rules will help save you from many headaches and endless hours of frustration when using automation templates.
### Enabled Jinja extensions 
Jinja supports a set of language extensions that add new functionality to the language. To improve the experience of writing Jinja templates, we have enabled the following extensions:
  * (break and continue)
  * (do)


### Reusing templates 
You can write reusable Jinja templates by adding them to a custom_templates folder under your configuration directory. All template files must have the .jinja extension and be less than 5MiB. Templates in this folder will be loaded at startup. To reload the templates without restarting Home Assistant, invoke the action.
Once the templates are loaded, Jinja and will work using config/custom_templates as the base directory.
For example, you might define a macro in a template in config/custom_templates/formatter.jinja:
```
{% macro format_entity(entity_id) %}
{{ state_attr(entity_id, 'friendly_name') }} - {{ states(entity_id) }}
{% endmacro %}
```

Jinja
Copy
In your automations, you could then reuse this macro by importing it:
```
{% from 'formatter.jinja' import format_entity %}
{{ format_entity('sensor.temperature') }}
```

Jinja
Copy
Home Assistant also allows you to write macros with non-string return values by taking a named argument called returns and calling it with a return value. Once created, pass the macro into the as_function filter to use the returned value:
```
{%- macro macro_is_switch(entity_name, returns) -%}
 {%- do returns(entity_name.startswith('switch.')) -%}
{%- endmacro -%}
{%- set is_switch = macro_is_switch | as_function -%}
{{ "It's a switch!" if is_switch("switch.my_switch") else "Not a switch!" }}
```

Jinja
Copy
In this way, you can export utility functions that return scalar or complex values rather than just macros that render to strings.
## Home Assistant template extensions 
Extensions allow templates to access all of the Home Assistant specific states and adds other convenience functions and filters.
### Limited templates 
Templates for some as well as trigger_variables only support a subset of the Home Assistant template extensions. This subset is referred to as “Limited Templates”.
### This 
State-based and trigger-based template entities have the special template variable this available in their templates and actions. See more details and examples in the .
### States 
Not supported in .
Warning
Avoid using states.sensor.temperature.state, instead use states('sensor.temperature'). It is strongly advised to use the states(), is_state(), state_attr() and is_state_attr() as much as possible, to avoid errors and error message when the entity isn’t ready yet (e.g., during Home Assistant startup).
#### States examples 
The next two statements result in the same value if the state exists. The second one will result in an error if the state does not exist.
```
{{ states('device_tracker.paulus') }}
{{ states.device_tracker.paulus.state }}
```

Text
Copy
Print out a list of all the sensor states:
```
{% for state in states.sensor %}
 {{ state.entity_id }}={{ state.state }},
{% endfor %}
```

Text
Copy
Print out a list of all the sensor states sorted by entity_id:
```
{% for state in states.sensor | sort(attribute='entity_id') %}
 {{ state.entity_id }}={{ state.state }},
{% endfor %}
```

Text
Copy
Entities that are on:
```
{{ ['light.kitchen', 'light.dining_room'] | select('is_state', 'on') | list }}
```

Text
Copy
Other state examples:
```
{% if is_state('device_tracker.paulus', 'home') %}
 Ha, Paulus is home!
{% else %}
 Paulus is at {{ states('device_tracker.paulus') }}.
{% endif %}
#check sensor.train_departure_time state
{% if states('sensor.train_departure_time') in ("unavailable", "unknown") %}
 {{ ... }}
{% if has_value('sensor.train_departure_time') %}
 {{ ... }}

{% set state = states('sensor.temperature') %}{{ state | float + 1 if is_number(state) else "invalid temperature" }}
{% set state = states('sensor.temperature') %}{{ (state | float * 10) | round(2) if is_number(state)}}
{% set state = states('sensor.temperature') %}
{% if is_number(state) and state | float > 20 %}
 It is warm!
{% endif %}
{{ as_timestamp(states.binary_sensor.garage_door.last_changed) }}
{{ as_local(states.binary_sensor.garage_door.last_changed) }}
{{ as_timestamp(now()) - as_timestamp(states.binary_sensor.garage_door.last_changed) }}
{{ as_local(states.sensor.time.last_changed) }}
{{ states('sensor.expires') | as_datetime }}
# Make a list of states
{{ ['light.kitchen', 'light.dining_room'] | map('states') | list }}
```

Text
Copy
#### Formatting sensor states 
The examples below show the output of a temperature sensor with state 20.001, unit °C and user configured presentation rounding set to 1 decimal.
The following example results in the number 20.001:
```
{{ states('sensor.temperature') }}
```

Text
Copy
The following example results in the string "20.0 °C":
```
{{ states('sensor.temperature', with_unit=True) }}
```

Text
Copy
The following example result in the string "20.001 °C":
```
{{ states('sensor.temperature', with_unit=True, rounded=False) }}
```

Text
Copy
The following example results in the number 20.0:
```
{{ states('sensor.temperature', rounded=True) }}
```

Text
Copy
The following example results in the number 20.001:
```
{{ states.sensor.temperature.state }}
```

Text
Copy
The following example results in the string "20.0 °C":
```
{{ states.sensor.temperature.state_with_unit }}
```

Text
Copy
### Attributes 
Not supported in .
You can print an attribute with state_attr if state is defined.
#### Attributes examples 
```
{% if states.device_tracker.paulus %}
 {{ state_attr('device_tracker.paulus', 'battery') }}
{% else %}
 ??
{% endif %}
```

Text
Copy
With strings:
```
{% set tracker_name = "paulus"%}
{% if states("device_tracker." + tracker_name) != "unknown" %}
 {{ state_attr("device_tracker." + tracker_name, "battery")}}
{% else %}
 ??
{% endif %}
```

Text
Copy
List of friendly names:
```
{{ ['binary_sensor.garage_door', 'binary_sensor.front_door'] | map('state_attr', 'friendly_name') | list }}
```

Text
Copy
List of lights that are on with a brightness of 255:
```
{{ ['light.kitchen', 'light.dining_room'] | select('is_state', 'on') | select('is_state_attr', 'brightness', 255) | list }}
```

Text
Copy
### State translated 
Not supported in .
The state_translated function returns a translated state of an entity using a language that is currently configured in the .
#### State translated examples 
```
{{ states("sun.sun") }}       # below_horizon
{{ state_translated("sun.sun") }}  # Below horizon
{{ "sun.sun" | state_translated }} # Below horizon
```

Text
Copy
```
{{ states("binary_sensor.movement_backyard") }}       # on
{{ state_translated("binary_sensor.movement_backyard") }}  # Detected
{{ "binary_sensor.movement_backyard" | state_translated }} # Detected
```

Text
Copy
### Working with groups 
Not supported in .
The expand function and filter can be used to sort entities and expand groups. It outputs a sorted array of entities with no duplicates.
#### Expand examples 
```
{% for tracker in expand('device_tracker.paulus', 'group.child_trackers') %}
 {{ state_attr(tracker.entity_id, 'battery') }}
 {%- if not loop.last %}, {% endif -%}
{% endfor %}
```

Text
Copy
The same thing can also be expressed as a filter:
```
{{ expand(['device_tracker.paulus', 'group.child_trackers'])
 | selectattr("attributes.battery", 'defined')
 | join(', ', attribute="attributes.battery") }}
```

Text
Copy
```
{% for energy in expand('group.energy_sensors') if is_number(energy.state) %}
 {{ energy.state }}
 {%- if not loop.last %}, {% endif -%}
{% endfor %}
```

Text
Copy
The same thing can also be expressed as a test:
```
{{ expand('group.energy_sensors')
 | selectattr("state", 'is_number') | join(', ') }}
```

Text
Copy
### Entities 
  * is_hidden_entity(entity_id) returns whether an entity has been hidden. Can also be used as a test.


### Entities examples 
```
{{ area_entities('kitchen') | reject('is_hidden_entity') }} # Gets a list of visible entities in the kitchen area
```

Text
Copy
### Devices 
#### Devices examples 
```
{{ device_attr('deadbeefdeadbeefdeadbeefdeadbeef', 'manufacturer') }} # Sony
```

Text
Copy
```
{{ is_device_attr('deadbeefdeadbeefdeadbeefdeadbeef', 'manufacturer', 'Sony') }} # true
```

Text
Copy
```
{{ device_id('sensor.sony') }} # deadbeefdeadbeefdeadbeefdeadbeef
```

Text
Copy
```
{{ device_name('deadbeefdeadbeefdeadbeefdeadbeef') }} # Sony speaker
{{ device_name('sensor.sony') }} # Sony speaker
```

Text
Copy
### Config entries 
  * config_entry_id(entity_id) returns the config entry ID for a given entity ID. Can also be used as a filter.
  * config_entry_attr(config_entry_id, attr) returns the value of attr for the config entry of the given entity ID. Can also be used as a filter. The following attributes are allowed: domain, title, state, source, disabled_by. Not supported in .


#### Config entries examples 
```
{{ config_entry_id('sensor.sony') }} # deadbeefdeadbeefdeadbeefdeadbeef
```

Text
Copy
```
{{ config_entry_attr(config_entry_id('sensor.sony'), 'title') }} # Sony Bravia TV
```

Text
Copy
### Floors 
#### Floors examples 
```
{{ floors() }} # ['floor_id']
```

Text
Copy
```
{{ floor_id('First floor') }} # 'first_floor'
```

Text
Copy
```
{{ floor_id('First floor alias') }} # 'first_floor'
```

Text
Copy
```
{{ floor_id('my_device_id') }} # 'second_floor'
```

Text
Copy
```
{{ floor_id('sensor.sony') }} # 'first_floor'
```

Text
Copy
```
{{ floor_name('first_floor') }} # 'First floor'
```

Text
Copy
```
{{ floor_name('my_device_id') }} # 'Second floor'
```

Text
Copy
```
{{ floor_name('sensor.sony') }} # 'First floor'
```

Text
Copy
```
{{ floor_areas('first_floor') }} # ['living_room', 'kitchen']
```

Text
Copy
### Areas 
#### Areas examples 
```
{{ areas() }} # ['area_id']
```

Text
Copy
```
{{ area_id('Living Room') }} # 'deadbeefdeadbeefdeadbeefdeadbeef'
```

Text
Copy
```
{{ area_id('Living Room Alias') }} # 'deadbeefdeadbeefdeadbeefdeadbeef'
```

Text
Copy
```
{{ area_id('my_device_id') }} # 'deadbeefdeadbeefdeadbeefdeadbeef'
```

Text
Copy
```
{{ area_id('sensor.sony') }} # 'deadbeefdeadbeefdeadbeefdeadbeef'
```

Text
Copy
```
{{ area_name('deadbeefdeadbeefdeadbeefdeadbeef') }} # 'Living Room'
```

Text
Copy
```
{{ area_name('my_device_id') }} # 'Living Room'
```

Text
Copy
```
{{ area_name('sensor.sony') }} # 'Living Room'
```

Text
Copy
```
{{ area_entities('deadbeefdeadbeefdeadbeefdeadbeef') }} # ['sensor.sony']
```

Text
Copy
```
{{ area_devices('Living Room') }} # ['my_device_id']
```

Text
Copy
### Entities for an integration 
  * integration_entities(integration) returns a list of entities that are associated with a given integration, such as hue or zwave_js.
  * integration_entities(config_entry_title) if you have multiple entries set-up for an integration, you can also use the title you’ve set for the integration in case you only want to target a specific entry.


If there is more than one entry with the same title, the entities for all the matching entries will be returned, even if the entries are for different integrations. It’s not possible to search for entities of an untitled integration.
#### Integrations examples 
```
{{ integration_entities('hue') }} # ['light.hue_light_upstairs', 'light.hue_light_downstairs']
```

Text
Copy
```
{{ integration_entities('Hue bridge downstairs') }} # ['light.hue_light_downstairs']
```

Text
Copy
### Labels 
Each of the label template functions can also be used as a filter.
#### Labels examples 
```
{{ labels() }} # ['christmas_decorations', 'energy_saver', 'security']
```

Text
Copy
```
{{ labels("living_room") }} # ['christmas_decorations', 'energy_saver']
```

Text
Copy
```
{{ labels("my_device_id") }} # ['security']
```

Text
Copy
```
{{ labels("light.christmas_tree") }} # ['christmas_decorations']
```

Text
Copy
```
{{ label_id('Energy saver') }} # 'energy_saver'
```

Text
Copy
```
{{ label_name('energy_saver') }} # 'Energy saver'
```

Text
Copy
```
{{ label_areas('security') }} # ['driveway', 'garden', 'porch']
```

Text
Copy
```
{{ label_devices('energy_saver') }} # ['deadbeefdeadbeefdeadbeefdeadbeef']
```

Text
Copy
```
{{ label_entities('security') }} # ['camera.driveway', 'binary_sensor.motion_garden', 'camera.porch']
```

Text
Copy
### Issues 
  * issues() returns all open issues as a mapping of (domain, issue_id) tuples to the issue object.
  * issue(domain, issue_id) returns a specific issue for the provided domain and issue_id.


#### Issues examples 
```
{{ issues() }} # { ("homeassistant", "deprecated_yaml_ping"): {...}, ("cloud", "legacy_subscription"): {...} }
```

Text
Copy
```
{{ issue('homeassistant', 'python_version') }} # {"breaks_in_ha_version": "2024.4", "domain": "homeassistant", "issue_id": "python_version", "is_persistent": False, ...}
```

Text
Copy
### Immediate if (iif) 
A common case is to conditionally return a value based on another value. For example, return a “Yes” or “No” when the light is on or off.
This can be written as:
```
{% if is_state('light.kitchen', 'on') %}
 Yes
{% else %}
 No
{% endif %}
```

Text
Copy
Or using a shorter syntax:
```
{{ 'Yes' if is_state('light.kitchen', 'on') else 'No' }}
```

Text
Copy
Additionally, to the above, you can use the iif function/filter, which is an immediate if.
Syntax: iif(condition, if_true, if_false, if_none)
iif returns the value of if_true if the condition is truthy, the value of if_false if it’s falsy and the value of if_none if it’s None. An empty string, an empty mapping or an an empty list, are all falsy, refer to for an in depth explanation.
if_true is optional, if it’s omitted True is returned if the condition is truthy. if_false is optional, if it’s omitted False is returned if the condition is falsy. if_none is optional, if it’s omitted the value of if_false is returned if the condition is None.
Examples using iif:
```
{{ iif(is_state('light.kitchen', 'on'), 'Yes', 'No') }}
{{ is_state('light.kitchen', 'on') | iif('Yes', 'No') }}
{{ (states('light.kitchen') == 'on') | iif('Yes', 'No') }}
```

Text
Copy
Warning
The immediate if filter does not short-circuit like you might expect with a typical conditional statement. The if_true, if_false and if_none expressions will all be evaluated and the filter will simply return one of the resulting values. This means you cannot use this filter to prevent executing an expression which would result in an error.
For example, if you wanted to select a field from trigger in an automation based on the platform you might go to make this template: trigger.platform == 'event' | iif(trigger.event.data.message, trigger.to_state.state). This won’t work because both expressions will be evaluated and one will fail since the field doesn’t exist. Instead you have to do this trigger.event.data.message if trigger.platform == 'event' else trigger.to_state.state. This form of the expression short-circuits so if the platform is event the expression trigger.to_state.state will never be evaluated and won’t cause an error.
### Time 
now(), time_since(), time_until(), today_at(), and utcnow() are not supported in .
Tip
is the number of seconds that have elapsed since 00:00:00 UTC on 1 January 1970. Therefore, if used as a function’s argument, it can be substituted with a numeric value (int or float).
Important
If your template is returning a timestamp that should be displayed in the frontend (e.g., as a sensor entity with device_class: timestamp), you have to ensure that it is the ISO 8601 format (meaning it has the “T” separator between the date and time portion). Otherwise, frontend rendering on macOS and iOS devices will show an error. The following value template would result in such an error:
{{ states.sun.sun.last_changed }} => 2023-07-30 20:03:49.253717+00:00 (missing “T” separator)
To fix it, enforce the ISO conversion via isoformat():
{{ states.sun.sun.last_changed.isoformat() }} => 2023-07-30T20:03:49.253717+00:00 (contains “T” separator)
```
{{ 120 | timestamp_local }}
```

Text
Copy
### To/From JSON 
The to_json filter serializes an object to a JSON string. In some cases, it may be necessary to format a JSON string for use with a webhook, as a parameter for command-line utilities or any number of other applications. This can be complicated in a template, especially when dealing with escaping special characters. Using the to_json filter, this is handled automatically.
to_json also accepts boolean arguments for pretty_print, which will pretty print the JSON with a 2-space indent to make it more human-readable, and sort_keys, which will sort the keys of the JSON object, ensuring that the resulting string is consistent for the same input.
If you need to generate JSON that will be used by a parser that lacks support for Unicode characters, you can add ensure_ascii=True to have to_json generate Unicode escape sequences in strings.
The from_json filter operates similarly, but in the other direction, de-serializing a JSON string back into an object.
### To/From JSON examples 
#### Template 
```
{% set temp = {'temperature': 25, 'unit': '°C'} %}
stringified object: {{ temp }}
object|to_json: {{ temp|to_json(sort_keys=True) }}
```

Text
Copy
#### Output 
```
stringified object: {'temperature': 25, 'unit': '°C'}
object|to_json: {"temperature": 25, "unit": "°C"}
```

Text
Copy
Conversely, from_json can be used to de-serialize a JSON string back into an object to make it possible to easily extract usable data.
#### Template 
```
{% set temp = '{"temperature": 25, "unit": "°C"}'|from_json %}
The temperature is {{ temp.temperature }}{{ temp.unit }}
```

Text
Copy
#### Output 
```
The temperature is 25°C
```

Text
Copy
from_json(default) function will attempt to convert the input to json. If that fails, returns the default value, or if omitted raises an error.
#### Template 
```
{% set result = 'not json'|from_json('not json') %}
The value is {{ result }}
```

Text
Copy
#### Output 
```
The value is not json
```

Text
Copy
### Is defined 
Sometimes a template should only return if a value or object is defined, if not, the supplied default value should be returned. This can be useful to validate a JSON payload. The is_defined filter allows to throw an error if a value or object is not defined.
Example using is_defined to parse a JSON payload:
```
{{ value_json.val | is_defined }}
```

Text
Copy
This will throw an error UndefinedError: 'value_json' is undefined if the JSON payload has no val attribute.
### Version 
  * version() Returns a for the value given inside the brackets. 
    * This is also available as a filter (| version).


Examples:
### Distance 
Not supported in .
  * distance() measures the distance between home, an entity, or coordinates. The unit of measurement (kilometers or miles) depends on the system’s configuration settings.
  * closest() will find the closest entity.


#### Distance examples 
If only one location is passed in, Home Assistant will measure the distance from home.
```
Using Lat Lng coordinates: {{ distance(123.45, 123.45) }}
Using State: {{ distance(states.device_tracker.paulus) }}
These can also be combined in any combination:
{{ distance(123.45, 123.45, 'device_tracker.paulus') }}
{{ distance('device_tracker.anne_therese', 'device_tracker.paulus') }}
```

Text
Copy
#### Closest examples 
The closest function and filter will find the closest entity to the Home Assistant location:
```
Query all entities: {{ closest(states) }}
Query all entities of a specific domain: {{ closest(states.device_tracker) }}
Query all entities in group.children: {{ closest('group.children') }}
Query all entities in group.children: {{ closest(states.group.children) }}
```

Text
Copy
Find entities closest to a coordinate or another entity. All previous arguments still apply for second argument.
```
Closest to a coordinate: {{ closest(23.456, 23.456, 'group.children') }}
Closest to an entity: {{ closest('zone.school', 'group.children') }}
Closest to an entity: {{ closest(states.zone.school, 'group.children') }}
```

Text
Copy
Since closest returns a state, we can combine it with distance too.
```
{{ closest(states).name }} is {{ distance(closest(states)) }} kilometers away.
```

Text
Copy
The last argument of the closest function has an implicit expand, and can take any iterable sequence of states or entity IDs, and will expand groups:
```
Closest out of given entities:
  {{ closest(['group.children', states.device_tracker]) }}
Closest to a coordinate:
  {{ closest(23.456, 23.456, ['group.children', states.device_tracker]) }}
Closest to some entity:
  {{ closest(states.zone.school, ['group.children', states.device_tracker]) }}
```

Text
Copy
It will also work as a filter over an iterable group of entities or groups:
```
Closest out of given entities:
  {{ ['group.children', states.device_tracker] | closest }}
Closest to a coordinate:
  {{ ['group.children', states.device_tracker] | closest(23.456, 23.456) }}
Closest to some entity:
  {{ ['group.children', states.device_tracker] | closest(states.zone.school) }}
```

Text
Copy
### Contains 
Jinja provides by default a how return True when one element is in a provided list. The contains test and filter allow you to do the exact opposite and test for a list containing an element. This is particularly useful in select or selectattr filter, as well as to check if a device has a specific attribute, a supported_color_modes, a specific light effect.
Some examples:
  * {{ state_attr('light.dining_room', 'effect_list') | contains('rainbow') }} will return true if the light has a rainbow effect.
  * {{ expand('light.office') | selectattr("attributes.supported_color_modes", 'contains', 'color_temp') | list }} will return all light that support color_temp in the office group.
  * ```
{% set current_month = now().month %}
{% set extra_ambiance = [
 {'name':'Halloween', 'month': [10,11]},
 {'name':'Noel', 'month': [1,11,12]}
]%}
{% set to_add = extra_ambiance | selectattr('month', 'contains', current_month ) | map(attribute='name') | list %}
{% set to_remove = extra_ambiance | map(attribute='name') | reject('in', to_add) | list %}
{{ (state_attr('input_select.light_theme', 'options') + to_add ) | unique | reject('in', to_remove) | list }}
```

Text
Copy
This more complex example uses the contains filter to match the current month with a list. In this case, it’s used to generate a list of light theme to give to the Input select: Set options action.


### Numeric functions and filters 
Some of these functions can also be used in a . This means they can act as a normal function like this sqrt(2), or as part of a filter like this 2|sqrt.
Note
The numeric functions and filters raise an error if the input is not a valid number, optionally a default value can be specified which will be returned instead. The is_number function and filter can be used to check if a value is a valid number. Errors can be caught by the default filter.
### Complex type checking 
In addition to strings and numbers, Python (and Jinja) supports lists, sets, and dictionaries. To help you with testing these types, you can use the following tests:
Note that, in Home Assistant, Jinja has built-in tests for boolean (True/False), callable (any function), float (a number with a decimal), integer (a number without a decimal), iterable (a value that can be iterated over such as a list, set, string, or generator), mapping (mainly dict but also supports other dictionary like types), number (float or int), sequence (a value that can be iterated over and indexed such as list and string), and string.
### Type conversions 
While Jinja natively supports the conversion of an iterable to a list, it does not support conversion to a tuple or set. To help you with using these types, you can use the following functions:
  * set(x) will convert any iterable x to a set (e.g. set([1, 2]) == {1, 2})
  * tuple(x) will convert any iterable x to a tuple (e.g. tuple("abc") == ("a", "b", "c"))


Note that, in Home Assistant, to convert a value to a list, a string, an int, or a float, Jinja has built-in functions with names that correspond to each type.
### Iterating multiple objects 
The zip() function can be used to iterate over multiple collections in one operation.
```
{% set names = ['Living Room', 'Dining Room'] %}
{% set entities = ['sensor.living_room_temperature', 'sensor.dining_room_temperature'] %}
{% for name, entity in zip(names, entities) %}
 The {{ name }} temperature is {{ states(entity) }}
{% endfor %}
```

Text
Copy
zip() can also unzip lists.
```
{% set information = [
 ('Living Room', 'sensor.living_room_temperature'),
 ('Dining Room', 'sensor.dining_room_temperature')
] %}
{% set names, entities = zip(*information) %}
The names are {{ names | join(', ') }}
The entities are {{ entities | join(', ') }}
```

Text
Copy
### Functions and filters to process raw data 
These functions are used to process raw value’s in a bytes format to values in a native Python type or vice-versa. The pack and unpack functions can also be used as a filter. They make use of the Python 3 struct library. See: 
Note
Some examples:
### String filters 
Some examples:
### Hashing 
The template engine contains a few filters and functions to hash a string of data. A few very common hashing algorithms are supported: md5, sha1, sha256, and sha512.
Some examples:
### Regular expressions 
For more information on regular expressions See: 
### Shuffling 
The template engine contains a filter and function to shuffle a list.
Shuffling can happen randomly or reproducibly using a seed. When using a seed it will always return the same shuffled list for the same seed.
Some examples:
### Flatten a list of lists 
The template engine provides a filter to flatten a list of lists: flatten.
It will take a list of lists and return a single list with all the elements. The depth of the flattening can be controlled using the levels parameter. The flattening process is recursive, so it will flatten all nested lists, until the number of levels (if specified) is reached.
Some examples:
### Find common elements between lists 
The template engine provides a filter to find common elements between two lists: intersect.
This function returns a list containing all elements that are present in both input lists.
Some examples:
### Find elements in first list not in second list 
The template engine provides a filter to find elements that are in the first list but not in the second list: difference. This function returns a list containing all elements that are present in the first list but absent from the second list.
Some examples:
### Find elements that are in either list but not in both 
The template engine provides a filter to find elements that are in either of the input lists but not in both: symmetric_difference. This function returns a list containing all elements that are present in either the first list or the second list, but not in both.
Some examples:
### Combine all unique elements from two lists 
The template engine provides a filter to combine all unique elements from two lists: union. This function returns a list containing all unique elements that are present in either the first list or the second list.
Some examples:
### Combining dictionaries 
The template engine provides a function and filter to merge multiple dictionaries: combine.
It will take multiple dictionaries and merge them into a single dictionary. When used as a filter, the filter value is used as the first dictionary. The optional recursive parameter determines whether nested dictionaries should be merged (defaults to False).
Some examples:
### Working with macros 
Home Assistant provides two additional functions that make macros much more powerful.
  * apply is both a filter and a test that allows you to use any callable (macros or functions) wherever you can use other filters and tests. apply also passes along any additional parameters to the function. For example, if you had a function called double, you could call {{ [1, 2, 3, 4] | map('apply', double) | list }}, which would render as [2, 4, 6, 8]. Alternatively, if you had a function called is_multiple_of, you could call {{ [1, 2, 3, 4] | select('apply', is_multiple_of, 2) | list }}, which would render as [2, 4].
  * as_function is a filter that takes a macro that has a named parameter called returns. The macro can then call {%- do returns(return_value) -%}. After passing this macro into as_function, the resulting function returns your return value directly, preserving the underlying data type rather than rendering a string. You can return dictionaries, numbers, True/False (allowing you to write your own tests when used with apply), or any other value your code might produce.


## Merge action responses 
Using action responses we can collect information from various entities at the same time. Using the merge_response template we can merge several responses into one list.
Variable | Description  
---|---  
value | The incoming value (must be an action response).  
The entity_id key is appended to each dictionary within the template output list as a reference of origin. If the input dictionary already contains an entity_id key, the template will fail.
The value_key key is appended to each dictionary within the template output list as a reference of origin if the original service call was providing a list of dictionaries, for example, calendar.get_events or weather.get_forecasts.
Examples of these two keys can be seen in template output.
### Example 
```
{% set combined_forecast = merge_response(response) %}
{{ combined_forecast[0].precipitation | float(0) | round(1) }}
```

YAML
Copy
### Example how to sort 
Sorting the dictionaries within the list based on a specific key can be done directly by using Jinja’s sort filter.
```
{{ merge_response(calendar_response) | sort(attribute='start') | ... }}
```

YAML
Copy
### Example merge calendar action response 
```
{
 "calendar.sports": {
  "events": [
   {
    "start": "2024-02-27T17:00:00-06:00",
    "end": "2024-02-27T18:00:00-06:00",
    "summary": "Basketball vs. Rockets",
    "description": "",
   }
  ]
 },
 "calendar.local_furry_events": {"events": []},
 "calendar.yap_house_schedules": {
  "events": [
   {
    "start": "2024-02-26T08:00:00-06:00",
    "end": "2024-02-26T09:00:00-06:00",
    "summary": "Dr. Appt",
    "description": "",
   },
   {
    "start": "2024-02-28T20:00:00-06:00",
    "end": "2024-02-28T21:00:00-06:00",
    "summary": "Bake a cake",
    "description": "something good",
   }
  ]
 },
}
```

JSON
Copy
```
{{ merge_response(response_variable) }}
```

YAML
Copy
```
[
 {
  "description": "",
  "end": "2024-02-27T18:00:00-06:00",
  "entity_id": "calendar.sports",
  "start": "2024-02-27T17:00:00-06:00",
  "summary": "Basketball vs. Rockets",
  "value_key": "events"
 },
 {
  "description": "",
  "end": "2024-02-26T09:00:00-06:00",
  "entity_id": "calendar.yap_house_schedules",
  "start": "2024-02-26T08:00:00-06:00",
  "summary": "Dr. Appt",
  "value_key": "events"
 },
 {
  "description": "something good",
  "end": "2024-02-28T21:00:00-06:00",
  "entity_id": "calendar.yap_house_schedules",
  "start": "2024-02-28T20:00:00-06:00",
  "summary": "Bake a cake",
  "value_key": "events"
 }
]
```

JSON
Copy
### Example non-list action responses 
```
{
 "vacuum.deebot_n8_plus_1": {
  "header": {
   "ver": "0.0.1",
  },
  "payloadType": "j",
  "resp": {
   "body": {
    "msg": "ok",
   },
  },
 },
 "vacuum.deebot_n8_plus_2": {
  "header": {
   "ver": "0.0.1",
  },
  "payloadType": "j",
  "resp": {
   "body": {
    "msg": "ok",
   },
  },
 },
}
```

JSON
Copy
```
{{ merge_response(response_variable) }}
```

YAML
Copy
```
[
 {
  "entity_id": "vacuum.deebot_n8_plus_1",
  "header": {
   "ver": "0.0.1",
  },
  "payloadType": "j",
  "resp": {
   "body": {
    "msg": "ok",
   },
  },
 },
 {
  "entity_id": "vacuum.deebot_n8_plus_2",
  "header": {
   "ver": "0.0.1",
  },
  "payloadType": "j",
  "resp": {
   "body": {
    "msg": "ok",
   },
  },
 },
]
```

JSON
Copy
## Processing incoming data 
The other part of templating is processing incoming data. It allows you to modify incoming data and extract only the data you care about. This will only work for platforms and integrations that mention support for this in their documentation.
It depends per integration or platform, but it is common to be able to define a template using the value_template configuration key. When a new value arrives, your template will be rendered while having access to the following values on top of the usual Home Assistant extensions:
Variable | Description  
---|---  
value | The incoming value.  
value_json | The incoming value parsed as JSON.  
This means that if the incoming values looks like the sample below:
```
{
 "on": "true",
 "temp": 21
}
```

JSON
Copy
The template for on would be:
```
"{{value_json.on}}"
```

YAML
Copy
Nested JSON in a response is supported as well:
```
{
 "sensor": {
  "type": "air",
  "id": "12345"
 },
 "values": {
  "temp": 26.09,
  "hum": 56.73
 }
}
```

JSON
Copy
Just use the “Square bracket notation” to get the value.
```
"{{ value_json['values']['temp'] }}"
```

YAML
Copy
The following overview contains a couple of options to get the needed values:
```
# Incoming value:
{"primes": [2, 3, 5, 7, 11, 13]}
# Extract first prime number
{{ value_json.primes[0] }}
# Format output
{{ "%+.1f" | value_json }}
# Math
{{ value_json | float * 1024 if is_number(value_json) }}
{{ float(value_json) * (2**10) if is_number(value_json) }}
{{ value_json | log if is_number(value_json) }}
{{ log(1000, 10) }}
{{ sin(pi / 2) }}
{{ cos(tau) }}
{{ tan(pi) }}
{{ sqrt(e) }}
# Timestamps
{{ value_json.tst | timestamp_local }}
{{ value_json.tst | timestamp_utc }}
{{ value_json.tst | timestamp_custom('%Y', True) }}
```

Text
Copy
To evaluate a response, go to Developer Tools > Template, create your output in “Template editor”, and check the result.
```
{% set value_json=
  {"name":"Outside",
   "device":"weather-ha",
   "data":
    {"temp":"24C",
     "hum":"35%"
     } }%}
{{value_json.data.hum[:-1]}}
```

YAML
Copy
### Using templates with the MQTT integration 
The relies heavily on templates. Templates are used to transform incoming payloads (value templates) to state updates or incoming actions (command templates) to payloads that configure the MQTT device.
#### Using value templates with MQTT 
Value templates translate received MQTT payload to a valid state or attribute. The received MQTT is available in the value template variable, and in the value_json template variable if the received MQTT payload is valid JSON.
In addition, the template variables entity_id, name and this are available for MQTT entity value templates. The this attribute refers to the of the MQTT item.
Note
Example value template:
With given payload:
```
{ "state": "ON", "temperature": 21.902, "humidity": null }
```

JSON
Copy
Template {{ value_json.temperature | round(1) }} renders to 21.9.
Template {{ value_json.humidity }} renders to None.
#### Using command templates with MQTT 
For actions, command templates are defined to format the outgoing MQTT payload to a format supported by the remote device. When an action is executed, the template variable value has the action data in most cases unless otherwise specified in the documentation.
In addition, the template variables entity_id, name and this are available for MQTT entity command templates. The this attribute refers to the of the MQTT item.
Note
Example command template with JSON data:
With given value 21.9 template {"temperature": {{ value }} } renders to:
```
{
 "temperature": 21.9
}
```

JSON
Copy
Example command template with raw data:
When a command template renders to a valid bytes literal, then MQTT will publish this data as raw data. In other cases, a string representation will be published. So:
  * Template {{ "16" }} renders to payload encoded string "16".
  * Template {{ 16 }} renders to payload encoded string "16".
  * Template {{ pack(0x10, ">B") }} renders to a raw 1 byte payload 0x10.


### Determining types 
When working with templates, it can be useful to determine the type of the returned value from a method or the type of a variable at times.
For this, Home Assistant provides the typeof() template function and filter, which is inspired by the typeof operator. It reveals the type of the given value.
This is mostly useful when you are debugging or playing with templates in the developer tools of Home Assistant. However, it might be useful in some other cases as well.
Some examples:
## Some more things to keep in mind 
### entity_id that begins with a number 
If your template uses an entity_id that begins with a number (example: states.device_tracker.2008_gmc) you must use a bracket syntax to avoid errors caused by rendering the entity_id improperly. In the example given, the correct syntax for the device tracker would be: states.device_tracker['2008_gmc']
### Priority of operators 
The default priority of operators is that the filter (|) has priority over everything except brackets. This means that:
```
{{ states('sensor.temperature') | float / 10 | round(2) }}
```

Text
Copy
Would round 10 to 2 decimal places, then divide states('sensor.temperature') by 10 (rounded to 2 decimal places so 10.00). This behavior is maybe not the one expected, but priority rules imply that.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Troubleshooting your configuration - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/troubleshooting/

#  On this page
It can happen that you run into trouble while configuring Home Assistant. Perhaps an integration is not showing up or is acting strangely. This page will discuss a few of the most common problems.
Before we dive into common issues, make sure you know where your configuration directory is. Home Assistant will print out the configuration directory it is using when starting up.
Whenever an integration or configuration option results in a warning, it will be stored in .
## My integration does not show up 
When an integration does not show up, many different things can be the case. Before you try any of these steps, make sure to look at the and see if there are any errors related to your integration you are trying to set up.
If you have incorrect entries in your configuration files you can use the configuration check command (below) to assist in identifying them.
### Problems with the configuration 
One of the most common problems with Home Assistant is an invalid configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] or other configuration file.
configuration.yaml does not allow multiple sections to have the same name. If you want to load multiple platforms for one integration, you can append a number or string to the name or nest them:
```
sensor:
 - platform: forecast
  ...
 - platform: bitcoin
  ...
```

YAML
Copy
Another common problem is that a required configuration setting is missing. If this is the case, the integration will report this in . You can have a look at for instructions on how to setup the integrations.
See the integration for instructions on how to define the level of logging you require for specific modules.
If you find any errors or want to expand the documentation, please .
#### Problems with dependencies 
Almost all integrations have external dependencies to communicate with your devices and services. Sometimes Home Assistant is unable to install the necessary dependencies. If this is the case, it should show up in .
The first step is trying to restart Home Assistant and see if the problem persists. If it does, look at the log to see what the error is. If you can’t figure it out, please so we can investigate what is going on.
#### Problems with integrations 
It can happen that some integrations either do not work right away or stop working after Home Assistant has been running for a while. If this happens to you, please so that we can have a look.
#### Multiple files 
If you are using multiple files for your setup, make sure that the pointers are correct and the format of the files is valid. It’s important to understand the different types of !include and how the contents of each file should be structured - more information on the various methods of splitting your configuration into multiple files can be found .
```
light: !include devices/lights.yaml
sensor: !include devices/sensors.yaml
```

YAML
Copy
Contents of lights.yaml (notice it does not contain light:):
```
- platform: hyperion
 host: 192.168.1.98
 ...
```

YAML
Copy
Contents of sensors.yaml:
```
- platform: mqtt
 name: "Room Humidity"
 state_topic: "room/humidity"
- platform: mqtt
 name: "Door Motion"
 state_topic: "door/motion"
 ...
```

YAML
Copy
Note
Whenever you report an issue, be aware that we are volunteers who do not have access to every single device in the world nor unlimited time to fix every problem out there.
### Entity names 
The only characters valid in entity names are:
  * Lowercase letters
  * Numbers
  * Underscores


The entity name must not start or end with an underscore. If you create an entity with other characters from the UI, Home Assistant validates the name. If you change the name directly in the YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] file, then Home Assistant may not generate an error for that entity. However, attempts to use that entity will generate errors (or possibly fail silently).
For instructions on how to change an entity name, refer to the section on .
## Debug logs and diagnostics 
The first thing you will need before reporting an issue online is debug logs and diagnostics (if available) for the integration giving you trouble. Getting those ahead of time will ensure someone can help resolve your issue in the fastest possible manner.
### Enabling debug logging 
To enable debug logging for a specific integration, follow these steps:
  1. Go to .
  2. Select the integration for which you want to enable debug logging.
  3. In the top right of the page, open the three dots menu, and select Enable debug logging.
Screenshot showing the Enable debug logging menu item. 
  4. To see the error in the logs, you need to reproduce the error. Continue with the steps on .


### Disable debug logging and download logs 
Once you enable debug logging, you ideally need to make the error happen. Run your automation, change up your device or whatever was giving you an error and then come back and disable the debug logging. Disabling the debug logging is the same as enabling, but now the menu option says Disable debug logging. After you disable it, you will be automatically prompted you to download your log file. Save this to a safe location to upload later.
### Download diagnostics 
After you download logs, you will also want to download the diagnostics for the integration giving you trouble. If the integration provides diagnostics, it will appear in the three dots menu next to the integration configuration.
Example of Download Diagnostics. 
### Handling unexpected restarts or crashes 
Suppose you find that Home Assistant unexpectedly restarts or crashes; it’s likely that you have a misbehaving integration impacting system stability. Home Assistant has a built-in debug option that can help find implementation errors. It can also block many unsafe thread operations from crashing the system. Enabling debug has a slight performance impact on the system and is not recommended for long-term use. To enable debug, add the following to your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more]:
```
homeassistant:
 debug: true
```

YAML
Copy
Once debug is enabled, periodically check for new messages.
## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Integrating your gas usage - Home Assistant

Source: https://www.home-assistant.io/docs/energy/gas/

#  On this page


Some homes are connected to gas. Gas is being used to heat water, cook and heat up the home.
Home Assistant allows you to track your gas usage and easily compare it against your energy usage for the same period of time.
## Hardware 
Home Assistant will need to know the amount of gas that is being consumed.
### Connect to your meter 
The best way to get this data is directly from your gas meter that sits between your house and the grid. In certain countries these meters contain standardized ways of reading out the information locally or provide this information via the electricity meter.
#### Connect using a P1 port 
The P1 port is a standardized port on electricity meters in the Netherlands, Belgium and Luxembourg which also provides gas consumption information. A P1 reader can connect to this port and receive real-time information.
We have worked with creator to develop . It’s an affordable P1 reader powered by that will seamlessly integrate this information in Home Assistant. It is being sold on and the firmware is open source .
#### Read the Gas Meter using an AI-on-the-edge-device 
is a project running on an ESP32-CAM and can be fully integrated into Home Assistant using the Home Assistant Discovery Functionality of MQTT. It digitalizes your gas/water/electricity meter display and provides its data in various ways.
#### Read the Gas Meter using a magnetometer 
are the most common type of gas meter, seen in almost all residential installations, and their movement can frequently be observed with a magnetometer. The and are common and inexpensive options that ESPHome supports. A project that makes it easy to use these magnetometers and calibrate them is .
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Integrating individual device energy usage - Home Assistant

Source: https://www.home-assistant.io/docs/energy/individual-devices/

#  On this page
Home Assistant can integrate the energy usage of individual devices into Home Assistant. That way you can see the impact of individual devices on your total energy consumption. In addition to energy usage, Home Assistant also supports tracking individual water device usage, allowing you to monitor water consumption of specific devices in your home.
## Hardware for energy monitoring 
### Smart plugs 
Smart plugs sit between the device and the outlet and measure the energy flowing through the device.
Depending on what protocols you use at home, you can use Zigbee, Z-Wave or Wi-Fi based plugs.
### Smart relays 
Smart relays sit behind your “normal” switches and make them smart. It allows you to control the devices via Home Assistant and via the connected buttons/switches.
## Hardware for water monitoring 
For tracking individual water devices, you can use:
  * Smart water meters with device-level monitoring capabilities.
  * Inline flow meters that measure water flowing to specific appliances.
  * Smart appliances (washing machines, dishwashers, etc.) that report their own water consumption.


For more information on water metering hardware and integrations, see the .
## Devices with power (W) sensors 
Some smart devices, such as air conditioning, boilers, and others, may provide a power sensor, measured in Watts. You can use the to calculate the energy your device is using. You can then use the energy sensor in the Energy Dashboard, as individual devices. You can add the power sensor directly if it has the appropriate attributes. For information on setting up an entity for use in the Energy dashboard, refer to the .
## Upstream devices and hierarchies 
You can create a hierarchy of devices by setting one device as an “upstream device” of another. This means you can now establish parent-child relationships between devices within your energy configuration. This works for both energy and water devices.
For example, imagine having a breaker monitoring the total energy consumption of a circuit, but also separately tracking individual devices connected to that circuit.
For water usage, you might have a main water line meter and individual meters for appliances like washing machines or dishwashers. Without setting the device hierarchies, Home Assistant might double-count this usage. By setting the hierarchy, it understands these relationships and accurately shows the individual device usage without duplication. To set up an upstream device relationship:
  1. Add an energy or water consumption entity as an individual device.
  2. Then, when configuring other individual devices, you can select the previously added individual entity as their upstream device.


This hierarchical view helps you understand which devices are consuming energy or water from which sources and prevents usage from being counted multiple times.
Important
To set up a hierarchy, you must first add all related entities as individual devices in the energy dashboard. Only devices that are already listed under individual devices can be selected as “upstream device” for other devices.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Integrating your electricity grid - Home Assistant

Source: https://www.home-assistant.io/docs/energy/electricity-grid/

#  On this page
Energy management is all about knowing how much energy you’re consuming, where it’s coming from and where it’s going.
Almost all houses are connected to the electricity grid which provides the energy your home will need. The energy usage is being tracked by your energy meter and is billed to you by your energy provider. Energy prices can differ based on a schedule or change according to market price.
## Tariffs 
It has become popular for energy utilities to split the price of energy based on time of the day; this is done in order to incentivise consumers to shift their power needs towards times where the grid has lower loads. These periods of time are commonly referred to as Peak and Off Peak, exactly because they match periods of time where everyone is consuming energy (Peak) and periods of time where the energy is abundant but no one is using it (Off Peak). Therefore Peak energy is more expensive then Off Peak energy.
If you want to split energy usage into multiple tariffs, .
## Hardware 
Home Assistant will need to know the amount of energy flowing through your meter. This data can be tracked in various ways.
### Connect to your meter 
The best way to get this data is directly from your electricity meter that sits between your house and the grid. In certain countries these meters contain standardized ways of reading out the information locally.
#### Connect using a P1 port 
The P1 port is a standardized port in the Netherlands, Belgium and Luxembourg. A P1 reader can connect to this port and receive real-time information.
We have worked with creator to develop . It’s an affordable P1 reader powered by that will seamlessly integrate this information in Home Assistant. It is being sold on and the firmware is open source .
#### Connect via Zigbee Energy Profile 
The Zigbee Energy Profile is a wireless energy standard to provide real-time information about electricity usage. This standard is available in some meters in the US, UK, Canada, and Australia. This is not “normal” Zigbee as implemented by Home Assistant but requires special certified hardware and often requires that the Zigbee connection be provisioned by your utility. As such, your utility, assuming they support this at all, will have a list of currently supported hardware.
The is one such device that implements this which supports a local API and is compatible with Home Assistant.
#### Reading the meter via a pulse counter 
Many meters, including older ones, have an LED that will flash whenever energy passes through it. For example, each flash is a 1/1000th kWh. By monitoring the time between flashes it’s possible to determine the energy consumption.
We have developed , an open source solution powered by ESPHome’s . You put it on top of the activity LED of your electricity meter and it will bring your consumption into Home Assistant.
#### Reading the meter via a IEC62056-21 
The IEC62056-21 is a common protocol not only for electric meters. It uses an infrared port to read data. has created an for reading this data. is a complete project that allows easy installation. 
#### Using (Smart Message Language) interface 
In countries like Germany, SML (Smart Message Language) is used typically. ESPHome’s is one way to integrate it. If you prefer to integrate it via MQTT, is another open source option.
#### Read the meter using an AI-on-the-edge-device 
is a project running on an ESP32-CAM and can be fully integrated into Home Assistant using the Home Assistant discovery functionality of MQTT. It digitalizes your gas/water/electricity meter display and provides its data in various ways.
### Using a CT clamp sensor 
Current transformer (CT) clamp sensors measure your energy usage by looking at the current passing through an electrical wire. This makes it possible to calculate the energy usage. In Home Assistant we have support for off-the-shelf CT clamp sensors or you can build your own.
  * The off-the-shelf solution that we advise is the . The device has a local API, updates are pushed to Home Assistant and it has a high quality .
  * You can build your own using ESPHome’s or energy meter sensors like the . For the DIY route, check out to get started.
  * Using a Raspberry Pi, you can use a CT clamp HAT from LeChacal called . They can be stacked to expand the number of lines to monitor. They also provide Active, Apparent, and Reactive power and power factor for single-phase and three-phase installations. They integrate with Home Assistant using MQTT.


Attention! Installing CT clamp sensor devices requires opening your electrical cabinet. This work should be done by someone familiar with electrical wiring and may require a licensed professional in some regions. Your qualified installer will know how to do this.
Disclaimer: Some links in this section are affiliate links.
### Data provided by your energy provider 
Some energy providers will provide you real-time information about your usage and have this data integrated into Home Assistant.
### Manual integration 
If you manually integrate your sensors, for example, using the or integrations: Make sure you set and provide the device_class, state_class, and unit_of_measurement for those sensors.
### Troubleshooting 
If you are unable to select your energy or power sensor in the grid consumption drop-down, make sure that its value is being recorded in the Recorder settings.
Disclaimer: Some links on this page are affiliate links helping support the Home Assistant project.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## YAML syntax - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/yaml/

#  On this page
Home Assistant uses the syntax for configuration. While most integrations can be configured through the UI, some integrations require you to edit your file to specify its settings.
## YAML Style Guide 
This page gives a high-level introduction to the YAML syntax used in Home Assistant. For a more detailed description and more examples, refer to the .
## A first example 
The following YAML example entry assumes that you would like to set up the with the .
```
notify:
 platform: pushbullet
 api_key: "o.1234abcd"
 name: pushbullet
```

YAML
Copy
  * An integration provides the core logic for some functionality (like notify provides sending notifications).
  * A platform makes the connection to a specific software or hardware platform (like pushbullet works with the service from pushbullet.com).


The basics of YAML syntax are block collections and mappings containing key-value pairs. Each item in a collection starts with a - while mappings have the format key: value. This is somewhat similar to a Hash table or more specifically a dictionary in Python. These can be nested as well. Beware that if you specify duplicate keys, the last value for a key is used.
## Indentation in YAML 
In YAML, indentation is important for specifying relationships. Indented lines are nested inside lines that are one level higher. In the above example, platform: pushbullet is a property of (nested inside) the notify integration.
Getting the right indentation can be tricky if you’re not using an editor with a fixed-width font. Tabs are not allowed to be used for indentation. The convention is to use 2 spaces for each level of indentation.
## Comments 
Strings of text following a # are comments. They are ignored by the system. Comments explain in plain language what a particular code block is supposed to do. For future-you or someone else looking at the file.
### Example with comment and nesting 
The next example shows an integration that uses a block collection for the values of options. The other properties (like name:) are specified using mappings. Note that the second line just has threat: with no value on the same line. Here, threat is the name of the input_select. The values for it are everything nested below it.
```
input_select:
 threat:
  name: "Threat level"
  # A collection is used for options
  options:
   - 0
   - 1
   - 2
   - 3
  initial: 0
```

YAML
Copy
### Example of nested mapping 
The following example shows nesting a collection of mappings in a mapping. In Home Assistant, this would create two sensors that each use the MQTT platform but have different values for their state_topic (one of the properties used for MQTT sensors).
```
sensor:
 - platform: mqtt
  state_topic: "sensor/topic"
 - platform: mqtt
  state_topic: "sensor2/topic"
```

YAML
Copy
## Including values 
### Environment variables 
On Home Assistant CoreHome Assistant Core is the Python program at the heart of Home Assistant. It is part of all installation types. It can be installed standalone (without Home Assistant Supervisor) as a container using Docker (this is typically referred to as the Home Assistant Container installation type). For development, Core can also be run using a Virtual Environment (previously referred as the Home Assistant Core installation type). For production setup, the Home Assistant Core installation type is deprecated. installations, you can include values from your system’s environment variables with !env_var. Note that this will only work for Home Assistant CoreHome Assistant Core is the Python program at the heart of Home Assistant. It is part of all installation types. It can be installed standalone (without Home Assistant Supervisor) as a container using Docker (this is typically referred to as the Home Assistant Container installation type). For development, Core can also be run using a Virtual Environment (previously referred as the Home Assistant Core installation type). For production setup, the Home Assistant Core installation type is deprecated. installations, in a scenario where it is possible to specify these. Regular Home Assistant users are recommended to use !include statements instead.
```
example:
 password: !env_var PASSWORD
```

YAML
Copy
#### Default value 
If an environment variable is not set, you can fall back to a default value.
```
example:
 password: !env_var PASSWORD default_password
```

YAML
Copy
### Including entire files 
To improve readability, you can source out certain domains from your main configuration file with the !include-syntax.
```
light: !include lights.yaml
```

YAML
Copy
More information about this feature can also be found at .
## Common issues 
### found character ‘\t’ 
If you see the following message:
```
found character '\t' that cannot start any token
```

Txt
Copy
This means that you’ve mistakenly entered a tab character, instead of spaces.
### Upper and lower case 
Home Assistant is case sensitive, a state of 'on' is not the same as 'On' or 'ON'. Similarly an entity of group.Doors is not the same as group.doors.
If you’re having trouble, check the case that Home Assistant is reporting in the dev-state menu, under Developer tools.
### Booleans 
YAML treats Y, true, Yes, ON all as true and n, FALSE, No, off as false. This means that if you want to set the state of an entity to on you must quote it as 'on' otherwise it will be translated as setting the state to true. The same applies to off.
Not quoting the value may generate an error such as:
```
not a valid value for dictionary value @ data
```

Txt
Copy
## Validating YAML syntax 
With all these indents and rules, it is easy to make a mistake. The best way to check if your YAML syntax is correct (validate) depends on the editor you use. We can’t list them all here.
  * If you edit the files directly in Home Assistant, refer to the section: 


## Related topics 
## Related links 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Integrating your home batteries - Home Assistant

Source: https://www.home-assistant.io/docs/energy/battery/

#  On this page


A home battery allows homes to store energy when you are either producing more solar power than you’re using, or store energy from the grid if the current price is low.
Home Assistant allows you to track how much energy flows from/to your battery.
## Hardware 
Home Assistant will need to know the amount of energy flowing from/to your batteries. This data can be tracked in various ways.
### Provided by the battery 
Some battery vendors have an API to integrate the data into your Home Assistant instance. An example is .
### Using a CT clamp sensor 
Current transformer (CT) clamp sensors measure your energy usage by looking at the current passing through an electrical wire. This makes it possible to calculate the energy usage. In Home Assistant we have support for off-the-shelf CT clamp sensors or you can build your own.
  * The off-the-shelf solution that we advise is the . The device has a local API, updates are pushed to Home Assistant and it has a high quality .
  * You can build your own using ESPHome’s or energy meter sensors like the . For the DIY route, check out to get started.
  * Using a Raspberry Pi, you can use a CT clamp HAT from LeChacal called . They can be stacked to expand the number of lines to monitor. They also provide Active, Apparent, and Reactive power and power factor for single-phase and three-phase installations. They integrate with Home Assistant using MQTT.


Attention! Installing CT clamp sensor devices requires opening your electrical cabinet. This work should be done by someone familiar with electrical wiring and may require a licensed professional in some regions. Your qualified installer will know how to do this.
Disclaimer: Some links in this section are affiliate links.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Integrating your solar panels - Home Assistant

Source: https://www.home-assistant.io/docs/energy/solar-panels/

#  On this page


Gain insight into your energy production by integrating your solar panels into Home Assistant.
If you also set up , you will be able to see expected solar production and automate based on planned production.
## Hardware 
Home Assistant will need to know the amount of energy that is being produced. This can be done in various ways.
### Using a CT clamp sensor 
Current transformer (CT) clamp sensors measure your energy usage by looking at the current passing through an electrical wire. This makes it possible to calculate the energy usage. In Home Assistant we have support for off-the-shelf CT clamp sensors or you can build your own.
  * The off-the-shelf solution that we advise is the . The device has a local API, updates are pushed to Home Assistant and it has a high quality .
  * You can build your own using ESPHome’s or energy meter sensors like the . For the DIY route, check out to get started.
  * Using a Raspberry Pi, you can use a CT clamp HAT from LeChacal called . They can be stacked to expand the number of lines to monitor. They also provide Active, Apparent, and Reactive power and power factor for single-phase and three-phase installations. They integrate with Home Assistant using MQTT.


Attention! Installing CT clamp sensor devices requires opening your electrical cabinet. This work should be done by someone familiar with electrical wiring and may require a licensed professional in some regions. Your qualified installer will know how to do this.
Disclaimer: Some links in this section are affiliate links.
### Connecting to your inverter 
Some solar inverters have APIs that can be read by Home Assistant.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Icons - Home Assistant

Source: https://www.home-assistant.io/docs/frontend/icons/

#  On this page
Home Assistant utilizes the community-driven (MDI) project for icons in the frontend. The icon library is a superset of the base icon library provided by Google and contains thousands of community-made icons for very specific applications, industries, and use-cases.
## Default icons 
Every entity in Home Assistant has a default icon assigned to it. There are way too many to list out here, but you’ll see them in your dashboard. You can to change the icons displayed to you.
## Finding icons 
### Icon picker 
The most common way you can find icons is by using the icon picker built right into Home Assistant. Select the Icon field when customizing an entity and start typing. The list will filter to icons that match your search criteria. You can also scroll through all available icons when the field is empty.
Tip
The icon picker will filter by icon name and by aliases applied to the icon by the MDI project. For example, typing “user” will show you most “account”-named icons.
For more detailed steps on customizing entities, including their icon, refer to .
### Material design icons picker browser extension 
The easiest way to browse and find icons outside of Home Assistant is with the official browser extension. The extension is available for Chrome, Firefox, and Edge and is maintained by the MDI team.
Note
Not all icons that appear in the MDI Picker Browser Extension may be available in Home Assistant (yet!). While the browser extension is updated as MDI releases new packages, Home Assistant may lag behind until its next release.
### Material design icons on the Pictogrammers website 
The last way to browse through available icons is by viewing the library on the Pictogrammers website, . Select an icon you’d like to use, then click “Home Assistant” to see an example of its usage.
Note
The Pictogrammers website will always show the latest release of the material design icons library. However, you may find icons that may not yet be available in Home Assistant (yet!). Watch the Home Assistant release notes for announcements on upgrades of the Material Design Icons library.
## Suggesting or contributing new icons 
Being open-source like Home Assistant, the material design icons library is always accepting suggestions and contributions to expand the library.
Note
Before suggesting or creating a new icon, it is very important that you and , open and closed, on their GitHub. Try searching with different terms that might mean the same thing. (e.g. “user”, “person”, “account”)
### Suggesting a new icon 
If you have an idea for an icon that isn’t currently in the library, but are not interested in creating it yourself, .
### Contributing a New Icon 
If you want to contribute a new icon to the library, familiarize yourself with the in the Material Design system. Then create your icon and .
#### Tips for creating new icons 
### Suggesting an icon alias 
Sometimes an icon exists, but you aren’t able to find it with the terms you were searching for. If this has ever happened to you, please that can be added to existing icons.
## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Integrating your water usage - Home Assistant

Source: https://www.home-assistant.io/docs/energy/water/

#  On this page
Home Assistant allows you to track your water usage in the home energy management too.
Although water usage is not strictly “energy”, it is still a valuable resource to track and monitor as it is often tightly coupled with energy usage (like gas). Additionally, it can help you reduce your ecological footprint by using less water.
### Home water meters 
There are several ways to measure water usage in your home. Multiple methods exist for reading your water usage. Older water meters typically feature a common arrow or only display total consumption. For these meters, you may require an with an ESP32 camera. While effective, this solution can be tedious to set up as it leans towards a DIY approach.
Newer water meters are equipped with a rotary disk that can be read using two methods. The first method utilizes light sensors, while the second method employs proximity sensors. The proximity sensor detects changes in the magnetic field, with each rotation of the disk representing one liter of water used. Meanwhile, the light sensor method operates on an autocorrelation technique, providing accuracy down to 100 milliliters instead of the traditional one-liter step.
For most water meters, the rotary encoder disk suffices the light sensor version. However, some older or specialized meters may necessitate the use of a proximity meter instead.
Home Assistant also has integrations build into the platform that connect with existing products
## Home Assistant integrations 
Home Assistant will need to know the amount of water that is being consumed to be able to track usage. Several hardware options are available to do this. Depending on your setup, the required hardware is provided by your public water utility company, or you may need to buy your own.
Some hardware with water meters may also provide additional practical functions or sensors, such as , for example, for controlling water shutoff, or temperature and pressure (to enable freeze alarms).
We have the following integrations available for existing products that can provide information about water usage:
There are also products for water usage monitoring that are based on existing common IoT protocol standards:


## Individual water devices 
Similar to tracking individual energy devices, Home Assistant supports tracking water usage of individual devices. This feature allows you to monitor water consumption from specific appliances or fixtures in your home, such as washing machines, dishwashers, or individual faucets.
You can create hierarchies of water devices by setting one device as an “upstream device” of another. This prevents double-counting when you have, for example, a main water meter and individual device meters. For more details on setting up device hierarchies and preventing double-counting, see the .
## Community-made sensors 
If your water meter lacks a rotary disk, magnetic disk, or coil. There are alternative solutions available to seamlessly integrate water monitoring into your smart home setup:
  * is a project running on an ESP32-CAM and can be fully integrated into Home Assistant using the Home Assistant Discovery Functionality of MQTT. It digitalizes your gas/water/electricity meter display and provides its data in various ways.


If you have a Culligan Water Softener, you may be able to interface with the inbuilt DEBUG PORT and receive water usage stats including Gallons (gal), Gallons Per Minute (gal/min), and Gallons to Recharge (gal):
  * (ESPHome)


Alternatively, the following shops sell ESPHome-based devices that use a 3-phase light sensor to detect a rotating disk in your water meter and convert this to the amount of water used in milliliters (ml):
  * (ESPHome)


Alternatively, the following shops sell ESPHome-based devices, that use a proximity sensor to detect a rotating magnet in your water meter and use that pulse to count each liter of water used:
## DIY 
Maybe you like to build one yourself?
If you manually integrate your sensors, for example, using the or integrations: Make sure you set and provide the device_class, state_class, and unit_of_measurement for those sensors.
For any of the above-listed options, make sure it actually works with the type of water meter you have before getting one.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Frontend of Home Assistant - Home Assistant

Source: https://www.home-assistant.io/docs/frontend/

#  On this page
The Home Assistant provides the graphical user interface that allows you to browse and control the state of your house, manage automations, and configure integrations.
Home Assistant comes with . But you can also create and customize your own dashboards.
## Creating and styling your own dashboards 
To learn how to create and style your own dashboards, refer to the following topics:
## Organizing and filtering data 
To learn how to organize and filter your data on an existing dashboard, refer to the following topics:
  * into , , , and 


## User- or browser-dependent settings, general settings 
### User- or browser-dependent settings 
Some of the frontend settings depend on the user. Other settings can be set by client. This allows you for example to have different languages per user, and a different theme depending on the device that is used to display Home Assistant.
To change these settings, in the bottom left, select your username to open your .
  * To change general settings such as language, number and time format, go to the User settings.
  * To change browser dependent settings such as the theme, default dashboard, or whether or not to show the sidebar, change the Browser settings.


### Themes 
Themes can be set per browser. In the , you can define some theme settings, such as whether you want a light or dark theme. However, more detailed theme settings require YAML configuration. Refer to the documentation of the .
### General settings 
Some of the settings, such as location and currency, were defined during the onboarding process. They can be changed under . Refer to the documentation on .
## Apps for Android and iOS 
If you are looking for information on Home Assistant for Android or iOS, refer to the .
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Glossary - Home Assistant

Source: https://www.home-assistant.io/docs/glossary/

#  On this page
The glossary covers terms which are used around Home Assistant.
## A 
### Action 
Actions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. An action is a software function that interacts with targets to make something happen. Actions can use other actions and/or scenes to interact with entities and cause these entities to do something. Actions can also include conditions and a delay. An action can perform multiple actions at the same time. For example, if your presence is detected in a room, an action may perform one action to turn on a light and perform another action to start playing music after a delay. Actions are also used on the dashboard, for example as tap or hold action on a UI element. When triggered, the action performs another action. Home Assistant provides a series of predefined actions, such as homeassistant.turn_on, homeassistant.toggle, or homeassistant.reload.
### Actor 
An entity that receives a control signal and performs an action in a system.
### Add-on 
Add-ons are additional standalone third-party software packages that can be installed on Home Assistant OS. Most of these, add-on provided, applications can be integrated into Home Assistant using integrations. Examples of add-ons are: an MQTT broker, database service or a file server.
### Area 
An area in Home Assistant is a of devices and entities that are meant to match areas (or rooms) in the physical world: your home. For example, the living room area groups devices and entities in your living room. Areas allow you to target actions at an entire group of devices. For example, turning off all the lights in the living room. Locations within your home such as living room, dance floor, etc. Areas can be assigned to floors. Areas can also be used for automatically generated cards, such as the .
### Automation 
Automations connect one or more triggers to one or more actions in a ‘when trigger then do action’ fashion with additional optional conditions. For example, an automation might connect the trigger ‘sunset’ to the action ‘turn the lights on’ but only if the condition ‘someone is home’ is met. Pre-made automations for common use-cases are available via .
## B 
### Backup 
Home Assistant has built-in functionality to create files containing a copy of your configuration. This can be used to restore your Home Assistant as well as migrate to a new system. The backup feature is available for all .
### Binary sensor 
A binary sensor returns information about things that only have two states - such as on or off.
### Blueprint 
A blueprint is a , , or entity configuration with certain parts marked as configurable. This allows users to create multiple scripts, automations or template entities based on the same blueprint, with each having its own configuration-specific settings. Blueprints are shared by the community on the in the forum.
### Button 
A button entity can fire an event, or trigger an action towards a device or service. It can be compared to a physical push button. The button entity does not have a state like on or off, but keeps the timestamp of when it was last pressed in the Home Assistant UI or via an action.
## C 
### Category 
A category is an organization tool that allows items in a table. Like labels, categories allow grouping irrespective of the items’ physical location. For example, on the automations page, you can create the categories “Notifications” or “NFC tags” to view your automations grouped or filtered. Categories are unique for each table. The automations page can have different categories than the scene, scripts, or helpers settings page.
### Climate 
The Climate entity allows you to control and monitor HVAC (heating, ventilating, and air conditioning) devices and thermostats.
### Commissioning 
In the context of Matter devices, commissioning is the process of adding a device to a Matter controller. It is the equivalent of pairing a device in Zigbee or Z-Wave. Commissioning is done by scanning a QR code or entering a code manually. The code is printed on the device or its packaging. The code contains information about the device, such as its type, manufacturer, and serial number. The controller uses this information to identify the device and to download the required information to control the device. For example, the controller downloads the device’s capabilities, such as the supported commands and the available attributes. The controller also downloads the device’s configuration, such as the device’s name and location.
### Component 
Better known as: Integrations. Integrations used to be known as components.
### Condition 
Conditions are an optional part of an automation that will prevent an action from firing if they are not met.
### Configuration file 
The configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI.
### Cover 
Covers are devices such as blinds, garage doors, etc that can be opened and closed and optionally set to a specific position.
### Custom integration 
A custom integration is an integration that has been created by someone from the Home Assistant community and has been published for others to use at their own risk. Custom integrations are not supported by the Home Assistant project. They are not reviewed or tested by the Home Assistant development team and thus may negatively impact the stability of your Home Assistant instance. An example of a custom integration is the integration.
### Customize 
Customization allows you to overwrite the default parameters of your devices in the configuration.
## D 
### Device 
A device is a model representing a physical or logical unit that contains entities. Example for a device as a physical unit A smart plug named ‘Coffee machine’ which provides 2 entities: a switch entity to turn power on or off (‘Coffee machine power switch’) and a sensor entity for power monitoring (‘Coffee machine power sensor’). Example for a device as a logical unit An ecobee thermostat with 4 room sensors. This thermostat is seen as 5 devices in Home Assistant: 1 device for the thermostat with 4 sensors, and 1 device for each room sensor. Each device can be in a different area and may have more than one input or output within that area. Devices have properties such as ID, manufacturer, name, model, hardware version, firmware version, connections, etc.
### Device tracker 
Device trackers are used to track the presence, or location, of a device.
### Diagnostics 
The diagnostics integration provides a way to download diagnostic data from a device or integration for sharing in issue reports. Sharing diagnostics data when reporting an issue allows developers to diagnose and fix your reported problem quicker.
### Discovery 
Discovery is the automatic setup of zeroconf/mDNS and uPnP devices after they are discovered.
### Domain 
Each integration in Home Assistant has a unique identifier: a domain. All of the entities and actions available in Home Assistant are provided by integrations and thus belong to such a domain. The first part of the entity or action, before the . shows the domain they belong to. For example light.kitchen is an entity in the light domain from the , while hue.activate_scene is the activate_scene action for the hue domain which belongs to the .
## E 
### Entity 
An entity represents a sensor, actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a device or a service. Entities have states. Example for entities as part of a device A combined temperature and humidity sensor device provides two sensor entities. One for temperature (e.g. sensor.temperature with state 21.0 and unit °C) and one for humidity (e.g. sensor.humidity with state 65.4 and unit %). Example for entities as part of a service A weather service that provides 3 entities: wind speed, air pressure, and ozon level. Example of an entity used for control A fan that is turned on when the temperature exceeds 30 °C. There are standardized types of entities for common integrations such as light, switch, camera, sensor, fan, or vacuum. Some entities are not part of a device or service. Examples of standalone entities are automation, script, scene entities, and helper entities (e.g. input helpers). Most properties of entities are related to the state. Entities have optional attributes such as friendly name, unit of measurement, and an icon or picture that can be displayed in the frontend.
### Event 
Every time something happens in Home Assistant, an event is fired. There are different types of events, such as state change events, when an action was triggered, or the time changed. All entities produce state change events. Every time a state changes, a state change event is produced. Events can be used to trigger automations or scripts. For example, you can trigger an automation when a light is turned on, then a speaker turns on in that room. Events can also be used to trigger actions in the frontend. For example, you can trigger an action when a button is pressed.
### Event entity 
Events are signals that are emitted when something happens, for example, when a user presses a physical button like a doorbell or when a button on a remote control is pressed.
## F 
### Floor 
A floor in Home Assistant is a of areas that are meant to match the physical floors in your home. Devices & entities are not assigned to floors but to areas. A floor has properties such as: Floor ID, name, aliases (for use in assistants), an icon, and a floor level. Some of these properties are optional. The level number can be negative to reflect floors below the basement. Floors can be used in automations and scripts as a target for actions. For example, to turn off all the lights on the downstairs floor when you go to bed.
### Frontend 
The frontend is a necessary component for the UI, it is also where you can define your themes.
## G 
### Group 
Groups are a way to organize your entities into a single unit.
## H 
### HASS 
HASS is an abbreviation for Home Assistant that was commonly used in the past. This abbreviation is no longer actively used. It is recommended to use the full name “Home Assistant” instead of abbreviations.
### HassOS 
Another name for Home Assistant Operating System
### Home Assistant Container 
Home Assistant Container is a standalone container-based installation of Home Assistant Core. Any compatible runtime can be used, but the documentation focus is on Docker.
### Home Assistant Core 
Home Assistant Core is the Python program at the heart of Home Assistant. It is part of all installation types. It can be installed standalone (without Home Assistant Supervisor) as a container using Docker (this is typically referred to as the Home Assistant Container installation type). For development, Core can also be run using a Virtual Environment (previously referred as the Home Assistant Core installation type. For production setup, the .
### Home Assistant Operating System 
Home Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users.
### Home Assistant Supervised 
The Home Assistant Supervised installation type is a full UI managed home automation ecosystem that runs the Home Assistant Core program, the Home Assistant Supervisor and add-ons. It comes pre-installed on Home Assistant OS, but can be installed standalone on Debian Linux systems. It leverages Docker, which is managed by the Home Assistant Supervisor. The .
### Home Assistant Supervisor 
The Home Assistant Supervisor is a program that manages a Home Assistant installation, taking care of installing and updating Home Assistant, add-ons, itself, and, if used, updating the Home Assistant Operating System.
### Host 
A device that can communicate with other devices on a network. During setup and configuration, an input requesting a Host typically refers to a device’s network address so that Home Assistant can attempt to connect to it. This may be in the form of a hostname, URL, IP address or some other type of network identifier. If you do not know the hostname or IP address of a device, you can find it in your router’s webinterface. For example, if your device is connected wirelessly, somewhere there is a page listing all the devices that are connected to your network. It depends on your router, where exactly this page is. It could be under Network > Wireless.
## I 
### Image 
The Image integration allows other integrations to display a static image.
### Integration 
Integrations connect and integrate Home Assistant with devices, services, and more. They contain all the logic to handle vendor- and device-specific implementations, such as authentication or specific protocols. The integration brings such device-specific elements into Home Assistant in a standardized way. For example, the integration integrates the Philips Hue bridge and its connected bulbs into Home Assistant, making them available as Home Assistant light entities you can control.
### Intent 
Intent is a term used with voice assistants. The intent is what Home Assistant thinks you want it to do when it extracts a command from your voice or text utterance. Currently, the following intents are supported out of the box: HassTurnOn, HassTurnOff, HassGetState, and HassLightSet. These intents allow you to turn things on or off, inquire about a state, or change the brightness or color of a light.
## L 
### Label 
Labels in Home Assistant allow elements irrespective of their physical location or type. Labels can be assigned to areas, devices, entities, automations, scenes, scripts, and helpers. Labels can be used in automations and scripts as a target for actions. Labels can also be used to filter data. For example, you can filter the list of devices to show only devices with the label heavy energy usage or turn these devices off when there is not a lot of solar energy available.
### Light 
A light has a brightness you can control, and optionally color temperature or RGB color control.
### Long-term statistics 
Home Assistant saves long-term statistics for a sensor if the entity has a state_class of measurement, total, or total_increasing. For short-term statistics, a snapshot is taken every 5 minutes. For long-term statistics, an hourly aggregate is stored of the short-term statistics. Short-term statistics are automatically purged after a predefined period (default is 10 days). Long-term statistics are never purged.
### Lovelace 
Lovelace is the original code name of the UI that is now known as .
## M 
### Matter 
Matter is an open-source standard that defines how to control smart home devices on a Wi-Fi or Thread network. The aim of the standard is to improve security and to make devices interoperable across vendors, replacing proprietary protocols for smart home ecosystems. Unlike other standards, Matter allows joining the same device to multiple controllers. For example, you can add a light to Google Home, Apple Home, and Home Assistant at the same time. A bridge device can be used to connect devices running on other smart home technologies such as Zigbee or Z-Wave.
## N 
### Notification 
You can use notifications to send messages, pictures, and more, to devices.
## P 
### Package 
Packages allow you to bundle different component configurations together.
### Platform 
Platforms are building blocks provided by some integrations to be used by other integrations. For example, the integration provides the light platform that is utilized by all integrations providing light entities such as e.g. .
### Polling 
Data polling is the process of querying a device or service at regular intervals to check for updates or retrieve data. By defining a custom polling interval, you can control how frequently your system checks for new data, which can help optimize performance and reduce unnecessary network traffic.
## R 
### Reload 
Applies the changes made to the Home Assistant configuration files. Changes are normally automatically updated. However, changes made outside of the front end will not be reflected in Home Assistant and require a reload. To perform a manual reload, go to Settings > System > Restart Home Assistant (top right) > Quick reload. If you do not see the Quick reload option in the menu, you need to enable Advanced mode in your user settings. More granular reload options are available in YAML configuration reloading section in Developer tools > YAML.
## S 
### Scene 
Scenes capture the states you want certain entities to be. For example, a scene can specify that light A should be turned on and light B should be bright red.
### Script 
Scripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on.
### Selector 
Selectors are components for the user interface. Some selectors can, for example, show a toggle button to turn something on or off, while another select can filter a list of devices to show only devices that have motion-sensing capabilities.
### Sensor 
Sensors return information about a thing, for instance the level of water in a tank.
### Service 
The term “service” in Home Assistant is used in the sense of an information service. For example, the municipal waste management service that provides entities for organic, paper, and packaging waste. In terms of functionality, the information service is like a device. It is called service to avoid confusion, as it does not come with a piece of hardware.
### State 
The state holds the information of interest of an entity. For example, if a light is on or off, the current temperature, or the amount of energy used. Entities store 3 timestamps related to the state: last_updated, last_changed, and last_reported. Each entity has exactly one state and the state only holds one value at a time. However, entities can store attributes related to that state. For example, the state of a light is on, and the related state attributes could be its current brightness and color values. State change events can be used as triggers. The current state can be used in conditions.
### Switch 
Switches are things that have two states you can select between, such as turning on or off a socket.
## T 
### TTS 
TTS (text-to-speech) allows Home Assistant to talk to you.
### Template 
A template is an automation definition that can include variables for the action or data from the trigger values. This allows automations to generate dynamic actions.
### Thread 
Thread is a low-power mesh networking standard that is specifically designed for smart home applications. It is a protocol that defines how devices communicate. Mesh topology means that the devices can communicate with each other directly, without going through a central controller first. Thread uses the same radio frequency (RF) technology as Zigbee, but provides IP connectivity similar to Wi-Fi. Unlike Zigbee, Thread does not specify how to control devices. How Thread-enabled devices are controlled is specified in a higher level protocol such as HomeKit or Matter.
### Thread border router 
A Thread border router forwards data packets between your local network and the Thread network. This enables smart home devices within a Thread network to communicate with IPv6-capable devices in your local network. A Thread border router is connected to your network either via Wi-Fi or Ethernet and uses its radio frequency (RF) radio to communicate with the Thread mesh network. In case of Matter, the data that is forwarded is encrypted. Examples of Thread border routers are the Nest Hub (2nd gen), the HomePod mini, and the Home Assistant Connect ZBT-2 together with the OpenThread Border Router add-on.
### Trigger 
A trigger is a set of values or conditions of a platform that are defined to cause an automation to run.
## U 
### Update 
An update entity is an entity that indicates if an update is available for a device or service. This can be any update, be it a firmware update for a device like a light bulb or router, or a software update for an add-on or a container.
## V 
### Valve 
Valves are devices to control the flow of liquids and gases. All valves in Home Assistant can be opened and closed. Some valves can also be set to a specific position.
### Variables 
Variables are used to store values in memory that can be processed for example, in a script.
## Y 
### YAML 
YAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files.
## Z 
### Zone 
Zones allow you to specify certain regions on a map. They enable zone presence-detection and can be used in automations. For example, to start the vacuum after you left home or start the heating at home when you leave the office.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## I'm locked out! - Home Assistant

Source: https://www.home-assistant.io/docs/locked_out/

#  On this page
The sections below deal with recovering from a situation where you are not able to sign in, or need to recover your data.
## Forgot username 
### Symptom: I’m the owner and I forgot my username 
You are the owner of the Home Assistant server and you cannot login because you forgot your username.
#### Remedy 
  1. Check if the following conditions are met: 
     * you are using the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. 
     * you have access to the Home Assistant server.
  2. Open a terminal connection to Home Assistant: 
  3. In the terminal, enter the auth list command. 
     * This command lists all users that are registered on your Home Assistant.


## Forgot password 
### Symptom: I’m the owner and I forgot my password 
You are the owner or administrator of Home Assistant and forgot your password.
### Remedy: resetting an owner’s password 
If you are the owner or have administrator, there are different methods to reset a password, depending on your situation:


#### To reset a password while still logged in 
The method used to reset a password depends on your user rights:
#### To reset an owner’s password, via console 
Use this procedure only if the following conditions are met:
  * You can access the Home Assistant console on the device itself (not via the SSH terminal from the add-ons).


  1. If you are using a Home Assistant Yellow or Green, refer to their documentation. 
     * If you are using a Home Assistant Yellow, refer to the following procedure: 
     * If you are using a Home Assistant Green, refer to the following procedure: 
  2. If you are not using a Yellow or Green: Connect to the console of the Home Assistant server: 
     * If you are using a virtual machine, connect to your virtual machine console.
     * If you are using another board, connect a keyboard and monitor to your device and access the terminal. The procedure is likely very similar to the one described for the Home Assistant Green.
  3. Once you have opened the Home Assistant command line, enter the following command: 
     * Command: auth reset --interactive 
     * This will display a list of users. Select your user and enter a new password when prompted.
     * Troubleshooting: If you see the message zsh: command not found: auth, you likely did not enter the command in the serial console connected to the device itself, but in the terminal within Home Assistant.
  4. You can now log in to Home Assistant using this new password.


#### To reset a user’s password, via the container command line 
If you are running Home Assistant in a container, you can use the command line in the container with the hass command to change your password. The steps below refer to a Home Assistant container in Docker named homeassistant. Note that while working in the container, commands will take a few moments to execute.
  1. docker exec -it homeassistant bash to open to the container command line
  2. hass to create a default user, if this is your first time using the tool
  3. hass --script auth --config /config change_password existing_user new_password to change the password
  4. exit to exit the container command line
  5. docker restart homeassistant to restart the container.


#### To reset a user’s password, as an owner via the web interface 
Only the owner can change other user’s passwords.
  1. In the bottom left, select your user to go to the page and make sure Advanced Mode is activated.
  2. Go to and select the person for which you want to change the password.
  3. At the bottom of the dialog box, select Change Password. 
     * Note: this is available as the owner, not administrator.
  4. Enter the new password, and select OK.
  5. Confirm the new password by entering it again, and select OK again.
  6. A confirmation box will be displayed with the text Password was changed successfully.


## Preparing the system to start a new onboarding process 
If you lose the password associated with the owner account and the steps above do not work to reset the password, the only way to resolve this is to start a new onboarding process.
## Recovering data for Home Assistant 
Unless your SD card/data is corrupted, you can still get to your files or troubleshoot further. There are a few routes:
  * Connect a USB keyboard and HDMI monitor directly to the Raspberry Pi.
  * Remove the SD and access the files from another machine (preferably one running Linux).


## Connect directly 
If you’re using a Raspberry Pi, you’re likely going to have to pull the power in order to get your monitor recognized at boot. Pulling power has a risk of corrupting the SD, but you may not have another option. Most standard USB keyboards should be recognized easily.
Once you’re connected, you’ll see a running dmesg log. Hit the enter key to interrupt the log. Sign in as “root”. There is no password.
You will then be at the Home Assistant CLI, where you can run the custom commands. These are the same as you would run using the SSH add-on but without using ha in front of it. For example:
## Accessing files from the SD/HDD 
### Remove the SD and access the files from another computer 
The files are on an EXT4 partition (hassos-data) and the path is /mnt/data/supervisor. These are easily accessed using another Linux machine with EXT support.
For Windows or macOS you will need third party software. Below are some options.
  * Windows: (read-only access to the SD)
  * macOS: 


## Deleting a user 
You need to be an owner or have administrator rights to delete a user.
  1. Go to and select the person which you want to delete. 
     * Note: you cannot delete the owner.
  2. At the bottom of the dialog box, select Delete. 
     * A confirmation dialog box will be displayed.
  3. To confirm, select OK.


## Related topics 


## Related links 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Labels - Home Assistant

Source: https://www.home-assistant.io/docs/organizing/labels/

#  On this page
Labels in Home Assistant allow grouping elements irrespective of their physical location or type. Labels can be assigned to areas, devices, entities, automations, scenes, scripts, and helpers. Labels can be used in automations and scripts as a target for actions. Labels can also be used to filter data.
For example, you can filter the list of devices to show only devices with the label heavy energy usage or turn these devices off when there is not a lot of solar energy available.
## Creating a label 
Follow these steps to create a new label from the Labels view.
  1. Go to and on top, select the Labels tab.
  2. Select the Create label button.
  3. In the dialog, enter the label details:
     * Give the label a Name (required).
     * Add an icon (We use ).
     * Add a Color.
  4. Select Create.
Result: A new label is created.


## Applying labels 
Follow these steps to apply a label
  1. To apply a label to an area:
     * Go to .
     * On the area card, select the edit button.
     * Select one or more labels or select Add new label to create a new one.
  2. To apply a label to a device, entity, or helper:
  3. To apply a label to an automation, scene, or script:


## Deleting a label 
Follow these steps to delete a label. It will be removed from all the list entries it was applied to. If you used this label in automations or script as targets, you need to adjust those.
  1. Go to and on top, select the Labels tab.
  2. In the list of labels, find the label you want to delete and select the three dots menu.
  3. Select Delete.
  4. If you used this label in automations or script as targets, you need to adjust those.


## Removing labels 
  1. Go to the data table that contains the element from which you want to remove the label: 
     * Go to Settings > Devices & Services and open the respective tab.
     * Or, go to and open the respective tab.
  2. Select the button. 
     * From the list, select all the items from which you want to remove a label.
     * In the top right corner, select the three dots menu, then select Add label.
     * Then, deselect the checkbox for the label you want to remove.


## Related topics 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Floors - Home Assistant

Source: https://www.home-assistant.io/docs/organizing/floors/

#  On this page
A floor in Home Assistant is a logical grouping of areasAn area in Home Assistant is a logical grouping of devices and entities that are meant to match areas (or rooms) in the physical world: your home. For example, the living room area groups devices and entities in your living room. [Learn more] meant to match your home’s physical floors.
Devices and entities cannot be assigned to floors directly but to areas. Floors can be used in automationsAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] and scriptsScripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on. [Learn more] as a target for actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more]. For example, to turn off all the lights on the downstairs floor when you go to bed.
## Creating a floor 
Follow these steps to create a new floor.
  1. Go to and select Create floor.
  2. In the dialog, enter the floor details:
  3. Select Add.
Result: A new floor is created.
  4. You can now .


## Reordering floors on built-in dashboards 
Follow these steps to rearrange floors and areas on the built-in dashboards (such as Overview, Lights, and Security).
  1. Go to .
  2. There are 2 options to rearrange items: 
     * Option 1: Use drag-and-drop.
     * Option 2: In the top-right corner, select the three dots menu and select Reorder floors and areas.
       * In the dialog, move the floors or areas you want to rearrange:


## Deleting a floor 
Follow these steps to delete a floor. Areas that are assigned to a floor will become unassigned. AutomationsAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] and scriptsScripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on. [Learn more] or voice assistants that used a floor as a target will no longer work as they no longer have a target.
  1. Go to .
  2. Next to the floor, select the three dots menu and select Delete floor.
  3. If you have automationsAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more], scriptsScripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on. [Learn more], or voice assistants that used floors as a target, you will need to update these.


## Related topics 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Categories - Home Assistant

Source: https://www.home-assistant.io/docs/organizing/categories/

#  On this page
Categories let you group and filter items in a table. Like labels, categories allow grouping irrespective of the items physical location.
For example, on the automations page, you can create the categories “Notifications” or “NFC tags” to view your automations grouped or filtered. These categories group automations on the automation page, but have no effect anywhere else. Categories are unique for each table. The automations page can have different categories than the scene, scripts, or helpers settings page.
## Creating a category 
Follow these steps to create a new category.
  1. Go to and open the respective tab.
  2. In the top left, select the Filters button.
  3. Select Category, then Add category.
  4. Enter a name, select an icon and select Add.
Result: A new category is created.


## Assigning a category 
  1. Go to and open the respective tab.
  2. To assign a category to a single item:
     * Find the item in the list and select the three dots menu.
     * Select Assign category and select the category from the list.
     * If the category is not in the list, select Add new category and make a new one.
  3. To assign a category to multiple items:
  4. Once categories are applied, the table items are grouped by those categories.
     * The example shows 2 categories: Coffee and housekeeping.


## Editing or deleting a category 
To rename or delete a category, follow these steps:
  1. Go to and open the respective tab.
  2. In the top left, select the Filters button.
  3. In the list, find the category you want to edit and select the three dots menu next to it.
  4. Select Edit category or Delete category.


## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Installation - Home Assistant

Source: https://www.home-assistant.io/hassio/installation/

#  On this page
The first step to getting started with Home Assistant is to install it on a device. There are many ways to run it for all kinds of scenarios and all kinds of skill levels. 
Easiest 
## Plug and play with Home Assistant Green 
The affordable Home Assistant Green is the easiest way to start using Home Assistant. It's plug-and-play and comes with already installed. 
### Home Assistant Green 
The easiest way to get started with Home Assistant
SKILLS REQUIRED 
  * Interest in setting up a smart home


TOOLS REQUIRED 
  * Ethernet connection


Easy 
## DIY with Raspberry Pi 
Raspberry Pi, a mini low-cost computer, is one of the most popular platforms for running Home Assistant. If you want to learn how to DIY, this is a good way to start and gain experience. 
### Install Home Assistant on Raspberry Pi 
A low-cost DIY solution to get started with Home Assistant
SKILLS REQUIRED 
  * Assembling a Raspberry Pi setup
  * Flashing a Raspberry Pi


TOOLS REQUIRED 
  * Raspberry Pi 4 or 5 with power supply (minimum 2 GB RAM)
  * MicroSD card
  * Ethernet connection


## About installation types 
Home Assistant offers two different installation types. Home Assistant Operating System is the recommended installation type. 
  * Home Assistant Operating System: An embedded, minimalistic operating system designed to run the Home Assistant ecosystem on single board computers (like the Home Assistant Green or a Raspberry Pi) or Virtual Machines. It is the most convenient option in terms of installation and maintenance and it supports add-onsAdd-ons are additional standalone third-party software packages that can be installed on Home Assistant OS. [Learn more]. Home Assistant Operating System is the recommended installation type for most users.
  * Home Assistant Container: Container-based installation of Home Assistant. You need to bring your own system (such as Linux) with container orchestration (like Docker), and manually handle updates. Home Assistant Container installations don’t have access to add-onsAdd-ons are additional standalone third-party software packages that can be installed on Home Assistant OS. [Learn more]. 
    * Note: Some integrations, such as Thread and Z-Wave, are controlled by add-onsAdd-ons are additional standalone third-party software packages that can be installed on Home Assistant OS. [Learn more]. There is no out-of-the-box support for these on Container installations. 


HA OS1  | Container1   
---|---  
One-click updates   
1: Names are abbreviated. The full names of the installation types are: Home Assistant Operating System Home Assistant Container 
Intermediate 
## Extend with Home Assistant Yellow 
The extensible Home Assistant Yellow comes with all the ingredients you need to help you build a robust smart home. All you need to do is to bring your own Raspberry Pi Compute Module. 
### Home Assistant Yellow 
The powerful way to run Home Assistant
SKILLS REQUIRED 
  * You're comfortable following instructions on:
  * Installing a compute module and a heat sink
  * Flashing a Raspberry Pi


TOOLS REQUIRED 
Hard 
## Install on other hardware 
Home Assistant can be repurposed and installed on various hardware, such as an Odroid or a generic x86-64 machine. The Home Assistant Operating System allows you to install Home Assistant on these devices even if you have little to no Linux experience. 
### Install Home Assistant on Odroid devices 
A more powerful alternative to Raspberry Pi
SKILLS REQUIRED 
  * You're comfortable following instructions on:
  * Writing boot images
  * Installing an SD card or eMMC


TOOLS REQUIRED 
  * An Odroid device
  * MicroSD card or eMMC
  * Ethernet connection


### Install Home Assistant on x86-64 machines 
Repurpose workstation hardware to run Home Assistant
SKILLS REQUIRED 
  * You can use a command line and install a boot medium on your hardware
  * You're comfortable configuring the BIOS based on instructions.


TOOLS REQUIRED 
Expert 
### Install Home Assistant variants on Raspberry Pi 
A low-cost DIY solution to get started with Home Assistant
SKILLS REQUIRED 
TOOLS REQUIRED 
  * Raspberry Pi 3, 4 or 5 with power supply
  * MicroSD card
  * Ethernet connection


### Install Home Assistant on Linux 
Use Home Assistant OS, Container
SKILLS REQUIRED 
  * Advanced knowledge of Linux
  * Using Linux command line
  * Using Docker Compose (for HA Container)


TOOLS REQUIRED 
  * Machine with Linux installed


### Install Home Assistant on macOS 
Use Home Assistant OS on a VM
SKILLS REQUIRED 
  * Advanced knowledge of macOS
  * Using macOS command line


TOOLS REQUIRED 
  * Machine with macOS installed


### Install Home Assistant on Windows 
Use Home Assistant OS on a VM
SKILLS REQUIRED 
  * Know how to find an IP address on your router
  * Advanced knowledge of Windows
  * Using Linux command line


TOOLS REQUIRED 
  * Machine with Windows installed
  * VirtualBox (for VM)


### Install Home Assistant on other systems 
Use Home Assistant on virtual machines, NAS, and more
SKILLS REQUIRED 
  * Know how to find an IP address on your router
  * Advanced knowledge of Windows
  * Using Linux command line


TOOLS REQUIRED 
  * Machine with Windows installed
  * VirtualBox (for VM)


### Deprecated installation types 
Home Assistant used to offer two additional installation types for advanced users: Home Assistant CoreHome Assistant Core is the Python program at the heart of Home Assistant. It is part of all installation types. It can be installed standalone (without Home Assistant Supervisor) as a container using Docker (this is typically referred to as the Home Assistant Container installation type). For development, Core can also be run using a Virtual Environment (previously referred as the Home Assistant Core installation type). For production setup, the Home Assistant Core installation type is deprecated. and Home Assistant SupervisedThe Home Assistant Supervised installation type is a full UI managed home automation ecosystem that runs the Home Assistant Core program, the Home Assistant Supervisor and add-ons. It comes pre-installed on Home Assistant OS, but can be installed standalone on Debian Linux systems. It leverages Docker, which is managed by the Home Assistant Supervisor. The Home Assistant Supervised installation type is deprecated.. These two methods are now . 
  * Home Assistant Supervised: Manual installation of the Supervisor. 
  * Home Assistant Core: Manual installation using Python virtual environment. 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Getting started
#  On this page



## Areas - Home Assistant

Source: https://www.home-assistant.io/docs/organizing/areas/

#  On this page
An area in Home Assistant is a logical grouping of devicesA device is a model representing a physical or logical unit that contains entities. and entitiesAn entity represents a sensor, actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a device or a service. [Learn more] that are meant to match areas (or rooms) in the physical world of your home.
For example, the “Living room” area groups devices and entities in your living room. Areas allow you to target an entire group of devices with an action. For example, turning off all the lights in the living room. Areas can be assigned to floorsA floor in Home Assistant is a logical grouping of areas that are meant to match the physical floors in your home. Devices & entities are not assigned to floors but to areas. Floors can be used in automations and scripts as a target for actions. For example, to turn off all the lights on the downstairs floor when you go to bed. [Learn more]. Areas can also be used to automatically generate cards, such as the .
## Creating an area 
Follow these steps to create a new area from the Areas view.
  1. Go to and select Create area.
  2. In the dialog, enter the area details:
  3. Select Add.
Result: A new area is created.


## Assigning areas to floors and add labels 
If an area has not yet been assigned to a floorA floor in Home Assistant is a logical grouping of areas that are meant to match the physical floors in your home. Devices & entities are not assigned to floors but to areas. Floors can be used in automations and scripts as a target for actions. For example, to turn off all the lights on the downstairs floor when you go to bed. [Learn more], it is shown in the Unassigned areas section. Follow these steps to assign an area to a floor.
  1. Go to and select Create area.
  2. On the area card, select the edit button.
  3. In the dialog, select the floorA floor in Home Assistant is a logical grouping of areas that are meant to match the physical floors in your home. Devices & entities are not assigned to floors but to areas. Floors can be used in automations and scripts as a target for actions. For example, to turn off all the lights on the downstairs floor when you go to bed. [Learn more] and add labelsLabels in Home Assistant allow grouping elements irrespective of their physical location or type. Labels can be assigned to areas, devices, entities, automations, scenes, scripts, and helpers. Labels can be used in automations and scripts as a target for actions. Labels can also be used to filter data. [Learn more] if you like.


## Assigning an area to multiple items 
You can assign an area to multiple items at once in the automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more], sceneScenes capture the states you want certain entities to be. For example, a scene can specify that light A should be turned on and light B should be bright red. [Learn more], scriptScripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on. [Learn more], and deviceA device is a model representing a physical or logical unit that contains entities. pages.
  1. Depending on what you want to assign, go to one of the following pages:
     * For automations, scripts, or scenes and open the respective tab.
     * For devices, go to .
  2. In the list, you want to assign to an area.
  3. In the top right corner, select Move to area and select the target area from the list.


## Editing an area 
Follow these steps to edit an area.
  1. Go to and on the area card, select the edit button.
  2. In the dialog, adjust the area details you want to change: 


## Reordering areas on built-in dashboards 
Follow these steps to rearrange floors and areas on the built-in dashboards (such as Overview, Lights, and Security).
  1. Go to .
  2. There are 2 options to rearrange items: 
     * Option 1: Use drag-and-drop.
     * Option 2: In the top-right corner, select the three dots menu and select Reorder floors and areas.
       * In the dialog, move the floors or areas you want to rearrange:


## Deleting an area 
Follow these steps to delete an area. It will be removed from all the floors it was assigned to. All the devices that were assigned to this area will become unassigned. If you used this area in automations or script as targets, or with voice assistant, these will no longer work.
  1. Go to and select the area card.
  2. In the top right corner, select the three dots menu. Then, select Delete.
  3. If you used this area in automations or script as targets, or with voice assistant, they will no longer work.
     * You can adjust or delete the related scripts or automations.
  4. If you still had devices in that area, they are no longer assigned to any room.
     * If you have moved the devices, you can now reassign them to a new area.


## Related topics 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Working with tables - Home Assistant

Source: https://www.home-assistant.io/docs/organizing/tables

#  On this page
When working with tables, you can select multiple items to apply an action. If you have items by assigning them to floors, areas, labels, or directories, you can also filter your data accordingly.
## Selecting multiple items in a table 
  1. In your table, select the button.
  2. In the list, select the items of interest.
  3. You can now apply changes to all selected elements, such as or .


## Filtering items in a table 
You can filter a table so that only items matching certain criteria are shown.
To filter items in a table, follow these steps:
  1. In the top left corner above the table, select the Filters button.
  2. In the filters panel, select your filter criteria.
     * You can filter for , , , and if you have previously defined them.
     * The list of available criteria depends on the type of table.


## Grouping and sorting items in a table 
You can group items in a table according to certain criteria. The number of shown items stays the same. No items will be hidden.
To group items in a table, follow these steps:
  1. In the top right above the table, select the Group by button.
  2. The items will be grouped according to the criteria you chose.
     * The list of available criteria depends on the type of table. 
       * The example shows a list of devices, grouped by manufacturer.
       * In contrast, the entities table does not allow grouping by manufacturer, but by entity domains.
  3. To sort the items, select the Sort by button.
  4. To get a better overview, you can collapse groups in the list.


## Customizing columns 
You can show or hide columns and change the order. Your customized columns are stored in your browser, so you only have to set it up once, and it will be remembered for the next time you visit the page.
To customize columns, follow these steps:
  1. In the top right corner of the table, select the cog wheel.
  2. To hide a column, deselect it.
  3. To rearrange the order, grab the column and move it to its new position.
  4. To sort, select the column header of interest.


## Related topics 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Scenes editor - Home Assistant

Source: https://www.home-assistant.io/docs/scene/editor/

#  On this page


From the UI choose Settings which is located in the sidebar, then click on Automations & Scenes to go to the scene editor. Press the Add Scene button in the lower right corner to get started.
Choose a meaningful name for your scene.
Select all the devicesA device is a model representing a physical or logical unit that contains entities. (or entitiesAn entity represents a sensor, actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a device or a service. [Learn more] when advanced mode is enabled on your user profile) you want to include in your scene. The state of your devices will be saved, so it can be restored when you are finished creating your scene. Set the state of the devices to how you want them to be in your scene, this can be done by clicking on it and edit the state from the popup, or any other method that changes the state. On the moment you save the scene, all the states of your devices are stored in the scene. When you leave the editor the states of the devices are restored to the state from before you started editing. The menu on the top-right has options to Duplicate scene and Delete scene.
A scene can be called in automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] action and scriptsScripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on. [Learn more] using a turn on scene actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more]:
```
action: scene.turn_on
target:
 entity_id: scene.my_unique_id
```

YAML
Copy
## Updating your configuration to use the editor 
First, check that you have activated the configuration editor.
```
# Activate the configuration editor
config:
```

YAML
Copy
The scene editor reads and writes to the file scenes.yaml in the root of your folder. Currently, both the name of this file and its location are fixed. Make sure that you have set up the scene integration to read from it:
```
# Configuration.yaml example
scene: !include scenes.yaml
```

YAML
Copy
If you still want to use your old scene section, add a label to the old entry:
```
scene old:
 - name: ...
```

YAML
Copy
You can use the scene: and scene old: sections at the same time:
  * scene old: to keep your manual designed scenes
  * scene: to save the scene created by the online editor


```
scene: !include scenes.yaml
scene old: !include_dir_merge_list scenes
```

YAML
Copy
## Migrating your scenes to scenes.yaml 
If you want to migrate your old scenes to use the editor, you’ll have to copy them to scenes.yaml. Make sure that scenes.yaml remains a list! For each scene that you copy over, you’ll have to add an id. This can be any string as long as it’s unique.
For example:
```
# Example scenes.yaml entry
- id: my_unique_id # <-- Required for editor to work.
 name: Romantic
 entities:
  light.tv_back_light: on
  light.ceiling:
   state: on
   xy_color: [0.33, 0.66]
   brightness: 200
```

YAML
Copy
Note
Any comments in the YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] file will be lost and templates will be reformatted when you update a scene via the editor.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Script Syntax - Home Assistant

Source: https://www.home-assistant.io/docs/scripts/

#  On this page
Scripts are a sequence of actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] that Home Assistant will execute. Scripts are available as an entity through the standalone but can also be embedded in automationsAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] and configurations.
When the script is executed within an automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more], the trigger variable is available. See .
## Script syntax 
The script syntax basic structure is a list of key/value maps that contain actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more]. If a script contains only 1 actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more], the wrapping list can be omitted.
All actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] support an optional alias.
```
# Example script integration containing script syntax
script:
 example_script:
  sequence:
   # This is written using the Script Syntax
   - alias: "Turn on ceiling light"
    action: light.turn_on
    target:
     entity_id: light.ceiling
   - alias: "Notify that ceiling light is turned on"
    action: notify.notify
    data:
     message: "Turned on the ceiling light!"
```

YAML
Copy
## Perform an action 
Performing an action can be done in various ways. For all the different possibilities, have a look at the .
```
- alias: "Bedroom lights on"
 action: light.turn_on
 target:
  entity_id: group.bedroom
 data:
  brightness: 100
```

YAML
Copy
### Activate a scene 
Scripts may also use a shortcut syntax for activating scenesScenes capture the states you want certain entities to be. For example, a scene can specify that light A should be turned on and light B should be bright red. [Learn more] instead of calling the scene.turn_on action.
```
- scene: scene.morning_living_room
```

YAML
Copy
## Variables 
The variables actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] allows you to set/override variables that will be accessible by templates in actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] after it. See also for how to define variables accessible in the entire script.
```
- alias: "Set variables"
 variables:
  entities:
   - light.kitchen
   - light.living_room
  brightness: 100
- alias: "Control lights"
 action: light.turn_on
 target:
  entity_id: "{{ entities }}"
 data:
  brightness: "{{ brightness }}"
```

YAML
Copy
Variables can be templated.
```
- alias: "Set a templated variable"
 variables:
  blind_state_message: "The blind is {{ states('cover.blind') }}."
- alias: "Notify about the state of the blind"
 action: notify.mobile_app_iphone
 data:
  message: "{{ blind_state_message }}"
```

YAML
Copy
### Scope of variables 
The variables actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] assigns the values to previously defined variables with the same name. If a variable was not previously defined, it is assigned in the top-level (script run) scope.
```
sequence:
 # Set the people variable to a default value
 - variables:
   people: 0
 # Try to increment people if Paulus is home
 - if:
   - condition: state
    entity_id: device_tracker.paulus
    state: "home"
  then:
   - variables:
     people: "{{ people + 1 }}"
     paulus_home: true
   - action: notify.notify
    data:
     message: "There are {{ people }} people home" # "There are 1 people home"
 # Variable value is now updated
 - action: notify.notify
  data:
   message: "There are {{ people }} people home {% if paulus_home is defined %}(including Paulus){% endif %}"
   # "There are 1 people home (including Paulus)"
```

YAML
Copy
## Test a condition 
While executing a script you can add a condition in the main sequence to stop further execution. When a condition does not return true, the script will stop executing. For documentation on the many different conditions refer to the .
Note
The condition actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] only stops executing the current sequence block. When it is used inside a action, only the current iteration of the repeat loop will stop. When it is used inside a action, only the actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] within that choose will stop.
```
# If paulus is home, continue to execute the script below these lines
- alias: "Check if Paulus is home"
 condition: state
 entity_id: device_tracker.paulus
 state: "home"
```

YAML
Copy
condition can also be a list of conditions and execution will then only continue if ALL conditions return true.
```
- alias: "Check if Paulus ishome AND temperature is below 20"
 conditions:
  - condition: state
   entity_id: "device_tracker.paulus"
   state: "home"
  - condition: numeric_state
   entity_id: "sensor.temperature"
   below: 20
```

YAML
Copy
## Wait for time to pass (delay) 
Delays are useful for temporarily suspending your script and start it at a later moment. We support different syntaxes for a delay as shown below.
```
# Seconds
# Waits 5 seconds
- alias: "Wait 5s"
 delay: 5
```

YAML
Copy
```
# HH:MM
# Waits 1 hour
- delay: "01:00"
```

YAML
Copy
```
# HH:MM:SS
# Waits 1.5 minutes
- delay: "00:01:30"
```

YAML
Copy
```
# Supports milliseconds, seconds, minutes, hours, days
# Can be used in combination, at least one required
# When using milliseconds, consider that delay as *at least* X milliseconds. It won´t be exact.
# Waits 1 minute
- delay:
  minutes: 1
```

YAML
Copy
All forms accept templates.
```
# Waits however many minutes input_number.minute_delay is set to
- delay: "{{ states('input_number.minute_delay') | multiply(60) | int }}"
```

YAML
Copy
## Wait 
These actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] allow a script to wait for entities in the system to be in a certain state as specified by a template, or some event to happen as expressed by one or more triggers.
### Wait for a template 
This actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] evaluates the template, and if true, the script will continue. If not, then it will wait until it is true.
The template is re-evaluated whenever an entity ID that it references changes state. If you use non-deterministic functions like now() in the template it will not be continuously re-evaluated, but only when an entity ID that is referenced is changed. If you need to periodically re-evaluate the template, reference a sensor from the integration that will update minutely or daily.
```
# Wait until media player is stopped
- alias: "Wait until media player is stopped"
 wait_template: "{{ is_state('media_player.floor', 'stop') }}"
```

YAML
Copy
### Wait for a trigger 
This actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] can use the same triggers that are available in an automation’s trigger section. See . The script will continue whenever any of the triggers fires. All previously defined , and are passed to the trigger.
```
# Wait for a custom event or light to turn on and stay on for 10 sec
- alias: "Wait for MY_EVENT or light on"
 wait_for_trigger:
  - trigger: event
   event_type: MY_EVENT
  - trigger: state
   entity_id: light.LIGHT
   to: "on"
   for: 10
```

YAML
Copy
### Wait timeout 
With both types of waits it is possible to set a timeout after which the script will continue its execution if the condition/event is not satisfied. Timeout has the same syntax as delay, and like delay, also accepts templates.
```
# Wait for sensor to change to 'on' up to 1 minute before continuing to execute.
- wait_template: "{{ is_state('binary_sensor.entrance', 'on') }}"
 timeout: "00:01:00"
```

YAML
Copy
You can also get the script to abort after the timeout by using optional continue_on_timeout: false.
```
# Wait for IFTTT event or abort after specified timeout.
- wait_for_trigger:
  - trigger: event
   event_type: ifttt_webhook_received
   event_data:
    action: connected_to_network
 timeout:
  minutes: "{{ timeout_minutes }}"
 continue_on_timeout: false
```

YAML
Copy
Without continue_on_timeout: false the script will always continue since the default for continue_on_timeout is true.
### Wait variable 
After each time a wait completes, either because the condition was met, the event happened, or the timeout expired, the variable wait will be created/updated to indicate the result.
Variable | Description  
---|---  
wait.completed |  true if the condition was met, false otherwise  
wait.remaining | Timeout remaining, or none if a timeout was not specified  
wait.trigger | Exists only after wait_for_trigger. Contains information about which trigger fired. (See .) Will be none if no trigger happened before timeout expired  
This can be used to take different actions based on whether or not the condition was met, or to use more than one wait sequentially while implementing a single timeout overall.
```
# Take different actions depending on if condition was met.
- wait_template: "{{ is_state('binary_sensor.door', 'on') }}"
 timeout: 10
- if:
  - "{{ not wait.completed }}"
 then:
  - action: script.door_did_not_open
 else:
  - action: script.turn_on
   target:
    entity_id:
     - script.door_did_open
     - script.play_fanfare
# Wait a total of 10 seconds.
- wait_template: "{{ is_state('binary_sensor.door_1', 'on') }}"
 timeout: 10
 continue_on_timeout: false
- action: switch.turn_on
 target:
  entity_id: switch.some_light
- wait_for_trigger:
  - trigger: state
   entity_id: binary_sensor.door_2
   to: "on"
   for: 2
 timeout: "{{ wait.remaining }}"
 continue_on_timeout: false
- action: switch.turn_off
 target:
  entity_id: switch.some_light
```

YAML
Copy
## Fire an event 
This actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] allows you to fire an event. Events can be used for many things. It could trigger an automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] or indicate to another integration that something is happening. For instance, in the below example it is used to create an entry in the Activity panel.
```
- alias: "Fire LOGBOOK_ENTRY event"
 event: LOGBOOK_ENTRY
 event_data:
  name: Paulus
  message: is waking up
  entity_id: device_tracker.paulus
  domain: light
```

YAML
Copy
You can also use event_data to fire an event with custom data. This could be used to pass data to another script awaiting an event trigger.
The event_data accepts templates.
```
- event: MY_EVENT
 event_data:
  name: myEvent
  customData: "{{ myCustomVariable }}"
```

YAML
Copy
### Raise and Consume Custom Events 
The following automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] example shows how to raise a custom event called event_light_state_changed with entity_id as the event data. The actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] part could be inside a script or an automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more].
```
- alias: "Fire Event"
 triggers:
  - trigger: state
   entity_id: switch.kitchen
   to: "on"
 actions:
  - event: event_light_state_changed
   event_data:
    state: "on"
```

YAML
Copy
The following automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] example shows how to capture the custom event event_light_state_changed with an , and retrieve corresponding entity_id that was passed as the event trigger data, see for more details.
```
- alias: "Capture Event"
 triggers:
  - trigger: event
   event_type: event_light_state_changed
 actions:
  - action: notify.notify
   data:
    message: "kitchen light is turned {{ trigger.event.data.state }}"
```

YAML
Copy
## Repeat a group of actions 
This actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] allows you to repeat a sequence of other actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more]. Nesting is fully supported. There are three ways to control how many times the sequence will be run.
### Counted repeat 
This form accepts a count value. The value may be specified by a template, in which case the template is rendered when the repeat step is reached.
```
script:
 flash_light:
  mode: restart
  sequence:
   - action: light.turn_on
    target:
     entity_id: "light.{{ light }}"
   - alias: "Cycle light 'count' times"
    repeat:
     count: "{{ count|int * 2 - 1 }}"
     sequence:
      - delay: 2
      - action: light.toggle
       target:
        entity_id: "light.{{ light }}"
 flash_hallway_light:
  sequence:
   - alias: "Flash hallway light 3 times"
    action: script.flash_light
    data:
     light: hallway
     count: 3
```

YAML
Copy
### For each 
This repeat form accepts a list of items to iterate over. The list of items can be a pre-defined list, or a list created by a template.
The sequence is ran for each item in the list, and current item in the iteration is available as repeat.item.
The following example will turn a list of lights:
```
repeat:
 for_each:
  - "living_room"
  - "kitchen"
  - "office"
 sequence:
  - action: light.turn_off
   target:
    entity_id: "light.{{ repeat.item }}"
```

YAML
Copy
Other types are accepted as list items, for example, each item can be a template, or even an mapping of key/value pairs.
```
repeat:
 for_each:
  - language: English
   message: Hello World
  - language: Dutch
   message: Hallo Wereld
 sequence:
  - action: notify.phone
   data:
    title: "Message in {{ repeat.item.language }}"
    message: "{{ repeat.item.message }}!"
```

YAML
Copy
### While loop 
This form accepts a list of conditions (see for available options) that are evaluated before each time the sequence is run. The sequence will be run as long as the condition(s) evaluate to true.
```
script:
 do_something:
  sequence:
   - action: script.get_ready_for_something
   - alias: "Repeat the sequence AS LONG AS the conditions are true"
    repeat:
     while:
      - condition: state
       entity_id: input_boolean.do_something
       state: "on"
      # Don't do it too many times
      - condition: template
       value_template: "{{ repeat.index <= 20 }}"
     sequence:
      - action: script.something
```

YAML
Copy
The while also accepts a . For example:
```
- repeat:
  while: "{{ is_state('sensor.mode', 'Home') and repeat.index < 10 }}"
  sequence:
   - ...
```

YAML
Copy
### Repeat until 
This form accepts a list of conditions that are evaluated after each time the sequence is run. Therefore the sequence will always run at least once. The sequence will be run until the condition(s) evaluate to true.
```
automation:
 - triggers:
   - trigger: state
    entity_id: binary_sensor.xyz
    to: "on"
  conditions:
   - condition: state
    entity_id: binary_sensor.something
    state: "off"
  actions:
   - alias: "Repeat the sequence UNTIL the conditions are true"
    repeat:
     sequence:
      # Run command that for some reason doesn't always work
      - action: shell_command.turn_something_on
      # Give it time to complete
      - delay:
        milliseconds: 200
     until:
      # Did it work?
      - condition: state
       entity_id: binary_sensor.something
       state: "on"
```

YAML
Copy
until also accepts a . For example:
```
- repeat:
  until: "{{ is_state('device_tracker.iphone', 'home') }}"
  sequence:
   - ...
```

YAML
Copy
### Repeat loop variable 
A variable named repeat is defined within the repeat actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] (i.e., it is available inside sequence, while & until.) It contains the following fields:
field | description  
---|---  
first | True during the first iteration of the repeat sequence  
index | The iteration number of the loop: 1, 2, 3, …  
last | True during the last iteration of the repeat sequence, which is only valid for counted loops  
## If-then 
This actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] allows you to conditionally (if), based on or more (which are and combined), run a sequence of actions (then) and optionally supports running other sequence when the condition didn’t pass (else).
```
script:
 - if:
   - alias: "If no one is home"
    condition: state
    entity_id: zone.home
    state: 0
  then:
   - alias: "Then start cleaning already!"
    action: vacuum.start
    target:
     area_id: living_room
  # The `else` is fully optional and can be omitted
  else:
   - action: notify.notify
    data:
     message: "Skipped cleaning, someone is home!"
```

YAML
Copy
This actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] supports nesting, however, if you find yourself using nested if-then actions in the else part, you may want to consider using instead.
## Choose a group of actions 
This actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] allows you to select a sequence of other actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] from a list of sequences. Nesting is fully supported.
Each sequence is paired with a list of conditions. (See the for available options and how multiple conditions are handled.) The first sequence whose conditions are all true will be run. An optional default sequence can be included which will be run only if none of the sequences from the list are run.
An optional alias can be added to each of the sequences, excluding the default sequence.
The choose actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] can be used like an “if/then/elseif/then…/else” statement. The first conditions/sequence pair is like the “if/then”, and can be used just by itself. Or additional pairs can be added, each of which is like an “elif/then”. And lastly, a default can be added, which would be like the “else.”
```
# Example with "if", "elif" and "else"
automation:
 - triggers:
   - trigger: state
    entity_id: input_boolean.simulate
    to: "on"
  mode: restart
  actions:
   - choose:
     # IF morning
     - conditions:
       - condition: template
        value_template: "{{ now().hour < 9 }}"
      sequence:
       - action: script.sim_morning
     # ELIF day
     - conditions:
       - condition: template
        value_template: "{{ now().hour < 18 }}"
      sequence:
       - action: light.turn_off
        target:
         entity_id: light.living_room
       - action: script.sim_day
    # ELSE night
    default:
     - action: light.turn_off
      target:
       entity_id: light.kitchen
     - delay:
       minutes: "{{ range(1, 11)|random }}"
     - action: light.turn_off
      target:
       entity_id: all
```

YAML
Copy
conditions also accepts a . For example:
```
automation:
 - triggers:
   - trigger: state
    entity_id: input_select.home_mode
  actions:
   - choose:
     - conditions: >
       {{ trigger.to_state.state == 'Home' and
         is_state('binary_sensor.all_clear', 'on') }}
      sequence:
       - action: script.arrive_home
        data:
         ok: true
     - conditions: >
       {{ trigger.to_state.state == 'Home' and
         is_state('binary_sensor.all_clear', 'off') }}
      sequence:
       - action: script.turn_on
        target:
         entity_id: script.flash_lights
       - action: script.arrive_home
        data:
         ok: false
     - conditions: "{{ trigger.to_state.state == 'Away' }}"
      sequence:
       - action: script.left_home
```

YAML
Copy
More choose can be used together. This is the case of an IF-IF.
The following example shows how a single automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] can control entities that aren’t related to each other but have in common the same trigger.
When the sun goes below the horizon, the porch and garden lights must turn on. If someone is watching the TV in the living room, there is a high chance that someone is in that room, therefore the living room lights have to turn on too. The same concept applies to the studio room.
```
# Example with "if" and "if"
automation:
 - alias: "Turn lights on when the sun gets dim and if some room is occupied"
   triggers:
    - trigger: numeric_state
     entity_id: sun.sun
     attribute: elevation
     below: 4
   actions:
    # This must always apply
    - action: light.turn_on
     data:
      brightness: 255
      color_temp: 366
     target:
      entity_id:
       - light.porch
       - light.garden
    # IF a entity is ON
    - choose:
      - conditions:
        - condition: state
         entity_id: binary_sensor.livingroom_tv
         state: "on"
       sequence:
        - action: light.turn_on
         data:
          brightness: 255
          color_temp: 366
         target:
          entity_id: light.livingroom
     # IF another entity not related to the previous, is ON
    - choose:
      - conditions:
        - condition: state
         entity_id: binary_sensor.studio_pc
         state: "on"
       sequence:
        - action: light.turn_on
         data:
          brightness: 255
          color_temp: 366
         target:
          entity_id: light.studio
```

YAML
Copy
## Grouping actions 
The sequence actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] allows you to group multiple actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] together. Each action will be executed in order, meaning the next action will only be executed after the previous action has been completed.
Grouping actions in a sequence can be useful when you want to be able to collapse related groups in the user interface for organizational purposes.
Combined with the action, it can also be used to run multiple groups of actions in a sequence in parallel.
In the example below, two separate groups of actions are executed in sequence, one for turning on devices, the other for sending notifications. Each group of actions is executed in order, this includes the actions in each group and the groups themselves. In total, four actions are executed, one after the other.
```
automation:
 - triggers:
   - trigger: state
    entity_id: binary_sensor.motion
    to: "on"
  actions:
   - alias: "Turn on devices"
    sequence:
     - action: light.turn_on
      target:
       entity_id: light.ceiling
     - action: siren.turn_on
      target:
       entity_id: siren.noise_maker
   - alias: "Send notifications"
    sequence:
     - action: notify.person1
      data:
       message: "The motion sensor was triggered!"
     - action: notify.person2
      data:
       message: "Oh oh, someone triggered the motion sensor..."
```

YAML
Copy
## Parallelizing actions 
By default, all sequences of actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] in Home Assistant run sequentially. This means the next actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] is started after the current action has been completed.
This is not always needed, for example, if the sequence of actions doesn’t rely on each other and order doesn’t matter. For those cases, the parallel action can be used to run the actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] in the sequence in parallel, meaning all the actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] are started at the same time.
The following example shows sending messages out at the same time (in parallel):
```
automation:
 - triggers:
   - trigger: state
    entity_id: binary_sensor.motion
    to: "on"
  actions:
   - parallel:
     - action: notify.person1
      data:
       message: "These messages are sent at the same time!"
     - action: notify.person2
      data:
       message: "These messages are sent at the same time!"
```

YAML
Copy
It is also possible to run a group of actions sequentially inside the parallel actions. The example below demonstrates that:
```
script:
 example_script:
  sequence:
   - parallel:
     - sequence:
       - wait_for_trigger:
         - trigger: state
          entity_id: binary_sensor.motion
          to: "on"
       - action: notify.person1
        data:
         message: "This message awaited the motion trigger"
     - action: notify.person2
      data:
       message: "I am sent immediately and do not await the above action!"
```

YAML
Copy
Warning
Running actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] in parallel can be helpful in many cases, but use it with caution and only if you need it.
There are some caveats (see below) when using parallel actions.
While it sounds attractive to parallelize, most of the time, just the regular sequential actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] will work just fine.
Some of the caveats of running actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] in parallel:
  * There is no order guarantee. The actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] will be started in parallel, but there is no guarantee that they will be completed in the same order.
  * If one actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] fails or errors, the other actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] will keep running until they too have finished or errored.
  * Variables created/modified in one parallelized actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] can conflict with variables from another parallelized actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more]. Make sure to give them distinct names to prevent that.


## Stopping a script sequence 
It is possible to halt a script sequence at any point and return script responses using the stop actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more].
The stop actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] takes a text as input explaining the reason for halting the sequence. This text will be logged and shows up in the automationsAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] and script traces.
stop can be useful to halt a script halfway through a sequence when, for example, a condition is not met.
```
- stop: "Stop running the rest of the sequence"
```

YAML
Copy
To return a response from a script, use the response_variable option. This option expects the name of the variable that contains the data to return. The response data must contains a mapping of key/value pairs.
```
- stop: "Stop running the rest of the sequence"
 response_variable: "my_response_variable"
```

YAML
Copy
There is also an error option, to indicate we are stopping because of an unexpected error. It stops the sequence as well, but marks the automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] or script as failed to run.
```
- stop: "Well, that was unexpected!"
 error: true
```

YAML
Copy
## Continuing on error 
By default, a sequence of actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] will be halted when one of the actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] in that sequence encounters an error. The automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] or script will be halted, an error is logged, and the automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] or script run is marked as errored.
Sometimes these errors are expected, for example, because you know the action you perform can be problematic at times, and it doesn’t matter if it fails. You can set continue_on_error for those cases on such an actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more].
The continue_on_error is available on all actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] and is set to false. You can set it to true if you’d like to continue the actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] sequence, regardless of whether that actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] encounters an error.
The example below shows the continue_on_error set on the first actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more]. If it encounters an error; it will continue to the next actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more].
```
- alias: "If this one fails..."
 continue_on_error: true
 action: notify.super_unreliable_service_provider
 data:
  message: "I'm going to error out..."
- alias: "This one will still run!"
 action: persistent_notification.create
 data:
  title: "Hi there!"
  message: "I'm fine..."
```

YAML
Copy
Please note that continue_on_error will not suppress/ignore misconfiguration or errors that Home Assistant does not handle.
## Disabling an action 
Every individual actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] in a sequence can be disabled, without removing it. To do so, add enabled: false to the actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more]. For example:
```
# Example script with a disabled action
script:
 example_script:
  sequence:
   # This action will not run, as it is disabled.
   # The message will not be sent.
   - enabled: false
    alias: "Notify that the ceiling light is being turned on"
    action: notify.notify
    data:
     message: "Turning on the ceiling light!"
   # This action will run, as it is not disabled
   - alias: "Turn on the ceiling light"
    action: light.turn_on
    target:
     entity_id: light.ceiling
```

YAML
Copy
Actions can also be disabled based on limited templates or blueprint inputs.
```
blueprint:
 input:
  input_boolean:
   name: Boolean
   selector:
    boolean:
 actions:
  - delay: 0:35
   enabled: !input input_boolean
```

YAML
Copy
## Respond to a conversation 
The set_conversation_response script actionActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] allows returning a custom response when an automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] is triggered by a conversation engine, for example a voice assistant. The conversation response can be templated.
```
# Example of a templated conversation response resulting in "Testing 123"
- variables:
  my_var: "123"
- set_conversation_response: "{{ 'Testing ' + my_var }}":
```

YAML
Copy
The response is handed to the conversation engine when the automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] finishes. If the set_conversation_response is executed multiple times, the most recent response will be handed to the conversation engine. To clear the response, set it to None:
```
# Example of a clearing a conversation response
set_conversation_response: ~
```

YAML
Copy
If the automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] was not triggered by a conversation engine, the response will not be used by anything.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Scenes - Home Assistant

Source: https://www.home-assistant.io/docs/scene/

#  On this page
You can create scenes that capture the states you want certain entities to be. For example, a scene can specify that light A should be turned on and light B should be bright red. Scenes are available as an entity through the standalone but can also be embedded in automationsAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] and scriptsScripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on. [Learn more].
```
# Example configuration.yaml entry
scene:
 - name: Romantic
  entities:
   light.tv_back_light: "on"
   light.ceiling:
    state: "on"
    xy_color: [0.33, 0.66]
    brightness: 200
 - name: Movies
  entities:
   light.tv_back_light:
    state: "on"
    brightness: 125
   light.ceiling: off
   media_player.sony_bravia_tv:
    state: "on"
    source: HDMI 1
```

YAML
Copy
## How to configure your scene 
In the scene you define in your YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] files, please ensure you use all required parameters as listed below.
####  Configuration Variables 
name string Required 
Friendly name of the scene. 
entities list Required 
Entities to control and their desired state. 
As you can see, there are two ways to define the states of each entity_id:
  * Define the state directly with the entity. Be aware, that state needs to be defined.
  * Define a complex state with its attributes. You can see all attributes available for a particular entity under developer-tools -> state.


Scenes can be activated using the action scene.turn_on (there is no ‘scene.turn_off’ action).
```
# Example automation
automation:
 triggers:
  - trigger: state
   entity_id: device_tracker.sweetheart
   from: "not_home"
   to: "home"
 actions:
  - action: scene.turn_on
   target:
    entity_id: scene.romantic
```

YAML
Copy
## Applying a scene without defining it 
With the scene.apply action you are able to apply a scene without first defining it via configuration. Instead, you pass the states as part of the data. The format of the data is the same as the entities field in a configuration.
```
# Example automation
automation:
 triggers:
  - trigger: state
   entity_id: device_tracker.sweetheart
   from: "not_home"
   to: "home"
 actions:
  - action: scene.apply
   data:
    entities:
     light.tv_back_light:
      state: "on"
      brightness: 100
     light.ceiling: off
     media_player.sony_bravia_tv:
      state: "on"
      source: "HDMI 1"
```

YAML
Copy
## Using scene transitions 
Both the scene.apply and scene.turn_on actions support setting a transition, which enables you to smoothen the transition to the scene.
This is an example of an automation that sets a romantic scene, in which the light will transition to the scene in 2.5 seconds.
```
# Example automation
automation:
 triggers:
  - trigger: state
   entity_id: device_tracker.sweetheart
   from: "not_home"
   to: "home"
 actions:
  - action: scene.turn_on
   target:
    entity_id: scene.romantic
   data:
    transition: 2.5
```

YAML
Copy
Transitions are currently only support by lights, which in their turn, have to support it as well. However, the scene itself does not have to consist of only lights to have a transition set.
## Reloading scenes 
Whenever you make a change to your scene configuration, you can call the scene.reload action to reload the scenes.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Conditions - Home Assistant

Source: https://www.home-assistant.io/docs/scripts/conditions/

#  On this page
Conditions can be used within a scriptScripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on. [Learn more] or automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] to prevent further execution. When a condition evaluates true, the script or automation will be executed. If any other value is returned, the script or automation stops executing. A condition will look at the system at that moment. For example, a condition can test if a switch is currently turned on or off.
Unlike a triggerA trigger is a set of values or conditions of a platform that are defined to cause an automation to run. [Learn more], which is always or, conditions are and by default - all conditions have to be true.
All conditions support an optional alias.
## Logical conditions 
### AND condition 
Test multiple conditions in one condition statement. Passes if all embedded conditions are true.
```
conditions:
 - alias: "Paulus home AND temperature below 20"
  condition: and
  conditions:
   - condition: state
    entity_id: "device_tracker.paulus"
    state: "home"
   - condition: numeric_state
    entity_id: "sensor.temperature"
    below: 20
```

YAML
Copy
If you do not want to combine AND and OR conditions, you can list them sequentially.
The following configuration works the same as the one listed above:
```
conditions:
 - condition: state
  entity_id: "device_tracker.paulus"
  state: "home"
 - condition: numeric_state
  entity_id: "sensor.temperature"
  below: 20
```

YAML
Copy
Currently you need to format your conditions like this to be able to edit them using the .
The AND condition also has a shorthand form. The following configuration works the same as the ones listed above:
```
conditions:
 alias: "Paulus home AND temperature below 20"
 - and:
  - condition: state
   entity_id: "device_tracker.paulus"
   state: "home"
  - condition: numeric_state
   entity_id: "sensor.temperature"
   below: 20
```

YAML
Copy
### OR condition 
Test multiple conditions in one condition statement. Passes if any embedded condition is true.
```
conditions:
 - alias: "Paulus home OR temperature below 20"
  condition: or
  conditions:
   - condition: state
    entity_id: "device_tracker.paulus"
    state: "home"
   - condition: numeric_state
    entity_id: "sensor.temperature"
    below: 20
```

YAML
Copy
The OR condition also has a shorthand form. The following configuration works the same as the one listed above:
```
conditions:
 - alias: "Paulus home OR temperature below 20"
  or:
   - condition: state
    entity_id: "device_tracker.paulus"
    state: "home"
   - condition: numeric_state
    entity_id: "sensor.temperature"
    below: 20
```

YAML
Copy
### Mixed AND and OR conditions 
Test multiple AND and OR conditions in one condition statement. Passes if any embedded condition is true. This allows you to mix several AND and OR conditions together.
```
conditions:
 - condition: and
  conditions:
   - condition: state
    entity_id: "device_tracker.paulus"
    state: "home"
   - condition: or
    conditions:
     - condition: state
      entity_id: sensor.weather_precip
      state: "rain"
     - condition: numeric_state
      entity_id: "sensor.temperature"
      below: 20
```

YAML
Copy
Or in shorthand form:
```
conditions:
 - and:
  - condition: state
   entity_id: "device_tracker.paulus"
   state: "home"
  - or:
   - condition: state
    entity_id: sensor.weather_precip
    state: "rain"
   - condition: numeric_state
    entity_id: "sensor.temperature"
    below: 20
```

YAML
Copy
### NOT condition 
Test multiple conditions in one condition statement. Passes if all embedded conditions are not true.
```
conditions:
 - alias: "Paulus not home AND alarm not disarmed"
  condition: not
  conditions:
   - condition: state
    entity_id: device_tracker.paulus
    state: "home"
   - condition: state
    entity_id: alarm_control_panel.home_alarm
    state: "disarmed"
```

YAML
Copy
The NOT condition also has a shorthand form. The following configuration works the same as the one listed above:
```
conditions:
 alias: "Paulus not home AND alarm not disarmed"
 not:
  - condition: state
   entity_id: device_tracker.paulus
   state: "home"
  - condition: state
   entity_id: alarm_control_panel.home_alarm
   state: disarmed
```

YAML
Copy
## Numeric state condition 
This type of condition attempts to parse the state of the specified entity or the attribute of an entity as a number, and triggers if the value matches the thresholds (strictly below/above, so equal excluded).
If both below and above are specified, both tests have to pass.
```
conditions:
 - alias: "Temperature between 17 and 25 degrees"
  condition: numeric_state
  entity_id: sensor.temperature
  above: 17
  below: 25
```

YAML
Copy
You can optionally use a value_template to process the value of the state before testing it.
```
conditions:
 - condition: numeric_state
  entity_id: sensor.temperature
  above: 17
  below: 25
  # If your sensor value needs to be adjusted
  value_template: "{{ float(state.state) + 2 }}"
```

YAML
Copy
It is also possible to test the condition against multiple entities at once. The condition will pass if all entities match the thresholds.
```
conditions:
 - condition: numeric_state
  entity_id:
   - sensor.kitchen_temperature
   - sensor.living_room_temperature
  below: 18
```

YAML
Copy
Alternatively, the condition can test against a state attribute. The condition will pass if the attribute value of the entity matches the thresholds.
```
conditions:
 - condition: numeric_state
  entity_id: climate.living_room_thermostat
  attribute: temperature
  above: 17
  below: 25
```

YAML
Copy
Number helpers (input_number entities), number, sensor, and zone entities that contain a numeric value, can be used in the above and below options to make the condition more dynamic.
```
conditions:
 - condition: numeric_state
  entity_id: climate.living_room_thermostat
  attribute: temperature
  above: input_number.temperature_threshold_low
  below: input_number.temperature_threshold_high
```

YAML
Copy
## State condition 
Tests if an entity has a specified state.
```
conditions:
 - alias: "Paulus not home for an hour and a bit"
  condition: state
  entity_id: device_tracker.paulus
  state: "not_home"
  # optional: Evaluates to true only if state was this for last X time.
  for:
   hours: 1
   minutes: 10
   seconds: 5
```

YAML
Copy
It is also possible to test the condition against multiple entities at once. The condition will pass if all entities match the state.
```
conditions:
 - condition: state
  entity_id:
   - light.kitchen
   - light.living_room
  state: "on"
```

YAML
Copy
Instead of matching all, it is also possible if one of the entities matches. In the following example the condition will pass if any entity matches the state.
```
conditions:
 - condition: state
  entity_id:
   - binary_sensor.motion_sensor_left
   - binary_sensor.motion_sensor_right
  match: any
  state: "on"
```

YAML
Copy
Testing if an entity is matching a set of possible conditions; The condition will pass if the entity matches one of the states given.
```
conditions:
 - condition: state
  entity_id: alarm_control_panel.home
  state:
   - "armed_away"
   - "armed_home"
```

YAML
Copy
Or, combine multiple entities with multiple states. In the following example, both media players need to be either paused or playing for the condition to pass.
```
conditions:
 - condition: state
  entity_id:
   - media_player.living_room
   - media_player.kitchen
  state:
   - "playing"
   - "paused"
```

YAML
Copy
Alternatively, the condition can test against a state attribute. The condition will pass if the attribute matches the given state.
```
conditions:
 - condition: state
  entity_id: climate.living_room_thermostat
  attribute: fan_mode
  state: "auto"
```

YAML
Copy
Finally, the state option accepts helper entities (also known as input_* entities). The condition will pass if the state of the entity matches the state of the given helper entity.
```
conditions:
 - condition: state
  entity_id: alarm_control_panel.home
  state: input_select.guest_mode
```

YAML
Copy
You can also use templates in the for option.
```
conditions:
 - condition: state
  entity_id: device_tracker.paulus
  state: "home"
  for:
   minutes: "{{ states('input_number.lock_min')|int }}"
   seconds: "{{ states('input_number.lock_sec')|int }}"
```

YAML
Copy
The for template(s) will be evaluated when the condition is tested.
### Sun condition 
#### Sun state condition 
The sun state can be used to test if the sun has set or risen.
```
conditions:
 - alias: "Sun up"
  condition: state # 'day' condition: from sunrise until sunset
  entity_id: sun.sun
  state: "above_horizon"
```

YAML
Copy
```
conditions:
 - alias: "Sun down"
  condition: state # from sunset until sunrise
  entity_id: sun.sun
  state: "below_horizon"
```

YAML
Copy
### Sun elevation condition 
The sun elevation can be used to test if the sun has set or risen, it is dusk, it is night, etc. when a trigger occurs. For an in-depth explanation of sun elevation, see .
```
conditions:
 - condition: and # 'twilight' condition: dusk and dawn, in typical locations
  conditions:
   - condition: template
    value_template: "{{ state_attr('sun.sun', 'elevation') < 0 }}"
   - condition: template
    value_template: "{{ state_attr('sun.sun', 'elevation') > -6 }}"
```

YAML
Copy
```
conditions:
 condition: template # 'night' condition: from dusk to dawn, in typical locations
 value_template: "{{ state_attr('sun.sun', 'elevation') < -6 }}"
```

YAML
Copy
### Sunset/sunrise condition 
The sun condition can also test if the sun has already set or risen when a trigger occurs. The before and after keys can only be set to sunset or sunrise. They have a corresponding optional offset value (before_offset, after_offset) that can be added, similar to the .
Note that if only before key is used, the condition will be true from midnight until sunrise/sunset. If only after key is used, the condition will be true from sunset/sunrise until midnight. If both before: sunrise and after: sunset keys are used, the condition will be true from midnight until sunrise and from sunset until midnight. If both after: sunrise and before: sunset keys are used, the condition will be true from sunrise until sunset.
Tip
The sunset/sunrise conditions do not work in locations inside the polar circles, and also not in locations with a highly skewed local time zone. In those cases it is advised to use conditions evaluating the solar elevation instead of the before/after sunset/sunrise conditions.
This is an example of 1 hour offset before sunset:
```
conditions:
 - condition: sun
  after: sunset
  after_offset: "-01:00:00"
```

YAML
Copy
This is ‘when dark’ - equivalent to a state condition on sun.sun of below_horizon:
```
conditions:
 - condition: sun
  after: sunset
  before: sunrise
```

YAML
Copy
This is ‘when light’ - equivalent to a state condition on sun.sun of above_horizon:
```
conditions:
 - condition: sun
  after: sunrise
  before: sunset
```

YAML
Copy
A visual timeline is provided below, showing an example of when these conditions are true. In this chart, sunrise is at 6:00, and sunset is at 18:00 (6:00 PM). The green areas of the chart indicate when the specified conditions are true.
## Template condition 
The template condition tests if the renders a value equal to true. This is achieved by having the template result in a true boolean expression or by having the template render True.
```
conditions:
 - alias: "Iphone battery above 50%"
  condition: template
  value_template: "{{ (state_attr('device_tracker.iphone', 'battery_level')|int) > 50 }}"
```

YAML
Copy
Within an automation, template conditions also have access to the trigger variable as .
### Template condition shorthand notation 
The template condition has a shorthand notation that can be used to make your scripts and automations shorter.
For example:
```
conditions: "{{ (state_attr('device_tracker.iphone', 'battery_level')|int) > 50 }}"
```

YAML
Copy
Or in a list of conditions, allowing to use existing conditions as described in this chapter and one or more shorthand template conditions
```
conditions:
 - "{{ (state_attr('device_tracker.iphone', 'battery_level')|int) > 50 }}"
 - condition: state
  entity_id: alarm_control_panel.home
  state: armed_away
 - "{{ is_state('device_tracker.iphone', 'away') }}"
```

YAML
Copy
This shorthand notation can be used everywhere in Home Assistant where conditions are accepted. For example, in , and conditions:
```
conditions:
 - condition: or
  conditions:
   - "{{ is_state('device_tracker.iphone', 'away') }}"
   - condition: numeric_state
    entity_id: "sensor.temperature"
    below: 20
```

YAML
Copy
It’s also supported in the repeat action’s while or until option, or in a choose action’s conditions option:
```
- while: "{{ is_state('sensor.mode', 'Home') and repeat.index < 10 }}"
 sequence:
  - ...
```

YAML
Copy
```
- choose:
  - conditions: "{{ is_state('sensor.mode', 'Home') and repeat.index < 10 }}"
   sequence:
    - ...
```

YAML
Copy
It’s also supported in script or automation condition actions:
```
- condition: "{{ is_state('device_tracker.iphone', 'away') }}"
```

YAML
Copy
## Time condition 
The time condition can test if it is after a specified time, before a specified time or if it is a certain day of the week.
```
conditions:
 - alias: "Time 15~02"
  condition: time
  # At least one of the following is required.
  after: "15:00:00"
  before: "02:00:00"
  weekday:
   - mon
   - wed
   - fri
```

YAML
Copy
Valid values for weekday are mon, tue, wed, thu, fri, sat, sun. Note that if only before key is used, the condition will be true from midnight until the specified time. If only after key is used, the condition will be true from the specified time until midnight. Time condition windows can span across the midnight threshold if both after and before keys are used. In the example above, the condition window is from 3pm to 2am.
Tip
A better weekday condition could be by using the .
For the after and before options a time helper (input_datetime entity), a time entity, or another sensor entity containing a timestamp with the “timestamp” device class, can be used instead.
```
conditions:
 - alias: "Example referencing a time helper"
  condition: time
  after: input_datetime.house_silent_hours_start
  before: input_datetime.house_silent_hours_end
 - alias: "Example referencing a time entity"
  before: time.dnd_start
 - alias: "Example referencing another sensor"
  after: sensor.groceries_delivery_time
```

YAML
Copy
Note
Note that the time condition only takes the time into account. If a referenced sensor or helper entity contains a timestamp with a date, the date part is fully ignored.
## Trigger condition 
The trigger condition can test if an automation was triggered by a certain trigger, identified by the trigger’s id.
```
conditions:
 - condition: trigger
  id: event_trigger
```

YAML
Copy
For a trigger identified by its index, both a string and integer is allowed:
```
conditions:
 - condition: trigger
  id: "0"
```

YAML
Copy
```
conditions:
 - condition: trigger
  id: 0
```

YAML
Copy
It is possible to give a list of triggers:
```
conditions:
 - condition: trigger
  id:
   - event_1_trigger
   - event_2_trigger
```

YAML
Copy
## Zone condition 
Zone conditions test if an entity is in a certain zone. For zone automation to work, you need to have set up a device tracker platform that supports reporting GPS coordinates.
```
conditions:
 - alias: "Paulus at home"
  condition: zone
  entity_id: device_tracker.paulus
  zone: zone.home
```

YAML
Copy
It is also possible to test the condition against multiple entities at once. The condition will pass if all entities are in the specified zone.
```
conditions:
 - condition: zone
  entity_id:
   - device_tracker.frenck
   - device_tracker.daphne
  zone: zone.home
```

YAML
Copy
Testing if an entity is matching a set of possible zones; The condition will pass if the entity is in one of the zones.
```
conditions:
 - condition: zone
  entity_id: device_tracker.paulus
  state:
   - zone.home
   - zone.work
```

YAML
Copy
Or, combine multiple entities with multiple zones. In the following example, both entities need to be either in the home or the work zone for the condition to pass.
```
conditions:
 condition: zone
 entity_id:
  - device_tracker.frenck
  - device_tracker.daphne
 state:
  - zone.home
  - zone.work
```

YAML
Copy
## Examples 
```
conditions:
 - condition: numeric_state
  entity_id: sun.sun
  value_template: "{{ state.attributes.elevation }}"
  below: 1
 - condition: state
  entity_id: light.living_room
  state: "off"
 - condition: time
  before: "23:00:00"
  after: "14:00:00"
 - condition: state
  entity_id: script.light_turned_off_5min
  state: "off"
```

YAML
Copy
## Disabling a condition 
Every individual condition can be disabled, without removing it. To do so, add enabled: false to the condition configuration.
This can be useful if you want to temporarily disable a condition, for example, for testing. A disabled condition will behave as if it were removed.
For example:
```
# This condition will always pass, as it is disabled.
conditions:
 - enabled: false
  condition: state
  entity_id: sun.sun
  state: "above_horizon"
```

YAML
Copy
Conditions can also be disabled based on limited templates or blueprint inputs.
```
blueprint:
 input:
  input_boolean:
   name: Boolean
   selector:
    boolean:
  input_number:
   name: Number
   selector:
    number:
     min: 0
     max: 100
 trigger_variables:
  _enable_number: !input input_number
 conditions:
  - condition: state
   entity_id: sun.sun
   state: "above_horizon"
   enabled: !input input_boolean
  - condition: state
   entity_id: sun.sun
   state: "below_horizon"
   enabled: "{{ _enable_number < 50 }}"
```

YAML
Copy
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Performing actions - Home Assistant

Source: https://www.home-assistant.io/docs/scripts/perform-actions/

#  On this page
Various integrations allow performing actionsActions are used in several places in Home Assistant. As part of a script or automation, actions define what is going to happen once a trigger is activated. In scripts, an action is called sequence. [Learn more] when a certain event occurs. The most common one is performing an action when an automation triggerA trigger is a set of values or conditions of a platform that are defined to cause an automation to run. [Learn more] happens. But an action can also be called from a scriptScripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on. [Learn more], a dashboard, or via voice command devices such as Amazon Echo.
The configuration options to perform action are the same between all integrations and are described on this page.
Examples on this page will be given as part of an automation integration configuration but different approaches can be used for other integrations too.
Tip
Use the “Actions” tab under Developer tools to discover available actions.
### The basics 
Perform the action homeassistant.turn_on on the entityAn entity represents a sensor, actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a device or a service. [Learn more] group.living_room. This will turn all members of group.living_room on. You can also use entity_id: all and it will turn on all possible entities.
```
action: homeassistant.turn_on
target:
 entity_id: group.living_room
```

YAML
Copy
### Targeting areas and devices 
Instead of targeting an entity, you can also target an areaAn area in Home Assistant is a logical grouping of devices and entities that are meant to match areas (or rooms) in the physical world: your home. For example, the living room area groups devices and entities in your living room. [Learn more] or deviceA device is a model representing a physical or logical unit that contains entities.. Or a combination of these. This is done with the target key.
A target is a map that contains at least one of the following: area_id, device_id, entity_id. Each of these can be a list. The values should be lower-cased.
The following example uses a single action to turn on the lights in the living room area, 2 additional light devices and 2 additional light entities:
```
action: light.turn_on
target:
 area_id: living_room
 device_id:
  - ff22a1889a6149c5ab6327a8236ae704
  - 52c050ca1a744e238ad94d170651f96b
 entity_id:
  - light.hallway
  - light.landing
```

YAML
Copy
### Passing data to the action 
You can also specify other parameters beside the entity to target. For example, the light.turn_on action allows specifying the brightness.
```
action: light.turn_on
target:
 entity_id: group.living_room
data:
 brightness: 120
 rgb_color: [255, 0, 0]
```

YAML
Copy
A full list of the parameters for an action can be found on the documentation page of each integration, in the same way as it’s done for the light.turn_on .
### Use templates to decide which action to perform 
You can use support to dynamically choose which action to perform. For example, you can perform a certain action based on if a light is on.
```
action: >
 {% if states('sensor.temperature') | float > 15 %}
  switch.turn_on
 {% else %}
  switch.turn_off
 {% endif %}
entity_id: switch.ac
```

YAML
Copy
### Using the Actions developer tool 
You can use the Actions developer tool to test data to pass in an action. For example, you may test turning on or off a ‘group’ (See for more info)
To turn a group on or off, pass the following info:
  * Domain: homeassistant 
  * Action: turn_on 
  * Action data: { "entity_id": "group.kitchen" } 


### Use templates to determine the attributes 
Templates can also be used for the data that you pass to the action.
```
action: thermostat.set_temperature
target:
 entity_id: >
  {% if is_state('device_tracker.paulus', 'home') %}
   thermostat.upstairs
  {% else %}
   thermostat.downstairs
  {% endif %}
data:
 temperature: "{{ 22 - distance(states.device_tracker.paulus) }}"
```

YAML
Copy
You can use a template returning a native dictionary as well, which is useful if the attributes to be set depend on the situation.
```
action: climate.set_temperature
data: >
 {% if states('sensor.temperature_living') < 19 %}
  {"hvac_mode": "heat", "temperature": 19 }
 {% else %}
  {"hvac_mode": "auto" }
 {% endif %}
```

YAML
Copy
### Use templates to handle response data 
Some actions may respond with data that can be used in automation. This data is called action response data. Action response data is typically used for data that is dynamic or large and which may not be suited for use in entity state. Examples of action response data are upcoming calendar events for the next week or detailed driving directions.
Templates can also be used for handling response data. The action can specify a response_variable. This is the that contains the response data. You can define any name for your response_variable. This example performs an action and stores the response in the variable called agenda.
```
action: calendar.get_events
target:
 entity_id: calendar.school
data:
 duration:
  hours: 24
response_variable: agenda
```

YAML
Copy
You may then use the response data in the variable agenda in another action in the same script. The example below sends a notification using the response data.
Important
Which data fields can be used in an action depends on the type of notification that is used.
```
action: notify.gmail_com
data:
 target: "gduser1@workspacesamples.dev"
 title: "Daily agenda for {{ now().date() }}"
 message: >-
  Your agenda for today:
  <p>
  {% for event in agenda['calendar.school'].events %}
  {{ event.start}}: {{ event.summary }}<br>
  {% endfor %}
  </p>
```

YAML
Copy
### homeassistant actions 
There are four homeassistant actions that aren’t tied to any single domain, these are:
Complete action details and examples can be found on the page.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Tools - Home Assistant

Source: https://www.home-assistant.io/docs/tools/

#  On this page
Home Assistant ships a couple of helpers for the command-line and the frontend which simplify common tasks, are helping with migrations, and ensure that Home Assistant runs properly.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Editing the Documentation and Creating a Pull Request on Github - Community Guides - Home Assistant Community

Source: https://community.home-assistant.io/t/editing-the-documentation-and-creating-a-pull-request-on-github/9573

  * More 


Categories 
Tags 
​  ​ 
# 
You have selected 0 posts. 
8.9k views  42 likes  8 links  12 users 
1 / 17 
Jan 2017 
silvrr
10
It is easy to help keep our documentation up to date and it is a simple way you can contribute to the Home Assistant project.
First go to and sign up for an account. Its quick free and easy. Sign up and sign in.
At the bottom of every documentation page there is an Edit button for you to click.
When you click that link you will be brought to a new page with contents of the page you wanted to edit. In the upper right there is a pencil icon, click it to edit the page.
On the resulting page you can edit the text. Use the existing content and reference the existing page for figuring out how to edit the content. Usually the page just needs some tweaking so you don’t need to start over, just add on or delete some text.
If you are making a large change/new page be sure to read the documentation standards before getting started. See: 
When you are done, click the green Commit changes button.
Then fill in some detail about your change in the pop-up window and click the green Propose changes button
On the next page, click the green Create Pull Request button
On the next page add any additional comments and fill out the two checklists. Then click green Create Pull Request button.
You’re Done! You just submitted your first pull request and contributed to improving Home Assistant!
If this is your first time submitting you likely will need to sign the CLA. This is easy to do and you will either brought straight to it or receive an e-mail to complete this step. Its as simple as reading and clicking another box.
From here you will get an e-mail stating that your pull request was submitted and it will identify some reviewers based on who has worked on the page in the past. You will continue to get e-mails with updates on the status as needed. Eventually you will get one that it has been merged and your changes will go live sometime after.
If all of this seems too much then click the feedback link at the bottom of the documentation page instead and provide details of what you think needs fixing.
You will need a github account for this too (see top of this guide).
8.9k views  42 likes  8 links  12 users 
DanielhiversenDaniel Høyer
Great, I think that would be great to have in documentation
Zen
I agree. This is just the sort of thing that we needed to have written up. Excellent work, !
rpiteraRobert Pitera
- I’m not sure if you realized the meta joke you just made.  Wouldn’t adding this to the documentation be roughly the same process?
- Thanks so much for this!
silvrr
Great example of why everyone needs to submit pull requests. In making this little tutorial I made a few tweaks to the yeelight component as shown above to provide the example. As I was paying more attention to making the tutorial than the config example there were errors in it. (spacing and and a missed colon )
to save the day! He submitted a Pull Request and fixed the errors which should go live shortly. This just goes to show that we need everyone to be helping with the documentation. Also I need to focus on one thing at a time so I don’t make people frustrated with my config errors. (Sorry )
LeeJSLee
My pleasure!
mark.carlineMark
This is great. I have lots of my own documents I’ve stored at home which I’ve used to record how I’ve setup some zwave specific devices so I’ll see about moving them here.


2 years later 
klaasnicolaasKlaas Schoute
one picture is not loading
silvrr
Thanks, I think this needs an update anyway. Added to my todo list.
2 months later 
MagnaScott
Might want to add what to do if you have clicked “Propose file change”, but then notice something needs to be changed (say I noticed a mistake in my edit), prior to clicking “Create pull request”. In other words, go back to editing before creating the pull request.
26 days later 
silvrr
OK, I updated the first post with the current workflow. I wasn’t getting this done so I did it as I was making an edit and noticed an issue.
Future items to add:
  1. Creating a github account?
  2. CLA signing process?
  3. Editing after you have clicked “Propose file change”


If anyone is going through the steps and wants to post the steps/screenshots I will either add them to my post or link to your post.
1 year later 
DavidFW1960David
You can edit them but the changes need to be approved and merged. It’s not the wild Wild West.
2 months later 
Trevor
Thanks just created my first edit
Trevor
…and it was rejected for being classed as duplicating an existing example.
There will be no Hello World code snippets in this documentation 
4 years later 
tom_l
Updated December 2024.
7 months later 
donburch888Don Burch
The link to the documentation standards in the original post seems to have gone 404. After a little research I think that https://developers.home-assistant.io/docs/en/documentation_standards.html should be https://developers.home-assistant.io/docs/documenting/standards/
tom_l
You can fix it:
Reply 
###  New & Unread Topics 
Topic list, column headers with buttons are sortable. Topic  |  Replies  |  Views  |  Activity   
---|---|---|---  
Broadlink RM4 mini IP - How to fix “Setup Failed”  |  |  2.1k  |   
The correct silly-walk to set up InfluxDB as of August 2025  |  |  430  |   
Influxdb: making a includes only configuration a step easier using labels  |  |  153  |   
Tado Radiator Valves - replacing Tado cloud  |  |  390  |   
How to set up Tailscale Funnel to securely access Home Assistant from anywhere for free  |  |  1.6k  |   
###  Want to read more? Browse other topics in or . 
Invalid date  Invalid date 



## check_config - Home Assistant

Source: https://www.home-assistant.io/docs/tools/check_config/

#  On this page


Test any changes to your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file before launching Home Assistant. This script allows you to test changes without the need to restart Home Assistant.
```
hass --script check_config
```

Bash
Copy
The script has further options like checking configuration files which are not located in the default directory or showing your secrets for debugging.
```
$ hass --script check_config -h
usage: hass [-h] [--script {check_config}] [-c CONFIG] [-i [INFO]] [-f] [-s] [--json] [--fail-on-warnings]
Check Home Assistant configuration.
optional arguments:
 -h, --help      show this help message and exit
 --script {check_config}
 -c CONFIG, --config CONFIG
            Directory that contains the Home Assistant
            configuration
 -i [INFO], --info [INFO]
            Show a portion of the config
 -f, --files      Show used configuration files
 -s, --secrets     Show secret information
 --json        Output JSON format
 --fail-on-warnings  Exit non-zero if warnings are present
```

Bash
Copy
## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Developer tools - Home Assistant

Source: https://www.home-assistant.io/docs/tools/dev-tools/

#  On this page
The dashboard contains a section called Developer tools.
Screenshot of Home Assistant's developer tools. 
Section | Description  
---|---  
YAML | Lets you validate the configuration and trigger a reload or restart  
States | Sets the representation of an entity  
Actions | Performs actions from integrations  
Template | Renders templates  
Events | Fires events  
Statistics | Shows a list of long-term statistic entities  
Assist | Lets you see how Home Assistant Assist processes a sentence  
## What can I do with Developer Tools? 
The Developer Tools is meant for all (not just for the developers) to quickly try out things - like performing actions, updating states, raising events, and publishing messages in MQTT). It is also a necessary tool for those who write custom automations and scripts by hand. The following describes each of the sections in detail.
## YAML tab 
The YAML tab provides buttons to trigger a check of configuration files and to reload the configuration. Reloading is needed to apply changes that you’ve made to the configuration.
It is almost the same as the option under Settings > three dots menu (top right) > Restart Home Assistant > Quick reload. The only difference is that Quick reload reloads all the configuration, whereas this YAML tab allows you to only reload one specific configuration at a time.
### Reloading the YAML configuration 
For configuration changes to become effective, the configuration must be reloaded. Most integrations in Home Assistant (that do not interact with devicesA device is a model representing a physical or logical unit that contains entities. or servicesThe term “service” in Home Assistant is used in the sense of an information service. For example, the municipal waste management service that provides entities for organic, paper, and packaging waste. In terms of functionality, the information service is like a device. It is called service to avoid confusion, as it does not come with a piece of hardware.) can reload changes made to their configuration in configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] without needing to restart Home Assistant.
  1. Go to and scroll down to the YAML configuration reloading section (alternatively, hit anywhere in the UI and search for “reload”).
     * You are presented with a list of integrations, such as Automations or Conversation.
  2. Depending on what you find in the list, you can proceed with either reloading or you need to restart Home Assistant:
     * If the integration is listed, select it to reload the settings. 
       * For example, if you’ve changed the , you can select Location & customizations to apply those changes.
     * If the integration is not listed, you need to Restart Home Assistant for changes to take effect.


## States tab 
This section shows all the available entities, their corresponding state and the attribute values. The state and the attribute information is what Home Assistant sees at run time. To update the entity with a new state, or a new attribute value, click on the entity, scroll to the top, and modify the values, and click on “SET STATE” button.
Note that this is the state representation of a device within Home Assistant. That means, it is what Home Assistant sees, and it does not communicate with the actual device in any manner. The updated information can still be used to trigger events, and state changes. To communicate with the actual device, it is recommended to perform actions in the Actions section above, instead of updating state.
For example, changing the light.bedroom state from off to on does not turn on the light. If there is an automation that triggers on the state change of the light.bedroom, it will be triggered – even though the actual bulb has not turned on. Also, when the bulb state changes – the state information will be overridden (the refresh icon can be used to retrieve the latest information that Home Assistant has). In other words, the changes that are made through the “States” section are temporary, and are recommended to use for testing purposes only.
The table containing all entities can be filtered for each column. The used search is a wildcard search meaning that if you input “office” in the entity column filter, every entity whose ID matches “*office*” will be shown. You can also add your own wildcards in the search input (e.g., “office*light”). The attribute filter supports separate filters for attribute names and values, separated by a colon “:”. So the filter “location:3” will result in the table showing all entities that have an attribute name that contains “location” and whose attribute value contains “3”.
## Actions tab 
This section is used to perform actions that are available in Home Assistant.
The list of actions in the Actions dropdown are automatically populated based on the integrations that are found in the configuration, automation and script files. If a desired action does not exist, it means either the integration is not configured properly or not defined in the configuration, automation or script files.
When an action is selected, and if that action requires an entity_id to be passed, the Entity dropdown will automatically be populated with corresponding entities.
An action may also require additional input to be passed. It is commonly referred to as “action data”. The action data is accepted in YAML format, and it may be optional depending on the action.
When an entity is selected from the Entity dropdown, it automatically populates action data with the corresponding entity_id. The action data YAML can then be modified to pass additional [optional] parameters. The following is an illustration on how to perform a light.turn_on action.
To turn on a light bulb, use the following steps:
  1. Select light.turn_on from the Action dropdown.
  2. Select the entity (typically the light bulb) from the Entity dropdown (if no entity_id is selected, it turns on ALL lights)
  3. If an entity is selected, the action data is populated with basic YAML that will be passed to the action. Additional data can also be passed by updating the YAML as below.


```
entity_id: light.bedroom
brightness: 255
rgb_color: [255, 0, 0]

```

## Template editor tab 
The template editor provides a way to quickly test templates prior to placing them into automations and scripts. A code editor is on the left side and your real-time output is displayed in the preview on the right side.
By default, this will contain sample code that illustrates how templates can be written and tested. This sample code can be removed and replaced with your own. You can restore the default example by pressing the “Reset to Demo Template” button beneath the code editor.
For more information about Jinja2, visit , and also read templating document .
## Events tab 
In the Events section, you can either fire an event on the event bus or subscribe to an event type in order to view the event data JSON.
### Fire an event 
To fire an event, simply type the name of the event, and pass the event data in JSON format. For example, to fire a custom event, enter the event_type as event_light_state_changed and the event data JSON as
```
state: on

```

If there is an automation that handles that event, it will be automatically triggered. See below:
```
- alias: "Capture Event"
 triggers:
  - trigger: event
   event_type: event_light_state_changed
 actions:
  - action: notify.notify
   data:
    message: "Light is turned "

```

### Subscribe to an event 
To subscribe to an event, enter the event event type under “Listen to events” and click “Start listening”. Some events types are listed in the Events section under “Active listeners”. You can usually find information about event types for a particular integration in its documentation. You can then examine the event data JSON to find the correct parameters for your automations.
For example, subscribing to the event type shelly.click of the Shelly integration, returns event data JSON similar to the following on a button press.
```
Event 0 fired 9:53 AM:
{
  "event_type": "shelly.click",
  "data": {
    "device_id": "e09c64a22553484d804353ef97f6fcd6",
    "device": "shellybutton1-A4C12A45174",
    "channel": 1,
    "click_type": "single"
  },
  "origin": "LOCAL",
  "time_fired": "2021-04-28T08:53:12.755729+00:00",
  "context": {
    "id": "e0f379706563aaa0c2c1fda5174b5a0e",
    "parent_id": null,
    "user_id": null
  }
}

```

## Statistics tab 
The Statistics tab shows a list of long-term statistic entities. If the long term statistics is not working for an entity, a Fix Issue link is shown. Select it to view a description of the issue. There might also be an option to fix the issue.
Another use of the is to correct any measurements. Select the icon. Use date & time to search for the incorrect data point and adjust the value.
## Assist tab 
The Assist tab lets you see how Home Assistant’s Assist processes a sentence.
If no matching intent is found, then Assist is unable to interpret the sentence. If a matching intent was found, information is provided on the action that will be performed on which entities. The example below shows how the following sentence was parsed: what lights are on in the office.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Quick bar - Home Assistant

Source: https://www.home-assistant.io/docs/tools/quick-bar/

#  On this page
The Quick bar allows you to quickly look up entities or run commands without needing to navigate away from your current view (Similar to the “quick open” feature in VS Code, Chrome Developer Tools, etc).
It can be launched from anywhere in the frontend using .
Quick Bar for accessing entities and running commands 
## Hotkeys 
Type these from anywhere in the application to launch the dialog.
Mode | Hotkey | Switch Modes  
---|---|---  
Entity Filter | e | Type > at start of input to switch to command palette. Type # at start of input to switch to device filter.  
Command Palette | c | Remove > from start of input to switch to entity filter.  
Device Filter | d | Remove # from start of input to switch to entity filter.  
Create link | m | Open a new tab to create a my link to the page you are on.  
Assist | a | Open the Home Assistant Assist dialog.  
Important
The application must have focus for the hotkey to register. If the dialog doesn’t launch, try clicking into an empty part of the main content area of Home Assistant and type it again.
## Entity filter 
Hotkey: e
Similar to , but more lightweight and accessible from anywhere in the frontend.
Filter for entities in Quick Bar's entity filter mode 
Once launched, start typing your entity id (or ) to get back a filtered list of entities. Clicking on an entity (or hitting enter when the desired entity is highlighted) will open the “More Info” dialog for that entity.
This is helpful when, say, you are in the middle of writing an automation and need some quick insight about an entity but don’t want to navigate away to Developer Tools.
## Device filter 
Hotkey: d
Similar to , but accessible from anywhere in the frontend.
Once launched, start typing your device name to get back a filtered list of your devices. Clicking on a device (or hitting enter when the desired device is highlighted) will open the selected device detail page.
This is helpful when you need to quickly access a device’s detail page without navigating your way through the menu.
## Command palette 
Hotkey: c
Run various commands from anywhere without having to navigate to another view.
Run commands in Quick Bar's "command palette" 
### Currently-supported commands 
Type | Available  
---|---  
Navigate | All entries in the sidebar and settings  
Reload | All currently-supported “Reload {domain}” actions.(E.g., “Reload Scripts”)   
Server | Restart/Stop  
## My links 
Hotkey: m
Create links from any supported page in the user interface, when invoked on a supported page it will open a new tab that will allow you to share the link in different formats.
## Assist 
Hotkey: a
Opens the Assist dialog to interact with Home Assistant using your voice or by text. This feature is only available if you have set up a voice assistant.
Learn more about .
## Disabling shortcuts 
You can enable or disable all of Home Assistant’s keyboard shortcuts by going to your User Profile and clicking the “Keyboard Shortcuts” toggle button.
Toggle button for enabling/disabling keyboard shortcuts added by Home Assistant. 
## Tips 
### Search by “bits and pieces” rather than an exact substring 
We know something like “light.ch” should match “light.chandelier”. Similarly, “telev” should match “media_player.television”.
But with Quick Bar, “lich” would also match “light.chandelier”, and “plyrtv” would also match “media_player.television”. It checks letter sequences rather than exact substrings.
One nice use-case for this is that you can quickly filter out an entire domain of entities with just a couple letters and a period. For example, “li.” will match any “light.*” entities. Continuing with “li.ch” would bring up the chandelier right away.
### Filters work against friendly name too 
If “light.hue_ceiling_light” has been named “Chandelier”, you can type either “hue_ceil” or “chand” to find it.
### Use the enter key any time to open the top result in the list 
As soon as the item you wanted shows up at the top of your filtered results, just hit “enter” to activate it – no need to arrow down to the item, or click with your mouse.
### Use arrow keys to move around the list 
When in the text field, use the down arrow ↓ to navigate down the item list. Hit enter to activate the currently-highlighted row.
When in the item list, use the up arrow ↑ to navigate up the item list, and to get back into the text field.
### Typing more letters will always add to your filter string 
Say you’ve just used arrow keys to navigate half-way down the list, and want to add more text to your filter. You don’t need to click back into the text field, just start typing new letters and they’ll append to your filter.
## Troubleshooting 
### Dialog doesn’t launch using hotkeys 
There are a few possible reasons why the quick bar dialog won’t launch:
  1. Your user is not an admin.
  2. The application lost focus. Try clicking into the main content area of the application and typing the shortcut again.
  3. You have disabled Keyboard Shortcuts in your User Profile settings.
  4. Shortcut is marked by browser as non-overridable. Firefox does this with some shortcuts, for example. But this shouldn’t be a problem with single-key shortcuts currently used by the Quick Bar.
  5. Some other application or browser extension is using or overriding the shortcut. Try disabling the extension.


### A command is missing 
The command list only shows commands that are available to you based on your user settings, and loaded integrations.
For example, if you don’t have automations: in your config, then you won’t see the “Reload Automations” command.
If “Advanced Mode” is turned off in User Settings, then any command related to advanced mode will not appear in the list.
If a command is missing that you feel is in error, please create an issue on GitHub.
### Shortcuts interfere with accessibility tools, browser extensions, or are otherwise annoying 
You can in your User settings.
Please consider submitting an issue explaining why the shortcut was disruptive to you. Keyboard shortcuts are new to Home Assistant, and getting them right is a challenge for any Web application. We rely on user feedback to ensure the experience is minimally-disruptive.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## General troubleshooting - Home Assistant

Source: https://www.home-assistant.io/docs/troubleshooting_general/

#  On this page
This page provides some information about more generic troubleshooting topics.
## Home Assistant went into recovery mode 
### Symptom: Home Assistant is in recovery mode 
On top of the page you see a red banner. On the Overview page, you see a Recovery mode notification.
### Description 
When Home Assistant is in recovery mode, there was an issue with the configuration.
Recovery mode loads a minimum set of integrations to allow troubleshooting the configuration. Recovery mode will use the parts of the configuration that was used the last time Home Assistant started successfully. You can still see the user interface, the settings, and add-ons.
### Resolution 
You need to identify the issue in the configuration files and fix it there. The issue could be caused by something as simple as an invalid YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] file.
## Restarting Home Assistant in safe mode 
If your Home Assistant is acting up and you cannot identify a root cause, you can use Safe mode to narrow down the number of possible causes. Safe mode loads Home Assistant Core, but no custom integrations, no custom cards, and no custom themes. If the issue does not persist in Safe mode, the issue is not with Home Assistant Core. Before reporting an issue, check if the issue persists in Safe mode.
You can enable Safe mode in several ways:
## I don’t see any updates 
Typically, updates are shown at the top of the Settings page. If you don’t see them there, the Visibility option might be disabled.
### Resolution 
  1. On the System page, in the top-right corner, select the three dots menu and select Check for updates.
  2. Go to . 
     * Select the update notification.
     * Select the cogwheel , then set Visible to active.


## Related topics 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Android Flavors | Home Assistant Companion Docs

Source: https://companion.home-assistant.io/docs/core/android-flavors

The  Android app is being offered in 2 different flavors as either full or minimal. The full flavor of the app is offered via the and has the full set of features offered as it requires Google Play Services. The full flavor is offered for both production and .
The minimal flavor of the app does not require Google Play Services and is available in the section on GitHub as an APK. It can also be installed from . However, updates may be delayed because F-Droid builds new releases independently. This flavor does not support location tracking. Additionally, the following sensors are unavailable: .
In addition to these 2 flavors users can also find debug APKs on the section for each pull request submitted to GitHub. The debug version of the app can be installed side by side the production or beta version of the app. This allows users to help test upcoming features and fixes. Both the minimal and full flavors offer a debug version.
Certificate fingerprints
Below are the SHA-256 fingerprints for the signing certificate.
Play Store/GitHub releases: 11:19:4B:A8:09:B4:2D:DF:0E:1A:7D:EC:68:42:A5:9C:7F:F1:11:9C:54:82:E9:5F:EB:FF:D5:C6:01:4D:AA:5A
F-Droid releases: 17:48:52:50:A0:3A:0F:2B:3F:29:2A:05:4F:59:5A:9E:79:4B:EE:F8:0C:F9:10:F7:B3:BB:B8:09:8A:BF:6D:50
You can compare them with your downloaded apk / installed application using apksigner verify --print-certs app-(full/minimal)-release.apk or 



## Home Assistant Context | Home Assistant Data Science Portal

Source: https://data.home-assistant.io/docs/context/

On this page
Context is used to tie events and states together in Home Assistant. Whenever anything (e.g. an automation or user interaction) triggers a new change, a new context is assigned. This context will be attached to all events and states that happen as result of the change. The context thus allows to attribute all changes to their original cause internally and in the logbook.
A context object contains the following fields:
Field| Description  
---|---  
id| Unique identifier for the context.  
user_id| Unique identifier of the user that started the change, in case it is known to home assistant. This field is most notably populated, if the change is initiatited via the frontend. The user_id is used for restricting the ability to access and change the state of your home.  
parent_id| Unique identifier of the parent context's id that started the change. Most notably, automations will generate a new context, even if the trigger already has one. This is done to decouple the automation actions from the user privileges possibly associated to the trigger. Note that, currently, not all triggers generate a context.  
In the following example, all events and states will refer to the same context (either directly in their context.id or via context.parent_id):
Context is not stored in their own table in the database. Instead, each event row maintains it's own columns to store context.
Currently, there is no native way to retrieve the original cause of a context in automations or templates. 
## Example queries
### Finding the context_id for a state_changed event in the database.
```
SELECT states_meta.entity_id, states.state, hex(states.context_id_bin), hex(states.context_user_id_bin), hex(states.context_parent_id_bin) FROM states LEFT JOIN states_meta ON (states.metadata_id=states_meta.metadata_id);
```

### Finding the context_id for an event in the database.
```
SELECT event_types.event_type, event_data.shared_data, hex(events.context_id_bin), hex(events.context_user_id_bin), hex(events.context_parent_id_bin) FROM events LEFT JOIN event_data ON (events.data_id=event_data.data_id) LEFT JOIN event_types ON (events.event_type_id=event_types.event_type_id);
```






## Latest installation topics in Community Guides - Home Assistant Community

Source: https://community.home-assistant.io/tags/c/community-guides/51/installation

#  Community Guides 
The Community Guides section is a place to share guides/tutorials with our community. Every post/topic in this section works like a Wiki and can be edited and improved by anybody. Please note, guides provided in this section may be outdated/broken and are not supported by Home Assistant. Use these at your own risk. 
  * More 


Categories 
Tags 
​  ​ 
  1. Community Guides 
  2. installation 



Topic list, column headers with buttons are sortable. Topic  |  Posters  |  Replies  |  Views  |  Activity   
---|---|---|---|---  
Install and Set up Home Assistant OS on XpressReal T3  |  |  |  136  |   
Installing Home Assistant OS using Proxmox 8  |  |  |  600k  |   
Installing HAOS in a VM on TrueNAS  |  |  |  103k  |   
Installing Home Assistant Supervised on a Raspberry Pi using Debian 12  |  |  |  247k  |   
Installing Home Assistant Core on Fedora  |  |  |  12.6k  |   
Guide: Home Assistant Core - Restoring a Backup  |  |  |  106k  |   
Installing Home Assistant Supervised using Debian 12  |  |  |  515k  |   
Steps to reduce Write Cycles and extend SD/SSD life expectancy  |  |  |  50.5k  |   
Install Home Assistant OS with KVM on Ubuntu headless (CLI only)  |  |  |  97.5k  |   
Installing HAOS on Apple Silicon Macs using VMware Fusion  |  |  |  3.4k  |   
Install Home Assistant as a VM on Unraid  |  |  |  63.1k  |   
Homeassistant core on Android (Guide Dec’22)  |  |  |  73.3k  |   
Installing HA (core) on Apple Silicon Macs using Homebrew  |  |  |  675  |   
Solution to a hanged “Preparing Home Installation” screen during new install on a Raspberry Pi 4 (DNS fix)  |  |  |  68.3k  |   
Python 3.13 backport for Debian 12 bookworm  |  |  |  6.7k  |   
Installing Home Assistant on your MikroTik Router with Containers  |  |  |  18.1k  |   
Home Assistant Installation Methods  |  |  |  67.9k  |   
HTTPS for your HomeAssistant in your local LAN  |  |  |  3.4k  |   
Securing Home Assistant with Cloudflare  |  |  |  45.5k  |   
Installing Home Assistant Supervised on Orange Pi 3B  |  |  |  36.9k  |   
How to restore a backup  |  |  |  147k  |   
Installing Home Assistant on VMWare Player / Workstation 16 (or 17)  |  |  |  54.6k  |   
Guide: How to install Home Assistant supervised on Rpi4 with RaspiOS (64 bit) - October 2022  |  |  |  68.8k  |   
HomeAssistant on FreeBSD using bhyve  |  |  |  1.2k  |   
Installing Home Assistant on a RPi 4b with SSD boot  |  |  |  210k  |   
Setup Ecowitt weather station (WS 5500, aka WS 2900)  |  |  |  3.4k  |   
Home Assistant Core on Android Tablet  |  |  |  164k  |   
If you are new to HA, read this first; it might assist you with choices as you start your journey  |  |  |  5.3k  |   
Python 3.12 backport for Debian 12 bookworm  |  |  |  13.3k  |   
Install Home Assistant OS with VirtualBox on Ubuntu headless (CLI only)  |  |  |  32.0k  |   
Invalid date  Invalid date 



## Developing an add-on | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/add-ons

Add-ons for Home Assistant allow the user to extend the functionality around Home Assistant. This can be running an application that Home Assistant can integrate with (like an MQTT broker) or to share the configuration via Samba for easy editing from other computers. Add-ons can be configured via the Supervisor panel in Home Assistant.
Under the hood, add-ons are container images published to a container registry like and . Developers can create repositories that contain multiple add-ons for easy sharing with the community.
Useful links:



## Getting more help | Home Assistant Companion Docs

Source: https://companion.home-assistant.io/docs/troubleshooting/more-help

If after reading the docs here you are still having issues, try the following resources.
For general help and configuration advice
  * Visit the 
  * Post on the or .


For bug reports
  * Please raise an issue on the or the .


For feature requests
  * To request a new feature, open a discussion in the Home Assistant GitHub organization. Use the discussion page of the related platform: 
    * .


For issues, corrections or amendments to these docs
  * Either use the edit button on the page you wish to amend (docs are written in ), you will need a account to submit changes; or
  * raise an issue on the for the docs.





## Getting Started | Home Assistant Companion Docs

Source: https://companion.home-assistant.io/docs/getting_started/

On this page
New onboarding experience
Starting with  app version 2025.11.0, there's a new streamlined onboarding process. .
## Installation
This sections provides the minimal system requirements and installation instructions.
### System Requirements
## Setting Up
  * If your Home Assistant instance is correctly set up for , you should be able set up the Companion App from any location.
  * If you're connected to the same network as your Home Assistant, it will automatically be detected during set up.


  1. Download the Home Assistant Companion App from the or .
  2. When you open the app for the first time, you'll be guided through the process of connecting to your Home Assistant instance. Follow the steps.
     * You are asked to grant the required permissions to integrate your phone with Home Assistant.
     * One of the permissions requested is for location access.
     * If this permission is denied, then you will not get a device_tracker or any sensor entity created for the device.
  3. Once you are done on the first screen, select Continue.
     * The app will start checking your network for Home Assistant instances. 
       * If an instance is found, tap the instance and follow the prompts to connect and log in to your Home Assistant.
       * If you are not connected to the same local network as your Home Assistant instance, tap Enter Address Manually and enter the address you use to remotely connect to your Home Assistant instance (using the Remote UI is recommended but not required).
  4. Once you have connected and logged into your Home Assistant instance, you will be asked to grant permission for the app to work with your iOS device beyond basic browsing of your Home Assistant instance.
  5. Once you have granted or denied permissions, the app will create the required connections to your Home Assistant instance and then take you to your Home Assistant home screen.
     * Depending on the app version, you may see a "What's New" screen in between the end of setup and be taken to your home screen.
     * Once you see the home screen, the installation is complete.
  6. If you have difficulties completing setting up the app, refer to the .


info
Remember to login using your credentials and not to use , if you have that enabled otherwise the app will only work on the trusted network.
## Adding Additional Servers
or 
note
Requires Home Assistant 2021.10 or newer.
Once you have set up your first server, you can add additional Home Assistant instances.
  1. In the Companion app, go to > Companion App.
  2. Select the Add Server option. 
     * Servers on the same local network as your device will be discovered and listed automatically.
  3. If the new server is not listed automatically, enter the address in the same way as setting up the first server.


## TLS Client Authentication
If your Home Assistant requires TLS Client Authentication (because it is behind a reverse proxy configured to perform TLS Client Authentication), the app will ask for a certificate. If no matching certificate is installed or supplied, you might see an error or a blank screen depending on your setup.
Please refer to your device and Android version documentation to install the certificate. Make sure to install the certificate as a "VPN & app user certificate". An example for Pixel phones is available here: .
Wear OS does not support authentication with installed certificates. The app cannot transfer the certificate to the Wear OS app automatically, therefore you are asked to provide a certificate during the Wear OS app onboarding. The certificate and key need to be provided as a single file in PKCS12 format. If that does not work, refer to the .
## New onboarding ( 2025.11.0)
Starting with app version 2025.11.0, the onboarding process has been redesigned to provide a more streamlined setup experience. The new flow includes enhanced security options and clearer permission explanations.
### Step-by-step onboarding process
  1. Welcome screen: When you first open the app, you'll see the Home Assistant Companion app welcome screen with options to Connect to my Home Assistant or Learn more.
  2. Network discovery: The app will search for Home Assistant instances on your network.
     * If found, the app will try to automatically connect your Home Assistant server
     * In case multiple servers were found, you will see a list to choose from
     * If not found or connecting remotely, tap Enter address manually and provide your Home Assistant URL
  3. Login: Enter your Home Assistant credentials to authenticate.
  4. Device naming: Choose a name for your device as it will appear in Home Assistant.
     * This name is used to identify your phone in Home Assistant
  5. Location permission: The app will ask for location access to enable powerful automations and secure connections.
  6. System location permission: Your device will show the standard location permission dialog.
     * Select Allow Once, Allow While Using the App, or Don't Allow
     * For full functionality, including background automations, choose Allow While Using the App, then in the next prompt Allow always
  7. Connection security level: If you plan to use a non-encrypted URL (such as your local IP address), you'll need to choose a security level:
     * Most secure: Only allows non-encrypted connections when you're on your home network (requires location permission)
     * Less secure: Allows non-encrypted connections from any network (not recommended for public networks)
     * You can read more about .
  8. Setup completion: The app will finalize the connection and take you to your Home Assistant dashboard.





## Getting Started | Home Assistant Companion Docs

Source: https://companion.home-assistant.io/docs/getting_started

On this page
New onboarding experience
Starting with  app version 2025.11.0, there's a new streamlined onboarding process. .
## Installation
This sections provides the minimal system requirements and installation instructions.
### System Requirements
## Setting Up
  * If your Home Assistant instance is correctly set up for , you should be able set up the Companion App from any location.
  * If you're connected to the same network as your Home Assistant, it will automatically be detected during set up.


  1. Download the Home Assistant Companion App from the or .
  2. When you open the app for the first time, you'll be guided through the process of connecting to your Home Assistant instance. Follow the steps.
     * You are asked to grant the required permissions to integrate your phone with Home Assistant.
     * One of the permissions requested is for location access.
     * If this permission is denied, then you will not get a device_tracker or any sensor entity created for the device.
  3. Once you are done on the first screen, select Continue.
     * The app will start checking your network for Home Assistant instances. 
       * If an instance is found, tap the instance and follow the prompts to connect and log in to your Home Assistant.
       * If you are not connected to the same local network as your Home Assistant instance, tap Enter Address Manually and enter the address you use to remotely connect to your Home Assistant instance (using the Remote UI is recommended but not required).
  4. Once you have connected and logged into your Home Assistant instance, you will be asked to grant permission for the app to work with your iOS device beyond basic browsing of your Home Assistant instance.
  5. Once you have granted or denied permissions, the app will create the required connections to your Home Assistant instance and then take you to your Home Assistant home screen.
     * Depending on the app version, you may see a "What's New" screen in between the end of setup and be taken to your home screen.
     * Once you see the home screen, the installation is complete.
  6. If you have difficulties completing setting up the app, refer to the .


info
Remember to login using your credentials and not to use , if you have that enabled otherwise the app will only work on the trusted network.
## Adding Additional Servers
or 
note
Requires Home Assistant 2021.10 or newer.
Once you have set up your first server, you can add additional Home Assistant instances.
  1. In the Companion app, go to > Companion App.
  2. Select the Add Server option. 
     * Servers on the same local network as your device will be discovered and listed automatically.
  3. If the new server is not listed automatically, enter the address in the same way as setting up the first server.


## TLS Client Authentication
If your Home Assistant requires TLS Client Authentication (because it is behind a reverse proxy configured to perform TLS Client Authentication), the app will ask for a certificate. If no matching certificate is installed or supplied, you might see an error or a blank screen depending on your setup.
Please refer to your device and Android version documentation to install the certificate. Make sure to install the certificate as a "VPN & app user certificate". An example for Pixel phones is available here: .
Wear OS does not support authentication with installed certificates. The app cannot transfer the certificate to the Wear OS app automatically, therefore you are asked to provide a certificate during the Wear OS app onboarding. The certificate and key need to be provided as a single file in PKCS12 format. If that does not work, refer to the .
## New onboarding ( 2025.11.0)
Starting with app version 2025.11.0, the onboarding process has been redesigned to provide a more streamlined setup experience. The new flow includes enhanced security options and clearer permission explanations.
### Step-by-step onboarding process
  1. Welcome screen: When you first open the app, you'll see the Home Assistant Companion app welcome screen with options to Connect to my Home Assistant or Learn more.
  2. Network discovery: The app will search for Home Assistant instances on your network.
     * If found, the app will try to automatically connect your Home Assistant server
     * In case multiple servers were found, you will see a list to choose from
     * If not found or connecting remotely, tap Enter address manually and provide your Home Assistant URL
  3. Login: Enter your Home Assistant credentials to authenticate.
  4. Device naming: Choose a name for your device as it will appear in Home Assistant.
     * This name is used to identify your phone in Home Assistant
  5. Location permission: The app will ask for location access to enable powerful automations and secure connections.
  6. System location permission: Your device will show the standard location permission dialog.
     * Select Allow Once, Allow While Using the App, or Don't Allow
     * For full functionality, including background automations, choose Allow While Using the App, then in the next prompt Allow always
  7. Connection security level: If you plan to use a non-encrypted URL (such as your local IP address), you'll need to choose a security level:
     * Most secure: Only allows non-encrypted connections when you're on your home network (requires location permission)
     * Less secure: Allows non-encrypted connections from any network (not recommended for public networks)
     * You can read more about .
  8. Setup completion: The app will finalize the connection and take you to your Home Assistant dashboard.





## Connection security level | Home Assistant Companion Docs

Source: https://companion.home-assistant.io/docs/getting_started/connection-security-level

On this page
If you want to use a unencrypted URL to connect to Home Assistant (such as your local IP address for local connection), you will have to set the connection security level. You can choose between two security options in the app.
note
It is required to choose an option when onboarding a new server. If you added a server before the connection security level options were added, you'll be asked to choose one when starting the app.
## Option 1: Most secure (recommended)
This option ensures the app only connect to a unencrypted URL (for example, http://homeassistant.local:8123) when you are currently on your specified home network. When you are not on the specified home network, the app will display a screen blocking access and describing the requirements to connect. This also means that background activity will be blocked until a secure connection can be established.
You can specify your Wi-Fi SSID (for example, "GrandmaHome5G") to be considered your home network. To change the setting open the > Companion app > [server name] anytime you want.
Additional options
Android
You can also set using a VPN or Ethernet access as home network.
macOS
You can define a "Hardware address" as home network, which is useful for wired connections.
To retrieve the information above, the app needs the location access permission from your device, since network information could be used for location positioning. We understand that this is not desirable for all users, but this restriction is imposed by Apple platforms and Android. Your location will never be used for anything besides retrieving the network information. You are always in control if you want to share your location to your local Home Assistant server.
Important
The location permission must be set to Always and Precise for iOS and Allow all the time for Android for the app to function correctly in the background.
## Option 2: Less secure
If you don’t grant location permission or disable location at the OS level but still need to access a unencrypted URL (for example, ), you can choose this option. Use it only if absolutely necessary; it is not recommended, as it may expose your Home Assistant data to network eavesdropping, especially on public Wi-Fi.
## Why these options exist
These security options were introduced to protect your Home Assistant instance from potential security risks when using unencrypted connections.
When you connect to Home Assistant using an unencrypted URL (such as http://homeassistant.local:8123), all data transmitted between your device and Home Assistant is sent in plain text. This includes your login credentials, and any commands you send. On your home network, this is generally acceptable since the traffic stays within your local network. However, if you accidentally connect from a public Wi-Fi network or untrusted location, malicious actors could potentially intercept your Home Assistant data.
The Most secure option prevents these risks by ensuring unencrypted connections only work when you're on your home network. The Less secure option removes this protection, and is not recommended for most users.
For maximum security, we recommend using HTTPS connections with valid SSL certificates always, especially when accessing Home Assistant remotely.
To know more about networking check our .
## FAQ
### Why am I seeing the connection security prompt?
Starting with version 2025.11, the companion app will ask you to choose a security level if your setup includes an unencrypted URL (HTTP instead of HTTPS). This prompt helps protect your Home Assistant credentials from being exposed on public networks.
If you have HTTPS for all your URLs and still saw this prompt, please update to the latest app version.
### What do "Most secure" and "Less secure" mean?
  * Most secure: The app will only use unencrypted connections when you're on your specified home network. This requires location permission so the app can check your current Wi-Fi SSID.
  * Less secure: The app will use unencrypted connections regardless of which network you're on. This is not recommended if you ever connect to public Wi-Fi networks.


warning
Choosing "Less secure" may expose your Home Assistant credentials if you connect from a public network. Make sure you trust all networks you connect to when using this option.
### What happens when I'm not on my home network with "Most secure" enabled?
The app will block access and display a screen explaining the situation. Background activity (for example, widgets and sensors) will also pause until a secure connection can be established.
This happens because the app cannot verify you're on a trusted network, so it refuses to send credentials over a potentially insecure connection. Once you return to your home network (or connect via HTTPS), the app will resume normal operation automatically.
If you see the blocking screen with additional prompts, it means the app needs something to work correctly—such as location permission or home network configuration.
### How do I set up my home network?
  1. Grant location permission when prompted (required for the Most secure option).
  2. Connect to your home Wi-Fi network.
  3. Go to > Companion app > [your server] > Internal URL.
  4. Add your home Wi-Fi SSID to the list.


You can add multiple SSIDs if you have more than one home network.
### Can I specify the Hardware Address (Ethernet) instead of just the SSID?
On macOS, yes.
On Android and iOS, this is not currently available. For iOS, this is due to platform limitations.
### Does this feature work when I'm connected through a VPN?
Android
You can select the VPN connected option as home network in > Companion app > [your server] > Home network.
note
This option only detects connection to any VPN. Connection to a specific VPN cannot be detected due to platform limitations.
iOS
No. The connection security level feature uses your Wi-Fi SSID to determine if you're at home. When connected via VPN, the app cannot detect your physical location through Wi-Fi.
If you rely on VPN for remote access, you'll need to configure your setup differently:
  1. Set your local Home Assistant address as the external URL (since you access it the same way whether home or away).
  2. Ensure your VPN is connected whenever you want to interact with Home Assistant remotely.


warning
If you set your local (HTTP) address as the external URL and forget to connect your VPN on a public network, this may expose your Home Assistant credentials.
### I use VPN for all remote access. Should I enable this feature?
If you've set your local address as the external URL, the connection security level setting won't affect how the app connects: it will always use that external URL.
However, for advanced use cases, you may still want different internal and external URLs. In that case, enable the Most secure option to ensure your internal (possibly HTTP) URL is only used when you're actually at home.
### Will the app send my credentials if Home Assistant is unreachable?
Yes, the app will attempt to connect using your configured URLs, for example, when retrieving the state of an entity to display in your widget or when executing a shortcut in Shortcuts app.
If your external URL is HTTP (not recommended for remote access), credentials would be sent unencrypted when the app attempts to connect. To prevent this behavior use the option Most secure.
### I chose "Less secure" but now want to change it. How?
Go to > Companion app > [your server] > Connection security level to change your preference at any time. To define your home network, go to > Companion app > [your server] > Internal URL.
### What happens if I don't grant location permission?
Without location permission, the app cannot determine which network you're currently connected to. If you choose Most secure without granting location access, the app will only be able to use your external (HTTPS) URL.
If you need to use an unencrypted internal URL and don't want to grant location permission, you'll need to select "Less secure"—but .



## Android Gallery | Home Assistant Companion Docs

Source: https://companion.home-assistant.io/docs/gallery/android

On this page
Screenshots
## Onboarding
### Welcome
The first screen of the app
### Discovery
This screen will show all discovered Home Assistant instances, if discovery fails you may select Enter address manually
### Manual Setup
On this screen you can manually enter your Home Assistant instance in case discovery failed to find it.
### Authentication
On this screen you will login to your Home Assistant server
### Final Step
On this screen you can change the default device name, you can also enable location tracking if you are on the Play Store version.
## Settings
All settings found in Configuration > Companion App
### Manage Sensors
List of all sensors, you can use the filter at the top show only enabled sensors and also to search
### Sensor Details
All details of a sensor including state and attributes. You can also configure sensor settings from this page.
### NFC
Create and read NFC tags
### Persistent Connection Settings
Manage the persistent connection to retrieve local push notifications
### Notification History
Last 25 notifications, you can use the filter at the top to show the last 100 and also to search against all notifications.
### Notification Details
The full details of the notification
### Manage Quick Setting Tiles
Setup and edit quick setting tiles, they will need to be configured in the app first before they are functional
### Manage Launcher Shortcuts
Setup and edit launcher shortcuts to quickly navigate to any place in the frontend.
### Manage Widgets
Create and edit widgets on your home screen
### Logs
View and share the on device logs
## Widgets
Configuration pages for widgets
### Entity State Widget
### Service Call Widget
### Media Player Widget
### Template Widget
### Widgets Home screen
How all the widgets look on the home screen



## Home Assistant Android | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/android

On this page
## Welcome to the Home Assistant Android project
Are you ready to make a difference in the world of smart home technology? The Home Assistant Android app is an open-source project that empowers users to control their smart homes seamlessly. Whether you're a developer, designer, or enthusiast, your contributions matter!
Explore the GitHub repository to see how far we've come and where you can help!
## Why contribute?
## How you can help
We welcome contributions of all kinds! Here are some ways you can get involved:
## Ready to get started?
  1. Check out our get started guide for step-by-step instructions.
  2. Join our Discord community, make sure you select the developer role and head to the Android project thread to connect with other contributors.


Together, we can create something extraordinary. Let's build the future of smart homes, one contribution at a time!



## Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/entity_registry_index/

On this page
The entity registry is a registry where Home Assistant keeps track of entities. Any entity that is added to Home Assistant which specifies the will be registered in the registry.
Being registered has the advantage that the same entity will always get the same entity ID. It will also prevent other entities from using that entity ID.
A user is also able to override the name of an entity in the entity registry. When set, the name in the entity registry is used in favor of the name the device might give itself.
## Unique ID
It is important that it is not possible for the user to change the unique ID, because the system would lose all its settings related to the unique ID.
An entity is looked up in the registry based on a combination of the platform type (e.g., light), and the integration name (domain) (e.g. hue) and the unique ID of the entity. Entities should not include the domain (e.g., your_integration) and platform type (e.g., light) in their Unique ID as the system already accounts for these identifiers.
If a device has a single unique id but provides multiple entities, combine the unique id with unique identifiers for the entities. For example, if a device measures both temperature and humidity, you can uniquely identify the entities using {unique_id}-{sensor_type}.
## Unique ID requirements
### Example acceptable sources for a unique ID
### Unique ID of last resort
For entities that are setup by a config entry, the Config Entry ID can be used as a last resort if no other Unique ID is available.
### Unacceptable sources for a unique ID



## Entity | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/core/entity

On this page
For a generic introduction of entities, see .
## Basic implementation
Below is an example switch entity that keeps track of its state in memory. In addition, the switch in the example represents the main feature of a device, meaning the entity has the same name as its device.
Please refer to for how to give an entity its own name.
```
from homeassistant.components.switch import SwitchEntityclass MySwitch(SwitchEntity):  _attr_has_entity_name = True  def __init__(self):    self._is_on = False    self._attr_device_info = ... # For automatic device registration    self._attr_unique_id = ...  @property  def is_on(self):    """If the switch is currently on or off."""    return self._is_on  def turn_on(self, **kwargs):    """Turn the switch on."""    self._is_on = True  def turn_off(self, **kwargs):    """Turn the switch off."""    self._is_on = False
```

That's all there is to it to build a switch entity! Continue reading to learn more or check out the .
## Updating the entity
An entity represents a device. There are various strategies to keep your entity in sync with the state of the device, the most popular one being polling.
### Polling
With polling, Home Assistant will ask the entity from time to time (depending on the update interval of the component) to fetch the latest state. Home Assistant will poll an entity when the should_poll property returns True (the default value). You can either implement your update logic using update() or the async method async_update(). This method should fetch the latest state from the device and store it in an instance variable for the properties to return it.
### Subscribing to updates
When you subscribe to updates, your code is responsible for letting Home Assistant know that an update is available. Make sure you have the should_poll property return False.
Whenever you receive a new state from your subscription, you can tell Home Assistant that an update is available by calling schedule_update_ha_state() or async callback async_schedule_update_ha_state(). Pass in the boolean True to the method if you want Home Assistant to call your update method before writing the update to Home Assistant.
## Generic properties
The entity base class has a few properties common among all Home Assistant entities. These properties can be added to any entity regardless of the type. All these properties are optional and don't need to be implemented.
These properties are always called when the state is written to the state machine.
tip
Properties should always only return information from memory and not do I/O (like network requests). Implement update() or async_update() to fetch data.
Because these properties are always called when the state is written to the state machine, it is important to do as little work as possible in the property.
To avoid calculations in a property method, set the corresponding , or if the values never change, use .
Name| Type| Default| Description  
---|---|---|---  
assumed_state| bool| False| Return True if the state is based on our assumption instead of reading it from the device.  
attribution| str | None| None| The branding text required by the API provider.  
available| bool| True| Indicate if Home Assistant is able to read the state or control the underlying device, see for more details.  
device_class| str | None| None| Extra classification of what the device is. Each domain specifies their own. Device classes can come with extra requirements for unit of measurement and supported features.  
entity_picture| str | None| None| Url of a picture to show for the entity.  
extra_state_attributes| dict | None| None| Extra information to store in the state machine. It needs to be information that further explains the state, it should not be static information like firmware version.  
has_entity_name| bool| False| Return True if the entity's name property represents the entity itself (required for new integrations). This is explained in more detail below.  
name| str | None| None| Name of the entity. Avoid hard coding a natural language name, use a instead.  
should_poll| bool| True| Should Home Assistant check with the entity for an updated state. If set to False, entity will need to notify Home Assistant of new updates by calling one of the .  
state| str | int | float | None| None| The state of the entity. In most cases this is implemented by the domain base entity and should not be implemented by integrations.  
supported_features| int | None| None| Flag features supported by the entity. Domains specify their own.  
translation_key| str | None| None| A key for looking up translations of the entity's state in and for translating the state into a matching .  
translation_placeholders| dict | None| None| Placeholder definitions for .  
warning
It's allowed to change device_class, supported_features or any property included in a domain's capability_attributes. However, since these entity properties often are not expected to change at all and some entity consumers may not be able to update them at a free rate, we recommend only changing them when absolutely required and at a modest interval.
As an example, such changes will cause voice assistant integrations to resynchronize with the supporting cloud service.
warning
Entities that generate a significant amount of state changes can quickly increase the size of the database when the extra_state_attributes also change frequently. Minimize the number of extra_state_attributes for these entities by removing non-critical attributes or creating additional sensor entities.
## Registry properties
The following properties are used to populate the entity and device registries. They are read each time the entity is added to Home Assistant. These properties only have an effect if unique_id is not None.
Name| Type| Default| Description  
---|---|---|---  
device_info| DeviceInfo | None| None|  descriptor for   
entity_category| EntityCategory | None| None| Classification of a non-primary entity. Set to EntityCategory.CONFIG for an entity that allows changing the configuration of a device, for example, a switch entity, making it possible to turn the background illumination of a switch on and off. Set to EntityCategory.DIAGNOSTIC for an entity that exposes some configuration parameter or diagnostics of a device but does not allow changing it, for example, a sensor showing RSSI or MAC address. Use it also for button entities that trigger a device identification mechanism (with IDENTIFY device class).  
entity_registry_enabled_default| bool| True| Indicate if the entity should be enabled or disabled when first added to the entity registry. This includes fast-changing diagnostic entities or, assumingly less commonly used entities. For example, a sensor exposing RSSI or battery voltage should typically be set to False; to prevent unneeded (recorded) state changes or UI clutter by these entities.  
entity_registry_visible_default| bool| True| Indicate if the entity should be hidden or visible when first added to the entity registry.  
unique_id| str | None| None| A unique identifier for this entity. It must be unique within a platform (like light.hue). It should not be configurable or changeable by the user.   
## Advanced properties
The following properties are also available on entities. However, they are for advanced use only and should be used with caution. These properties are always called when the state is written to the state machine.
Name| Type| Default| Description  
---|---|---|---  
capability_attributes| dict | None| None| State attributes which are stored in the entity registry. This property is implemented by the domain base entity and should not be implemented by integrations.  
force_update| bool| False| Write each update to the state machine, even if the data is the same. Example use: when you are directly reading the value from a connected sensor instead of a cache. Use with caution, will spam the state machine.  
icon| str | None| None| Icon to use in the frontend. Using this property is not recommended. .  
state_attributes| dict | None| None| State attributes of a base domain. This property is implemented by the domain base entity and should not be implemented by integrations.  
unit_of_measurement| str | None| The unit of measurement that the entity's state is expressed in. In most cases, for example for the number and sensor domains, this is implemented by the domain base entity and should not be implemented by integrations.  
## System properties
The following properties are used and controlled by Home Assistant, and should not be overridden by integrations.
Name| Type| Default| Description  
---|---|---|---  
enabled| bool| True| Indicate if entity is enabled in the entity registry. It also returns True if the platform doesn't support the entity registry. Disabled entities will not be added to Home Assistant.  
## Entity naming
Avoid setting an entity's name to a hard coded English string, instead, the name should be . Examples of when the name should not be translated are proper nouns, model names, and name provided by a 3rd-party library.
Some entities are automatically named after their device class, this includes , , and entities and in many cases don't need to be named. For example, an unnamed sensor which has its device class set to temperature will be named "Temperature".
note
If an entity provides translations for the entity name, the used name depends on the system (backend) language at creation time, not the user’s UI language. For example, if your backend is set to German, new entities will be named in German — even if a user later switches their UI to French. Changing the backend language will only affect entities created after the change; existing entities retain their original names.
### has_entity_name True (Mandatory for new integrations)
The entity's name property only identifies the data point represented by the entity, and should not include the name of the device or the type of the entity. So for a sensor that represents the power usage of its device, this would be “Power usage”.
If the entity represents a single main feature of a device the entity should typically have its name property return None. The "main feature" of a device would for example be the LightEntity of a smart light bulb.
The friendly_name state attribute is generated by combining the entity name with the device name as follows:
  * The entity is not a member of a device: friendly_name = entity.name
  * The entity is a member of a device and entity.name is not None: friendly_name = f"{device.name} {entity.name}"
  * The entity is a member of a device and entity.name is None: friendly_name = f"{device.name}"


The entity_id is generated by combining the entity name with the device name as follows:
  * The entity is not a member of a device e.g. a helper "Everyone is home": entity_id = binary_sensor.everyone_is_home
  * The entity is a member of a device and entity.name is not None e.g. the battery of device named "nightlight": entity_id = sensor.nightlight_battery
  * The entity is a member of a device and entity.name is None e.g. the light of a device named "nightlight": entity_id = light.nightlight


Entity names should start with a capital letter, the rest of the words are lower case (unless it's a proper noun or a capitalized abbreviation of course).
#### Example of a switch entity which is the main feature of a device
Note: The example is using class attributes to implement properties, for other ways to implement properties see Property implementation. *Note: The example is incomplete, the unique_id property must be implemented, and the entity must be 
```
from homeassistant.components.switch import SwitchEntityclass MySwitch(SwitchEntity):  _attr_has_entity_name = True  _attr_name = None
```

#### Example of a switch entity which is either not the main feature of a device, or is not part of a device:
Note: The example is using class attributes to implement properties, for other ways to implement properties see Property implementation. *Note: If the entity is part of a device, the unique_id property must be implemented, and the entity must be 
```
from homeassistant.components.switch import SwitchEntityclass MySwitch(SwitchEntity):  _attr_has_entity_name = True  @property  def translation_key(self):    """Return the translation key to translate the entity's name and states."""    return my_switch
```

#### Example of an untranslated switch entity which is either not the main feature of a device, or is not part of a device:
```
from homeassistant.components.switch import SwitchEntityclass MySwitch(SwitchEntity):  _attr_has_entity_name = True  @property  def name(self):    """Name of the entity."""    return "Model X"
```

### has_entity_name not implemented or False (Deprecated)
The entity's name property may be a combination of the device name and the data point represented by the entity.
## Property implementation
### Property function
Writing property methods for each property is just a couple of lines of code, for example
```
class MySwitch(SwitchEntity):  @property  def icon(self) -> str | None:    """Icon of the entity."""    return "mdi:door"  ...
```

### Entity class or instance attributes
Alternatively, a shorter form is to set Entity class or instance attributes according to either of the following patterns:
```
class MySwitch(SwitchEntity):  _attr_icon = "mdi:door"  ...
```

```
class MySwitch(SwitchEntity):  def __init__(self, icon: str) -> None:    self._attr_icon = icon  ...
```

This does exactly the same as the first example but relies on a default implementation of the property in the base class. The name of the attribute starts with _attr_ followed by the property name. For example, the default device_class property returns the _attr_device_class class attribute.
Not all entity classes support the _attr_ attributes for their entity specific properties, please refer to the documentation for the respective entity class for details.
tip
If an integration needs to access its own properties it should access the property (self.name), not the class or instance attribute (self._attr_name).
### Entity description
The third way of setting entity properties is to use an entity description. To do this set an attribute named entity_description on the Entity instance with an EntityDescription instance. The entity description is a dataclass with attributes corresponding to most of the available Entity properties. Each entity integration that supports an entity platform, eg the switch integration, will define their own EntityDescription subclass that should be used by implementing platforms that want to use entity descriptions.
By default the EntityDescription instance has one required attribute named key. This is a string which is meant to be unique for all the entity descriptions of an implementing platform. A common use case for this attribute is to include it in the unique_id of the described entity.
The main benefit of using entity descriptions is that it defines the different entity types of a platform in a declarative manner, making the code much easier to read when there are many different entity types.
### Example
The below code snippet gives an example of best practices for when to implement property functions, when to use class or instance attributes and when to use entity descriptions.
```
from __future__ import annotationsfrom collections.abc import Callablefrom dataclasses import dataclassfrom example import ExampleDevice, ExampleExceptionfrom homeassistant.components.sensor import (  SensorDeviceClass,  SensorEntity,  SensorEntityDescription,  SensorStateClass,)from homeassistant.config_entries import ConfigEntryfrom homeassistant.const import (  EntityCategory,  UnitOfElectricCurrent,)from homeassistant.core import HomeAssistantfrom homeassistant.helpers.entity_platform import AddEntitiesCallbackfrom homeassistant.helpers.typing import StateTypefrom .const import DOMAIN, LOGGER@dataclass(kw_only=True)class ExampleSensorEntityDescription(SensorEntityDescription):  """Describes Example sensor entity."""  exists_fn: Callable[[ExampleDevice], bool] = lambda _: True  value_fn: Callable[[ExampleDevice], StateType]SENSORS: tuple[ExampleSensorEntityDescription, ...] = (  ExampleSensorEntityDescription(    key="estimated_current",    native_unit_of_measurement=UnitOfElectricCurrent.MILLIAMPERE,    device_class=SensorDeviceClass.CURRENT,    state_class=SensorStateClass.MEASUREMENT,    value_fn=lambda device: device.power,    exists_fn=lambda device: bool(device.max_power),  ),)async def async_setup_entry(  hass: HomeAssistant,  entry: ConfigEntry,  async_add_entities: AddEntitiesCallback,) -> None:  """Set up Example sensor based on a config entry."""  device: ExampleDevice = hass.data[DOMAIN][entry.entry_id]  async_add_entities(    ExampleSensorEntity(device, description)    for description in SENSORS    if description.exists_fn(device)  )class ExampleSensorEntity(SensorEntity):  """Represent an Example sensor."""  entity_description: ExampleSensorEntityDescription  _attr_entity_category = (    EntityCategory.DIAGNOSTIC  ) # This will be common to all instances of ExampleSensorEntity  def __init__(    self, device: ExampleDevice, entity_description: ExampleSensorEntityDescription  ) -> None:    """Set up the instance."""    self._device = device    self.entity_description = entity_description    self._attr_available = False # This overrides the default    self._attr_unique_id = f"{device.serial}_{entity_description.key}"  def update(self) -> None:    """Update entity state."""    try:      self._device.update()    except ExampleException:      if self.available: # Read current state, no need to prefix with _attr_        LOGGER.warning("Update failed for %s", self.entity_id)      self._attr_available = False # Set property value      return    self._attr_available = True    # We don't need to check if device available here    self._attr_native_value = self.entity_description.value_fn(      self._device    ) # Update "native_value" property
```

## Lifecycle hooks
Use these lifecycle hooks to execute code when certain events happen to the entity. All lifecycle hooks are async methods.
### async_added_to_hass()
Called when an entity has their entity_id and hass object assigned, before it is written to the state machine for the first time. Example uses: restore the state, subscribe to updates or set callback/dispatch function/listener.
### async_will_remove_from_hass()
Called when an entity is about to be removed from Home Assistant. Example use: disconnect from the server or unsubscribe from updates.
## Icons
Every entity in Home Assistant has an icon, which is used as a visual indicator to identify the entity more easily in the frontend. Home Assistant uses the icon set.
In most cases, Home Assistant will pick an icon automatically based on the entity's domain, device_class, and state. It is preferred to use the default icon if possible, to provide a consistent experience and to avoid confusion for the user. However, it is possible to override the default and provide a custom icon for an entity.
Regardless of the provided icon, it is always possible for the user to customize the icon to their liking in the frontend.
There are two ways to provide a custom icon for an entity, either by providing icon translations or by providing an icon identifier.
### Icon translations
This is the preferred way to provide a custom icon for an entity. Icon translations work similarly to , but instead of translating the state of an entity, they translate the states of an entity to icons.
The translation_key property of an entity defines the icon translation to use. This property is used to look up the translation in the entity section of the integration's icons.json file.
To differentiate entities and their translations, provide different translation keys. The following example shows icons.json for a Moon domain sensor entity with its translation_key property set to phase:
```
{ "entity": {  "sensor": {   "phase": {    "default": "mdi:moon",    "state": {     "new_moon": "mdi:moon-new",     "first_quarter": "mdi:moon-first-quarter",     "full_moon": "mdi:moon-full",     "last_quarter": "mdi:moon-last-quarter"    }   }  } }}
```

Notice that icons start with mdi: plus an . The default icon is used when the entity's state is not in the state section. The state section is optional, and if not provided, the default icon will be used for all states.
Icons for entity state attributes can also be provided in cases where the frontend shows icons for the state attributes. Examples include climate presets and fan modes. It's not possible to provide icons for other state attributes. The following example provides icons for a climate entity with its translation_key property set to ubercool. This entity has a preset_mode state attribute, which can be set to vacation or night. The frontend will use these in, for example, the climate card.
```
{ "entity": {  "climate": {   "ubercool": {    "state_attributes": {     "preset_mode": {      "default": "mdi:confused",      "state": {       "vacation": "mdi:umbrella-beach",       "night": "mdi:weather-night"      }     }    }   }  } }}
```

### Icon property
Another way to provide an icon for an entity is by setting the icon property of an entity, which returns a string referencing the mdi icon. As this property is a method, it is possible to return different icons based on custom logic unlike with icon translations. For example, it's possible to calculate the icon based on the state as in the example below, or return different icons based on something that is not part of the entity's state.
```
class MySwitch(SwitchEntity):  @property  def icon(self) -> str | None:    """Icon of the entity, based on time."""    if now().hour < 12:      return "mdi:weather-night"    return "mdi:weather-sunny"  ...
```

It is not possible to provide icons for state attributes using the icon property. Please note that using the icon property is discouraged; using the above-mentioned icon translations is preferred.
## Excluding state attributes from recorder history
State attributes which are not suitable for state history recording should be excluded from state history recording by including them in either of _entity_component_unrecorded_attributes or _unrecorded_attributes.
  * _entity_component_unrecorded_attributes: frozenset[str] may be set in a base component class, e.g. in light.LightEntity
  * _unrecorded_attributes: frozenset[str] may be set in an integration's platform e.g. in an entity class defined in platform hue.light.


The MATCH_ALL constant can be used to exclude all attributes instead of typing them separately. This can be useful for integrations providing unknown attributes or when you simply want to exclude all without typing them separately.
Using the MATCH_ALL constant does not stop recording for device_class, state_class, unit_of_measurement, and friendly_name as they might also serve other purposes and, therefore, should not be excluded from recording.
Examples of platform state attributes which are exluded from recording include the entity_picture attribute of image entities which will not be valid after some time, the preset_modes attribute of fan entities which is not likely to change. Examples of integration specific state attributes which are excluded from recording include description and location state attributes in platform trafikverket.camera which do not change.
tip
The _entity_component_unrecorded_attributes and _unrecorded_attributes must be declared as class attributes; instance attributes will be ignored.
## Changing the entity model
If you want to add a new feature to an entity or any of its subtypes (light, switch, etc), you will need to propose it first in our . Only additions will be considered that are common features among various vendors.



## Architecture overview | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/architecture_index

On this page
Home Assistant provides a platform for home control and home automation. Home Assistant is not just an application: it's an embedded system that provides an experience like other consumer off-the-shelf products: onboarding, configuration and updating is all done via an easy to use interface.
  * The provides the bare minimal Linux environment to run Supervisor and Core.
  * The manages the operating system.
  * The interacts with the user, the supervisor and IoT devices & services.


## Running parts of the stack
Users have different requirements for what they want from a home automation platform. That's why it is possible to run only part of the Home Assistant stack. For more information, see the .





## Creating custom panels | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/custom-ui/creating-custom-panels

On this page
Panels are pages that show information within Home Assistant and can allow controlling it. Panels are linked from the sidebar and rendered full screen. They have real-time access to the Home Assistant object via JavaScript. Examples of panels in the app are dashboards, Map, Logbook and History.
Besides components registering panels, users can also register panels using the panel_custom component. This allows users to quickly build their own custom interfaces for Home Assistant.
## Introduction
Panels are defined as custom elements. You can use any framework that you want, as long as you wrap it up as a custom element. To quickly get started with a panel, create a new file <config>/www/example-panel.js with this content
```
import "https://unpkg.com/wired-card@2.1.0/lib/wired-card.js?module";import { LitElement, html, css,} from "https://unpkg.com/lit-element@2.4.0/lit-element.js?module";class ExamplePanel extends LitElement { static get properties() {  return {   hass: { type: Object },   narrow: { type: Boolean },   route: { type: Object },   panel: { type: Object },  }; } render() {  return html`   <wired-card elevation="2">    <p>There are ${Object.keys(this.hass.states).length} entities.</p>    <p>The screen is${this.narrow ? "" : " not"} narrow.</p>    Configured panel config    <pre>${JSON.stringify(this.panel.config, undefined, 2)}</pre>    Current route    <pre>${JSON.stringify(this.route, undefined, 2)}</pre>   </wired-card>  `; } static get styles() {  return css`   :host {    background-color: #fafafa;    padding: 16px;    display: block;   }   wired-card {    background-color: white;    padding: 16px;    display: block;    font-size: 18px;    max-width: 600px;    margin: 0 auto;   }  `; }}customElements.define("example-panel", ExamplePanel);
```

Then add to your configuration.yaml:
```
panel_custom: - name: example-panel  # url_path needs to be unique for each panel_custom config  url_path: redirect-server-controls  sidebar_title: Example Panel  sidebar_icon: mdi:server  module_url: /local/example-panel.js  config:   # Data you want to make available to panel   hello: world
```

## API reference
The Home Assistant frontend will pass information to your panel by setting properties on your custom element. The following properties are set:
Property| Type| Description  
---|---|---  
hass| object| Current state of Home Assistant  
narrow| boolean| if the panel should render in narrow mode  
panel| object| Panel information. Config is available as panel.config.  
## JavaScript versions
The Home Assistant user interface is currently served to browsers in modern JavaScript and older JavaScript (ES5). The older version has a wider browser support but that comes at a cost of size and performance.
If you do need to run with ES5 support, you will need to load the ES5 custom elements adapter before defining your element:
```
window.loadES5Adapter().then(function() { customElements.define('my-panel', MyCustomPanel)});
```






## Home Assistant Frontend | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend

The Home Assistant frontend allows users to browse and control the state of their house, manage their automations and configure integrations.
The frontend is designed as a mobile-first experience. It is a progressive web application and offers an app-like experience to our users.
The Home Assistant frontend needs to be fast. But it also needs to work on a wide range of old devices. To do this, we ship two versions of the frontend:
  * Latest: this build is compatible with the two latest versions of evergreen browsers and is optimized to be fast.
  * ES5: this build is compatible with browsers released in the last 5+ years and is optimized to be compatible.


A device that runs the latest technology does not also have to be fast. You can buy budget Android phones that run the latest Android version with access to the latest Firefox and Chrome browsers, but with low performance chipset and limited memory. Our latest build needs to run smooth on these devices too.
For a deep dive into our frontend and its design choices, see .



## Home Assistant Core | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/development_index

The core of Home Assistant is built from the ground up to be easily extensible using integrations. In this section, we're focusing on how to develop integrations.
Before you start, make sure that you have read up on the overall so that you are familiar with the concepts that make up Home Assistant.
For support or questions about contributing to Home Assistant development, join #developers or create a thread in #support on . Assign the Developer role: in the sidebar, select Channels & Roles, then choose I want to contribute dev skills to Home Assistant to gain access to these channels.



## Frontend architecture | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/architecture

On this page
The Home Assistant frontend is built using web components. This is a modern web technology allowing us to encapsulate templates, styling and logic into a single file and expose it as an HTML tag in the browser. These components are composable, allowing a very dynamic and powerful foundation of our application.
## Structure
The Home Assistant frontend can be broken up in 4 parts:
### Bootstrap
File: src/entrypoints/core.ts
This is a very tiny script which is the first thing that is loaded on the page. It is responsible for checking for authentication credentials and setting up the websocket connection with the backend.
The script allows us to start downloading the data while also downloading the rest of the UI in parallel.
### App shell
File: src/entrypoints/app.ts
This is everything that is required to render the sidebar and handle the routing.
### Panels
Folder: src/panels/
Each page in Home Assistant is a panel. Components can register extra panels to be shown to the user. Examples of panels are "states", "map", "logbook" and "history".
### Dialogs
Folder: src/dialogs
Certain information and data entry is presented to users in flows. Dialogs can be triggered on any page. The most common one is the entity more info dialog, which allows users to dig into an entity's state, history, and settings.
## Data flow
The frontend leverages the and the to interact with Home Assistant.
The data is made available as the hass property which is passed down to every component. The hass property contains the core state and has methods to call APIs.
Components can subscribe to information that is not available in the core state. Subscriptions run through the websocket API which keeps the data in sync with the backend.
We use a unidirectional data flow. When you make a change in the backend (like turning on a light), the hass object will be updated at the root of the application and will be made available to every component that needs it.
## Routing
The frontend uses decentralized routing. Each component only knows enough about the routing to know how to handle the part it's responsible for. Further routing is passed down the component tree.
For example, the <home-assistant> main component will look at the first part of the url to decide which panel should be loaded. Each panel can have its own mapping between the url and what content to show.



## Custom badge | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/custom-ui/custom-badge

On this page
are small widgets that sit at the top of a view, above all cards. We offer a built-in badge, the , but you're not just limited that one. You can build and use your own!
## Defining your badge
Defining a badge is done in a very similar way to defining a .
Let's create a basic badge that displays custom text at the top of the screen. Create a new file in your Home Assistant config dir as <config>/www/text-badge.js and put in the following contents:
```
class TextBadge extends HTMLElement { // Whenever the state changes, a new `hass` object is set. Use this to // update your content. set hass(hass) {  this._hass = hass;  this.updateContent(); } // The user supplied configuration. Throw an exception and Home Assistant // will render an error badge. setConfig(config) {  if (!config.entity) {   throw new Error("You need to define an entity");  }  this.config = config;  this.updateContent(); } updateContent() {  if (!this.config || !this._hass) return;  const entityId = this.config.entity;  const state = this._hass.states[entityId];  const stateStr = state ? state.state : "unavailable";  this.innerHTML = `<p>${stateStr}</p>`; }}customElements.define("text-badge", TextBadge);
```

## Referencing your new badge
In our example badge, we defined a badge with the tag text-badge (see last line), so our badge type will be custom:text-badge. And because you created the file in your <config>/www directory, it will be accessible in your browser via the url /local/ (if you have recently added the www folder you will need to re-start Home Assistant for files to be picked up).
Add a resource to your dashboard configuration with URL /local/text-badge.js and type module ().
You can then use your badge in your dashboard configuration:
```
# Example dashboard configurationviews: - name: Example  badges:   - type: "custom:text-badge"    entity: light.bedside_lamp
```

## API
Custom badges are defined as a . It's up to you to decide how to render your DOM inside your element. You can use Polymer, Angular, Preact or any other popular framework (except for React – ).
Home Assistant will call setConfig(config) when the configuration changes (rare). If you throw an exception if the configuration is invalid, Home Assistant will render an error badge to notify the user.
Home Assistant will set when the state of Home Assistant changes (frequent). Whenever the state changes, the component will have to update itself to represent the latest state.
## Graphical badge configuration
Your badge can define a getConfigElement method that returns a custom element for editing the user configuration. Home Assistant will display this element in the badge editor in the dashboard.
Your badge can also define a getStubConfig method that returns a default badge configuration (without the type: parameter) in json form for use by the badge type picker in the dashboard.
Home Assistant will call the setConfig method of the config element on setup. Home Assistant will update the hass property of the config element on state changes, and the lovelace element, which contains information about the dashboard configuration.
Changes to the configuration are communicated back to the dashboard by dispatching a config-changed event with the new configuration in its detail.
To have your badge displayed in the badge picker dialog in the dashboard, add an object describing it to the array window.customBadges. Required properties of the object are type and name (see example below).
```
import "./text-badge-editor.js";class TextBadge extends HTMLElement {  ... static getConfigElement() {  return document.createElement("text-badge-editor"); } static getStubConfig() {  return { entity: "sun.sun" }; }}customElements.define("text-badge", TextBadge);
```

```
class TextBadgeEditor extends HTMLElement { setConfig(config) {  this._config = config; } configChanged(newConfig) {  const event = new Event("config-changed", {   bubbles: true,   composed: true,  });  event.detail = { config: newConfig };  this.dispatchEvent(event); }}customElements.define("text-badge-editor", TextBadgeEditor);window.customBadges = window.customBadges || [];window.customBadges.push({ type: "text-badge", name: "Text badge", preview: false, // Optional - defaults to false description: "A custom badge made by me!", // Optional documentationURL:  "https://developers.home-assistant.io/docs/frontend/custom-ui/custom-badge", // Adds a help link in the frontend badge editor});
```




## Custom card | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/custom-ui/custom-card

On this page
are our approach to defining your user interface for Home Assistant. We offer a lot of built-in cards, but you're not just limited to the ones that we decided to include in Home Assistant. You can build and use your own!
## Defining your card
This is a basic example to show what's possible.
Create a new file in your Home Assistant config dir as <config>/www/content-card-example.js and put in the following contents:
```
class ContentCardExample extends HTMLElement { // Whenever the state changes, a new `hass` object is set. Use this to // update your content. set hass(hass) {  // Initialize the content if it's not there yet.  if (!this.content) {   this.innerHTML = `    <ha-card header="Example-card">     <div class="card-content"></div>    </ha-card>   `;   this.content = this.querySelector("div");  }  const entityId = this.config.entity;  const state = hass.states[entityId];  const stateStr = state ? state.state : "unavailable";  this.content.innerHTML = `   The state of ${entityId} is ${stateStr}!   <br><br>   <img src="http://via.placeholder.com/350x150">  `; } // The user supplied configuration. Throw an exception and Home Assistant // will render an error card. setConfig(config) {  if (!config.entity) {   throw new Error("You need to define an entity");  }  this.config = config; } // The height of your card. Home Assistant uses this to automatically // distribute all cards over the available columns in masonry view getCardSize() {  return 3; } // The rules for sizing your card in the grid in sections view getGridOptions() {  return {   rows: 3,   columns: 6,   min_rows: 3,   max_rows: 3,  }; }}customElements.define("content-card-example", ContentCardExample);
```

## Referencing your new card
In our example card we defined a card with the tag content-card-example (see last line), so our card type will be custom:content-card-example. And because you created the file in your <config>/www directory, it will be accessible in your browser via the url /local/ (if you have recently added the www folder you will need to re-start Home Assistant for files to be picked up).
Add a resource to your dashboard configuration with URL /local/content-card-example.js and type module ().
You can then use your card in your dashboard configuration:
```
# Example dashboard configurationviews: - name: Example  cards:   - type: "custom:content-card-example"    entity: input_boolean.switch_tv
```

## API
Custom cards are defined as a . It's up to you to decide how to render your DOM inside your element. You can use Polymer, Angular, Preact or any other popular framework (except for React – ).
### Configuration
Home Assistant will call setConfig(config) when the configuration changes (rare). If you throw an exception if the configuration is invalid, Home Assistant will render an error card to notify the user.
Home Assistant will set when the state of Home Assistant changes (frequent). Whenever the state changes, the component will have to update itself to represent the latest state.
### Sizing in masonry view
Your card can define a getCardSize method that returns the size of your card as a number or a promise that will resolve to a number. A height of 1 is equivalent to 50 pixels. This will help Home Assistant distribute the cards evenly over the columns in the . A card size of 1 will be assumed if the method is not defined.
Since some elements can be lazy loaded, if you want to get the card size of another element, you should first check it is defined.
```
return customElements .whenDefined(element.localName) .then(() => element.getCardSize());
```

### Sizing in sections view
You can define a getGridOptions method that returns the min, max and default number of cells your card will take in the grid if your card is used in the . Each section is divided in 12 columns. If you don't define this method, the card will take 12 columns and will ignore the rows of the grid.
A cell of the grid is defined with the following dimension:
  * width: width of the section divided by 12 (approximately 30px)
  * height: 56px
  * gap between cells: 8px


The different grid options are:
For the number of columns, it's highly recommended to use multiple of 3 for the default value (3, 6, 9 or 12) so your card will have better looking on the dashboard by default.
Example of implementation:
```
public getGridOptions() { return {  rows: 2,  columns: 6,  min_rows: 2, };}
```

In this example, the card will take 6 x 2 cells by default. The height of the card cannot be smaller than 2 rows. According to the cell dimension, the card will have a height of 120px (2 * 56px + 8px).
## Advanced example
Resources to load in dashboards are imported as a JS module import. Below is an example of a custom card using JS modules that does all the fancy things.
Create a new file in your Home Assistant config dir as <config>/www/wired-cards.js and put in the following contents:
```
import "https://unpkg.com/wired-card@0.8.1/wired-card.js?module";import "https://unpkg.com/wired-toggle@0.8.0/wired-toggle.js?module";import { LitElement, html, css,} from "https://unpkg.com/lit-element@2.0.1/lit-element.js?module";function loadCSS(url) { const link = document.createElement("link"); link.type = "text/css"; link.rel = "stylesheet"; link.href = url; document.head.appendChild(link);}loadCSS("https://fonts.googleapis.com/css?family=Gloria+Hallelujah");class WiredToggleCard extends LitElement { static get properties() {  return {   hass: {},   config: {},  }; } render() {  return html`   <wired-card elevation="2">    ${this.config.entities.map((ent) => {     const stateObj = this.hass.states[ent];     return stateObj      ? html`        <div class="state">         ${stateObj.attributes.friendly_name}         <wired-toggle          .checked="${stateObj.state === "on"}"          @change="${(ev) => this._toggle(stateObj)}"         ></wired-toggle>        </div>       `      : html` <div class="not-found">Entity ${ent} not found.</div> `;    })}   </wired-card>  `; } setConfig(config) {  if (!config.entities) {   throw new Error("You need to define entities");  }  this.config = config; } // The height of your card. Home Assistant uses this to automatically // distribute all cards over the available columns. getCardSize() {  return this.config.entities.length + 1; } _toggle(state) {  this.hass.callService("homeassistant", "toggle", {   entity_id: state.entity_id,  }); } static get styles() {  return css`   :host {    font-family: "Gloria Hallelujah", cursive;   }   wired-card {    background-color: white;    padding: 16px;    display: block;    font-size: 18px;   }   .state {    display: flex;    justify-content: space-between;    padding: 8px;    align-items: center;   }   .not-found {    background-color: yellow;    font-family: sans-serif;    font-size: 14px;    padding: 8px;   }   wired-toggle {    margin-left: 8px;   }  `; }}customElements.define("wired-toggle-card", WiredToggleCard);
```

Add a resource to your dashboard config with URL /local/wired-cards.js and type module.
And for your configuration:
```
# Example dashboard configurationviews: - name: Example  cards:   - type: "custom:wired-toggle-card"    entities:     - input_boolean.switch_ac_kitchen     - input_boolean.switch_ac_livingroom     - input_boolean.switch_tv
```

## Graphical card configuration
Your card can define a getConfigElement method that returns a custom element for editing the user configuration. Home Assistant will display this element in the card editor in the dashboard.
Your card can also define a getStubConfig method that returns a default card configuration (without the type: parameter) in json form for use by the card type picker in the dashboard.
Home Assistant will call the setConfig method of the config element on setup. Home Assistant will update the hass property of the config element on state changes, and the lovelace element, which contains information about the dashboard configuration.
Changes to the configuration are communicated back to the dashboard by dispatching a config-changed event with the new configuration in its detail.
To have your card displayed in the card picker dialog in the dashboard, add an object describing it to the array window.customCards. Required properties of the object are type and name (see example below).
```
class ContentCardExample extends HTMLElement { static getConfigElement() {  return document.createElement("content-card-editor"); } static getStubConfig() {  return { entity: "sun.sun" } } ...}customElements.define('content-card-example', ContentCardExample);
```

```
class ContentCardEditor extends LitElement { setConfig(config) {  this._config = config; } configChanged(newConfig) {  const event = new Event("config-changed", {   bubbles: true,   composed: true,  });  event.detail = { config: newConfig };  this.dispatchEvent(event); }}customElements.define("content-card-editor", ContentCardEditor);window.customCards = window.customCards || [];window.customCards.push({ type: "content-card-example", name: "Content Card", preview: false, // Optional - defaults to false description: "A custom card made by me!", // Optional documentationURL:  "https://developers.home-assistant.io/docs/frontend/custom-ui/custom-card", // Adds a help link in the frontend card editor});
```

### Using the built-in form editor
While one way to configure a graphical editor is to supply a custom editor element, another option for cards with relatively simple configuration requirements is to use the built-in frontend form editor. This is done by defining a static getConfigForm function in your card class, that returns a form schema defining the shape of your configuration form.
Example:
```
 static getConfigForm() {  return {   schema: [    { name: "label", selector: { label: {} } },    { name: "entity", required: true, selector: { entity: {} } },    {     type: "grid",     name: "",     schema: [      { name: "name", selector: { text: {} } },      {       name: "icon",       selector: {        icon: {},       },       context: {        icon_entity: "entity",       },      },      {       name: "attribute",       selector: {        attribute: {},       },       context: {        filter_entity: "entity",       },      },      { name: "unit", selector: { text: {} } },      { name: "theme", selector: { theme: {} } },      { name: "state_color", selector: { boolean: {} } },     ],    },   ],   computeLabel: (schema) => {    if (schema.name === "icon") return "Special Icon";    return undefined;   },   computeHelper: (schema) => {    switch (schema.name) {     case "entity":      return "This text describes the function of the entity selector";     case "unit":      return "The unit of measurement for this card";    }    return undefined;   },   assertConfig: (config) => {    if (config.other_option) {     throw new Error("'other_option' is unexpected.");    }   },  }; }
```

From this function, you should return an object with up to 4 keys:
This example then results in the following config form: 
#### Form Schema Elements
The form schema can have individual controls, grids, or expansion panels, configured with the following options:
Controls:
  * name (required): The name of the control.
  * selector (optional): The selector configuration for this control (see for available options)
  * type (optional): If selector is not defined, there are native form types like float and boolean, though using selectors is preferred.


Grids:
Expansion Panel:
This is not an exhaustive list of all options, more configuration options are listed at 



## Frontend data | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/data/

On this page
The frontend passes a single hass object around. This object contains the latest state, allows you to send commands back to the server and provides helpers to format entity state.
Whenever a state changes, a new version of the objects that changed are created. So you can easily see if something has changed by doing a strict equality check:
```
const changed = newVal !== oldVal;
```

In order to see the data available in the hass object, visit your HomeAssistant frontend in your favorite browser and open the browser's developer tools. On the elements panel, select the <home-assistant> element, or any other element that has the hass property, and then run the following command in the console panel:
```
$0.hass
```

This method of reading the hass object should only be used as a reference. In order to interact with hass in your code, make sure it is passed to your code correctly.
## Data
### hass.states
An object containing the states of all entities in Home Assistant. The key is the entity_id, the value is the state object.
```
{ "sun.sun": {  "entity_id": "sun.sun",  "state": "above_horizon",  "attributes": {   "next_dawn": "2018-08-18T05:39:19+00:00",   "next_dusk": "2018-08-17T18:28:52+00:00",   "next_midnight": "2018-08-18T00:03:51+00:00",   "next_noon": "2018-08-18T12:03:58+00:00",   "next_rising": "2018-08-18T06:00:33+00:00",   "next_setting": "2018-08-17T18:07:37+00:00",   "elevation": 60.74,   "azimuth": 297.69,   "friendly_name": "Sun"  },  "last_changed": "2018-08-17T13:46:59.083836+00:00",  "last_updated": "2018-08-17T13:49:30.378101+00:00",  "context": {   "id": "74c2b3b429c844f18e59669e4b41ec6f",   "user_id": null  }, }, "light.ceiling_lights": {  "entity_id": "light.ceiling_lights",  "state": "on",  "attributes": {   "min_mireds": 153,   "max_mireds": 500,   "brightness": 180,   "color_temp": 380,   "hs_color": [    56,    86   ],   "rgb_color": [    255,    240,    35   ],   "xy_color": [    0.459,    0.496   ],   "white_value": 200,   "friendly_name": "Ceiling Lights",   "supported_features": 151  },  "last_changed": "2018-08-17T13:46:59.129248+00:00",  "last_updated": "2018-08-17T13:46:59.129248+00:00",  "context": {   "id": "2c6bbbbb66a84a9dae097b6ed6c93383",   "user_id": null  }, }}
```

### hass.user
The logged in user.
```
{ "id": "758186e6a1854ee2896efbd593cb542c", "name": "Paulus", "is_owner": true, "is_admin": true, "credentials": [  {   "auth_provider_type": "homeassistant",   "auth_provider_id": null  } ]}
```

## Methods
All methods starting with call are async methods. This means that they will return a Promise that will resolve with the result of the call.
### hass.callService(domain, service, data)
Call a service action on the backend.
```
hass.callService('light', 'turn_on', { entity_id: 'light.kitchen'});
```

### hass.callWS(message)
Call a WebSocket command on the backend.
```
this.hass.callWS({ type: 'config/auth/create', name: 'Paulus',}).then(userResponse => console.log("Created user", userResponse.user.id));
```

### hass.callApi(method, path, data)
Call an API on the Home Assistant server. For example, if you want to fetch all Home Assistant backups by issuing a GET request to /api/hassio/backups:
```
hass.callApi('get', 'hassio/backups') .then(backups => console.log('Received backups!', backups));
```

If you need to pass in data, pass a third argument:
```
hass.callApi('delete', 'notify.html5', { subscription: 'abcdefgh' });
```

info
We're moving away from API calls and are migrating everything to hass.callWS(message) calls.
## Entity state formatting
These methods allow you to format the state and attributes of an entity. The value will be localized using user profile settings (language, number format, date format, timezone) and unit of measurement.
### hass.formatEntityState(stateObj, state)
Format the state of an entity. You need to pass the entity state object.
```
hass.formatEntityState(hass.states["light.my_light"]); // "On"
```

You can force the state value using the second optional parameter.
```
hass.formatEntityState(hass.states["light.my_light"], 'off'); // "Off"
```

### hass.formatEntityAttributeValue(stateObj, attribute, value)
Format the attribute value of an entity. You need to pass the entity state object and the attribute name.
```
hass.formatEntityAttributeValue(hass.states["climate.thermostat"], "current_temperature"); // "20.5 °C"
```

You can force the state value using the third optional parameter.
```
hass.formatEntityAttributeValue(hass.states["climate.thermostat"], "current_temperature", 18); // "18 °C"
```

### hass.formatEntityAttributeName(stateObj, attribute)
Format the attribute name of an entity. You need to pass the entity state object and the attribute name.
```
hass.formatEntityAttributeName(hass.states["climate.thermostat"], "current_temperature"); // "Current temperature"
```




## Extending the WebSocket API | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/extending/websocket-api

On this page
As a component you might have information that you want to make available to the frontend. For example, the media player will want to make album covers available for the frontend to show. Our frontend is communicating with the backend over the websocket API, which can be extended with custom commands.
## Registering a command (Python)
To register a command, you need to have a message type, a message schema and a message handler. Your component does not have to add the websocket API as a dependency. You register your command, and if the user is using the websocket API, the command will be made available.
### Defining your command schema
A command schema is made up of a message type and what type of data we expect when the command is invoked. You define both the command type and the data schema via a decorator on your command handler. Message handlers are callback functions that are run inside the event loop.
```
from homeassistant.components import websocket_api@websocket_api.websocket_command(  {    vol.Required("type"): "frontend/get_panels",    vol.Optional("preload_panels"): bool,  })@callbackdef ws_get_panels(  hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None:  """Handle the websocket command."""  panels = ...  connection.send_result(msg["id"], {"panels": panels})
```

#### Doing I/O or sending a delayed response
If your command needs to interact with the network, a device or needs to compute information, you will need to queue a job to do the work and send the response. To do this, make your function async and decorate with @websocket_api.async_response.
```
from homeassistant.components import websocket_api@websocket_api.websocket_command(  {    vol.Required("type"): "camera/get_thumbnail",    vol.Optional("entity_id"): str,  })@websocket_api.async_responseasync def ws_handle_thumbnail(  hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None:  """Handle get media player cover command."""  # Retrieve media player using passed in entity id.  player = hass.data[DOMAIN].get_entity(msg["entity_id"])  # If the player does not exist, send an error message.  if player is None:    connection.send_error(        msg["id"], "entity_not_found", "Entity not found"    )    return  data, content_type = await player.async_get_media_image()  # No media player thumbnail available  if data is None:    connection.send_error(      msg["id"], "thumbnail_fetch_failed", "Failed to fetch thumbnail"    )    return  connection.send_result(    msg["id"],    {      "content_type": content_type,      "content": base64.b64encode(data).decode("utf-8"),    },  )
```

### Registering with the Websocket API
With all pieces defined, it's time to register the command. This is done inside your setup method.
```
from homeassistant.components import websocket_apiasync def async_setup(hass, config):  """Setup of your component."""  websocket_api.async_register_command(hass, ws_get_panels)  websocket_api.async_register_command(hass, ws_handle_thumbnail)
```

## Calling the command from the frontend (JavaScript)
With your command defined, it's time to call it from the frontend! This is done using JavaScript. You will need access to the hass object which holds the WebSocket connection to the backend. Then just call hass.connection.sendMessagePromise. This will return a promise that will resolve if the command succeeds and errors if the command fails.
```
hass.connection.sendMessagePromise({  type: 'media_player/thumbnail',  entity_id: 'media_player.living_room_tv',}).then(  (resp) => {    console.log('Message success!', resp.result);  },  (err) => {    console.error('Message failed!', err);  });
```

If your command is not sending a response, you can use hass.connection.sendMessage.



## Frontend development | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/development

On this page
The Home Assistant frontend is built using web components. For more background about our technology choices, .
caution
Do not use development mode in production. Home Assistant uses aggressive caching to improve the mobile experience. This is disabled during development so that you do not have to restart the server in between changes.
## Setting up the environment
Follow our guide to set up a proper development environment first.
### Getting the code
The first step is to fork the and add the upstream remote. You can place the forked repository anywhere on your system.
```
git clone git@github.com:YOUR_GIT_USERNAME/frontend.gitcd frontendgit remote add upstream https://github.com/home-assistant/frontend.git
```

### Configuring Home Assistant
You will need to have an instance of Home Assistant set up. For a development instance see our guide on .
There are two ways to test the frontend. You either run a development instance Home Assistant Core, or you configure the frontend to connect to an existing Home Assistant instance. The first option is how it will work in production. The second allows running a development frontend against an existing Home Assistant with minimal interference. The downside is that not everything can be tested this way. For example, the login page will always be the one built-in into your Home Assistant.
  * With a dev instance of HA Core
  * With a production instance of HA Core


#### Developing with Visual Studio Code + dev container
To configure Home Assistant to use the development mode for the frontend, update the frontend config in your configuration.yaml and set the path to the frontend repository that you cloned in the last step:
If you are using Visual Studio Code with dev containers for Home Assistant Core, you need to mount the frontend repository into the dev container. Add the following section to .devcontainer/devcontainer.json in the Home Assistant Core repository:
```
"mounts": [ "source=/path/to/hass/frontend,target=/workspaces/frontend,type=bind,consistency=cached"]
```

Rebuild the dev container by pressing Shift+Command+P (Mac) / Ctrl+Shift+P (Windows/Linux) to open the Command Palette, then selecting the Dev Containers: Rebuild Container command.
Edit config/configuration.yaml at the root of the Home Assistant Core repository to add this entry:
```
frontend: development_repo: /workspaces/frontend
```

note
This is the mounted path inside the dev container, see the target parameter above. If the source path is incorrect, the web frontend won't work.
Run Home Assistant Core from VS Code:
  1. Open the Command Palette: 
     * Mac: Shift+Command+P
     * Windows/Linux: Ctrl+Shift+P
  2. Select Tasks: Run Task
  3. Select Run Home Assistant Core


caution
The change to .devcontainer/devcontainer.json should be excluded from any PR as it contains your local path to the frontend repository. Since the settings in .devcontainer/devcontainer.json are only processed during the container rebuild, you can safely roll back the change after the rebuild has completed.
#### Developing with a manual environment
If you set up the development environment for Home Assistant Core manually, fill in the frontend repository path in configuration.yaml:
```
frontend: # Example path: /home/paulus/dev/hass/frontend development_repo: /path/to/hass/frontend
```

tip
The configuration.yaml file can be found in the config directory at the root of the Home Assistant Core repository. If the path is incorrect or otherwise inaccessible, the web frontend won't work.
If you want to connect your development frontend to an existing home assistant instance without replacing the UI completely, you will need to add the url under which your development frontend is hosted in configuration.yaml of the home assistant it will be connecting to. Like this:
```
http: cors_allowed_origins:  - http://localhost:8124
```

After you've setup your frontend development environment so that you can run the script/develop script as described in section . You can use the following command as a replacement to develop and run the frontend on and it will connect to the Home Assistant running on . Note that if you are running this command from a devcontainer, the url should be accessible from the container host.
```
script/develop_and_serve
```

You can change the Home Assistant url the frontend connects to by passing the -c option. This will also work for existing production core instances. It does not need to be a development version hosted locally. However, if you change the value for this option you will need to logout from your development frontend before it actually switches to the new value. For example:
```
script/develop_and_serve -c https://homeassistant.local:8123
```

You can change the port the frontend is served on by passing the -p option. Note that if you are running from a devcontainer, you will need to setup port forwarding as well if you want to access it from the container host. For example:
```
script/develop_and_serve -p 8654
```

### Installing Node.js (manual environment only)
Node.js is required to build the frontend. The preferred method of installing node.js is with . Install nvm using the instructions in the , and install the correct node.js by running the following command:
```
nvm install
```

is used as the package manager for node modules. 
### Install development dependencies and fetch latest translations
Bootstrap the frontend development environment by installing development dependencies and downloading the latest translations.
```
nvm usescript/bootstrapscript/setup_translations
```

note
This needs to be done manually, even if you are using dev containers. Also, you will be asked to enter a code and authorize the script to fetch the latest translations.
note
If you are using a development container, run these commands inside the container.
## Development
### Run development server
Run this script to build the frontend and run a development server:
```
nvm usescript/develop
```

When the script has completed building the frontend, and Home Assistant Core has been set up correctly, the frontend will be accessible at http://localhost:8123. The server will automatically rebuild the frontend when you make changes to the source files.
### Run development frontend over existing HA instance
Run this command to start the development server:
```
nvm usescript/develop_and_serve -c https://homeassistant.local:8123
```

You may need to replace "" with your local Home Assistant url.
### Browser settings
Open Google Chrome's Developer tools, and make sure you have cache disabled and correct settings to avoid stale content:
info
Instructions are for Google Chrome
  1. Disable cache by ticking the box in Network > Disable cache


  1. Enable Bypass for network in Application > Service Workers > Bypass for network


## Creating pull requests
If you're planning on issuing a PR back to the Home Assistant codebase you need to fork the frontend project and add your fork as a remote to the Home Assistant frontend repo.
```
git remote add fork <github URL to your fork>
```

When you've made your changes and are ready to push them change to the working directory for the frontend project and then push your changes
```
git add -Agit commit -m "Added new feature X"git push -u fork HEAD
```

## Building the frontend
If you're making changes to the way the frontend is packaged, it might be necessary to try out a new packaged build of the frontend in the main repository (instead of pointing it at the frontend repo). To do so, first build a production version of the frontend by running script/build_frontend.
To test it out inside Home Assistant, run the following command from the main Home Assistant repository:
```
pip3 install -e /path/to/hass/frontend/ --config-settings editable_mode=compathass --skip-pip-packages home-assistant-frontend
```




## Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/design

We maintain a design portal at that provides information about various frontend aspects such as:
When new components or features are added to the frontend, those need to be added to the design portal. This portal page explains the details on how to do so: 
note
While the portal is publicly named "design", it is referred to as "gallery" in the frontend repository. That is why the script to run the gallery locally in your development environment can be found at gallery/script/develop_gallery and the source code in gallery/src.



## Registering resources | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/custom-ui/registering-resources

If you want to extend the Home Assistant interface with custom cards, strategies or views you need to load external resources.
The first step is to make it accessible for the Home Assistant frontend. This is done by creating a new directory in your config folder called www. Create this directory and restart Home Assistant.
Once restarted, you can put files in this directory. Each file will be accessible without authentication via the UI at /local.
The next step is to register these resources with the Home Assistant interface. This is done by navigating to the Resources page by following below link:
(Note: Once redirected, click the three dots menu in the top-right.)
note
This area is only available when the active user's profile has "advanced mode" enabled.
Alternatively, you can also register the resource by adding it to the resources section of lovelace in the configuration:
```
resources: - url: /local/<name of the resource>.js  type: module
```




## Frontend data | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/data

On this page
The frontend passes a single hass object around. This object contains the latest state, allows you to send commands back to the server and provides helpers to format entity state.
Whenever a state changes, a new version of the objects that changed are created. So you can easily see if something has changed by doing a strict equality check:
```
const changed = newVal !== oldVal;
```

In order to see the data available in the hass object, visit your HomeAssistant frontend in your favorite browser and open the browser's developer tools. On the elements panel, select the <home-assistant> element, or any other element that has the hass property, and then run the following command in the console panel:
```
$0.hass
```

This method of reading the hass object should only be used as a reference. In order to interact with hass in your code, make sure it is passed to your code correctly.
## Data
### hass.states
An object containing the states of all entities in Home Assistant. The key is the entity_id, the value is the state object.
```
{ "sun.sun": {  "entity_id": "sun.sun",  "state": "above_horizon",  "attributes": {   "next_dawn": "2018-08-18T05:39:19+00:00",   "next_dusk": "2018-08-17T18:28:52+00:00",   "next_midnight": "2018-08-18T00:03:51+00:00",   "next_noon": "2018-08-18T12:03:58+00:00",   "next_rising": "2018-08-18T06:00:33+00:00",   "next_setting": "2018-08-17T18:07:37+00:00",   "elevation": 60.74,   "azimuth": 297.69,   "friendly_name": "Sun"  },  "last_changed": "2018-08-17T13:46:59.083836+00:00",  "last_updated": "2018-08-17T13:49:30.378101+00:00",  "context": {   "id": "74c2b3b429c844f18e59669e4b41ec6f",   "user_id": null  }, }, "light.ceiling_lights": {  "entity_id": "light.ceiling_lights",  "state": "on",  "attributes": {   "min_mireds": 153,   "max_mireds": 500,   "brightness": 180,   "color_temp": 380,   "hs_color": [    56,    86   ],   "rgb_color": [    255,    240,    35   ],   "xy_color": [    0.459,    0.496   ],   "white_value": 200,   "friendly_name": "Ceiling Lights",   "supported_features": 151  },  "last_changed": "2018-08-17T13:46:59.129248+00:00",  "last_updated": "2018-08-17T13:46:59.129248+00:00",  "context": {   "id": "2c6bbbbb66a84a9dae097b6ed6c93383",   "user_id": null  }, }}
```

### hass.user
The logged in user.
```
{ "id": "758186e6a1854ee2896efbd593cb542c", "name": "Paulus", "is_owner": true, "is_admin": true, "credentials": [  {   "auth_provider_type": "homeassistant",   "auth_provider_id": null  } ]}
```

## Methods
All methods starting with call are async methods. This means that they will return a Promise that will resolve with the result of the call.
### hass.callService(domain, service, data)
Call a service action on the backend.
```
hass.callService('light', 'turn_on', { entity_id: 'light.kitchen'});
```

### hass.callWS(message)
Call a WebSocket command on the backend.
```
this.hass.callWS({ type: 'config/auth/create', name: 'Paulus',}).then(userResponse => console.log("Created user", userResponse.user.id));
```

### hass.callApi(method, path, data)
Call an API on the Home Assistant server. For example, if you want to fetch all Home Assistant backups by issuing a GET request to /api/hassio/backups:
```
hass.callApi('get', 'hassio/backups') .then(backups => console.log('Received backups!', backups));
```

If you need to pass in data, pass a third argument:
```
hass.callApi('delete', 'notify.html5', { subscription: 'abcdefgh' });
```

info
We're moving away from API calls and are migrating everything to hass.callWS(message) calls.
## Entity state formatting
These methods allow you to format the state and attributes of an entity. The value will be localized using user profile settings (language, number format, date format, timezone) and unit of measurement.
### hass.formatEntityState(stateObj, state)
Format the state of an entity. You need to pass the entity state object.
```
hass.formatEntityState(hass.states["light.my_light"]); // "On"
```

You can force the state value using the second optional parameter.
```
hass.formatEntityState(hass.states["light.my_light"], 'off'); // "Off"
```

### hass.formatEntityAttributeValue(stateObj, attribute, value)
Format the attribute value of an entity. You need to pass the entity state object and the attribute name.
```
hass.formatEntityAttributeValue(hass.states["climate.thermostat"], "current_temperature"); // "20.5 °C"
```

You can force the state value using the third optional parameter.
```
hass.formatEntityAttributeValue(hass.states["climate.thermostat"], "current_temperature", 18); // "18 °C"
```

### hass.formatEntityAttributeName(stateObj, attribute)
Format the attribute name of an entity. You need to pass the entity state object and the attribute name.
```
hass.formatEntityAttributeName(hass.states["climate.thermostat"], "current_temperature"); // "Current temperature"
```




## Custom card feature | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/custom-ui/custom-card-feature

On this page
Some dashboard cards have support for . These widgets add quick controls to the card. We offer a lot of built-in features, but you're not just limited to the ones that we decided to include in Home Assistant. You can build and use your own in the same way as defining .
## Defining your card feature
Below is an example of a custom card feature for .
```
import { LitElement, html, css,} from "https://unpkg.com/lit-element@2.0.1/lit-element.js?module";const supportsButtonPressCardFeature = (stateObj) => { const domain = stateObj.entity_id.split(".")[0]; return domain === "button";};class ButtonPressCardFeature extends LitElement { static get properties() {  return {   hass: undefined,   config: undefined,   stateObj: undefined,  }; } static getStubConfig() {  return {   type: "custom:button-press-card-feature",   label: "Press",  }; } setConfig(config) {  if (!config) {   throw new Error("Invalid configuration");  }  this.config = config; } _press(ev) {  ev.stopPropagation();  this.hass.callService("button", "press", {   entity_id: this.stateObj.entity_id,  }); } render() {  if (   !this.config ||   !this.hass ||   !this.stateObj ||   !supportsButtonPressCardFeature(this.stateObj)  ) {   return null;  }  return html`   <button class="button" @click=${this._press}>    ${this.config.label || "Press"}   </button>  `; } static get styles() {  return css`   .button {    display: block;    height: var(--feature-height, 42px);    width: 100%;    border-radius: var(--feature-border-radius, 12px);    border: none;    background-color: #eeeeee;    cursor: pointer;    transition: background-color 180ms ease-in-out;   }   .button:hover {    background-color: #dddddd;   }   .button:focus {    background-color: #cdcdcd;   }  `; }}customElements.define("button-press-card-feature", ButtonPressCardFeature);window.customCardFeatures = window.customCardFeatures || [];window.customCardFeatures.push({ type: "button-press-card-feature", name: "Button press", supported: supportsButtonPressCardFeature, // Optional configurable: true, // Optional - defaults to false});
```

If you want your feature to better integrate with the default design of home assistant, you can use these CSS variables:
  * --feature-height: Recommended height (42px).
  * --feature-border-radius: Recommended border radius (12px). It be can useful to set button or slider border radius.
  * --feature-button-spacing: Recommended space between buttons (12px). It can be useful if you have multiple buttons in your feature.


The main difference with custom cards is the graphical configuration option. To have it displayed in the card editor, you must add an object describing it to the array window.customCardFeatures.
Required properties of the object are type and name. It is recommended to define the supported option with a function, so the editor can only propose the feature if it is compatible with the selected entity in the card. Set configurable to true if your entity has additional configuration (e.g. label option in the example above) so the editor.
Also, the static functions getConfigElement and getStubConfig work the same as with normal custom cards.





## Custom view layout | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/custom-ui/custom-view

On this page
By default Home Assistant will try to show the cards in a masonry layout (like Pinterest). A custom view layout allows developers to override this and define the layout mechanism (like a grid).
## API
You define your custom view as a . It's up to you to decide how to render your DOM inside your element. You can use Lit Element, Preact, or any other popular framework (except for React – ).
Custom Views receive the following:
```
interface LovelaceViewElement { hass?: HomeAssistant; lovelace?: Lovelace; index?: number; cards?: Array<LovelaceCard | HuiErrorCard>; badges?: LovelaceBadge[]; setConfig(config: LovelaceViewConfig): void;}
```

Cards and Badges will be created and maintained by the core code and given to the custom view. The custom views are meant to load the cards and badges and display them in a customized layout.
## Example
(note: this example does not have all of the properties but the necessities to show the example)
```
import { LitElement, html } from "https://unpkg.com/@polymer/lit-element@^0.6.1/lit-element.js?module";class MyNewView extends LitElement { setConfig(_config) {} static get properties() {  return {   cards: {type: Array, attribute: false}  }; } render() {  if(!this.cards) {   return html``;  }  return html`${this.cards.map((card) => html`<div>${card}</div>`)}`; }}
```

And you can define this element in the Custom Element Registry just as you would with a Custom Card:
```
customElements.define("my-new-view", MyNewView);
```

A custom view can be used by adding the following to the definition of your view:
```
- title: Home View type: custom:my-new-view badges: [...] cards: [...]
```

The default masonry view is an example of a layout element. ().
## Store custom data
If your view requires data to persist at a card level, there is a view_layout in the card configuration that can be used to store information. Example: Key, X and Y coordinates, width and height, etc. This can be useful when you need to store the location or dimensions of a card for your view.
```
- type: weather-card view_layout:  key: 1234  width: 54px entity: weather.my_weather
```

## Edit, delete, or add a card
To call the core frontend dialogs to edit, delete or add a card, you can simply call these three events:
```
Event: "ll-delete-card"Detail: { path: [number] | [number, number] }Event: "ll-edit-card"Detail: { path: [number] | [number, number] }Event: "ll-create-card"Detail: none
```

To call an event, you can use:
```
// Delete 4th card in the current viewthis.dispatchEvent(new CustomEvent("ll-edit-card", { detail: { path: [3] } })) // this refers to the card element
```




## Custom strategies | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/custom-ui/custom-strategy

On this page
Introduced in Home Assistant 2021.5.
Strategies are JavaScript functions that generate dashboard configurations. When a user has not created a dashboard configuration yet, an auto-generated dashboard is shown. That configuration is generated using a built-in strategy.
It's possible for developers to create their own strategies to generate dashboards. Strategies can use all of Home Assistant's data and the user's dashboard configuration to create something new.
A strategy can be applied to the whole configuration or to a specific view.
Strategies are defined as a custom element in a JavaScript file, and included . Home Assistant will call static functions on the class instead of rendering it as a custom element.
## Dashboard strategies
A dashboard strategy is responsible for generating a full dashboard configuration. This can either be from scratch, or based on an existing dashboard configuration that is passed in.
Two parameters are passed to the strategy:
Key| Description  
---|---  
config| Dashboard strategy configuration.  
hass| The Home Assistant object.  
```
class StrategyDemo { static async generate(config, hass) {  return {   title: "Generated Dashboard",   views: [    {     "cards": [      {       "type": "markdown",       "content": `Generated at ${(new Date).toLocaleString()}`      }     ]    }   ]  }; }}customElements.define("ll-strategy-my-demo", StrategyDemo);
```

Use the following dashboard configuration to use this strategy:
```
strategy: type: custom:my-demo
```

## View strategies
A view strategy is responsible for generating the configuration of a specific dashboard view. The strategy is invoked when the user opens the specific view.
Two parameters are passed to the strategy:
Key| Description  
---|---  
config| View strategy configuration.  
hass| The Home Assistant object.  
```
class StrategyDemo { static async generate(config, hass) {  return {   "cards": [    {     "type": "markdown",     "content": `Generated at ${(new Date).toLocaleString()}`    }   ]  }; }}customElements.define("ll-strategy-my-demo", StrategyDemo);
```

Use the following dashboard configuration to use this strategy:
```
views:- strategy:  type: custom:my-demo
```

## Full example
It's recommended for a dashboard strategy to leave as much work to be done to the view strategies. That way the dashboard will show up for the user as fast as possible. This can be done by having the dashboard generate a configuration with views that rely on its own strategy.
Below example will create a view per area, with each view showing all entities in that area in a grid.
```
class StrategyDashboardDemo { static async generate(config, hass) {  // Query all data we need. We will make it available to views by storing it in strategy options.  const [areas, devices, entities] = await Promise.all([   hass.callWS({ type: "config/area_registry/list" }),   hass.callWS({ type: "config/device_registry/list" }),   hass.callWS({ type: "config/entity_registry/list" }),  ]);  // Each view is based on a strategy so we delay rendering until it's opened  return {   views: areas.map((area) => ({    strategy: {     type: "custom:my-demo",     area,      devices,      entities,    },    title: area.name,    path: area.area_id,   })),  }; }}class StrategyViewDemo { static async generate(config, hass) {  const { area, devices, entities } = config;  const areaDevices = new Set();  // Find all devices linked to this area  for (const device of devices) {   if (device.area_id === area.area_id) {    areaDevices.add(device.id);   }  }  const cards = [];  // Find all entities directly linked to this area  // or linked to a device linked to this area.  for (const entity of entities) {   if (    entity.area_id     ? entity.area_id === area.area_id     : areaDevices.has(entity.device_id)   ) {    cards.push({     type: "button",     entity: entity.entity_id,    });   }  }  return {   cards: [    {     type: "grid",     cards,    },   ],  }; }}customElements.define("ll-strategy-dashboard-my-demo", StrategyDashboardDemo);customElements.define("ll-strategy-view-my-demo", StrategyViewDemo);
```

Use the following dashboard configuration to use this strategy:
```
strategy: type: custom:my-demo
```






## External authentication | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/external-authentication

On this page
By default, the frontend will take care of its own authentication tokens. If none are found, it will redirect the user to the login page and it will take care of updating the token.
If you want to embed the Home Assistant frontend in an external app, you will want to store the authentication inside the app but make it available to the frontend. To support this, Home Assistant exposes an external authentication API.
To activate this API, load the frontend with ?external_auth=1 appended to the URL. If this is passed in, Home Assistant will expect either window.externalApp (for Android) or window.webkit.messageHandlers (for iOS) to be defined containing the methods described below.
## Get access token
This API has been introduced in Home Assistant 0.78.
When the frontend loads, it will request an access token from the external authentication. It does so by calling one of the following methods with an options object. The options object defines the callback method to be called with the response and an optional force boolean which is set to true if the access token should be refreshed, regardless if it has expired or not.
The force boolean has been introduced in Home Assistant 0.104 and might not always be available.
```
window.externalApp.getExternalAuth({ callback: "externalAuthSetToken", force: true});// orwindow.webkit.messageHandlers.getExternalAuth.postMessage({ callback: "externalAuthSetToken", force: true});
```

The response should contain a boolean if it was successful and an object containing an access token and the number of seconds that it will remain valid. Pass the response to the function defined in the options object.
```
// To be called by external appwindow.externalAuthSetToken(true, { access_token: "qwere", expires_in: 1800});// If unable to get new access tokenwindow.externalAuthSetToken(false);
```

The frontend will call this method when the page first loads and whenever it needs a valid token but the previous received token has expired.
## Revoke token
This API has been introduced in Home Assistant 0.78.
When the user presses the logout button on the profile page, the external app will have to , and log the user out.
```
window.externalApp.revokeExternalAuth({ callback: "externalAuthRevokeToken"});// orwindow.webkit.messageHandlers.revokeExternalAuth.postMessage({ callback: "externalAuthRevokeToken"});
```

When done, the external app has to call the function defined in the options object.
```
// To be called by external appwindow.externalAuthRevokeToken(true);// If unable to logoutwindow.externalAuthRevokeToken(false);
```






## Home Assistant Supervisor | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/supervisor

On this page
The Supervisor allows the user to manage their Home Assistant installation from Home Assistant. The Supervisor has the following responsibilities:
## Architecture





## Miscellaneous | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/misc

Catch all category. Topics are not related to one another.



## Voice in Home Assistant | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/voice/overview

On this page
Building a voice assistant is a complex task. It requires a lot of different technologies to work together. This page will give you an overview of the different parts inside Home Assistant and how they will work together.
## Capturing the user's speech
The thing that the above diagram does not describe is how the user's speech is captured. There will be many ways to do this.
The ultimate goal is to make Voice Satellites. These are devices that can be placed anywhere in the house. Once it detects the hot word, it will capture the user's speech, send it to Home Assistant, and play the response back to the user.





## Contributing translation | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/translations

On this page
Translations for Home Assistant are managed through , an online translation management tool. Our translations are split between four projects: a backend project for platform-specific translations, a frontend project for UI translations, and two for the official companion apps. Click the links below to join the projects! Even if your language is completely translated, extra proofreading is a big help! Please feel free to review the existing translations, and vote for alternatives that might be more appropriate.
For more information about the translation editor and tools, please see the .
Translations are downloaded from Lokalise on every build, so all major, minor, beta releases and nightly builds will have the latest translations available.
## Translation placeholders
Some translation strings will contain special placeholders that will be replaced at runtime.
Placeholders defined in square brackets [] (shown in green in Lokalise) are . These are primarily used to link translation strings that will be duplicated, rather then redefining the same translation over and over again. Where sensible, the translation should make use of those (the square brackets placeholder value can be easily taken over by clicking on the "Source Alt+0" button in the Lokalise edit mode). Different languages may not have the same duplicates as English, and are welcome to link duplicate translations that are not linked in English.
Placeholders shown in curly brackets {} are that will be replaced with a live value when Home Assistant is running. Any translation argument placeholders present in the original string must be included in the translated string and must not be translated! These placeholders may include special syntax for defining plurals or other replacement rules. The above linked format.js guide explains the syntax for adding plural definitions and other rules.
## Rules
  1. Only native speakers should submit translations.
  2. Stick to .
  3. Don't translate or change proper nouns like Home Assistant, Supervisor or Hue.
  4. For a region-specific translation, keys that will be the same as the base translation should clone the source string. You can do this with Ctrl+Insert or selecting Insert Source in the interface. This helps keep track of what has, or has not been reviewed whilst also simplifying the workflow.
  5. Translations under the state_badge keys will be used for the notification badge display. These translations should be short enough to fit in the badge label without overflowing. This can be tested in the Home Assistant UI either by editing the label text with your browsers development tools, or by using the States tab of developer tools in the Home Assistant UI. In the UI, enter a new entity ID (device_tracker.test), and enter the text you want to test in state.
  6. If text will be duplicated across different translation keys, make use of the Lokalise key reference feature where possible. The base translation provides examples of this underneath the states translations. Please see the documentation for more details.


## Adding a new language
If your language is not listed you can request it at . Please provide both the English name and the native name for your language. For example:
```
English Name: GermanNative Name: Deutsch
```

info
Region specific translations (en-US, fr-CA) will only be included if translations for that region need to differ from the base language translation.
### Maintainer steps to add a new language
  1. Language tags have to follow . A list of most language tags can be found here: . Examples: fr, fr-CA, zh-Hans. Only include the country code if country specific overrides are being included, and the base language is already translated.
  2. Add the language tag and native name in src/translations/translationMetadata.json. Examples: "Français", "Français (CA)"
  3. Add the new language in Lokalise. Note: Sometimes you have to change the tag in Lokalise (Language -> Language settings -> custom ISO code).


## Language specific guidelines
Most languages have multiple possible translations of a sentence. Please take a look at the guidelines for your language here, where you can also find some typical mistakes to prevent. The sections are written in their corresponding languages, as this makes explaining the grammar easier and only native speakers should submit translations (see ).
### German
  * Du/Sie: Duze in den Übersetzungen, und verwende nicht das formale "Sie".


#### Typische Fehler
  * Achte auf den richtigen Imperativ. Der Imperativ ist die Befehlsform, z. B. "Gib mir das Wasser". Falsch wäre hier: "Gebe mir das Wasser" (siehe ).


### French
  * Blueprint: il a été décidé de ne pas traduire ce mot et de le considérer comme un nom propre. Cela évite les confusions avec les traductions de map et template et facilite la recherche de Blueprint à importer sur Internet. Il faut donc toujours utiliser Blueprint avec une majuscule.





## Built-in intents | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/intent_builtin

On this page
The following intents are supported:
  * HassTurnOn, HassTurnOff, HassGetState, HassNevermind, HassRespond, HassBroadcast, HassSetPosition, HassGetCurrentDate, HassGetCurrentTime, HassLightSet, HassClimateSetTemperature, HassClimateGetTemperature, HassShoppingListAddItem, HassShoppingListCompleteItem, HassGetWeather, HassListAddItem, HassListCompleteItem, HassVacuumStart, HassVacuumReturnToBase, HassMediaPause, HassMediaUnpause, HassMediaNext, HassMediaPrevious, HassSetVolume, HassMediaPlayerMute, HassMediaPlayerUnmute, HassSetVolumeRelative, HassMediaSearchAndPlay, HassStartTimer, HassCancelAllTimers, HassCancelTimer, HassIncreaseTimer, HassDecreaseTimer, HassPauseTimer, HassUnpauseTimer, HassTimerStatus, HassFanSetSpeed, HassLawnMowerStartMowing, HassLawnMowerDock


The following intents are deprecated:
  * HassOpenCover, HassCloseCover, HassToggle, HassHumidifierSetpoint, HassHumidifierMode, HassShoppingListLastItems


Slots
For HassTurnOn and HassTurnOff, the slots are optional.
Possible slot combinations are:
Slot combination| Example  
---|---  
name only| table light  
area only| kitchen  
area and name| living room reading light  
area and domain| kitchen lights  
area and device class| bathroom humidity  
device class and domain| carbon dioxide sensors  
## Supported intents
### HassTurnOn
Turns on a device or entity
Provided by the homeassistant integration.
### HassTurnOff
Turns off a device or entity
Provided by the homeassistant integration.
### HassGetState
Gets or checks the state of an entity
Provided by the homeassistant integration.
### HassNevermind
Does nothing. Used to cancel a request
Provided by the homeassistant integration.
### HassRespond
Returns response but takes no action
  * response - Text to respond with


Provided by the homeassistant integration.
### HassBroadcast
Announces a message on other satellites
  * message - Message to broadcast (required)


Provided by the assist_satellite integration.
### HassSetPosition
Sets the position of an entity
Provided by the homeassistant integration.
### HassGetCurrentDate
Gets the current date
Provided by the homeassistant integration.
### HassGetCurrentTime
Gets the current time
Provided by the homeassistant integration.
### HassLightSet
Sets the brightness or color of a light
Provided by the light integration.
### HassClimateSetTemperature
Sets the desired indoor temperature
Provided by the climate integration.
### HassClimateGetTemperature
Gets the actual indoor temperature (not the desired indoor temperature as set by HassClimateSetTemperature)
  * name - Name of a device or entity
  * area - Name of an area
  * floor - Name of a floor


Provided by the climate integration.
### HassShoppingListAddItem
Adds an item to the shopping list
  * item - Item to add (required)


Provided by the shopping_list integration.
### HassShoppingListCompleteItem
Checks off an item from the shopping list
  * item - Item to check off (required)


Provided by the shopping_list integration.
### HassGetWeather
Gets the current weather
  * name - Name of the weather entity to use


Provided by the weather integration.
### HassListAddItem
Adds an item to a todo list
  * item - Item to add (required)
  * name - Name of the list (required)


Provided by the todo integration.
### HassListCompleteItem
Checks off an item from a todo list
  * item - Item to check off (required)
  * name - Name of the list (required)


Provided by the todo integration.
### HassVacuumStart
Starts a vacuum
  * name - Name of a device or entity
  * area - Name of an area
  * floor - Name of a floor


Provided by the vacuum integration.
### HassVacuumReturnToBase
Returns a vacuum to base
  * name - Name of a device or entity
  * area - Name of an area


Provided by the vacuum integration.
### HassMediaPause
Pauses a media player
  * name - Name of a device or entity
  * area - Name of an area


Provided by the media_player integration.
### HassMediaUnpause
Unpauses a media player
  * name - Name of a device or entity
  * area - Name of an area


Provided by the media_player integration.
### HassMediaNext
Skips a media player to the next item
  * name - Name of a device or entity
  * area - Name of an area


Provided by the media_player integration.
### HassMediaPrevious
Skips a media player back to the previous item
  * name - Name of a device or entity
  * area - Name of an area


Provided by the media_player integration.
### HassSetVolume
Sets the volume of a media player
  * name - Name of a device or entity
  * area - Name of an area
  * volume_level - Volume level from 0 to 100 (required)


Provided by the media_player integration.
### HassMediaPlayerMute
Mutes a media player
  * name - Name of a device or entity


Provided by the media_player integration.
### HassMediaPlayerUnmute
Unmutes a media player
  * name - Name of a device or entity


Provided by the media_player integration.
### HassSetVolumeRelative
Increases or decreases the volume of a media player
Provided by the media_player integration.
### HassMediaSearchAndPlay
Searched for a media item and plays it
Provided by the media_player integration.
### HassStartTimer
Starts a timer
Provided by the homeassistant integration.
### HassCancelAllTimers
Cancels all timers
  * area - Area of the device used to start the timer


Provided by the homeassistant integration.
### HassCancelTimer
Cancels a timer
Provided by the homeassistant integration.
### HassIncreaseTimer
Adds time to a timer
Provided by the homeassistant integration.
### HassDecreaseTimer
Removes time from a timer
Provided by the homeassistant integration.
### HassPauseTimer
Pauses a running timer
Provided by the homeassistant integration.
### HassUnpauseTimer
Resumes a paused timer
Provided by the homeassistant integration.
### HassTimerStatus
Reports status of one or more timers
Provided by the homeassistant integration.
### HassFanSetSpeed
Set the speed of a fan
Provided by the fan integration.
### HassLawnMowerStartMowing
Starts a lawn mower
  * name - Name of a device or entity


Provided by the lawn_mower integration.
### HassLawnMowerDock
Sends a lawn mower to dock
  * name - Name of a device or entity


Provided by the lawn_mower integration.
## Deprecated intents
These are old intents that are not supported by template matching sentences and are planned to be removed or replaced.
### HassOpenCover
Deprecated; use HassTurnOn instead.
Open a cover.
Slot name| Type| Required| Description  
---|---|---|---  
name| string| Yes| Name of the cover entity to open.  
### HassCloseCover
Deprecated; use HassTurnOff instead.
Close a cover.
Slot name| Type| Required| Description  
---|---|---|---  
name| string| Yes| Name of the cover entity to close.  
### HassToggle
Toggle the state of an entity.
Slot name| Type| Required| Description  
---|---|---|---  
name| string| Yes| Name of the entity to toggle.  
### HassHumidifierSetpoint
Set target humidity.
Slot name| Type| Required| Description  
---|---|---|---  
name| string| Yes| Name of the entity to control.  
humidity| integer, 0-100| Yes| Target humidity to set.  
### HassHumidifierMode
Set humidifier mode if supported by the humidifier.
Slot name| Type| Required| Description  
---|---|---|---  
name| string| Yes| Name of the entity to control.  
mode| string| Yes| The mode to switch to.  
### HassShoppingListLastItems
List the last 5 items on the shopping list.
This intent has no slots.





## External bus | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/frontend/external-bus

On this page
The frontend is able to set up a message bus with an external app that is embedding the Home Assistant frontend. This system is a generalization of the , making it easier to add more commands in the future without extensive plumbing on either the app or frontend side.
## Message exchange
Just like external auth, message exchange is achieved by the external app making a JavaScript method available.
Messages are passed to the external app as serialized JSON objects. The function that will be called takes a single parameter: a string. The external app will have to process the message and deal with it accordingly (or ignore it).
On Android, your app needs to define the following method:
```
window.externalApp.externalBus(message: string)
```

On iOS, your app needs to define the following method:
```
window.webkit.messageHandlers.externalBus.postMessage(message: string);
```

To send messages to the frontend, serialize your message to JSON and call the following function from the external app:
```
window.externalBus(message: string)
```

## Message format
The message describes an action or a piece of information that the sender wants the receiver to do or know about. If it's an action, the sender will expect a response with the result of that action. A response to a command can either be successful or failed.
### Action and info message format
The format of a message that contains or provides information is the same. It contains an identifier, a type and an optional payload (depending on the type).
A result message will reuse the identifier in the response, to indicate to which action the response is related.
The basic format of a message is the following:
```
{ id: number; type: string; payload?: unknown;}
```

An example message:
```
{ "id": 5, "type": "config/get"}
```

### Result message format
If the message was an action, the sender will expect a response with the result. The response is either success or failure.
The type of result depends on the type of the message that it is responding to. For example, if it is responding to config/get, the result should be an object describing the configuration.
Message formats:
```
interface SuccessResult { id: number; type: "result"; success: true; result: unknown;}interface ErrorResult { id: number; type: "result"; success: false; error: {  code: string;  message: string; };}
```

## Supported messages
### Get external config
Available in: Home Assistant 0.92 Type: config/get Direction: frontend to external app. Expects answer: yes
Query the external app for the external configuration. The external configuration is used to customize the experience in the frontend.
Expected response payload:
```
{ hasSettingsScreen: boolean; canWriteTag: boolean;}
```

  * hasSettingsScreen set to true if the external app will show a configuration screen when it receives the command config_screen/show. If so, a new option will be added to the sidebar to trigger the configuration screen.
  * canWriteTag set to true if the external app is able to write tags and so can support the tag/write command.


### Show config screen config_screen/show
Available in: Home Assistant 0.92 Type: config_screen/show Direction: frontend to external app. Expect answer: no
Show the configuration screen of the external app.
### Connection status update connection-status
Available in: Home Assistant 0.92 Type: connection-status Direction: frontend to external app. Expect answer: no
Notify the external app if the frontend is connected to Home Assistant.
Payload structure:
```
{ event: "connected" | "auth-invalid" | "disconnected";}
```

### Trigger haptic haptic
Available in: Home Assistant 0.92 Type: haptic Direction: frontend to external app. Expect answer: no
Notify the external app to trigger haptic feedback.
Payload structure:
```
{ hapticType:  | "success"  | "warning"  | "failure"  | "light"  | "medium"  | "heavy"  | "selection";}
```

### Write tag tag/write
Available in: Home Assistant 0.115 Type: tag/write Direction: frontend to external app Expect answer: yes
Tell the external app to open the UI to write to a tag. Name is the name of the tag as entered by the user. The name is null if no name has been set.
```
{ tag: string; name: string | null;}
```

Expected response payload is an empty object for now. We might add more later:
```
{}
```




## Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/operating-system

On this page
The Home Assistant Operating System is a purpose built operating system specifically designed to run Home Assistant on single board computers and x86-64 systems. It aims to provide a robust and maintenance free operating system to run Home Assistant.
Home Assistant Operating System (HAOS) is using the build system. Buildroot is not a Linux distribution in the classic sense. It provides the infrastructure and build system to build a Linux distribution. Buildroot allows us to cross compile for different architectures which makes it especially useful when compiling for architectures which typically come with fewer resources such as Arm based systems. HAOS consists of a fairly regular stack of Linux and GNU software, using Linux, the GNU C library, systemd init daemon and the Docker container engine required by the Home Assistant Supervisor.
### Components





## Automation Trigger - Home Assistant

Source: https://www.home-assistant.io/docs/automation/trigger

#  On this page
Triggers are what starts the processing of an automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] rule. When any of the automation’s triggers becomes true (trigger fires), Home Assistant will validate the , if any, and call the .
An automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] can be triggered by an eventEvery time something happens in Home Assistant, an event is fired. There are different types of events, such as state change events, when an action was triggered, or the time changed. All entities produce state change events. Every time a state changes, a state change event is produced. Events can be used to trigger automations or scripts. For example, you can trigger an automation when a light is turned on, then a speaker turns on in that room. Events can also be used to trigger actions in the frontend. For example, you can trigger an action when a button is pressed. [Learn more], a certain entityAn entity represents a sensor, actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a device or a service. [Learn more] stateThe state holds the information of interest of an entity, for example, if a light is on or off. Each entity has exactly one state and the state only holds one value at a time. However, entities can store attributes related to that state such as brightness, color, or a unit of measurement. [Learn more], at a given time, and more. These can be specified directly or more flexible via templates. It is also possible to specify multiple triggers for one automation.
## Trigger ID 
All triggers can be assigned an optional id. If the ID is omitted, it will instead be set to the index of the trigger. The id can be referenced from . The id does not have to be unique for each trigger, and it can be used to group similar triggers for use later in the automation (i.e., several triggers of different types that should all turn some entity on).
### Video tutorial 
This video tutorial explains how trigger IDs work.
```
automation:
 triggers:
  - trigger: event
   event_type: "MY_CUSTOM_EVENT"
   id: "custom_event"
  - trigger: mqtt
   topic: "living_room/switch/ac"
   id: "ac_on"
  - trigger: state # This trigger will be assigned id="2"
   entity_id:
    - device_tracker.paulus
    - device_tracker.anne_therese
   to: "home"
```

YAML
Copy
## Trigger variables 
There are two different types of variables available for triggers. Both work like .
The first variant allows you to define variables that will be set when the trigger fires. The variables will be able to use templates and have access to .
The second variant is setting variables that are available when attaching a trigger when the trigger can contain templated values. These are defined using the trigger_variables key at an automation level. These variables can only contain . The triggers will not re-apply if the value of the template changes. Trigger variables are a feature meant to support using blueprint inputs in triggers.
```
automation:
 trigger_variables:
  my_event: example_event
 triggers:
  - trigger: event
   # Able to use `trigger_variables`
   event_type: "{{ my_event }}"
   # These variables are evaluated and set when this trigger is triggered
   variables:
    name: "{{ trigger.event.data.name }}"
```

YAML
Copy
## Event trigger 
An event trigger fires when an is being received. Events are the raw building blocks of Home Assistant. You can match events on just the event name or also require specific event data or context to be present.
Events can be fired by integrations or via the API. There is no limitation to the types. A list of built-in events can be found .
```
automation:
 triggers:
  - trigger: event
   event_type: "MY_CUSTOM_EVENT"
   # optional
   event_data:
    mood: happy
   context:
    user_id:
    # any of these will match
     - "MY_USER_ID"
     - "ANOTHER_USER_ID"
```

YAML
Copy
It is also possible to listen for multiple events at once. This is useful for event that contain no, or similar, data and contexts.
```
automation:
 triggers:
  - trigger: event
   event_type:
    - automation_reloaded
    - scene_reloaded
```

YAML
Copy
It’s also possible to use in the event_type, event_data and context options.
Important
The event_type, event_data and context templates are only evaluated when setting up the trigger, they will not be reevaluated for every event.
```
automation:
 trigger_variables:
  sub_event: ABC
  node: ac
  value: on
 triggers:
  - trigger: event
   event_type: "{{ 'MY_CUSTOM_EVENT_' ~ sub_event }}"
```

YAML
Copy
## Home Assistant trigger 
Fires when Home Assistant starts up or shuts down.
```
automation:
 triggers:
  - trigger: homeassistant
   # Event can also be 'shutdown'
   event: start
```

YAML
Copy
Note
Automations triggered by the shutdown event have 20 seconds to run, after which they are stopped to continue with the shutdown.
## MQTT trigger 
Fires when a specific message is received on given MQTT topic. Optionally can match on the payload being sent over the topic. The default payload encoding is ‘utf-8’. For images and other byte payloads use encoding: '' to disable payload decoding completely.
```
automation:
 triggers:
  - trigger: mqtt
   topic: "living_room/switch/ac"
   # Optional
   payload: "on"
   encoding: "utf-8"
```

YAML
Copy
The payload option can be combined with a value_template to process the message received on the given MQTT topic before matching it with the payload. The trigger in the example below will trigger only when the message received on living_room/switch/ac is valid JSON, with a key state which has the value "on".
```
automation:
 triggers:
  - trigger: mqtt
   topic: "living_room/switch/ac"
   payload: "on"
   value_template: "{{ value_json.state }}"
```

YAML
Copy
It’s also possible to use in the topic and payload options.
Note
The topic and payload templates are only evaluated when setting up the trigger, they will not be re-evaluated for every incoming MQTT message.
```
automation:
 trigger_variables:
  room: "living_room"
  node: "ac"
  value: "on"
 triggers:
  - trigger: mqtt
   topic: "{{ room ~ '/switch/' ~ node}}"
   # Optional
   payload: "{{ 'state:' ~ value }}"
   encoding: "utf-8"
```

YAML
Copy
## Numeric state trigger 
Fires when the numeric value of an entity’s state (or attribute’s value if using the attribute property, or the calculated value if using the value_template property) crosses a given threshold (equal excluded). On state change of a specified entity, attempts to parse the state as a number and fires if the value is changing from above to below or from below to above the given threshold (equal excluded).
Note
Crossing the threshold means that the trigger only fires if the state wasn’t previously within the threshold. If the current state of your entity is 50 and you set the threshold to below: 75, the trigger would not fire if the state changed to e.g. 49 or 72 because the threshold was never crossed. The state would first have to change to e.g. 76 and then to e.g. 74 for the trigger to fire.
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id: sensor.temperature
   # If given, will trigger when the value of the given attribute for the given entity changes..
   attribute: attribute_name
   # ..or alternatively, will trigger when the value given by this evaluated template changes.
   value_template: "{{ state.attributes.value - 5 }}"
   # At least one of the following required
   above: 17
   below: 25
   # If given, will trigger when the condition has been true for X time; you can also use days and milliseconds.
   for:
    hours: 1
    minutes: 10
    seconds: 5
```

YAML
Copy
Note
Listing above and below together means the numeric_state has to be between the two values. In the example above, the trigger would fire a single time if a numeric_state goes into the 17.1-24.9 range (above 17 and below 25). It will only fire again, once it has left the defined range and enters it again.
When the attribute option is specified the trigger is compared to the given attribute instead of the state of the entity.
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id: climate.kitchen
   attribute: current_temperature
   above: 23
```

YAML
Copy
More dynamic and complex calculations can be done with value_template. The variable ‘state’ is the of the entity specified by entity_id.
The state of the entity can be referenced like this:
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id: sensor.temperature
   value_template: "{{ state.state | float * 9 / 5 + 32 }}"
   above: 70
```

YAML
Copy
Attributes of the entity can be referenced like this:
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id: climate.kitchen
   value_template: "{{ state.attributes.current_temperature - state.attributes.temperature_set_point }}"
   above: 3
```

YAML
Copy
Number helpers (input_number entities), number, sensor, and zone entities that contain a numeric value, can be used in the above and below thresholds. However, the comparison will only be made when the entity specified in the trigger is updated. This would look like:
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id: sensor.outside_temperature
   # Other entity ids can be specified for above and/or below thresholds
   above: sensor.inside_temperature
```

YAML
Copy
The for: can also be specified as HH:MM:SS like this:
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id: sensor.temperature
   # At least one of the following required
   above: 17
   below: 25
   # If given, will trigger when condition has been for X time.
   for: "01:10:05"
```

YAML
Copy
You can also use templates in the for option.
```
automation:
 triggers:
  - trigger: numeric_state
   entity_id:
    - sensor.temperature_1
    - sensor.temperature_2
   above: 80
   for:
    minutes: "{{ states('input_number.high_temp_min')|int }}"
    seconds: "{{ states('input_number.high_temp_sec')|int }}"
 actions:
  - action: persistent_notification.create
   data:
    message: >
     {{ trigger.to_state.name }} too high for {{ trigger.for }}!
```

YAML
Copy
The for template(s) will be evaluated when an entity changes as specified.
Important
Use of the for option will not survive Home Assistant restart or the reload of automations. During restart or reload, automations that were awaiting for the trigger to pass, are reset.
If for your use case this is undesired, you could consider using the automation to set an to the desired time and then use that as an automation trigger to perform the desired actions at the set time.
## State trigger 
In general, the state trigger fires when the state of any of given entities changes. The behavior is as follows:
Tip
The values you see in your overview will often not be the same as the actual state of the entity. For instance, the overview may show Connected when the underlying entity is actually on. You should check the state of the entity by checking the states in the developer tool, under .
### Examples 
This automation triggers if either Paulus or Anne-Therese are home for one minute.
```
automation:
 triggers:
  - trigger: state
   entity_id:
    - device_tracker.paulus
    - device_tracker.anne_therese
   # Optional
   from: "not_home"
   # Optional
   to: "home"
   # If given, will trigger when the condition has been true for X time; you can also use days and milliseconds.
   for:
    hours: 0
    minutes: 1
    seconds: 0
```

YAML
Copy
It’s possible to give a list of from states or to states:
```
automation:
 triggers:
  - trigger: state
   entity_id: vacuum.test
   from:
    - "cleaning"
    - "returning"
   to: "error"
```

YAML
Copy
If you want to trigger on all state changes, but not on attribute changes, you can to to null (this would also work by setting from, not_from, or not_to to null):
```
automation:
 triggers:
  - trigger: state
   entity_id: vacuum.test
   to:
```

YAML
Copy
If you want to trigger on all state changes except specific ones, use not_from or not_to The not_from and not_to options are the counter parts of from and to. They can be used to trigger on state changes that are not the specified state.
```
automation:
 triggers:
  - trigger: state
   entity_id: vacuum.test
   not_from:
    - "unknown"
    - "unavailable"
   to: "on"
```

YAML
Copy
You cannot use from and not_from at the same time. The same applies to to and not_to.
### Triggering on attribute changes 
When the attribute option is specified, the trigger only fires when the specified attribute changes. Changes to other attributes or state changes are ignored.
For example, this trigger only fires when the boiler has been heating for 10 minutes:
```
automation:
 triggers:
  - trigger: state
   entity_id: climate.living_room
   attribute: hvac_action
   to: "heating"
   for: "00:10:00"
```

YAML
Copy
This trigger fires whenever the boiler’s hvac_action attribute changes:
```
automation:
 triggers:
  - trigger: state
   entity_id: climate.living_room
   attribute: hvac_action
```

YAML
Copy
### Holding a state or attribute 
You can use for to have the state trigger only fire if the state holds for some time.
This example fires, when the entity state changed to "on" and holds that state for 30 seconds:
```
automation:
 triggers:
  - trigger: state
   entity_id: light.office
   # Must stay "on" for 30 seconds
   to: "on"
   for: "00:00:30"
```

YAML
Copy
When holding a state, changes to attributes are ignored. Changes to attributes don’t cancel the hold time.
You can also fire the trigger when the state value changed from a specific state, but hasn’t returned to that state value for the specified time.
This can be useful, e.g., checking if a media player hasn’t turned “off” for the time specified, but doesn’t care about “playing” or “paused”.
```
automation:
 triggers:
  - trigger: state
   entity_id: media_player.kitchen
   # Not "off" for 30 minutes
   from: "off"
   for: "00:30:00"
```

YAML
Copy
Please note, that when using from, to and for, only the value of the to option is considered for the time specified.
In this example, the trigger fires if the state value of the entity remains the same for for the time specified, regardless of the current state value.
```
automation:
 triggers:
  - trigger: state
   entity_id: media_player.kitchen
   # The media player remained in its current state for 1 hour
   for: "01:00:00"
```

YAML
Copy
You can also use templates in the for option.
```
automation:
 triggers:
  - trigger: state
   entity_id:
    - device_tracker.paulus
    - device_tracker.anne_therese
   to: "home"
   for:
    minutes: "{{ states('input_number.lock_min')|int }}"
    seconds: "{{ states('input_number.lock_sec')|int }}"
 actions:
  - action: lock.lock
   target:
    entity_id: lock.my_place
```

YAML
Copy
The for template(s) will be evaluated when an entity changes as specified.
Tip
Use quotes around your values for from and to to avoid the YAML parser from interpreting values as booleans.
## Sun trigger 
### Sunset / Sunrise trigger 
Fires when the sun is setting or rising, i.e., when the sun elevation reaches 0°.
An optional time offset can be given to have it fire a set time before or after the sun event (e.g., 45 minutes before sunset). A negative value makes it fire before sunrise or sunset, a positive value afterwards. The offset needs to be specified in number of seconds, or in a hh:mm:ss format.
Tip
Since the duration of twilight is different throughout the year, it is recommended to use instead of sunset or sunrise with a time offset to trigger automations during dusk or dawn.
```
automation:
 triggers:
  - trigger: sun
   # Possible values: sunset, sunrise
   event: sunset
   # Optional time offset. This example will trigger 45 minutes before sunset.
   offset: "-00:45:00"
```

YAML
Copy
### Sun elevation trigger 
Sometimes you may want more granular control over an automation than simply sunset or sunrise and specify an exact elevation of the sun. This can be used to layer automations to occur as the sun lowers on the horizon or even after it is below the horizon. This is also useful when the “sunset” event is not dark enough outside and you would like the automation to run later at a precise solar angle instead of the time offset such as turning on exterior lighting. For most automations intended to run during dusk or dawn, a number between 0° and -6° is suitable; -4° is used in this example:
```
automation:
 - alias: "Exterior Lighting on when dark outside"
  triggers:
   - trigger: numeric_state
    entity_id: sun.sun
    attribute: elevation
    # Can be a positive or negative number
    below: -4.0
  actions:
   - action: switch.turn_on
    target:
     entity_id: switch.exterior_lighting
```

YAML
Copy
If you want to get more precise, you can use this , which will help you estimate what the solar elevation will be at any specific time. Then from this, you can select from the defined twilight numbers.
Although the actual amount of light depends on weather, topography and land cover, they are defined as:
  * Civil twilight: 0° > Solar angle > -6°
This is what is meant by twilight for the average person: Under clear weather conditions, civil twilight approximates the limit at which solar illumination suffices for the human eye to clearly distinguish terrestrial objects. Enough illumination renders artificial sources unnecessary for most outdoor activities.
  * Nautical twilight: -6° > Solar angle > -12°
  * Astronomical twilight: -12° > Solar angle > -18°


A very thorough explanation of this is available in the Wikipedia article about the .
## Tag trigger 
Fires when a is scanned. For example, a NFC tag is scanned using the Home Assistant Companion mobile application.
```
automation:
 triggers:
  - trigger: tag
   tag_id: A7-6B-90-5F
```

YAML
Copy
Additionally, you can also only trigger if a card is scanned by a specific device/scanner by setting the device_id:
```
automation:
 triggers:
  - trigger: tag
   tag_id: A7-6B-90-5F
   device_id: 0e19cd3cf2b311ea88f469a7512c307d
```

YAML
Copy
Or trigger on multiple possible devices for multiple tags:
```
automation:
 triggers:
  - trigger: tag
   tag_id:
    - "A7-6B-90-5F"
    - "A7-6B-15-AC"
   device_id:
    - 0e19cd3cf2b311ea88f469a7512c307d
    - d0609cb25f4a13922bb27d8f86e4c821
```

YAML
Copy
## Template trigger 
Template triggers work by evaluating a when any of the recognized entities change state. The trigger will fire if the state change caused the template to render ‘true’ (a non-zero number or any of the strings true, yes, on, enable) when it was previously ‘false’ (anything else).
This is achieved by having the template result in a true boolean expression (for example {{ is_state('device_tracker.paulus', 'home') }}) or by having the template render true (example below).
With template triggers you can also evaluate attribute changes by using is_state_attr (like {{ is_state_attr('climate.living_room', 'away_mode', 'off') }})
```
automation:
 triggers:
  - trigger: template
   value_template: "{% if is_state('device_tracker.paulus', 'home') %}true{% endif %}"
   # If given, will trigger when template remains true for X time.
   for: "00:01:00"
```

YAML
Copy
You can also use templates in the for option.
```
automation:
 triggers:
  - trigger: template
   value_template: "{{ is_state('device_tracker.paulus', 'home') }}"
   for:
    minutes: "{{ states('input_number.minutes')|int(0) }}"
```

YAML
Copy
The for template(s) will be evaluated when the value_template becomes ‘true’.
Templates that do not contain an entity will be rendered once per minute.
Important
Use of the for option will not survive Home Assistant restart or the reload of automations. During restart or reload, automations that were awaiting for the trigger to pass, are reset.
If for your use case this is undesired, you could consider using the automation to set an to the desired time and then use that as an automation trigger to perform the desired actions at the set time.
## Time trigger 
The time trigger is configured to fire once a day at a specific time, or at a specific time on a specific date. There are three allowed formats:
### Time string 
A string that represents a time to fire on each day. Can be specified as HH:MM or HH:MM:SS. If the seconds are not specified, :00 will be used.
```
automation:
 - triggers:
  - trigger: time
   # 24-hour time format. This trigger will fire at 3:32 PM
   at: "15:32:00"
```

YAML
Copy
### Input datetime 
The entity ID of an .
has_date | has_time | Description  
---|---|---  
true | true | Will fire at specified date & time.  
true | false | Will fire at midnight on specified date.  
false | true | Will fire once a day at specified time.  
```
automation:
 - triggers:
   - trigger: state
    entity_id: binary_sensor.motion
    to: "on"
  actions:
   - action: climate.turn_on
    target:
     entity_id: climate.office
   - action: input_datetime.set_datetime
    target:
     entity_id: input_datetime.turn_off_ac
    data:
     datetime: >
      {{ (now().timestamp() + 2*60*60)
        | timestamp_custom('%Y-%m-%d %H:%M:%S') }}
 - triggers:
   - trigger: time
    at: input_datetime.turn_off_ac
  actions:
   - action: climate.turn_off
    target:
     entity_id: climate.office
```

YAML
Copy
### Sensors of datetime device class 
The Entity ID of a with the “timestamp” device class.
```
automation:
 - triggers:
   - trigger: time
    at: sensor.phone_next_alarm
  actions:
   - action: light.turn_on
    target:
     entity_id: light.bedroom
```

YAML
Copy
### Sensors of datetime device class with offsets 
When the time is provided using a sensor of the timestamp device class, an offset can be provided. This offset will be added to (or subtracted from when negative) the sensor value.
For example, this trigger fires 5 minutes before the phone alarm goes off.
```
automation:
 - triggers:
   - trigger: time
    at:
     entity_id: sensor.phone_next_alarm
     offset: -00:05:00
  actions:
   - action: light.turn_on
    target:
     entity_id: light.bedroom
```

YAML
Copy
Important
When using a positive offset the trigger might never fire. This is due to the sensor changing before the offset is reached. For example, when using a phone alarm as a trigger, the sensor value will change to the new alarm time when the alarm goes off, which means this trigger will change to the new time as well.
### Multiple times 
Multiple times can be provided in a list. All formats can be intermixed.
```
automation:
 triggers:
  - trigger: time
   at:
    - input_datetime.leave_for_work
    - "18:30:00"
    - entity_id: sensor.bus_arrival
     offset: "-00:10:00"
```

YAML
Copy
### Limited templates 
It’s also possible to use for times.
```
blueprint:
 input:
  alarm:
   name: Alarm
   selector:
    text:
  hour:
   name: Hour
   selector:
    number:
     min: 0
     max: 24
 trigger_variables:
  my_alarm: !input alarm
  my_hour: !input hour
 trigger:
  - platform: time
   at:
   - "sensor.{{ my_alarm | slugify }}_time"
   - "{{ my_hour }}:30:00"
```

YAML
Copy
### Weekday filtering 
Time triggers can be filtered to fire only on specific days of the week using the weekday option. This allows you to create automations that only run on certain days, such as weekdays or weekends.
The weekday option accepts:
  * A single weekday as a string: "mon", "tue", "wed", "thu", "fri", "sat", "sun" 
  * A list of weekdays using the expanded format


#### Single weekday 
This example will turn on the lights only on Mondays at 8:00 AM:
```
automation:
 - triggers:
   - trigger: time
    at: "08:00:00"
    weekday: "mon"
  actions:
   - action: light.turn_on
    target:
     entity_id: light.bedroom
```

YAML
Copy
#### Multiple weekdays 
This example will run a morning routine only on weekdays (Monday through Friday) at 6:30 AM:
```
automation:
 - triggers:
   - trigger: time
    at: "06:30:00"
    weekday:
     - "mon"
     - "tue"
     - "wed"
     - "thu"
     - "fri"
  actions:
   - action: script.morning_routine
```

YAML
Copy
#### Weekend example 
This example demonstrates a different wake-up time for weekends:
```
automation:
 - alias: "Weekday alarm"
  triggers:
   - trigger: time
    at: "06:30:00"
    weekday:
     - "mon"
     - "tue"
     - "wed"
     - "thu"
     - "fri"
  actions:
   - action: script.weekday_morning
 - alias: "Weekend alarm"
  triggers:
   - trigger: time
    at: "08:00:00"
    weekday:
     - "sat"
     - "sun"
  actions:
   - action: script.weekend_morning
```

YAML
Copy
#### Combined with input datetime 
The weekday option works with all time formats, including input datetime entities:
```
automation:
 - triggers:
   - trigger: time
    at: input_datetime.work_start_time
    weekday:
     - "mon"
     - "tue"
     - "wed"
     - "thu"
     - "fri"
  actions:
   - action: notify.mobile_app
    data:
     title: "Work Day!"
     message: "Time to start working"
```

YAML
Copy
## Time pattern trigger 
With the time pattern trigger, you can match if the hour, minute or second of the current time matches a specific value. You can prefix the value with a / to match whenever the value is divisible by that number. You can specify * to match any value.
```
automation:
 triggers:
  - trigger: time_pattern
   # Matches every hour at 5 minutes past whole
   minutes: 5
automation 2:
 triggers:
  - trigger: time_pattern
   # Trigger once per minute during the hour of 3
   hours: "3"
   minutes: "*"
automation 3:
 triggers:
  - trigger: time_pattern
   # You can also match on interval. This will match every 5 minutes
   minutes: "/5"
```

YAML
Copy
Note
Do not prefix numbers with a zero - using '01' instead of '1' for example will result in errors.
## Persistent notification trigger 
Persistent notification triggers are fired when a persistent_notification is added or removed that matches the configuration options.
```
automation:
 triggers:
  - trigger: persistent_notification
   update_type:
    - added
    - removed
   notification_id: invalid_config
```

YAML
Copy
See the integration for more details on event triggers and the additional event data available for use by an automation.
## Webhook trigger 
Webhook trigger fires when a web request is made to the webhook endpoint: /api/webhook/<webhook_id>. The webhook endpoint is created automatically when you set it as the webhook_id in an automation trigger. The webhook_id can either be a static value or computed using .
Note
The webhook_id template is only evaluated when setting up the trigger, they will not be re-evaluated for incoming webhook triggers.
```
automation:
 trigger_variables:
  webhook_id_variable: "template_webhook_id"
 triggers:
  - trigger: webhook
   webhook_id: "some_hook_id"
   allowed_methods:
    - POST
    - PUT
   local_only: true
  - trigger: webhook
   webhook_id: ""
   allowed_methods:
    - POST
```

YAML
Copy
You can run this automation by sending an HTTP POST request to http://your-home-assistant:8123/api/webhook/some_hook_id. Here is an example using the curl command line program, with an example form data payload:
```
curl -X POST -d 'key=value&key2=value2' https://your-home-assistant:8123/api/webhook/some_hook_id
```

Bash
Copy
Webhooks support HTTP POST, PUT, HEAD, and GET requests; PUT requests are recommended. HTTP GET and HEAD requests are not enabled by default but can be enabled by adding them to the allowed_methods option. The request methods can also be configured in the UI by clicking the settings gear menu button beside the Webhook ID.
By default, webhook triggers can only be accessed from devices on the same network as Home Assistant or via . The local_only option should be set to false to allow webhooks to be triggered directly via the internet. This option can also be configured in the UI by clicking the settings gear menu button beside the Webhook ID.
Remember to use an HTTPS URL if you’ve secured your Home Assistant installation with SSL/TLS.
Note that a given webhook can only be used in one automation at a time. That is, only one automation trigger can use a specific webhook ID.
### Webhook data 
Payloads may either be encoded as form data or JSON. Depending on that, its data will be available in an automation template as either trigger.data or trigger.json. URL query parameters are also available in the template as trigger.query.
Note that to use JSON encoded payloads, the Content-Type header must be set to application/json, e.g.:
```
curl -X POST -H "Content-Type: application/json" -d '{ "key": "value" }' https://your-home-assistant:8123/api/webhook/some_hook_id
```

Bash
Copy
### Webhook security 
Webhook endpoints don’t require authentication, other than knowing a valid webhook ID. Security best practices for webhooks include:
## Zone trigger 
Zone trigger fires when an entity is entering or leaving the zone. The entity can be either a person, or a device_tracker. For zone automation to work, you need to have setup a device tracker platform that supports reporting GPS coordinates. This includes , the and the .
```
automation:
 triggers:
  - trigger: zone
   entity_id: person.paulus
   zone: zone.home
   # Event is either enter or leave
   event: enter # or "leave"
```

YAML
Copy
## Geolocation trigger 
Geolocation trigger fires when an entity is appearing in or disappearing from a zone. Entities that are created by a platform support reporting GPS coordinates. Because entities are generated and removed by these platforms automatically, the entity ID normally cannot be predicted. Instead, this trigger requires the definition of a source, which is directly linked to one of the Geolocation platforms.
Tip
This isn’t for use with device_tracker entities. For those look above at the zone trigger.
```
automation:
 triggers:
  - trigger: geo_location
   source: nsw_rural_fire_service_feed
   zone: zone.bushfire_alert_zone
   # Event is either enter or leave
   event: enter # or "leave"
```

YAML
Copy
## Device triggers 
Device triggers encompass a set of events that are defined by an integration. This includes, for example, state changes of sensors as well as button events from remotes. are set up through autodiscovery.
In contrast to state triggers, device triggers are tied to a device and not necessarily an entity. To use a device trigger, set up an automation through the browser frontend. If you would like to use a device trigger for an automation that is not managed through the browser frontend, you can copy the YAML from the trigger widget in the frontend and paste it into your automation’s trigger list.
## Calendar trigger 
Calendar trigger fires when a event starts or ends, allowing for much more flexible automations than using the Calendar entity state which only supports a single event start at a time.
An optional time offset can be given to have it fire a set time before or after the calendar event (e.g., 5 minutes before event start).
```
automation:
 triggers:
  - trigger: calendar
   # Possible values: start, end
   event: start
   # The calendar entity_id
   entity_id: calendar.light_schedule
   # Optional time offset
   offset: "-00:05:00"
```

YAML
Copy
See the integration for more details on event triggers and the additional event data available for use by an automation.
## Sentence trigger 
A sentence trigger fires when matches a sentence from a voice assistant using the default . Sentence triggers work with Home Assistant Assist. They will not work with external conversation agents such as OpenAI or Google Generative AI unless “Prefer handling commands locally” is enabled in the conversation agent settings.
Sentences are allowed to use some basic like optional and alternative words. For example, [it's ]party time will match both “party time” and “it’s party time”.
```
automation:
 triggers:
  - trigger: conversation
   command:
    - "[it's ]party time"
    - "happy (new year|birthday)"
```

YAML
Copy
The sentences matched by this trigger will be:
Punctuation and casing are ignored, so “It’s PARTY TIME!!!” will also match.
### Related topic 


### Sentence wildcards 
Adding one or more {lists} to your trigger sentences will capture any text at that point in the sentence. A slots object will be . This allows you to match sentences with variable parts, such as album/artist names or a description of a picture.
For example, the sentence play {album} by {artist} will match “play the white album by the beatles” and have the following variables available in the action templates:
  * {{ trigger.slots.album }} - “the white album”
  * {{ trigger.slots.artist }} - “the beatles”


Wildcards will match as much text as possible, which may lead to surprises: “play day by day by taken by trees” will match album as “day” and artist as “day by taken by trees”. Including extra words in your template can help: play {album} by artist {artist} can now correctly match “play day by day by artist taken by trees”.
## Multiple triggers 
It is possible to specify multiple triggers for the same rule. To do so just prefix the first line of each trigger with a dash (-) and indent the next lines accordingly. Whenever one of the triggers fires, processing of your automation rule begins.
```
automation:
 triggers:
  # first trigger
  - trigger: time_pattern
   minutes: 5
   # our second trigger is the sunset
  - trigger: sun
   event: sunset
```

YAML
Copy
## Multiple entity IDs for the same trigger 
It is possible to specify multiple entities for the same trigger. To do so add multiple entities using a nested list. The trigger will fire and start, processing your automation each time the trigger is true for any entity listed.
```
automation:
 triggers:
  - trigger: state
   entity_id:
    - sensor.one
    - sensor.two
    - sensor.three
```

YAML
Copy
## Disabling a trigger 
Every individual trigger in an automation can be disabled, without removing it. To do so, add enabled: false to the trigger. For example:
```
# Example script with a disabled trigger
automation:
 triggers:
  # This trigger will not trigger, as it is disabled.
  # This automation does not run when the sun is set.
  - enabled: false
   trigger: sun
   event: sunset
  # This trigger will fire, as it is not disabled.
  - trigger: time
   at: "15:32:00"
```

YAML
Copy
Triggers can also be disabled based on limited templates or blueprint inputs. These are only evaluated once when the automation is loaded.
```
blueprint:
 input:
  input_boolean:
   name: Boolean
   selector:
    boolean:
  input_number:
   name: Number
   selector:
    number:
     min: 0
     max: 100
 trigger_variables:
  _enable_number: !input input_number
 triggers:
  - trigger: sun
   event_type: sunrise
   enabled: !input input_boolean
  - trigger: sun
   event_type: sunset
   enabled: "{{ _enable_number < 50 }}"
```

YAML
Copy
## Merging lists of triggers 
Caution
This feature requires Home Assistant version 2024.10 or later. If using this in a blueprint, set the min_version for the blueprint to at least this version. See the for more details.
In some advanced cases (like for blueprints with trigger selectors), it may be necessary to insert a second list of triggers into the main trigger list. This can be done by adding a dictionary in the main trigger list with the sole key triggers, and the value for that key contains a second list of triggers. These will then be flattened into a single list of triggers. For example:
```
blueprint:
 name: Nested Trigger Blueprint
 domain: automation
 input:
  usertrigger:
   selector:
    trigger:
triggers:
 - trigger: event
  event_type: manual_event
 - triggers: !input usertrigger
```

YAML
Copy
This blueprint automation can then be triggered either by the fixed manual_event trigger, or additionally by any triggers selected in the trigger selector. This is also applicable for wait_for_trigger action.
## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Customizing entities - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/customizing-devices

#  On this page


After adding a new device, you might find the automatically assigned entity ID too technical and the entity lacking a friendly name. You can personalize these elements to better fit your naming conventions or modify other attributes like the icon.
To change entity attributes, follow these steps:
  1. Go to and select the entity from the list.
  2. In the top-right corner, select the cog icon.
  3. Enter or edit the attributes:
  4. To apply the changes, select Update.
  5. If you have used this entity in automations and scripts, you need to rename the entity ID there, too.
     * Go to open the respective tab and find your automation or script.


### Customizing an entity in YAML 
If your entity is not supported, or you could not customize what you need via the user interface, you need to edit the settings in your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file. For a detailed description of the entity configuration variables and information, refer to the .
## Related topics 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Packages - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/packages

#  On this page


Packages in Home Assistant provide a way to bundle configurations from multiple integrations. With packages, we have a way to include multiple integrations, or parts of integrations using any of the !include directives introduced in .
Packages are configured under the core homeassistant/packages in the configuration and take the format of a package name (no spaces, all lower case) followed by a dictionary with the package configuration. For example, package pack_1 would be created as:
```
homeassistant:
 ...
 packages:
  pack_1:
   ...package configuration here...
```

YAML
Copy
The package configuration can include: switch, light, automation, groups, or most other Home Assistant integrations including hardware platforms.
It can be specified inline or in a separate YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] file using !include.
Inline example, main configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more]:
```
homeassistant:
 ...
 packages:
  pack_1:
   switch:
    - platform: rest
     ...
   light:
    - platform: rpi
     ...
```

YAML
Copy
Include example, main configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more]:
```
homeassistant:
 ...
 packages:
  pack_1: !include my_package.yaml
```

YAML
Copy
The file my_package.yaml contains the “top-level” configuration:
```
switch:
 - platform: rest
  ...
light:
 - platform: rpi
  ...
```

YAML
Copy
There are some rules for packages that will be merged:
  1. Platform based integrations (light, switch, etc) can always be merged.
  2. Integrations where entities are identified by a key that will represent the entity_id ({key: config}) need to have unique ‘keys’ between packages and the main configuration file.
For example if we have the following in the main configuration. You are not allowed to re-use “my_input” again for input_boolean in a package:
```
input_boolean:
 my_input:
```

YAML
Copy
  3. Any integration that is not a platform [1], or dictionaries with Entity ID keys [2] can only be merged if its keys, except those for lists, are solely defined once.


Tip
Integrations inside packages can only specify platform entries using configuration style 1, where all the platforms are grouped under the integration name.
## Create a packages folder 
One way to organize packages is to create a folder named “packages” in your Home Assistant configuration directory. In the packages directory, you can store any number of packages in a YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] file. This entry in your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] will load all YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more]-files in this packages folder and its subfolders:
```
homeassistant:
 packages: !include_dir_named packages
```

YAML
Copy
The benefit of this approach is to pull all configurations required to integrate a system into one file—rather than keeping them spread across several files. You can use other !include methods for packages; for example !include_dir_merge_named. However, unlike !include_dir_merge_named, the !include_dir_named method uses the same indentation as the ‘configuration.yaml’. This means that you can copy and paste elements from the config file. With !include_dir_named, the file name is used as the package name. File names must be unique.
With the !include_dir_merge_named method, the package name has to be included in the file. The configuration below then needs to be indented accordingly. This means you cannot directly copy and paste from the configuration file.
```
homeassistant:
 packages: !include_dir_merge_named packages/
```

YAML
Copy
and in packages/subsystem1/functionality1.yaml:
```
subsystem1_functionality1:
 input_boolean:
 ...
 binary_sensor:
 ...
 automation:
```

YAML
Copy
## Customizing entities with packages 
It is possible to within packages. Just create your customization entries under:
```
homeassistant:
 customize:
```

YAML
Copy
Important
If you are moving configuration to packages, auth_providers must stay within ‘configuration.yaml’. See the general documentation for .
This is because Home Assistant processes the authentication provided early in the start-up process, even before packages are processed.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page





## Splitting up the configuration - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/splitting_configuration

#  On this page
So you’ve been using Home Assistant for a while now and your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] file brings people to tears because it has become so large. Or, you simply want to start off with the distributed approach. Here’s how to split the configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] into more manageable (read: human-readable) pieces.
## Example configuration files for inspiration 
First off, several community members have sanitized (read: without API keys/passwords) versions of their configurations available for viewing. You can see a .
As commenting code doesn’t always happen, please read on to learn in detail how configuration files can be structured.
## Analyzing the configuration files 
In this section, we are going use some example configuration files and look at their structure and format in more detail.
Now you might think that the configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] will be replaced during the splitting process. However, it will in fact remain, albeit in a much less cluttered form.
### The core configuration file 
In this lighter version, we will still need what could be called the core snippet:
```
homeassistant:
 # Name of the location where Home Assistant is running
 name: "My Home Assistant Instance"
 # Location required to calculate the time the sun rises and sets
 latitude: 37
 longitude: -121
 # 'metric' for Metric, 'us_customary' for US Customary
 unit_system: us_customary
 # Pick yours from here: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
 time_zone: "America/Los_Angeles"
 customize: !include customize.yaml
```

YAML
Copy
### Indentation, includes, comments, and modularization 
Note that each line after homeassistant: is indented two (2) spaces. Since the configuration files in Home Assistant are based on the YAML language, indentation and spacing are important. Also note that seemingly strange entry under customize:.
!include customize.yaml is the statement that tells Home Assistant to insert the parsed contents of customize.yaml at that point. The contents of the included file must be yaml data that is valid at the location it is included. This is how we are going to break a monolithic and hard to read file (when it gets big) into more manageable chunks.
Now before we start splitting out the different components, let’s look at the other integrations (in our example) that will stay in the base file:
```
history:
frontend:
logbook:
http:
 api_password: "ImNotTelling!"
ifttt:
 key: ["nope"]
mqtt:
 sensor:
  - name: "test sensor 1"
   state_topic: "test/some_topic1"
  - name: "test sensor 2"
   state_topic: "test/some_topic2"
```

YAML
Copy
As with the core snippet, indentation makes a difference:
#### Comments 
The # symbol (hash/pound) represents a “comment” as far as the commands are interpreted. Put another way, any line prefixed with a # will be ignored by the software. It is for humans only. Comments allow breaking up files for readability, as well as turning off features while leaving the entry intact.
#### Modularization and granularity 
While some of these integrations could technically be moved to a separate file, they are so small or “one off’s” where splitting them off is superfluous.
Now, lets assume that a blank file has been created in the Home Assistant configuration directory for each of the following:
```
automation.yaml
zone.yaml
sensor.yaml
switch.yaml
device_tracker.yaml
customize.yaml
```

Text
Copy
automation.yaml will hold all the automation integration details. zone.yaml will hold the zone integration details and so forth. These files can be called anything but giving them names that match their function will make things easier to keep track of.
Inside the base configuration file, add the following entries:
```
automation: !include automation.yaml
zone: !include zone.yaml
sensor: !include sensor.yaml
switch: !include switch.yaml
device_tracker: !include device_tracker.yaml
```

YAML
Copy
#### Include statements and packages to split files 
Nesting !include statements (having an !include within a file that is itself !included) will also work.
Some integrations support multiple top-level !include statements. This includes integrations defining an IoT domain. For example, light, switch, or sensor; as well as the automation, script, and template integrations, if you give a different label to each one.
Configuration for other integrations can instead be split up by using packages. To learn more about packages, see the page.
#### Top level keys 
Example of multiple top-level keys for the light platform.
```
light:
- platform: group
 name: "Bedside Lights"
 entities:
  - light.left_bedside_light
  - light.right_bedside_light
# define more light groups in a separate file
light groups: !include light-groups.yaml
# define some light switch mappings in a different file
light switches: !include light-switches.yaml
```

YAML
Copy
where light-groups.yaml might look like:
```
- platform: group
 name: "Outside Lights"
 entities:
  - light.porch_lights
  - light.patio_lights
```

YAML
Copy
with light-switches.yaml containing:
```
- platform: switch
 name: "Patio Lights"
 entity_id: switch.patio_lights
- platform: switch
 name: "Floor Lamp"
 entity_id: switch.floor_lamp_plug
```

YAML
Copy
Alright, so we’ve got the single integrations and the include statements in the base file, what goes in those extra files?
Let’s look at the device_tracker.yaml file from our example:
```
- platform: owntracks
- platform: nmap_tracker
 home_interval: 3
 hosts: 192.168.2.0/24
 track_new_devices: true
 interval_seconds: 40
 consider_home: 120
```

YAML
Copy
This small example illustrates how the “split” files work. In this case, we start with two (2) device tracker entries (owntracks and nmap). These files follow that is to say a fully left aligned leading entry (- platform: owntracks) followed by the parameter entries indented two (2) spaces.
This (large) sensor configuration gives us another example:
```
### sensor.yaml
### METEOBRIDGE #############################################
- platform: tcp
 name: "Outdoor Temp (Meteobridge)"
 host: 192.168.2.82
 timeout: 6
 payload: "Content-type: text/xml; charset=UTF-8\n\n"
 value_template: "{{value.split (' ')[2]}}"
 unit: C
- platform: tcp
 name: "Outdoor Humidity (Meteobridge)"
 host: 192.168.2.82
 port: 5556
 timeout: 6
 payload: "Content-type: text/xml; charset=UTF-8\n\n"
 value_template: "{{value.split (' ')[3]}}"
 unit: Percent
#### STEAM FRIENDS ##################################
- platform: steam_online
 api_key: ["not telling"]
 accounts:
  - 76561198012067051
#### TIME/DATE ##################################
- platform: time_date
 display_options:
  - "time"
  - "date"
- platform: worldclock
 time_zone: Etc/UTC
 name: "UTC"
- platform: worldclock
 time_zone: America/New_York
 name: "Ann Arbor"
```

YAML
Copy
You’ll notice that this example includes a secondary parameter section (under the steam section) as well as a better example of the way comments can be used to break down files into sections.
All of the above can be applied when splitting up files using packages. To learn more about packages, see the page.
That about wraps it up.
If you have issues, check the file indentations and check . If all else fails, head over to our and ask away.
## Debugging configuration files 
If you have many configuration files, Home Assistant provides a CLI that allows you to see how it interprets them. Each installation type has its own section in the common-tasks about this:


## Advanced usage 
We offer four advanced options to include whole directories at once. Please note that your files must have the .yaml file extension; .yml is not supported.
This will allow you to !include files with .yml extensions from within the .yaml files; without those .yml files being imported by the following commands themselves.
These work recursively. As an example using !include_dir_list automation, will include all 6 files shown below:
```
.
└── .homeassistant
  ├── automation
  │  ├── lights
  │  │  ├── turn_light_off_bedroom.yaml
  │  │  ├── turn_light_off_lounge.yaml
  │  │  ├── turn_light_on_bedroom.yaml
  │  │  └── turn_light_on_lounge.yaml
  │  ├── say_hello.yaml
  │  └── sensors
  │    └── react.yaml
  └── configuration.yaml (not included)
```

Bash
Copy
### Example: !include_dir_list 
configuration.yaml
```
automation:
 - alias: "Automation 1"
  triggers:
   - trigger: state
    entity_id: device_tracker.iphone
    to: "home"
  actions:
   - action: light.turn_on
    target:
     entity_id: light.entryway
 - alias: "Automation 2"
  triggers:
   - trigger: state
    entity_id: device_tracker.iphone
    from: "home"
  actions:
   - action: light.turn_off
    target:
     entity_id: light.entryway
```

YAML
Copy
can be turned into:
configuration.yaml
```
automation: !include_dir_list automation/presence/
```

YAML
Copy
automation/presence/automation1.yaml
```
alias: "Automation 1"
triggers:
 - trigger: state
  entity_id: device_tracker.iphone
  to: "home"
actions:
 - action: light.turn_on
  target:
   entity_id: light.entryway
```

YAML
Copy
automation/presence/automation2.yaml
```
alias: "Automation 2"
triggers:
 - trigger: state
  entity_id: device_tracker.iphone
  from: "home"
actions:
 - action: light.turn_off
  target:
   entity_id: light.entryway
```

YAML
Copy
It is important to note that each file must contain only one entry when using !include_dir_list.
### Example: !include_dir_named 
configuration.yaml
```
alexa:
 intents:
  LocateIntent:
   actions:
    action: notify.pushover
    data:
     message: "Your location has been queried via Alexa."
   speech:
    type: plaintext
    text: >
     {%- for state in states.device_tracker -%}
      {%- if state.name.lower() == User.lower() -%}
       {{ state.name }} is at {{ state.state }}
      {%- endif -%}
     {%- else -%}
      I am sorry. Pootie! I do not know where {{User}} is.
     {%- endfor -%}
  WhereAreWeIntent:
   speech:
    type: plaintext
    text: >
     {%- if is_state('device_tracker.iphone', 'home') -%}
      iPhone is home.
     {%- else -%}
      iPhone is not home.
     {% endif %}
```

YAML
Copy
can be turned into:
configuration.yaml
```
alexa:
 intents: !include_dir_named alexa/
```

YAML
Copy
alexa/LocateIntent.yaml
```
actions:
 action: notify.pushover
 data:
  message: "Your location has been queried via Alexa."
speech:
 type: plaintext
 text: >
  {%- for state in states.device_tracker -%}
   {%- if state.name.lower() == User.lower() -%}
    {{ state.name }} is at {{ state.state }}
   {%- endif -%}
  {%- else -%}
   I am sorry. Pootie! I do not know where {{User}} is.
  {%- endfor -%}
```

YAML
Copy
alexa/WhereAreWeIntent.yaml
```
speech:
 type: plaintext
 text: >
  {%- if is_state('device_tracker.iphone', 'home') -%}
   iPhone is home.
  {%- else -%}
   iPhone is not home.
  {% endif %}
```

YAML
Copy
### Example: !include_dir_merge_list 
configuration.yaml
```
automation:
 - alias: "Automation 1"
  triggers:
   - trigger: state
    entity_id: device_tracker.iphone
    to: "home"
  actions:
   - action: light.turn_on
    target:
     entity_id: light.entryway
 - alias: "Automation 2"
  triggers:
   - trigger: state
    entity_id: device_tracker.iphone
    from: "home"
  actions:
   - action: light.turn_off
    target:
     entity_id: light.entryway
```

YAML
Copy
can be turned into:
configuration.yaml
```
automation: !include_dir_merge_list automation/
```

YAML
Copy
automation/presence.yaml
```
- alias: "Automation 1"
 triggers:
  - trigger: state
   entity_id: device_tracker.iphone
   to: "home"
 actions:
  - action: light.turn_on
   target:
    entity_id: light.entryway
- alias: "Automation 2"
 triggers:
  - trigger: state
   entity_id: device_tracker.iphone
   from: "home"
 actions:
  - action: light.turn_off
   target:
    entity_id: light.entryway
```

YAML
Copy
It is important to note that when using !include_dir_merge_list, you must include a list in each file (each list item is denoted with a hyphen [-]). Each file may contain one or more entries.
### Example: !include_dir_merge_named 
configuration.yaml
```
group:
 bedroom:
  name: "Bedroom"
  entities:
   - light.bedroom_lamp
   - light.bedroom_overhead
 hallway:
  name: "Hallway"
  entities:
   - light.hallway
   - thermostat.home
 front_yard:
  name: "Front Yard"
  entities:
   - light.front_porch
   - light.security
   - light.pathway
   - sensor.mailbox
   - camera.front_porch
```

YAML
Copy
can be turned into:
configuration.yaml
```
group: !include_dir_merge_named group/
```

YAML
Copy
group/interior.yaml
```
bedroom:
 name: "Bedroom"
 entities:
  - light.bedroom_lamp
  - light.bedroom_overhead
hallway:
 name: Hallway
 entities:
  - light.hallway
  - thermostat.home
```

YAML
Copy
group/exterior.yaml
```
front_yard:
 name: "Front Yard"
 entities:
  - light.front_porch
  - light.security
  - light.pathway
  - sensor.mailbox
  - camera.front_porch
```

YAML
Copy
### Example: Combine !include_dir_merge_list with automations.yaml 
You want to go the advanced route and split your automations, but still want to be able to create ? In a chapter above we write about nesting !includes. Here is how we can do that for automations.
Using labels like manual or ui allows for using multiple keys in the config:
configuration.yaml
```
# My own handmade automations
automation manual: !include_dir_merge_list automations/
# Automations I create in the UI
automation ui: !include automations.yaml
```

YAML
Copy
## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## State and state object - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/state_object

#  On this page
Devices are represented in Home Assistant as entitiesAn entity represents a sensor, actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a device or a service. [Learn more]. The state of an entity (for example, if a light is on, at 50% brightness in orange) can be shown on the dashboard or be used in automations. This page looks at the concepts state, state object, and entity state attribute.
## State versus state object 
In Home Assistant, the state object is the current representation of the entityAn entity represents a sensor, actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a device or a service. [Learn more] with all its attributes at a given moment in time. This state is recorded as a state object. Entities constantly keep track of their state and write it into a state object, so that other entities/templates/frontend can access it. In the example—the light is on, at 50% brightness in orange—on is the actual state of the light. 50% brightness and the color are entity state attributes.
### About the state object 
The state object represents the state of an entity with its attributes at a specific point in time. All state objects will always have an entity id, a state, and timestamps when last updated, last changed, and last reported. The state prefix indicates that this information is part of the state object (which is related to the entity). For example, state.state is the state of the entity at a given time.
Field | Description  
---|---  
state.state | String representation of the current state of the entity. Example off.  
state.entity_id | Entity ID. Format: <domain>.<object_id>. Example: light.kitchen.  
state.domain | Domain of the entity. Example: light.  
state.object_id | Object ID of entity. Example: kitchen.  
state.name | Name of the entity. Based on friendly_name attribute with fall back to object ID. Example: Kitchen ceiling.  
state.last_changed | Time the state changed in the state machine in UTC time. This is not updated if only state attributes change. Example: 2013-09-17 07:32:51.715874+00:00.  
state.last_reported | Time the state was written to the state machine in UTC time. This timestamp is updated regardless of any changes to the state or state attributes. Example: 2013-09-17 07:32:51.715874+00:00.  
state.last_updated | Time the state or state attributes changed in the state machine in UTC time. This is not updated if neither state nor state attributes changed. Example: 2013-09-17 07:32:51.715874+00:00.  
state.attributes | A dictionary with extra attributes related to the current state.  
state.context | A dictionary with extra attributes related to the context of the state.  
### About the state 
The screenshot of the Developer Tools States page shows three lights in different states (the state.state): on, off, and unavailable. Each light comes with its own entity state attributes such as supported_color_modes, supported_features. These attributes have their own state: the state of the supported_color_modes attribute is color_temp and hs, the state of the supported_features attribute is 4.
Three lights with different states: `on`, `off`, or `unavailable`. 
The state.state is the heart of the . State holds the information of interest of an entity. For example, if a light is on or off, the current temperature, or the amount of energy used. The state object stores 3 timestamps related to the state: last_updated, last_changed, and last_reported. Each entity has exactly one state, and the state only holds one value at a time.
### About entity state attributes 
The state only holds one value at a time. However, entities can store related entity state attributes in the state object. For example, the state of a light is on, and the related attributes could be its current brightness and color values. can be used as triggers. The current state can be used in . The example below shows three lights with different entity state attributes.
Example showing three lights with different entity state attributes. 
Entities have some attributes that are not related to its state, such as friendly_name. A few attributes are available on all entities, such as friendly_name or icon. In addition to those, each integration has its own attributes to represent extra state data about the entity. For example, the light integration has attributes for the current brightness and color of the light. When an attribute is not available, Home Assistant will not write it to the state. Entity attributes are optional.
When using templates, attributes will be available by their name. For example state.attributes.assumed_state.
The table lists common state attributes that may be present, depending on the entity domain.
Attribute | Description  
---|---  
friendly_name | Name of the entity. Example: Kitchen Ceiling.  
icon | Icon to use for the entity in the frontend. Example: mdi:home.  
entity_picture | URL to a picture that should be used instead of showing the domain icon. Example: http://example.com/picture.jpg.  
assumed_state | Boolean if the current state is an assumption. Example: True.  
unit_of_measurement | The unit of measurement the state is expressed in. Used for grouping graphs or understanding the entity. Example: °C.  
attribution | The provider of the data. For example, “Data provided by rejseplanen.dk”, “Data provided by openSenseMap”  
device_class | The type of device that an entity represents. Used to display device specific information in the UI.  
supported_features | The features an entity supports. For covers, for example, it might list opening, closing, stopping, setting position. For media players, it might list play, pause, stop, and volume control   
When an attribute contains spaces, you can retrieve it like this: state_attr('sensor.livingroom', 'Battery numeric').
## Context 
Context is a property used in state objects and events. It ties eventsEvery time something happens in Home Assistant, an event is fired. There are different types of events, such as state change events, when an action was triggered, or the time changed. All entities produce state change events. Every time a state changes, a state change event is produced. Events can be used to trigger automations or scripts. For example, you can trigger an automation when a light is turned on, then a speaker turns on in that room. Events can also be used to trigger actions in the frontend. For example, you can trigger an action when a button is pressed. [Learn more] and statesThe state holds the information of interest of an entity, for example, if a light is on or off. Each entity has exactly one state and the state only holds one value at a time. However, entities can store attributes related to that state such as brightness, color, or a unit of measurement. [Learn more] together in Home Assistant. Whenever an automationAutomations in Home Assistant allow you to automatically respond to things that happen in and around your home. [Learn more] or user interaction causes a state to change, a new context is assigned in the state object. This context will be attached to all events and states that happen as a result of the change.
Field | Description  
---|---  
id | Unique identifier for the context.  
user_id | Unique identifier of the user that started the change. Will be None if the action was not started by a user (for example, started by an automation).  
parent_id | Unique identifier of the parent context that started the change, if available. For example, if an automation is triggered, the context of the trigger will be set as parent.  
## Examples 
  * Evaluate the state.last_changed of a switch entity:
```
{{ states.switch.my_switch.last_changed }}
```

Jinja
Copy
result type: string representing a datetime object e.g. 2025-11-11 12:56:10.244125+00:00


  * Evaluate the state.context.id of this switch:
```
{{ states.switch.my_switch.context.id }}
```

Jinja
Copy
result type: string representing an id code e.g. 01K9SF2R36KRV5N4PTC38S6KJ2F


  * Evaluate the state.context.user_id of this switch:
```
{{ states.switch.my_switch.context.user_id }}
```

Jinja
Copy
result type: string representing an user id code e.g. 01K9SF2R36KRV5N4PTC38SKS4LW6


## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Templating - Home Assistant

Source: https://www.home-assistant.io/docs/configuration/templating

#  On this page
This is an advanced feature of Home Assistant. You’ll need a basic understanding of:
  * , especially states.
  * The .


Templating is a powerful feature that allows you to control information going into and out of the system. It is used for:
  * Formatting outgoing messages in, for example, the platforms and integration.
  * Process incoming data from sources that provide raw data, like , or the .
  * .


## Building templates 
Templating in Home Assistant is powered by the templating engine. This means that we are using their syntax and make some custom Home Assistant variables available to templates during rendering. Jinja2 supports a wide variety of operations:
We will not go over the basics of the syntax, as Jinja2 does a great job of this in their .
The frontend has a to help develop and debug templates. Navigate to , create your template in the Template editor and check the results on the right.
Templates can get big pretty fast. To keep a clear overview, consider using YAML multiline strings to define your templates:
```
script:
 msg_who_is_home:
  sequence:
   - action: notify.notify
    data:
     message: >
      {% if is_state('device_tracker.paulus', 'home') %}
       Ha, Paulus is home!
      {% else %}
       Paulus is at {{ states('device_tracker.paulus') }}.
      {% endif %}
```

YAML
Copy
### Important template rules 
There are a few very important rules to remember when adding templates to YAML:
  1. You must surround single-line templates with double quotes (") or single quotes (').
  2. It is advised that you prepare for undefined variables by using if ... is not none or the , or both.
  3. It is advised that when comparing numbers, you convert the number(s) to a or an by using the respective .
  4. While the and filters do allow a default fallback value if the conversion is unsuccessful, they do not provide the ability to catch undefined variables.


Remembering these simple rules will help save you from many headaches and endless hours of frustration when using automation templates.
### Enabled Jinja extensions 
Jinja supports a set of language extensions that add new functionality to the language. To improve the experience of writing Jinja templates, we have enabled the following extensions:
  * (break and continue)
  * (do)


### Reusing templates 
You can write reusable Jinja templates by adding them to a custom_templates folder under your configuration directory. All template files must have the .jinja extension and be less than 5MiB. Templates in this folder will be loaded at startup. To reload the templates without restarting Home Assistant, invoke the action.
Once the templates are loaded, Jinja and will work using config/custom_templates as the base directory.
For example, you might define a macro in a template in config/custom_templates/formatter.jinja:
```
{% macro format_entity(entity_id) %}
{{ state_attr(entity_id, 'friendly_name') }} - {{ states(entity_id) }}
{% endmacro %}
```

Jinja
Copy
In your automations, you could then reuse this macro by importing it:
```
{% from 'formatter.jinja' import format_entity %}
{{ format_entity('sensor.temperature') }}
```

Jinja
Copy
Home Assistant also allows you to write macros with non-string return values by taking a named argument called returns and calling it with a return value. Once created, pass the macro into the as_function filter to use the returned value:
```
{%- macro macro_is_switch(entity_name, returns) -%}
 {%- do returns(entity_name.startswith('switch.')) -%}
{%- endmacro -%}
{%- set is_switch = macro_is_switch | as_function -%}
{{ "It's a switch!" if is_switch("switch.my_switch") else "Not a switch!" }}
```

Jinja
Copy
In this way, you can export utility functions that return scalar or complex values rather than just macros that render to strings.
## Home Assistant template extensions 
Extensions allow templates to access all of the Home Assistant specific states and adds other convenience functions and filters.
### Limited templates 
Templates for some as well as trigger_variables only support a subset of the Home Assistant template extensions. This subset is referred to as “Limited Templates”.
### This 
State-based and trigger-based template entities have the special template variable this available in their templates and actions. See more details and examples in the .
### States 
Not supported in .
Warning
Avoid using states.sensor.temperature.state, instead use states('sensor.temperature'). It is strongly advised to use the states(), is_state(), state_attr() and is_state_attr() as much as possible, to avoid errors and error message when the entity isn’t ready yet (e.g., during Home Assistant startup).
#### States examples 
The next two statements result in the same value if the state exists. The second one will result in an error if the state does not exist.
```
{{ states('device_tracker.paulus') }}
{{ states.device_tracker.paulus.state }}
```

Text
Copy
Print out a list of all the sensor states:
```
{% for state in states.sensor %}
 {{ state.entity_id }}={{ state.state }},
{% endfor %}
```

Text
Copy
Print out a list of all the sensor states sorted by entity_id:
```
{% for state in states.sensor | sort(attribute='entity_id') %}
 {{ state.entity_id }}={{ state.state }},
{% endfor %}
```

Text
Copy
Entities that are on:
```
{{ ['light.kitchen', 'light.dining_room'] | select('is_state', 'on') | list }}
```

Text
Copy
Other state examples:
```
{% if is_state('device_tracker.paulus', 'home') %}
 Ha, Paulus is home!
{% else %}
 Paulus is at {{ states('device_tracker.paulus') }}.
{% endif %}
#check sensor.train_departure_time state
{% if states('sensor.train_departure_time') in ("unavailable", "unknown") %}
 {{ ... }}
{% if has_value('sensor.train_departure_time') %}
 {{ ... }}

{% set state = states('sensor.temperature') %}{{ state | float + 1 if is_number(state) else "invalid temperature" }}
{% set state = states('sensor.temperature') %}{{ (state | float * 10) | round(2) if is_number(state)}}
{% set state = states('sensor.temperature') %}
{% if is_number(state) and state | float > 20 %}
 It is warm!
{% endif %}
{{ as_timestamp(states.binary_sensor.garage_door.last_changed) }}
{{ as_local(states.binary_sensor.garage_door.last_changed) }}
{{ as_timestamp(now()) - as_timestamp(states.binary_sensor.garage_door.last_changed) }}
{{ as_local(states.sensor.time.last_changed) }}
{{ states('sensor.expires') | as_datetime }}
# Make a list of states
{{ ['light.kitchen', 'light.dining_room'] | map('states') | list }}
```

Text
Copy
#### Formatting sensor states 
The examples below show the output of a temperature sensor with state 20.001, unit °C and user configured presentation rounding set to 1 decimal.
The following example results in the number 20.001:
```
{{ states('sensor.temperature') }}
```

Text
Copy
The following example results in the string "20.0 °C":
```
{{ states('sensor.temperature', with_unit=True) }}
```

Text
Copy
The following example result in the string "20.001 °C":
```
{{ states('sensor.temperature', with_unit=True, rounded=False) }}
```

Text
Copy
The following example results in the number 20.0:
```
{{ states('sensor.temperature', rounded=True) }}
```

Text
Copy
The following example results in the number 20.001:
```
{{ states.sensor.temperature.state }}
```

Text
Copy
The following example results in the string "20.0 °C":
```
{{ states.sensor.temperature.state_with_unit }}
```

Text
Copy
### Attributes 
Not supported in .
You can print an attribute with state_attr if state is defined.
#### Attributes examples 
```
{% if states.device_tracker.paulus %}
 {{ state_attr('device_tracker.paulus', 'battery') }}
{% else %}
 ??
{% endif %}
```

Text
Copy
With strings:
```
{% set tracker_name = "paulus"%}
{% if states("device_tracker." + tracker_name) != "unknown" %}
 {{ state_attr("device_tracker." + tracker_name, "battery")}}
{% else %}
 ??
{% endif %}
```

Text
Copy
List of friendly names:
```
{{ ['binary_sensor.garage_door', 'binary_sensor.front_door'] | map('state_attr', 'friendly_name') | list }}
```

Text
Copy
List of lights that are on with a brightness of 255:
```
{{ ['light.kitchen', 'light.dining_room'] | select('is_state', 'on') | select('is_state_attr', 'brightness', 255) | list }}
```

Text
Copy
### State translated 
Not supported in .
The state_translated function returns a translated state of an entity using a language that is currently configured in the .
#### State translated examples 
```
{{ states("sun.sun") }}       # below_horizon
{{ state_translated("sun.sun") }}  # Below horizon
{{ "sun.sun" | state_translated }} # Below horizon
```

Text
Copy
```
{{ states("binary_sensor.movement_backyard") }}       # on
{{ state_translated("binary_sensor.movement_backyard") }}  # Detected
{{ "binary_sensor.movement_backyard" | state_translated }} # Detected
```

Text
Copy
### Working with groups 
Not supported in .
The expand function and filter can be used to sort entities and expand groups. It outputs a sorted array of entities with no duplicates.
#### Expand examples 
```
{% for tracker in expand('device_tracker.paulus', 'group.child_trackers') %}
 {{ state_attr(tracker.entity_id, 'battery') }}
 {%- if not loop.last %}, {% endif -%}
{% endfor %}
```

Text
Copy
The same thing can also be expressed as a filter:
```
{{ expand(['device_tracker.paulus', 'group.child_trackers'])
 | selectattr("attributes.battery", 'defined')
 | join(', ', attribute="attributes.battery") }}
```

Text
Copy
```
{% for energy in expand('group.energy_sensors') if is_number(energy.state) %}
 {{ energy.state }}
 {%- if not loop.last %}, {% endif -%}
{% endfor %}
```

Text
Copy
The same thing can also be expressed as a test:
```
{{ expand('group.energy_sensors')
 | selectattr("state", 'is_number') | join(', ') }}
```

Text
Copy
### Entities 
  * is_hidden_entity(entity_id) returns whether an entity has been hidden. Can also be used as a test.


### Entities examples 
```
{{ area_entities('kitchen') | reject('is_hidden_entity') }} # Gets a list of visible entities in the kitchen area
```

Text
Copy
### Devices 
#### Devices examples 
```
{{ device_attr('deadbeefdeadbeefdeadbeefdeadbeef', 'manufacturer') }} # Sony
```

Text
Copy
```
{{ is_device_attr('deadbeefdeadbeefdeadbeefdeadbeef', 'manufacturer', 'Sony') }} # true
```

Text
Copy
```
{{ device_id('sensor.sony') }} # deadbeefdeadbeefdeadbeefdeadbeef
```

Text
Copy
```
{{ device_name('deadbeefdeadbeefdeadbeefdeadbeef') }} # Sony speaker
{{ device_name('sensor.sony') }} # Sony speaker
```

Text
Copy
### Config entries 
  * config_entry_id(entity_id) returns the config entry ID for a given entity ID. Can also be used as a filter.
  * config_entry_attr(config_entry_id, attr) returns the value of attr for the config entry of the given entity ID. Can also be used as a filter. The following attributes are allowed: domain, title, state, source, disabled_by. Not supported in .


#### Config entries examples 
```
{{ config_entry_id('sensor.sony') }} # deadbeefdeadbeefdeadbeefdeadbeef
```

Text
Copy
```
{{ config_entry_attr(config_entry_id('sensor.sony'), 'title') }} # Sony Bravia TV
```

Text
Copy
### Floors 
#### Floors examples 
```
{{ floors() }} # ['floor_id']
```

Text
Copy
```
{{ floor_id('First floor') }} # 'first_floor'
```

Text
Copy
```
{{ floor_id('First floor alias') }} # 'first_floor'
```

Text
Copy
```
{{ floor_id('my_device_id') }} # 'second_floor'
```

Text
Copy
```
{{ floor_id('sensor.sony') }} # 'first_floor'
```

Text
Copy
```
{{ floor_name('first_floor') }} # 'First floor'
```

Text
Copy
```
{{ floor_name('my_device_id') }} # 'Second floor'
```

Text
Copy
```
{{ floor_name('sensor.sony') }} # 'First floor'
```

Text
Copy
```
{{ floor_areas('first_floor') }} # ['living_room', 'kitchen']
```

Text
Copy
### Areas 
#### Areas examples 
```
{{ areas() }} # ['area_id']
```

Text
Copy
```
{{ area_id('Living Room') }} # 'deadbeefdeadbeefdeadbeefdeadbeef'
```

Text
Copy
```
{{ area_id('Living Room Alias') }} # 'deadbeefdeadbeefdeadbeefdeadbeef'
```

Text
Copy
```
{{ area_id('my_device_id') }} # 'deadbeefdeadbeefdeadbeefdeadbeef'
```

Text
Copy
```
{{ area_id('sensor.sony') }} # 'deadbeefdeadbeefdeadbeefdeadbeef'
```

Text
Copy
```
{{ area_name('deadbeefdeadbeefdeadbeefdeadbeef') }} # 'Living Room'
```

Text
Copy
```
{{ area_name('my_device_id') }} # 'Living Room'
```

Text
Copy
```
{{ area_name('sensor.sony') }} # 'Living Room'
```

Text
Copy
```
{{ area_entities('deadbeefdeadbeefdeadbeefdeadbeef') }} # ['sensor.sony']
```

Text
Copy
```
{{ area_devices('Living Room') }} # ['my_device_id']
```

Text
Copy
### Entities for an integration 
  * integration_entities(integration) returns a list of entities that are associated with a given integration, such as hue or zwave_js.
  * integration_entities(config_entry_title) if you have multiple entries set-up for an integration, you can also use the title you’ve set for the integration in case you only want to target a specific entry.


If there is more than one entry with the same title, the entities for all the matching entries will be returned, even if the entries are for different integrations. It’s not possible to search for entities of an untitled integration.
#### Integrations examples 
```
{{ integration_entities('hue') }} # ['light.hue_light_upstairs', 'light.hue_light_downstairs']
```

Text
Copy
```
{{ integration_entities('Hue bridge downstairs') }} # ['light.hue_light_downstairs']
```

Text
Copy
### Labels 
Each of the label template functions can also be used as a filter.
#### Labels examples 
```
{{ labels() }} # ['christmas_decorations', 'energy_saver', 'security']
```

Text
Copy
```
{{ labels("living_room") }} # ['christmas_decorations', 'energy_saver']
```

Text
Copy
```
{{ labels("my_device_id") }} # ['security']
```

Text
Copy
```
{{ labels("light.christmas_tree") }} # ['christmas_decorations']
```

Text
Copy
```
{{ label_id('Energy saver') }} # 'energy_saver'
```

Text
Copy
```
{{ label_name('energy_saver') }} # 'Energy saver'
```

Text
Copy
```
{{ label_areas('security') }} # ['driveway', 'garden', 'porch']
```

Text
Copy
```
{{ label_devices('energy_saver') }} # ['deadbeefdeadbeefdeadbeefdeadbeef']
```

Text
Copy
```
{{ label_entities('security') }} # ['camera.driveway', 'binary_sensor.motion_garden', 'camera.porch']
```

Text
Copy
### Issues 
  * issues() returns all open issues as a mapping of (domain, issue_id) tuples to the issue object.
  * issue(domain, issue_id) returns a specific issue for the provided domain and issue_id.


#### Issues examples 
```
{{ issues() }} # { ("homeassistant", "deprecated_yaml_ping"): {...}, ("cloud", "legacy_subscription"): {...} }
```

Text
Copy
```
{{ issue('homeassistant', 'python_version') }} # {"breaks_in_ha_version": "2024.4", "domain": "homeassistant", "issue_id": "python_version", "is_persistent": False, ...}
```

Text
Copy
### Immediate if (iif) 
A common case is to conditionally return a value based on another value. For example, return a “Yes” or “No” when the light is on or off.
This can be written as:
```
{% if is_state('light.kitchen', 'on') %}
 Yes
{% else %}
 No
{% endif %}
```

Text
Copy
Or using a shorter syntax:
```
{{ 'Yes' if is_state('light.kitchen', 'on') else 'No' }}
```

Text
Copy
Additionally, to the above, you can use the iif function/filter, which is an immediate if.
Syntax: iif(condition, if_true, if_false, if_none)
iif returns the value of if_true if the condition is truthy, the value of if_false if it’s falsy and the value of if_none if it’s None. An empty string, an empty mapping or an an empty list, are all falsy, refer to for an in depth explanation.
if_true is optional, if it’s omitted True is returned if the condition is truthy. if_false is optional, if it’s omitted False is returned if the condition is falsy. if_none is optional, if it’s omitted the value of if_false is returned if the condition is None.
Examples using iif:
```
{{ iif(is_state('light.kitchen', 'on'), 'Yes', 'No') }}
{{ is_state('light.kitchen', 'on') | iif('Yes', 'No') }}
{{ (states('light.kitchen') == 'on') | iif('Yes', 'No') }}
```

Text
Copy
Warning
The immediate if filter does not short-circuit like you might expect with a typical conditional statement. The if_true, if_false and if_none expressions will all be evaluated and the filter will simply return one of the resulting values. This means you cannot use this filter to prevent executing an expression which would result in an error.
For example, if you wanted to select a field from trigger in an automation based on the platform you might go to make this template: trigger.platform == 'event' | iif(trigger.event.data.message, trigger.to_state.state). This won’t work because both expressions will be evaluated and one will fail since the field doesn’t exist. Instead you have to do this trigger.event.data.message if trigger.platform == 'event' else trigger.to_state.state. This form of the expression short-circuits so if the platform is event the expression trigger.to_state.state will never be evaluated and won’t cause an error.
### Time 
now(), time_since(), time_until(), today_at(), and utcnow() are not supported in .
Tip
is the number of seconds that have elapsed since 00:00:00 UTC on 1 January 1970. Therefore, if used as a function’s argument, it can be substituted with a numeric value (int or float).
Important
If your template is returning a timestamp that should be displayed in the frontend (e.g., as a sensor entity with device_class: timestamp), you have to ensure that it is the ISO 8601 format (meaning it has the “T” separator between the date and time portion). Otherwise, frontend rendering on macOS and iOS devices will show an error. The following value template would result in such an error:
{{ states.sun.sun.last_changed }} => 2023-07-30 20:03:49.253717+00:00 (missing “T” separator)
To fix it, enforce the ISO conversion via isoformat():
{{ states.sun.sun.last_changed.isoformat() }} => 2023-07-30T20:03:49.253717+00:00 (contains “T” separator)
```
{{ 120 | timestamp_local }}
```

Text
Copy
### To/From JSON 
The to_json filter serializes an object to a JSON string. In some cases, it may be necessary to format a JSON string for use with a webhook, as a parameter for command-line utilities or any number of other applications. This can be complicated in a template, especially when dealing with escaping special characters. Using the to_json filter, this is handled automatically.
to_json also accepts boolean arguments for pretty_print, which will pretty print the JSON with a 2-space indent to make it more human-readable, and sort_keys, which will sort the keys of the JSON object, ensuring that the resulting string is consistent for the same input.
If you need to generate JSON that will be used by a parser that lacks support for Unicode characters, you can add ensure_ascii=True to have to_json generate Unicode escape sequences in strings.
The from_json filter operates similarly, but in the other direction, de-serializing a JSON string back into an object.
### To/From JSON examples 
#### Template 
```
{% set temp = {'temperature': 25, 'unit': '°C'} %}
stringified object: {{ temp }}
object|to_json: {{ temp|to_json(sort_keys=True) }}
```

Text
Copy
#### Output 
```
stringified object: {'temperature': 25, 'unit': '°C'}
object|to_json: {"temperature": 25, "unit": "°C"}
```

Text
Copy
Conversely, from_json can be used to de-serialize a JSON string back into an object to make it possible to easily extract usable data.
#### Template 
```
{% set temp = '{"temperature": 25, "unit": "°C"}'|from_json %}
The temperature is {{ temp.temperature }}{{ temp.unit }}
```

Text
Copy
#### Output 
```
The temperature is 25°C
```

Text
Copy
from_json(default) function will attempt to convert the input to json. If that fails, returns the default value, or if omitted raises an error.
#### Template 
```
{% set result = 'not json'|from_json('not json') %}
The value is {{ result }}
```

Text
Copy
#### Output 
```
The value is not json
```

Text
Copy
### Is defined 
Sometimes a template should only return if a value or object is defined, if not, the supplied default value should be returned. This can be useful to validate a JSON payload. The is_defined filter allows to throw an error if a value or object is not defined.
Example using is_defined to parse a JSON payload:
```
{{ value_json.val | is_defined }}
```

Text
Copy
This will throw an error UndefinedError: 'value_json' is undefined if the JSON payload has no val attribute.
### Version 
  * version() Returns a for the value given inside the brackets. 
    * This is also available as a filter (| version).


Examples:
### Distance 
Not supported in .
  * distance() measures the distance between home, an entity, or coordinates. The unit of measurement (kilometers or miles) depends on the system’s configuration settings.
  * closest() will find the closest entity.


#### Distance examples 
If only one location is passed in, Home Assistant will measure the distance from home.
```
Using Lat Lng coordinates: {{ distance(123.45, 123.45) }}
Using State: {{ distance(states.device_tracker.paulus) }}
These can also be combined in any combination:
{{ distance(123.45, 123.45, 'device_tracker.paulus') }}
{{ distance('device_tracker.anne_therese', 'device_tracker.paulus') }}
```

Text
Copy
#### Closest examples 
The closest function and filter will find the closest entity to the Home Assistant location:
```
Query all entities: {{ closest(states) }}
Query all entities of a specific domain: {{ closest(states.device_tracker) }}
Query all entities in group.children: {{ closest('group.children') }}
Query all entities in group.children: {{ closest(states.group.children) }}
```

Text
Copy
Find entities closest to a coordinate or another entity. All previous arguments still apply for second argument.
```
Closest to a coordinate: {{ closest(23.456, 23.456, 'group.children') }}
Closest to an entity: {{ closest('zone.school', 'group.children') }}
Closest to an entity: {{ closest(states.zone.school, 'group.children') }}
```

Text
Copy
Since closest returns a state, we can combine it with distance too.
```
{{ closest(states).name }} is {{ distance(closest(states)) }} kilometers away.
```

Text
Copy
The last argument of the closest function has an implicit expand, and can take any iterable sequence of states or entity IDs, and will expand groups:
```
Closest out of given entities:
  {{ closest(['group.children', states.device_tracker]) }}
Closest to a coordinate:
  {{ closest(23.456, 23.456, ['group.children', states.device_tracker]) }}
Closest to some entity:
  {{ closest(states.zone.school, ['group.children', states.device_tracker]) }}
```

Text
Copy
It will also work as a filter over an iterable group of entities or groups:
```
Closest out of given entities:
  {{ ['group.children', states.device_tracker] | closest }}
Closest to a coordinate:
  {{ ['group.children', states.device_tracker] | closest(23.456, 23.456) }}
Closest to some entity:
  {{ ['group.children', states.device_tracker] | closest(states.zone.school) }}
```

Text
Copy
### Contains 
Jinja provides by default a how return True when one element is in a provided list. The contains test and filter allow you to do the exact opposite and test for a list containing an element. This is particularly useful in select or selectattr filter, as well as to check if a device has a specific attribute, a supported_color_modes, a specific light effect.
Some examples:
  * {{ state_attr('light.dining_room', 'effect_list') | contains('rainbow') }} will return true if the light has a rainbow effect.
  * {{ expand('light.office') | selectattr("attributes.supported_color_modes", 'contains', 'color_temp') | list }} will return all light that support color_temp in the office group.
  * ```
{% set current_month = now().month %}
{% set extra_ambiance = [
 {'name':'Halloween', 'month': [10,11]},
 {'name':'Noel', 'month': [1,11,12]}
]%}
{% set to_add = extra_ambiance | selectattr('month', 'contains', current_month ) | map(attribute='name') | list %}
{% set to_remove = extra_ambiance | map(attribute='name') | reject('in', to_add) | list %}
{{ (state_attr('input_select.light_theme', 'options') + to_add ) | unique | reject('in', to_remove) | list }}
```

Text
Copy
This more complex example uses the contains filter to match the current month with a list. In this case, it’s used to generate a list of light theme to give to the Input select: Set options action.


### Numeric functions and filters 
Some of these functions can also be used in a . This means they can act as a normal function like this sqrt(2), or as part of a filter like this 2|sqrt.
Note
The numeric functions and filters raise an error if the input is not a valid number, optionally a default value can be specified which will be returned instead. The is_number function and filter can be used to check if a value is a valid number. Errors can be caught by the default filter.
### Complex type checking 
In addition to strings and numbers, Python (and Jinja) supports lists, sets, and dictionaries. To help you with testing these types, you can use the following tests:
Note that, in Home Assistant, Jinja has built-in tests for boolean (True/False), callable (any function), float (a number with a decimal), integer (a number without a decimal), iterable (a value that can be iterated over such as a list, set, string, or generator), mapping (mainly dict but also supports other dictionary like types), number (float or int), sequence (a value that can be iterated over and indexed such as list and string), and string.
### Type conversions 
While Jinja natively supports the conversion of an iterable to a list, it does not support conversion to a tuple or set. To help you with using these types, you can use the following functions:
  * set(x) will convert any iterable x to a set (e.g. set([1, 2]) == {1, 2})
  * tuple(x) will convert any iterable x to a tuple (e.g. tuple("abc") == ("a", "b", "c"))


Note that, in Home Assistant, to convert a value to a list, a string, an int, or a float, Jinja has built-in functions with names that correspond to each type.
### Iterating multiple objects 
The zip() function can be used to iterate over multiple collections in one operation.
```
{% set names = ['Living Room', 'Dining Room'] %}
{% set entities = ['sensor.living_room_temperature', 'sensor.dining_room_temperature'] %}
{% for name, entity in zip(names, entities) %}
 The {{ name }} temperature is {{ states(entity) }}
{% endfor %}
```

Text
Copy
zip() can also unzip lists.
```
{% set information = [
 ('Living Room', 'sensor.living_room_temperature'),
 ('Dining Room', 'sensor.dining_room_temperature')
] %}
{% set names, entities = zip(*information) %}
The names are {{ names | join(', ') }}
The entities are {{ entities | join(', ') }}
```

Text
Copy
### Functions and filters to process raw data 
These functions are used to process raw value’s in a bytes format to values in a native Python type or vice-versa. The pack and unpack functions can also be used as a filter. They make use of the Python 3 struct library. See: 
Note
Some examples:
### String filters 
Some examples:
### Hashing 
The template engine contains a few filters and functions to hash a string of data. A few very common hashing algorithms are supported: md5, sha1, sha256, and sha512.
Some examples:
### Regular expressions 
For more information on regular expressions See: 
### Shuffling 
The template engine contains a filter and function to shuffle a list.
Shuffling can happen randomly or reproducibly using a seed. When using a seed it will always return the same shuffled list for the same seed.
Some examples:
### Flatten a list of lists 
The template engine provides a filter to flatten a list of lists: flatten.
It will take a list of lists and return a single list with all the elements. The depth of the flattening can be controlled using the levels parameter. The flattening process is recursive, so it will flatten all nested lists, until the number of levels (if specified) is reached.
Some examples:
### Find common elements between lists 
The template engine provides a filter to find common elements between two lists: intersect.
This function returns a list containing all elements that are present in both input lists.
Some examples:
### Find elements in first list not in second list 
The template engine provides a filter to find elements that are in the first list but not in the second list: difference. This function returns a list containing all elements that are present in the first list but absent from the second list.
Some examples:
### Find elements that are in either list but not in both 
The template engine provides a filter to find elements that are in either of the input lists but not in both: symmetric_difference. This function returns a list containing all elements that are present in either the first list or the second list, but not in both.
Some examples:
### Combine all unique elements from two lists 
The template engine provides a filter to combine all unique elements from two lists: union. This function returns a list containing all unique elements that are present in either the first list or the second list.
Some examples:
### Combining dictionaries 
The template engine provides a function and filter to merge multiple dictionaries: combine.
It will take multiple dictionaries and merge them into a single dictionary. When used as a filter, the filter value is used as the first dictionary. The optional recursive parameter determines whether nested dictionaries should be merged (defaults to False).
Some examples:
### Working with macros 
Home Assistant provides two additional functions that make macros much more powerful.
  * apply is both a filter and a test that allows you to use any callable (macros or functions) wherever you can use other filters and tests. apply also passes along any additional parameters to the function. For example, if you had a function called double, you could call {{ [1, 2, 3, 4] | map('apply', double) | list }}, which would render as [2, 4, 6, 8]. Alternatively, if you had a function called is_multiple_of, you could call {{ [1, 2, 3, 4] | select('apply', is_multiple_of, 2) | list }}, which would render as [2, 4].
  * as_function is a filter that takes a macro that has a named parameter called returns. The macro can then call {%- do returns(return_value) -%}. After passing this macro into as_function, the resulting function returns your return value directly, preserving the underlying data type rather than rendering a string. You can return dictionaries, numbers, True/False (allowing you to write your own tests when used with apply), or any other value your code might produce.


## Merge action responses 
Using action responses we can collect information from various entities at the same time. Using the merge_response template we can merge several responses into one list.
Variable | Description  
---|---  
value | The incoming value (must be an action response).  
The entity_id key is appended to each dictionary within the template output list as a reference of origin. If the input dictionary already contains an entity_id key, the template will fail.
The value_key key is appended to each dictionary within the template output list as a reference of origin if the original service call was providing a list of dictionaries, for example, calendar.get_events or weather.get_forecasts.
Examples of these two keys can be seen in template output.
### Example 
```
{% set combined_forecast = merge_response(response) %}
{{ combined_forecast[0].precipitation | float(0) | round(1) }}
```

YAML
Copy
### Example how to sort 
Sorting the dictionaries within the list based on a specific key can be done directly by using Jinja’s sort filter.
```
{{ merge_response(calendar_response) | sort(attribute='start') | ... }}
```

YAML
Copy
### Example merge calendar action response 
```
{
 "calendar.sports": {
  "events": [
   {
    "start": "2024-02-27T17:00:00-06:00",
    "end": "2024-02-27T18:00:00-06:00",
    "summary": "Basketball vs. Rockets",
    "description": "",
   }
  ]
 },
 "calendar.local_furry_events": {"events": []},
 "calendar.yap_house_schedules": {
  "events": [
   {
    "start": "2024-02-26T08:00:00-06:00",
    "end": "2024-02-26T09:00:00-06:00",
    "summary": "Dr. Appt",
    "description": "",
   },
   {
    "start": "2024-02-28T20:00:00-06:00",
    "end": "2024-02-28T21:00:00-06:00",
    "summary": "Bake a cake",
    "description": "something good",
   }
  ]
 },
}
```

JSON
Copy
```
{{ merge_response(response_variable) }}
```

YAML
Copy
```
[
 {
  "description": "",
  "end": "2024-02-27T18:00:00-06:00",
  "entity_id": "calendar.sports",
  "start": "2024-02-27T17:00:00-06:00",
  "summary": "Basketball vs. Rockets",
  "value_key": "events"
 },
 {
  "description": "",
  "end": "2024-02-26T09:00:00-06:00",
  "entity_id": "calendar.yap_house_schedules",
  "start": "2024-02-26T08:00:00-06:00",
  "summary": "Dr. Appt",
  "value_key": "events"
 },
 {
  "description": "something good",
  "end": "2024-02-28T21:00:00-06:00",
  "entity_id": "calendar.yap_house_schedules",
  "start": "2024-02-28T20:00:00-06:00",
  "summary": "Bake a cake",
  "value_key": "events"
 }
]
```

JSON
Copy
### Example non-list action responses 
```
{
 "vacuum.deebot_n8_plus_1": {
  "header": {
   "ver": "0.0.1",
  },
  "payloadType": "j",
  "resp": {
   "body": {
    "msg": "ok",
   },
  },
 },
 "vacuum.deebot_n8_plus_2": {
  "header": {
   "ver": "0.0.1",
  },
  "payloadType": "j",
  "resp": {
   "body": {
    "msg": "ok",
   },
  },
 },
}
```

JSON
Copy
```
{{ merge_response(response_variable) }}
```

YAML
Copy
```
[
 {
  "entity_id": "vacuum.deebot_n8_plus_1",
  "header": {
   "ver": "0.0.1",
  },
  "payloadType": "j",
  "resp": {
   "body": {
    "msg": "ok",
   },
  },
 },
 {
  "entity_id": "vacuum.deebot_n8_plus_2",
  "header": {
   "ver": "0.0.1",
  },
  "payloadType": "j",
  "resp": {
   "body": {
    "msg": "ok",
   },
  },
 },
]
```

JSON
Copy
## Processing incoming data 
The other part of templating is processing incoming data. It allows you to modify incoming data and extract only the data you care about. This will only work for platforms and integrations that mention support for this in their documentation.
It depends per integration or platform, but it is common to be able to define a template using the value_template configuration key. When a new value arrives, your template will be rendered while having access to the following values on top of the usual Home Assistant extensions:
Variable | Description  
---|---  
value | The incoming value.  
value_json | The incoming value parsed as JSON.  
This means that if the incoming values looks like the sample below:
```
{
 "on": "true",
 "temp": 21
}
```

JSON
Copy
The template for on would be:
```
"{{value_json.on}}"
```

YAML
Copy
Nested JSON in a response is supported as well:
```
{
 "sensor": {
  "type": "air",
  "id": "12345"
 },
 "values": {
  "temp": 26.09,
  "hum": 56.73
 }
}
```

JSON
Copy
Just use the “Square bracket notation” to get the value.
```
"{{ value_json['values']['temp'] }}"
```

YAML
Copy
The following overview contains a couple of options to get the needed values:
```
# Incoming value:
{"primes": [2, 3, 5, 7, 11, 13]}
# Extract first prime number
{{ value_json.primes[0] }}
# Format output
{{ "%+.1f" | value_json }}
# Math
{{ value_json | float * 1024 if is_number(value_json) }}
{{ float(value_json) * (2**10) if is_number(value_json) }}
{{ value_json | log if is_number(value_json) }}
{{ log(1000, 10) }}
{{ sin(pi / 2) }}
{{ cos(tau) }}
{{ tan(pi) }}
{{ sqrt(e) }}
# Timestamps
{{ value_json.tst | timestamp_local }}
{{ value_json.tst | timestamp_utc }}
{{ value_json.tst | timestamp_custom('%Y', True) }}
```

Text
Copy
To evaluate a response, go to Developer Tools > Template, create your output in “Template editor”, and check the result.
```
{% set value_json=
  {"name":"Outside",
   "device":"weather-ha",
   "data":
    {"temp":"24C",
     "hum":"35%"
     } }%}
{{value_json.data.hum[:-1]}}
```

YAML
Copy
### Using templates with the MQTT integration 
The relies heavily on templates. Templates are used to transform incoming payloads (value templates) to state updates or incoming actions (command templates) to payloads that configure the MQTT device.
#### Using value templates with MQTT 
Value templates translate received MQTT payload to a valid state or attribute. The received MQTT is available in the value template variable, and in the value_json template variable if the received MQTT payload is valid JSON.
In addition, the template variables entity_id, name and this are available for MQTT entity value templates. The this attribute refers to the of the MQTT item.
Note
Example value template:
With given payload:
```
{ "state": "ON", "temperature": 21.902, "humidity": null }
```

JSON
Copy
Template {{ value_json.temperature | round(1) }} renders to 21.9.
Template {{ value_json.humidity }} renders to None.
#### Using command templates with MQTT 
For actions, command templates are defined to format the outgoing MQTT payload to a format supported by the remote device. When an action is executed, the template variable value has the action data in most cases unless otherwise specified in the documentation.
In addition, the template variables entity_id, name and this are available for MQTT entity command templates. The this attribute refers to the of the MQTT item.
Note
Example command template with JSON data:
With given value 21.9 template {"temperature": {{ value }} } renders to:
```
{
 "temperature": 21.9
}
```

JSON
Copy
Example command template with raw data:
When a command template renders to a valid bytes literal, then MQTT will publish this data as raw data. In other cases, a string representation will be published. So:
  * Template {{ "16" }} renders to payload encoded string "16".
  * Template {{ 16 }} renders to payload encoded string "16".
  * Template {{ pack(0x10, ">B") }} renders to a raw 1 byte payload 0x10.


### Determining types 
When working with templates, it can be useful to determine the type of the returned value from a method or the type of a variable at times.
For this, Home Assistant provides the typeof() template function and filter, which is inspired by the typeof operator. It reveals the type of the given value.
This is mostly useful when you are debugging or playing with templates in the developer tools of Home Assistant. However, it might be useful in some other cases as well.
Some examples:
## Some more things to keep in mind 
### entity_id that begins with a number 
If your template uses an entity_id that begins with a number (example: states.device_tracker.2008_gmc) you must use a bracket syntax to avoid errors caused by rendering the entity_id improperly. In the example given, the correct syntax for the device tracker would be: states.device_tracker['2008_gmc']
### Priority of operators 
The default priority of operators is that the filter (|) has priority over everything except brackets. This means that:
```
{{ states('sensor.temperature') | float / 10 | round(2) }}
```

Text
Copy
Would round 10 to 2 decimal places, then divide states('sensor.temperature') by 10 (rounded to 2 decimal places so 10.00). This behavior is maybe not the one expected, but priority rules imply that.
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Home Assistant

Source: https://www.home-assistant.io/docs/organzing/labels/

## Oh no! This page does not exist 😞 
SearchK



## Creating an automation blueprint - Home Assistant

Source: https://www.home-assistant.io/docs/blueprint/tutorial/

#  On this page
Tip
While the tutorial only shows how to create an automation blueprint, scriptsScripts are components that allow users to specify a sequence of actions to be executed by Home Assistant when turned on. [Learn more] also support blueprints in the same way.
## Creating an automation blueprint 
In this tutorial, we’re going to create an automation blueprint that controls a light based on a motion sensor. We will do this by taking an existing automation and converting it to a blueprint.
### Prerequisites 
### Creating an automation 
To create a blueprint, we first need to have a working automation. For this tutorial, we use a simple automation. The process for converting a complex automation is no different.
The automation we’re going to use in this tutorial controls a light based on a motion sensor:
```
triggers:
 - trigger: state
  entity_id: binary_sensor.motion_kitchen
actions:
 - action: >
   {% if trigger.to_state.state == "on" %}
    light.turn_on
   {% else %}
    light.turn_off
   {% endif %}
  target:
   entity_id: light.kitchen
```

YAML
Copy
The options that can be used with the trigger object are listed under . In this example, a is used. turn_on and turn_off are . They are not tied to a specific domain. You can use them on lights, switches, and other domains.
### Creating the blueprint file 
Automation blueprints are YAML files (with the .yaml extension) and live in the <config>/blueprints/automation/ folder. You can create as many subdirectories in this folder as you want.
To get started with our blueprint, we’re going to copy the above automation YAML and save it in that directory with the name motion_light_tutorial.yaml.
#### Add basic blueprint metadata 
Home Assistant needs to know about the blueprint. This is achieved by adding a blueprint: section. It should contain the domain of the integration it is for (automation) and name, the name of your blueprint. Optionally, you can also include a description for your blueprint.
Add this to the top of the file:
```
blueprint:
 name: Motion Light Tutorial
 description: Turn a light on based on detected motion
 domain: automation
```

YAML
Copy
#### Define the configurable parts as inputs 
Now we have to decide what steps we want to make configurable. We want to make it as re-usable as possible, without losing its original intent of turning on a light-based on a motion sensor.
Configurable parts in blueprints are called . To make the motion sensor entity configurable, we’re replacing the entity ID with a custom YAML tag !input. This YAML tag has to be combined with the name of the input:
```
triggers:
 - trigger: state
  entity_id: !input motion_sensor
```

YAML
Copy
For the light, we can offer some more flexibility. We want to allow the user to be able to define any device or area as the target. The target property in the action can contain references to areas, devices, and/or entities, so that’s what we will use.
Inputs are not limited to strings. They can contain complex objects too. So in this case, we’re going to mark the whole target as input:
```
actions:
 - action: >
   {% if trigger.to_state.state == "on" %}
    light.turn_on
   {% else %}
    light.turn_off
   {% endif %}
  target: !input target_light
```

YAML
Copy
#### Add the inputs to the metadata 
All parts that are marked as inputs need to be added to the metadata. The minimum is that we add their names as used in the automation:
```
blueprint:
 name: Motion Light Tutorial
 description: Turn a light on based on detected motion
 domain: automation
 input:
  motion_sensor:
  target_light:
```

YAML
Copy
For more information on blueprint inputs, refer to the documentation of the 
## Using your blueprint via configuration.yaml 
With the bare minimum metadata added, your blueprint is ready to use.
Open your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more] and add the following:
```
automation tutorial:
 use_blueprint:
  path: motion_light_tutorial.yaml
  input:
   motion_sensor: binary_sensor.kitchen
   target_light:
    entity_id: light.kitchen
```

YAML
Copy
Reload automations and your new automation should pop up. Because we configured the exact values as the original automation, they should work exactly the same.
## Improving the inputs 
Blueprints are easier to use if it’s easy to see what each field is used for.
### Add a user friendly names to the inputs 
We can improve this experience by adding names and descriptions to our inputs:
```
blueprint:
 name: Motion Light Tutorial
 description: Turn a light on based on detected motion
 domain: automation
 input:
  motion_sensor:
   name: Motion Sensor
   description: This sensor will be synchronized with the light.
  target_light:
   name: Lights
   description: The lights to keep in sync.
```

YAML
Copy
### Describe the inputs 
Our blueprint doesn’t currently describe what the inputs should contain. Without this information, Home Assistant will offer the user an empty text box.
To instead allow Home Assistant to offer more assistance, we will use . Selectors describe a type and can be used to help the user pick a matching value.
The selector for the motion sensor entity should describe that we want entities from the binary sensor domain that have the device class motion.
The selector for the target light should describe that we want to target light entities.
```
blueprint:
 name: Motion Light Tutorial
 domain: automation
 input:
  motion_sensor:
   name: Motion Sensor
   description: This sensor will be synchronized with the light.
   selector:
    entity:
     filter:
      - domain: binary_sensor
       device_class: motion
  target_light:
   name: Lights
   description: The lights to keep in sync.
   selector:
    target:
     entity:
      - domain: light
```

YAML
Copy
By limiting our blueprint to working with lights and motion sensors, we unlock a couple of benefits: the UI will be able to limit suggested values to lights and motion sensors instead of all devices. It will also allow the user to pick an area to control the lights in.
## The final blueprint 
After we have added all the steps, our blueprint will look like this:
```
blueprint:
 name: Motion Light Tutorial
 description: Turn a light on based on detected motion
 domain: automation
 input:
  motion_sensor:
   name: Motion Sensor
   description: This sensor will be synchronized with the light.
   selector:
    entity:
     filter:
      - domain: binary_sensor
       device_class: motion
  target_light:
   name: Lights
   description: The lights to keep in sync.
   selector:
    target:
     entity:
      - domain: light
triggers:
 - trigger: state
  entity_id: !input motion_sensor
actions:
 - action: >
   {% if trigger.to_state.state == "on" %}
    light.turn_on
   {% else %}
    light.turn_off
   {% endif %}
  target: !input target_light
```

YAML
Copy
## Using the blueprint via the UI 
  1. To configure your blueprint via the UI, go to .
  2. Find the Motion Light Tutorial blueprint and select Create Automation.


Important
Don’t forget to reload automations after you make changes to your blueprint to have the UI and the automation integration pick up the latest blueprint changes.
## Video tutorial 
This video tutorial explains how to create a blueprint that toggles a light on motion when the lux value is below a certain threshold.
## Share the love 
The final step is to share this blueprint with others. For this tutorial we’re going to share it on GitHub Gists.
### Share informally 
For this tutorial, we’re going to share it on GitHub Gists. This is a good option if you don’t want to publish your blueprint to a larger audience.
  1. Go to 
     * Gist description: blueprint tutorial
     * Filename including extension: motion_light_tutorial.yaml 
     * Content is the content of the blueprint file.
  2. Select Create Gist.
  3. To share your blueprint with other people, copy the URL of your new Gist. They can import it by going to and select Import blueprint.
  4. Celebrate! Cheers to you. You created your first blueprint and helped someone in the community.


### Share on the Blueprint Exchange 
If you follow the , you can share your blueprint on the Home Assistant Blueprint Exchange forum. This option is accessible to the general Home Assistant community but recommended only for your original blueprints. Please don’t post this tutorial to the Blueprint Exchange, but instead, remember this as an option for releasing your real blueprints.
## Related topics 
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## Frequently Asked Questions about home energy management - Home Assistant

Source: https://www.home-assistant.io/docs/energy/faq/

#  On this page
## Energy vs Power 
It’s a common mistake to take Power as an Energy value, but the two are not alike.
is a quantitative measurement of what it takes to produce work (e.g. heat water) while measures the speed at which energy is transferred.
Electrical Power is measured in Watts (W) and Electrical Energy is measured in kiloWatt-hour (kWh).
Think of this in a parallel to speed and distance: Power is the speed you are going and Energy is the distance driven.
Therefore Energy (kiloWatt-hour) is not an average of the Power you are consuming over a given period of time (the unit of the average power would be Watt or kiloWatt again). Energy is the integral (mathematical operation) of the Power function.
This difference is very important as you need to use the proper entities in our Energy dashboard.
## Creating an Energy Sensor out of a Power Sensor 
Since in Home Assistant, we don’t deal with Power functions but with samples of the power being used, we can’t do the integral (mathematical operation) directly and get the true amount of energy consumed/produced.
That said, if you can sample Power values fast enough (every few seconds) you can reliably measure energy transferred through mathematic approximations called . Home Assistant provides this mathematical operation through the .
## Split consumption by tariffs 
If you are using a 3rd party device (e.g. not reading directly from your utility meter device or from the utility provider cloud service) you need HA to split your energy measurements into 2 (or more) tariffs, in order to track these energy consumptions separately.
To accomplish such, you can use the . With this integration, you define as many tariffs as required (in accordance with your utility provider contract) and HA will be able to differentiate energy consumptions in each of the tariffs. Please note that each utility provider has its own time schedules for peak and off-peak and you are required to create an automation that switches the utility_meter entity from one tariff to the other.
## The energy dashboard is not visible 
If you do not see the Energy dashboard in the sidebar, make sure you have not removed from your configuration.yamlThe configuration.yaml file is the main configuration file for Home Assistant. It lists the integrations to be loaded and their specific configurations. In some cases, the configuration needs to be edited manually directly in the configuration.yaml file. Most integrations can be configured in the UI. [Learn more]. If you have, you will need to add the energy: integration manually.
## Troubleshooting missing entities 
### Condition 
You are trying to add a sensor to the energy dashboard, but it does not appear in the selection list.
### Resolution 
To find out why the sensor is not showing, check the following points:
####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page



## YAML Style Guide | Home Assistant Developer Docs

Source: https://developers.home-assistant.io/docs/documenting/yaml-style-guide/

On this page
In addition to our general , we also have a set of standards for documenting snippets of YAML. The standards described on this page, apply to all our YAML based code across the project, with the main focus on documentation.
Our YAML standards provide our end-users with a consistent look, the best practices and a uniform approach for solving problems in YAML.
## YAML
This section is about basic YAML usage, and thus not Home Assistant specific.
### Indentation
An indentation of 2 spaces must be used.
```
# Goodexample: one: 1# Badexample:  bad: 2
```

### Booleans
We should avoid the use of truthy boolean values in YAML. They often throw off people new to YAML. Therefore, we only allow the use of true and false as boolean values, in lower case.
This keeps it compatible with the YAML 1.2 specifications as well, since that version dropped support for several unquoted truthy booleans (e.g., y, n, yes, no, on, off and similar).
```
# Goodone: truetwo: false# Badone: Truetwo: onthree: yes
```

### Comments
Adding comments to blocks of YAML can really help the reader understand the example better.
The indentation level of the comment must match the current indentation level. Preferably the comment is written above the line the comment applies to, otherwise lines may become hard to read on smaller displays.
Comments should start with a capital letter and have a space between the comment hash # and the start of the comment.
```
# Goodexample: # Comment one: true# Acceptable, but prefer the aboveexample: one: true # Comment# Badexample:# Comment one: false #Comment two: false # comment three: false
```

### Sequences
Sequences in YAML are also known as lists or arrays. In the Home Assistant world, we refer to them as lists in end-user documentation. This originates from the Python language the Home Assistant core is developed in.
Sequences can be written in two different styles; block and flow style. We prefer the use of block style sequences.
#### Block style sequences
Block style sequences need to be indented under the key they belong to.
```
# Goodexample: - 1 - 2 - 3# Badexample:- 1- 2- 3
```

#### Flow style sequences
The use of flow style should be avoided. While simple, short and clean, with longer data in it, it becomes harder to read.
If used, flow style sequences have space after each comma , and no white space before opening and closing:
```
# Goodexample: [1, 2, 3]# Badexample: [ 1,2,3 ]example: [ 1, 2, 3 ]example: [1,2,3]example: ["light.living_room_window", "light.living_room_corner", "light.living_room_table"]
```

### Mappings
Mappings in YAML are also known as associative arrays, hash tables, key/value pairs, collections or dictionaries. In the Home Assistant world, we refer to them as mappings in end-user documentation.
Mappings can be written in different styles, however, we only allow the use of block style mappings. Flow style (that looks like JSON) is not allowed.
```
# Goodexample: one: 1 two: 2# Badexample: { one: 1, two: 2 }
```

### Null values
Null values should be implicitly marked. The use of explicit null values should be avoided (~ and null).
```
# Goodexample:# Badexample: ~example: null
```

### Strings
Strings are preferably quoted with double quotes (").
```
# Goodexample: "Hi there!"# Avoidexample: Hi there!# Badexample: 'Hi there!'
```

#### Multi-line strings
Avoid the use of \n or other new line indicators in YAML configuration when possible. The same applies to avoiding long, single line, strings.
Instead, make use of the literal style (preserves new lines) and folded style (does not preserve new lines) strings.
```
# Goodliteral_example: | This example is an example of literal block scalar style in YAML. It allows you to split a string into multiple lines.folded_example: > This example is an example of a folded block scalar style in YAML. It allows you to split a string into multi lines, however, it magically removes all the new lines placed in your YAML.# Badliteral_example: "This example is an example of literal block scalar style in YAML.\nIt allows you to split a string into multiple lines.\n"folded_example_same_as: "This example is an example of a folded block scalar style in YAML. It allows you to split a string into multi lines, however, it magically removes all the new lines placed in your YAML.\n"
```

In the examples above the no chomping operators are used (|, >). This is preferred, unless the example requires a different handling of the ending new line. In those cases the use of the strip operator (|-, >-: no trailing new line, any additional new lines are removed from the end) or keep operator (|+, >+: trailing new line, and keep all additional new lines from the end) is allowed.
### Additional string guidance
The Home Assistant YAML section, provides additional guidelines on how to handle strings in Home Assistant configuration examples.
## Home Assistant YAML
Within Home Assistant, we also have some things that can be done in different ways, while still adhering to the above set styling. This part is here to take care of that.
### Default values
A configuration option using a default value, should not be part of the example. Unless, the example is specifically for educating about that option.
For example, our condition options in automations, is optional and an empty list [] by default.
```
# Good- alias: "Test" triggers:  - trigger: state   entity_id: binary_sensor.motion# Bad- alias: "Test" triggers:  - trigger: state   entity_id: binary_sensor.motion condition: []
```

### Strings (continued)
As written in the first chapter, strings are preferably enquoted with double quotes. However, the following value types are exempted from this rule, as is makes our examples more readable:
```
# Goodactions: - action: notify.frenck  data:   message: "Hi there!" - action: light.turn_on  target:   entity_id: light.office_desk   area_id: living_room  data:   transition: 10# Badactions: - action: "notify.frenck"  data:   message: Hi there!
```

### Service action targets
If you want to fire a service action call for an entity ID (for example, to turn on a light), you can do so in three different ways.
The entity ID can be specified as a property of the action level, part of the data that is sent in the service action call or as an entity in a service action target.
Service action targets is the most modern way and allows one to target a service action call for an entity, device or area. Therefore, the target is the most flexible of the options available and is the one that should be used.
```
# Goodactions: - action: light.turn_on  target:   entity_id: light.living_room - action: light.turn_on  target:   area_id: light.living_room - action: light.turn_on  target:   area_id: living_room   entity_id: light.office_desk   device_id: 21349287492398472398# Badactions: - action: light.turn_on  entity_id: light.living_room - action: light.turn_on  data:   entity_id: light.living_room
```

### Properties that accept a scalar or a list of scalars
Home Assistant has a lot of places that access both a scalar value or a list of scalar values. Additionally, sometimes, it even accepts a comma-separated string value as a list.
The following applies in case a single value or a list of scalar values is accepted:
```
# Goodentity_id: light.living_roomentity_id: - light.living_room - light.office# Badentity_id: light.living_room, light.officeentity_id: [light.living_room, light.office]entity_id: - light.living_room
```

### Properties that accept a mapping or a list of mappings
Home Assistant has properties that accept both a mapping or a list of mappings. Well known examples are: condition, action, sequence.
In case a property accepts a single mapping or a list of mappings, a list of mappings must be used, even when a single mapping is passed in.
This makes it easier to understand that one can add more items to it and also easier to copy and paste a single item into your own code.
```
# Goodactions: - action: light.turn_on  target:   entity_id: light.living_room# Badactions: action: light.turn_on target:  entity_id: light.living_room
```

### Templates
Home Assistant templates are powerful, but they can be really confusing or hard to understand for a less experienced user. Therefore, the use of templates should be avoided if a pure YAML version is available.
Additionally, the use of templates requires additional escaping in our documentation to avoid our website code to confuse it for the Liquid syntax. Avoiding templates in general removes the need of additional escaping.
```
# Goodconditions: - condition: numeric_state  entity_id: sun.sun  attribute: elevation  below: 4# Badconditions: - condition: template  value_template: "{{ state_attr('sun.sun', 'elevation') < 4 }}"
```

#### Quoting style
Templates are strings, and thus are double-quoted. As a result of that, single quotes should be used inside the template.
```
# Goodexample: "{{ 'some_value' == some_other_value }}" # Badexample: '{{ "some_value" == some_other_value }}'
```

#### Template string length
Long lines in templates should be avoided and split across multiple lines to make more clear what happens and keep them readable.
See the chapters on strings above for additional information on multi-line string formatting.
```
# Goodvalue_template: >- {{  is_state('sensor.bedroom_co_status', 'Ok')  and is_state('sensor.kitchen_co_status', 'Ok')  and is_state('sensor.wardrobe_co_status', 'Ok') }}# Badvalue_template: "{{ is_state('sensor.bedroom_co_status', 'Ok') and is_state('sensor.kitchen_co_status', 'Ok') and is_state('sensor.wardrobe_co_status', 'Ok') }}"
```

#### Short style condition syntax
Prefer shorthand style templates over-expressive format, as they provide a cleaner syntax.
```
# Goodconditions: "{{ some_value == some_other_value }}" # Badconditions: - condition: template  value_template: "{{ some_value == some_other_value }}"
```

#### Filters
Spacing around the filter pipe marker | is required. If this makes readability unclear, the use of additional parentheses is recommended.
```
# Goodconditions: - "{{ some_value | float }}"  - "{{ some_value == (some_other_value | some_filter) }}" # Badconditions: - "{{ some_value == some_other_value|some_filter }}"  - "{{ some_value == (some_other_value|some_filter) }}"
```

#### Accessing states & state attributes
We do not allow the use of the states object directly if a helper method is available.
For example; don't use states.sensor.temperature.state, instead use states('sensor.temperature').
```
# Goodone: "{{ states('sensor.temperature') }}"two: "{{ state_attr('climate.living_room', 'temperature') }}"# Badone: "{{ states.sensor.temperature.state }}"two: "{{ states.climate.living_room.attributes.temperature }}"
```

This applies to states(), is_state(), state_attr() and is_state_attr(), to avoid errors and error messages when the entity isn’t ready yet (e.g., during Home Assistant startup).



## Troubleshooting | Home Assistant Companion Docs

Source: https://companion.home-assistant.io/docs/troubleshooting/faqs

On this page
Below is a list of common issues and troubleshooting advice to address them. For more support please 
## App crashes on set up
If you are running Home Assistant 0.110 and the app crashes after clicking "continue" during set up, you need to add values for internal_url and external_url. This can be done through the user interface via your . If you do not see this section, you may need to turn on "Advanced Mode" from your profile page first. If these fields are disabled it is likely you have have your configuration stored in configuration.yaml, in this case add the entries under homeassistant: i.e.:
```
homeassistant: ... external_url: URL internal_url: URL
```

Replacing URL with the address you use to access your Home Assistant instance. The values of internal_url and external_url can be the same and should be the same as you have for url: in the http: of configuration.yaml.
When you have saved these changes, restart Home Assisant and, after Home Assistant has finished restarting, reopen the the app.
## I don't see a notify.mobile_app action for my device in my dev-services panel
Once you have the Companion app you will need to restart Home Assistant for the notify.mobile_app action to register. On iOS the notify.mobile_app_<Device_ID> action will be created provided you granted notification permissions during setup, on Android the action will appear after the restart. If you can't see this, or force stop on Android. Then relaunch the Companion app and finally restart your Home Assistant instance. The action should now be listed in the Developer Tools > Actions panel.
If you don't see the action on iOS, check the notification settings within the app (swipe right to bring up the sidebar, then tap "", and then tap "Companion App", then "Notifications"). If the "Push ID" box is empty, tap the Reset button below it.
If you still don't see the action on Android follow the steps to .
## I have a notify.mobile_app_<Device_ID> action but don't receive notifications
Firstly, check your message payload is valid. Look at the examples in the or try sending the simple example below on the Developer Tools > Services page to your notify.mobile_app_<Device_ID> service.
```
{"message": "Hello World"}
```

If this notification is delivered the problem is most likely with your payload.
If the above doesn't work, try the following:
  1. Check your message limits: To allow us to provide a free notification service, each app target is limited to 500 notifications per day. and other special notifications do not count towards this limit.  In iOS you can check your remaining notifications within the Companion app by swiping right to open the sidebar and tapping "", and then tap "Companion App" then "Notifications" and scroll to the bottom of the page. The limit resets everyday at midnight UTC.
  2. Reset your push ID token:  If you have checked you still have notifications remaining, you can reset your notification at the top of the "Notifications" page within the "Companion App" page of . After doing this you may need to the iOS Companion app and then reopen the app and finally restart your Home Assistant instance.
  3. Check your system settings:
     * In the iOS Settings application, navigate to Notifications, then select Home Assistant, and ensure that "Allow Notifications" is toggled on.
     * In the Android Settings application, navigate to Apps, then select Home Assistant, then select Notifications, and ensure that "All Home Assistant notifications" is toggled on. If you're only receiving some notifications, check if the you're using is toggled on.
  4. Start fresh with the Android app:  If you still can't recieve notifications in the Android app then try to .


## I receive an SSL error and/or I am unable to connect to my Home Assistant Instance when away from Home
This often happens when you have the enabled but have do not have turned on. To address this either enable the or swipe right to open the sidebar and the tap "Settings", and then tap "Companion App" then under "Settings" tap "Connection". Make sure the switch next to "Connect Via Cloud" is off and enter the remote address of your Home Assistant Instance in the "External URL" field. This address must be for an encrypted connection, for instructions on setting up an encrypted remote connection to your Home Assistant instances, please see the or .
If you do not have set up at all, the problem is likely that the remote connection is not secured. The Companion App requires an encrypted connection for remote connections. Please see the or for instructions on setting up a secured connection.
## Something in Home Assistant doesn't work the same way it does on my desktop
This is probably not an issue with the Companion App but more likely with Home Assistant or the particular component that isn't behaving as expected. To test the cause please try the following steps.
  1. Firstly, swipe down in the iOS Companion app to refresh your view. In the Android app force stop the application and relaunch it.
  2. If the problem still persists, open your Home Assistant instance in the Safari/Chrome browser (you may have to sign in). If the problem is present in Safari/Chrome, please raise an issue on either the or if it is with a custom component, with the developer of that component. In your issue report, state that the problem exists when viewing on a mobile browser and not necessarily the Companion App.
  3. If the problem does not occur in Safari, please raise an issue on the or the . Please state you followed these steps and the problem only occurs in the Companion app.


## The status bar (top bar with cell/Wi-Fi strength) does not match my theme
If you are using iOS app prior to version 2020.2 or the Android app, to change the color of the status bar to match your Home Assistant theme, please use the action instead of the dropdown menu in the Home Assistant profile page. Using the action will generate an event allowing the Companion App to detect the theme change and apply the correct color to the status bar. See the documentation for details of which keys are used. Note that colors must be specified as hex values (e.g. #0099ff) in your theme and specifying element colors through variable names is not supported.
## I am running the Companion App on multiple devices, the sensor names are too similar and confusing, what can I do?
Starting in Home Assistant Core 0.106, the default sensor names will be registered with your device name as set in the iOS settings app or the Android Companion App Configuration page. For now, you will need to rename each sensor from within the of Home Assistant's Configuration page by following these steps.
  1. Go to the with Configuration.
  2. Find the "Mobile App: Device Name" integration corresponding the device you wish to rename the sensors of and open it
  3. For each sensor you wish to rename, click or tap on the sensor name and then the cog symbol.
  4. Under "Entity ID" change the entity id as required. Do not change sensor. or device_tracker. part of the ID
  5. Repeat Steps 4 and 5 for each sensor you wish to rename


## kCLError when pulling down to manually refresh the app/update Location
To fix this change the location permission for the Home Assistant App to "Always" in iOS Settings>Privacy>Location Services.
## Person entity is not updated with recent location
If you are using the person entity as opposed to the provided device_tracker entity, you may at times notice the person entity state not updating as you would expect. By default any new device you login to with the app will be added as a tracker to the person logging in, which may cause this issue. You can check the person entity using the following steps:
  1. Go to 
  2. Select the person having tracker issues
  3. Review the devices that belong to this person
  4. Remove any device that sits at home or is no longer used. Only keep devices that travel with you in this list.
  5. Save the changes


## Starting fresh with the Android app
At times you may need to start fresh with the Android app as a new feature may not be working properly or something odd happens. Make sure to follow each step precisely without skipping anything.
info
Not all but some issues can be solved by simply logging out of the app and logging back in. If you have setup in your server make sure to login to the app entering your credentials so the app can continue to work when not on the trusted network. If after you attempt to log out and log back and the issue still persists then please continue with the below steps.
  1. Check that Home Assistant Core, the and are up to date.
  2. Clear Storage or App data in Android app. Do not assume it is safe to uninstall and reinstall as that triggers auto-backup which we are trying to avoid here.
  3. In Home Assistant navigate to the . Remove the mobile app entry for the device in question. If you see more than 1 remove them all.
  4. Restart Home Assistant.
  5. Log back into the Android app. If you have more than 1 device, make sure to rename the device during onboarding. Remember to login using your credentials instead of Trusted Networks.


## Device Tracker is not updating in Android app
If you find that the device tracker is not updating as you would expect follow the below steps to ensure optimal settings.
  1. Make sure your device and server meet the prerequisites for location tracking: 
  2. Ensure the app has location permissions granted, all the time. (On Android 12 and newer, allow Precise location when prompted)
  3. Ensure that location (GPS) is enabled on your device.
  4. Allow background access and turn off 'battery optimizations' for the app. 
     * You can check background access in > Companion app. The setting should show a check mark ✔️.
     * Some manufacturers may add additional battery saving features (ex: Power Saving), make sure to disable all of those as well. You can usually access these from the system settings app.
  5. Turn on unrestricted data for the app. 
     * If Data Saver is on, Home Assistant may not send/receive data correctly.


Sometimes the above steps will still not result in location updates reaching your server. The app can receive a lot of location updates and may skip some of them. To determine why, review the app location history logs.
Go to > Companion app > Troubleshooting > Location tracking and enable location history. The app will now keep a log of all location updates received in the last 48 hours.
  * Each update will show the source (for example, "Background location") and result (for example, "Sent"). The app verifies that a location is valid before sending it, and an update may be skipped due to time, accuracy, duplicates, or other reasons.
  * The app should receive updates multiple times an hour. If you do not see updates after enabling the history, make sure to follow the previously mentioned steps. No location history is usually caused by limited background access for the Home Assistant app, or the Android system killing the app.
  * If multiple updates are skipped due to accuracy then check the GPS coordinates to ensure they were correct, and consider increasing the . For example, if you see a valid location getting skipped with accuracy around 350 then set the minimum accuracy setting to 400 as a buffer. Larger values may also lead to inconsistent results so go by valid reports in the logs.

Manual review steps
You can also manually review the location history by using the to determine whats going on. These logs contain more details, but are only kept while the app is open. The entire location decision making process is printed to the logs to help you understand whats happening. When you look at the logs pay attention to the lines that contain LocBroadcastReceiver to follow the decisions. Keep in mind you want roughly 10 minutes of logs so you may need to keep the app open to generate longer logs while the issue is happening.
Below is an example of what you can expect to see to ensure that location updates are coming to the phone. The app will verify that a location is valid before sending it back. These are the logs you can expect to see when a duplicate location is received. The app will not send the same location update to the server if it has not changed for 15 minutes since the last update was sent.
```
2021-02-03 09:03:00.900 7306-7306/? D/LocBroadcastReceiver: Received location update.2021-02-03 09:03:00.903 7306-7306/? D/LocBroadcastReceiver: Last Location:   Coords:(37.4220656, -122.0840897)  Accuracy: 4.663  Bearing: 86.7593462021-02-03 09:03:00.903 7306-7306/? D/LocBroadcastReceiver: Begin evaluating if location update should be skipped2021-02-03 09:03:00.903 7306-7306/? D/LocBroadcastReceiver: Received location that is 74 milliseconds old, 1612371780829 compared to 1612371780903 with source fused2021-02-03 09:03:00.903 7306-7306/? D/LocBroadcastReceiver: Duplicate location received, not sending to HA
```

Below you will find the expected log for successful location results. If you do not see lines like these, make sure to follow the previously mentioned steps.
```
2021-02-03 09:06:34.241 7306-7306/? D/LocBroadcastReceiver: Received location update.2021-02-03 09:06:34.245 7306-7306/? D/LocBroadcastReceiver: Last Location:   Coords:(37.4220656, -122.0840897)  Accuracy: 13.279  Bearing: 0.02021-02-03 09:06:34.245 7306-7306/? D/LocBroadcastReceiver: Begin evaluating if location update should be skipped2021-02-03 09:06:34.245 7306-7306/? D/LocBroadcastReceiver: Received location that is 1126 milliseconds old, 1612371993119 compared to 1612371994245 with source fused2021-02-03 09:06:34.309 7306-7430/? D/LocBroadcastReceiver: Location update sent successfully
```

The logs will indicate whether a report was skipped due to time, accuracy, duplicates or something else.
If you still do not receive location updates after following the above steps and believe this is incorrect, submit a GitHub . If possible attach at least 10 minutes of logs from this troubleshooting step to make it easier for others to help (this may be requested).
## Using a self-signed certificate leads to a blank page in Android
If you are using a self-signed certificate on Android then you may get stuck at a blank screen after entering and/or selecting your Home Assistant instance. In order to correct this issue you will need to make sure the URL is valid and that you import the certificate into Android's Trusted Certificates. Steps to perform this can be found . These steps were written for devices on Android 9+ but are very close for older supported devices.
## Android widget is not working
If you find that a widget is no longer working then these steps may help you resolve the issue.
  1. Check that data saver is disabled on the device, the widget will not work when it is enabled.
  2. Check that background data for the Home Assistant app is enabled.
  3. Remove and recreate the widget.


## Notify action is too similar or not showing up in Android
If you have more than 1 device of the same model and you did not rename your device in Companion App Configuration after logging in then you may have a conflict.
  1. Navigate to in the sidebar.
  2. Tap "Companion App"
  3. Change the Device Name under Device Registration.
  4. Restart Home Assistant to register the new notify action. (i.e. notify.mobile_app_<device_name>)


## Sensors are missing or not updating
When the app is not in the foreground, sensor updates are tied to location updates, so you need to make sure that location permissions are set to "Allow Always" in iOS settings.
The app will also try to send updates in the background however the frequency of these is determined by iOS and is heavily throttled to protect battery life. iOS uses an internal metric, which is not visible to app developers, to prioritize background activities for apps. Apps which you use more will be allowed to do more in the background more frequently, this means that the more you use the Companion App, iOS will learn that the app is important to you and allow more frequent updates via background fetch.
If you want to ensure that the sensors are updated when your device starts charging or the battery level goes below or above a certain limit, the most reliable way is to use an Automation in iOS's app. Set the "When" part to the desired condition and in the "Do" part select the "Update Sensors" action for Home Assistant. You will most likely want to turn off "Ask Before Running" to avoid being prompted before the update is sent. Due to limitations in iOS, you will however always see a notification from the Shortcuts app when these updates are sent.
On Android, sensors will show up as and when they have an update. Some will show up immediately upon enabling and others will show up once permissions have been granted and the state was retrieved. If you do not see a sensor then you may need to wait for the sensor to get a state update so it can send it to your Home Assistant server.
## Text to speech notifications are not working
Check that is updated. Check that it is also set as the default Text to Speech engine, this may be required for certain manufacturers.
## Android Crash Logs
The Android app makes use of Google's ADB feature to log errors. From time to time you may wish to inspect the logs or a developer may ask for crash logs in order to fix your issue. There is an option under Companion App > Troubleshooting > Show and Share Logs. This feature makes it a lot of easier to refresh, share and view the logs. The logs can then be used when you want to create an or when a developer asks for them to troubleshoot an issue. It is important to note that the device logs may or may not contain sensitive information like your Home Assistant URL so make sure to remove sensitive information before sharing.
## Android app battery drain
The android app offers many features, some of which may drain more battery than others. The default settings on the app strive to keep the app as battery friendly as possible. There may come a time when you enable a feature which may lead to more battery drain than desired. This section will list all the things to check on the application before you decide to . For the below options you will need to go to Companion App Settings to check and disable them one by one.
  1. If on the full version check that high accuracy mode is not left enabled all the time.
  2. If on the full version check that Single Accurate Location sensor does not have "Include in sensor updates" option enabled.
  3. Check that Persistent Connection is set to "Never".
  4. If the Bluetooth Transmitter sensor is enabled check that the transmitter is not left on all the time, only enable it when you wish to use it.
  5. Check that Sensor Update Frequency is set to "Normal".
  6. Check that none of the Notification Sensors have the allow list disabled in their respective settings. You always want to define an allow list to prevent heavy battery usage.
  7. If your default dashboard includes a livestream of any sort, try removing or replacing the default dashboard to one without a livestream.





## Installation - Home Assistant

Source: https://www.home-assistant.io/docs/installation/

#  On this page
The first step to getting started with Home Assistant is to install it on a device. There are many ways to run it for all kinds of scenarios and all kinds of skill levels. 
Easiest 
## Plug and play with Home Assistant Green 
The affordable Home Assistant Green is the easiest way to start using Home Assistant. It's plug-and-play and comes with already installed. 
### Home Assistant Green 
The easiest way to get started with Home Assistant
SKILLS REQUIRED 
  * Interest in setting up a smart home


TOOLS REQUIRED 
  * Ethernet connection


Easy 
## DIY with Raspberry Pi 
Raspberry Pi, a mini low-cost computer, is one of the most popular platforms for running Home Assistant. If you want to learn how to DIY, this is a good way to start and gain experience. 
### Install Home Assistant on Raspberry Pi 
A low-cost DIY solution to get started with Home Assistant
SKILLS REQUIRED 
  * Assembling a Raspberry Pi setup
  * Flashing a Raspberry Pi


TOOLS REQUIRED 
  * Raspberry Pi 4 or 5 with power supply (minimum 2 GB RAM)
  * MicroSD card
  * Ethernet connection


## About installation types 
Home Assistant offers two different installation types. Home Assistant Operating System is the recommended installation type. 
  * Home Assistant Operating System: An embedded, minimalistic operating system designed to run the Home Assistant ecosystem on single board computers (like the Home Assistant Green or a Raspberry Pi) or Virtual Machines. It is the most convenient option in terms of installation and maintenance and it supports add-onsAdd-ons are additional standalone third-party software packages that can be installed on Home Assistant OS. [Learn more]. Home Assistant Operating System is the recommended installation type for most users.
  * Home Assistant Container: Container-based installation of Home Assistant. You need to bring your own system (such as Linux) with container orchestration (like Docker), and manually handle updates. Home Assistant Container installations don’t have access to add-onsAdd-ons are additional standalone third-party software packages that can be installed on Home Assistant OS. [Learn more]. 
    * Note: Some integrations, such as Thread and Z-Wave, are controlled by add-onsAdd-ons are additional standalone third-party software packages that can be installed on Home Assistant OS. [Learn more]. There is no out-of-the-box support for these on Container installations. 


HA OS1  | Container1   
---|---  
One-click updates   
1: Names are abbreviated. The full names of the installation types are: Home Assistant Operating System Home Assistant Container 
Intermediate 
## Extend with Home Assistant Yellow 
The extensible Home Assistant Yellow comes with all the ingredients you need to help you build a robust smart home. All you need to do is to bring your own Raspberry Pi Compute Module. 
### Home Assistant Yellow 
The powerful way to run Home Assistant
SKILLS REQUIRED 
  * You're comfortable following instructions on:
  * Installing a compute module and a heat sink
  * Flashing a Raspberry Pi


TOOLS REQUIRED 
Hard 
## Install on other hardware 
Home Assistant can be repurposed and installed on various hardware, such as an Odroid or a generic x86-64 machine. The Home Assistant Operating System allows you to install Home Assistant on these devices even if you have little to no Linux experience. 
### Install Home Assistant on Odroid devices 
A more powerful alternative to Raspberry Pi
SKILLS REQUIRED 
  * You're comfortable following instructions on:
  * Writing boot images
  * Installing an SD card or eMMC


TOOLS REQUIRED 
  * An Odroid device
  * MicroSD card or eMMC
  * Ethernet connection


### Install Home Assistant on x86-64 machines 
Repurpose workstation hardware to run Home Assistant
SKILLS REQUIRED 
  * You can use a command line and install a boot medium on your hardware
  * You're comfortable configuring the BIOS based on instructions.


TOOLS REQUIRED 
Expert 
### Install Home Assistant variants on Raspberry Pi 
A low-cost DIY solution to get started with Home Assistant
SKILLS REQUIRED 
TOOLS REQUIRED 
  * Raspberry Pi 3, 4 or 5 with power supply
  * MicroSD card
  * Ethernet connection


### Install Home Assistant on Linux 
Use Home Assistant OS, Container
SKILLS REQUIRED 
  * Advanced knowledge of Linux
  * Using Linux command line
  * Using Docker Compose (for HA Container)


TOOLS REQUIRED 
  * Machine with Linux installed


### Install Home Assistant on macOS 
Use Home Assistant OS on a VM
SKILLS REQUIRED 
  * Advanced knowledge of macOS
  * Using macOS command line


TOOLS REQUIRED 
  * Machine with macOS installed


### Install Home Assistant on Windows 
Use Home Assistant OS on a VM
SKILLS REQUIRED 
  * Know how to find an IP address on your router
  * Advanced knowledge of Windows
  * Using Linux command line


TOOLS REQUIRED 
  * Machine with Windows installed
  * VirtualBox (for VM)


### Install Home Assistant on other systems 
Use Home Assistant on virtual machines, NAS, and more
SKILLS REQUIRED 
  * Know how to find an IP address on your router
  * Advanced knowledge of Windows
  * Using Linux command line


TOOLS REQUIRED 
  * Machine with Windows installed
  * VirtualBox (for VM)


### Deprecated installation types 
Home Assistant used to offer two additional installation types for advanced users: Home Assistant CoreHome Assistant Core is the Python program at the heart of Home Assistant. It is part of all installation types. It can be installed standalone (without Home Assistant Supervisor) as a container using Docker (this is typically referred to as the Home Assistant Container installation type). For development, Core can also be run using a Virtual Environment (previously referred as the Home Assistant Core installation type). For production setup, the Home Assistant Core installation type is deprecated. and Home Assistant SupervisedThe Home Assistant Supervised installation type is a full UI managed home automation ecosystem that runs the Home Assistant Core program, the Home Assistant Supervisor and add-ons. It comes pre-installed on Home Assistant OS, but can be installed standalone on Debian Linux systems. It leverages Docker, which is managed by the Home Assistant Supervisor. The Home Assistant Supervised installation type is deprecated.. These two methods are now . 
  * Home Assistant Supervised: Manual installation of the Supervisor. 
  * Home Assistant Core: Manual installation using Python virtual environment. 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Getting started
#  On this page



## Common tasks - Operating System - Home Assistant

Source: https://www.home-assistant.io/docs/installation/updating/

#  On this page
This section will provide guides to some common tasks and information which you will need in order to run, maintain, and edit your Home Assistant OS system. For further details on any particular subject, make sure to refer to the documentation for specific add-ons or topics listed here.
## Configuring access to files 
Your Home Assistant Operating server includes two repositories by default: The official core add-on repository, and the community add-on repository. All of the add-ons mentioned here can be installed by navigating to the add-on store using in the UI.
One of the first things to take care of after installing Home Assistant OS is to provide yourself access to files. There are several add-ons commonly used for this, and most users employ a mix of various add-ons. Default directories on the host are mapped to the add-ons so that they can be accessed by the services any particular add-on might provide. On the host system these directories exist on the /data partition at /mnt/data/supervisor/.
Using any of the add-ons listed below, the following directories are made available for access:
### Installing and using the Samba add-on 
The Samba add-on allows you to share the directories on Home Assistant with other systems on your network. After installing the add-on, you can then also edit files using the editor of your preference from your client computer. This add-on can be installed from the add-on store’s official repository.
To install the add-on, follow these steps:
  1. Go to and select Install.
  2. On the Configuration tab, define Username and Password, store them in a safe place, and save your changes. 
     * You can specify any username and password.
     * They are not related to the login credentials you use to log in to Home Assistant or to log in to the computer from which you are accessing the files.
     * The add-on won’t start if username and password are not defined.
  3. For further configuration information, refer to the Documentation tab.
  4. To start the add-on, on the Information tab, select Start.


To access the Home Assistant directories from the other device, follow these steps:
  1. Go to and take note of the Host name.
     * Alternatively, you can look up the host name or IP address of your Home Assistant on your router.
  2. How you connect from another device to Home Assistant depends on your system. Use one of the following options:
     * On Windows: Open File Explorer and in the address bar, enter the IP address or hostname with two backslashes as \\\your.ha.ip.address or \\\hostname.
Screenshot of File Explorer displaying the navigation to a file share using an IP address 
     * On OS X: Open Finder and select Go > Connect to Server… and enter the IP address or hostname as smb://your.ha.ip.address or smb://hostname.
     * On Ubuntu: Open Files and in the address bar, enter the IP address or hostname as smb://your.ha.ip.address or smb://hostname.
  3. Enter the credentials you entered in the Samba add-on configuration.
     * You also have the option of having the credentials stored so that you do not need to enter them again.
  4. Done! You now have access to the directories which you can then mount as a drive or pin to Quick Access.


### Installing and using the Visual Studio Code (VSC) add-on 
The Studio Code Server add-on provides access through a feature-packed web-based version of the Visual Studio Code editor. It currently only supports AMD64 and aarch64/ARM64 machines. The add-on also provides access to the Home Assistant Command Line Interface (CLI) using VSC’s built-in terminal, which allows for checking logs, stopping, and starting Home Assistant and add-ons, creating/restoring backups, and more. (See for further info).
Example of a configuration.yaml file, accessed using the Studio Code Server add-on on a Home Assistant Operating System installation. 
To install and use the Studio Code Server in Home Assistant, follow these steps:
  1. To install the add-on, go to and install the add-on.
  2. Once you have the add-on installed, if you want, select the Show in sidebar option. Then, select Start.
  3. For information on configuration settings, open the Documentation tab.
  4. To start browsing, on the Info tab, select Open Web UI.


### Installing and using the File Editor add-on 
The File Editor add-on is a web-based file system browser and text editor. It is a more basic and light weight alternative to Visual Studio Code. YAML files are automatically checked for syntax errors while editing.
Example of a configuration.yaml file, accessed using the File editor add-on on a Home Assistant Operating System installation. 
To install and use the File Editor in Home Assistant, follow these steps:
  1. To install the add-on, go to . 
     * Once you have the add-on installed, you can edit files within your /config directory.
  2. If you want to be able to access directories outside the /config directory, in the add-on, open the Configuration tab and disable the Enforce basepath option. 
     * Note: The Enforce basepath option is intended to protect you from inadvertently making changes to settings files.
  3. For information on other configuration settings, open the Documentation tab.
  4. To confirm your changes, select Save.
  5. To start browsing, on the Info tab, select Open Web UI.


### Installing and using the SSH add-on 
If you want to use the Home Assistant command line or an SSH client, you can do this through the Terminal & SSH add-on.
The Terminal & SSH add-on provides the following functionalities:
To get started with the Terminal & SSH add-on, follow these steps:
  1. In the bottom left, select your user to open the page. Make sure Advanced Mode is enabled.
  2. To install the add-on, go to the add-on store under and install the Terminal & SSH add-on.
  3. To use the web terminal, start the add-on, then select Open Web UI. 
     * You can now start typing your .
  4. If you want to access from an ssh client, you need to enter credentials: 
     * Open the Configuration page.
     * Enter a password or authorized Keys.
     * Then save and start the add-on.


## Backup 
To learn how to back up the system or how to restore a system from a backup, refer to the backup documentation under .
### Alternative: Creating a backup using the Home Assistant Command Line Interface 
In general, to create or restore from a backup, follow the steps described under . However, If you have the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. installed, you can also create a backup from the command line. Follow these steps:
  1. ha backups list - lists backups and their slugnames
  2. ha backups restore slugname - restores a specific backup
  3. ha backups new --name nameofbackup - create a backup


For additional information about command line usage, use the ha help command or refer to the .
## Updating Home Assistant 
If you have the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. installed, you receive update notifications from different components:
Each of these components needs to be updated separately.
### Updating the Home Assistant Operating System 
Updates of the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. are independent of other updates. They do not trigger repair issues and are usually backward-compatible.
#### Prerequisites 
#### To update the Home Assistant Operating System 
Using the UI
Using the CLI
  1. Open the Settings panel.
  2. On the top you will be presented with an update notification. 
  3. Open the notification for the component you want to update.
  4. If you want to update the system first (recommended), enable the backup toggle.
  5. Select Update.
  6. Check if there are any repair issues and check the logs to see if there are any issues with your configuration that need to be addressed.


```
ha os update
```

Bash
Copy
This updates to the latest version. If you want to update to a specific version instead, use ha os update --version 15.2.
Advanced: changing the boot slot used during the update 
#### About boot slots used during the update 
The Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. uses two boot slots. On first installation, boot slot A is used. After that, on each Operating System update, the other boot slot is updated and reboot is triggered. On that reboot, the system boots from the other boot slot (A ➝ B ➝ A,…). When booting fails, the system automatically uses the previous boot slot, so that it boots from the last working operating system.
#### Changing the boot slot used 
You can manually define that the previous boot slot is used. This can be useful in cases where the system boots but something still seems wrong. For example, when the device is no longer correctly detected or you see another issue that might be related to the latest update of the operating system.
  1. To check which boot slot is currently in use and what OS versions are installed in the individual slots, in the Home Assistant command line, enter the following command:
```
ha os info
```

Bash
Copy
  2. To change the boot slot, enter the following command:
     * This will boot into the other (previous) OS version.
```
ha os boot-slot other
```

Bash
Copy


Alternatively, if the Operating Systems runs on a platform that uses the GRUB bootloader, a boot menu is presented early in the boot. The alternative boot slot can be selected here, marking it active for future boots if the following boot attempt is successful.
### Updating Home Assistant Core 
#### Prerequisites 
  1. and store the backup and the somewhere safe. 
     * This ensures that you can if needed.
  2. Check the release notes for backward-incompatible changes on . Be sure to check all release notes between the version you are running and the one you are upgrading to. Use the search function in your browser (CTRL + f / CMD + f) and search for Backward-incompatible changes.


#### To update Home Assistant Core 
To update Home Assistant Core, choose one of the following options.
Using the UI
Using the CLI
  1. Open your Home Assistant UI.
  2. Navigate to the Settings panel.
  3. On the top you will be presented with an update notification.


  1. Open the notification for the component you want to update.
  2. If you want to backup the system first (recommended), enable the backup toggle.
  3. Select Update.
  4. After the update completed, check if there are any repair issues and check the logs to see if there are any issues with your configuration that need to be addressed.


```
ha core update --backup
```

Bash
Copy
The --backup flag here ensures that you have a partial backup of your current setup in case you need to downgrade.
## Network storage 
You can configure both Network File System (NFS) and Samba/Windows (CIFS) targets to be used within Home Assistant and add-ons. To list all your currently connected network storages, go to Settings > System > Storage in the UI.
Important
You need to update to Home Assistant Operating System 10.2 before you can use this feature.
Screenshot of the list of network shares inside the storage panel. 
### Add a new network storage 
  1. Go to Settings > System > Storage in the UI.
  2. Select Add network storage.
  3. Fill out all the information for your network storage.
  4. Select Connect.


Screenshot of connecting a new network storage. 
#### Network storage configuration 
Name 
This is the name that will be used for the mounted directory on your system. 
Usage 
Here, you select how the target should be used. See usage types below 
Server 
The IP/hostname of the server running NFS/CIFS. 
Protocol3 
The service the server is using for the network storage. 
[NFS]1 Remote share path 
The path used to connect to the remote storage server. 
[CIFS]2 Username 
The username to use when connecting to the storage server. Use User Principal Name for domain accounts. For example: user@domain.com. 
[CIFS]2 Password 
The password to use when connecting to the storage server. 
[CIFS]2 Share 
The share to connect to on the storage server. 
1 Options prefixed with [NFS] are only available for NFS targets. 2 Options prefixed with [CIFS] are only available for CIFS targets. 3 For the CIFS option, only version 2.1+ is supported.
##### Usage types 
Backup 
This will become a target. You can use it when creating an automatic or manual backup. The first storage you add of this type becomes your new default target. If you want to change the default target, check out the documentation below. 
Media 
A new directory with the name you gave your network storage will be created under /media. This directory can be accessed by Home Assistant and add-ons. 
Share 
A new directory with the name you gave your network storage will be created under /share. This directory can be accessed by Home Assistant and add-ons. 
### Change default local backup location 
By default, the first network storage of type Backup that you add is used as your local default backup location.
If you want to change the local network storage that is used to store your backups, follow these steps:
  1. Go to Settings > System > Backups.
  2. Select Settings and history.
  3. In the top-right corner, select the three dots menu and select Change default action location.
  4. Select your preferred network location and save your changes. 
  5. Troubleshooting: Don’t see your external storage location? This list contains only the network storage targets you have added of type Backup.


## Lost Password and password reset 
Please refer to the documentation page.
## Installing a third-party add-on repository 
Home Assistant allows anyone to create an add-on repository to share their own add-ons with the community.
Warning
Home Assistant cannot guarantee the quality or security of third-party add-ons. Use at your own risk.
To add an add-on repository, follow these steps:
  1. Copy the URL of the repository. 
     * The URL is the git repository clone URL (on GitHub, use the Code button and copy the HTTPS URL).
     * This documentation uses an example add-on repository. It is not practically useful but follows the same steps.
     * If you are interested in add-on development, refer to our .
```
https://github.com/home-assistant/hassio-addons-example
```

Text
Copy
  2. Go to and select Add-on store. 
  3. In the top-right corner, select the three dots menu, and select Repositories.
  4. Add the URL of the repository and select Add. 
     * Result: A new card for the repository will appear. 


### Troubleshooting: Repository is not showing up 
If you have added an add-on repository, but it’s not showing up, make sure to refresh your browser. If it still doesn’t show up, the add-on repository may contain invalid configuration data.
  1. Go to and select Supervisor in the top right corner to get the Supervisor log. 
     * It should tell you what went wrong.
  2. Report this information to the add-on repository author.


## Configuration check 
After changing configuration or automation files, check if the configuration is valid before restarting Home Assistant Core.
### Running a configuration check from the UI 
  1. Go to and enable Advanced Mode.
  2. Go to and in the Configuration validation section, select the Check configuration button. 
     * This is to make sure there are no syntax errors before restarting Home Assistant.
     * It checks for valid YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] and valid config structures.
  3. If you need to do a more comprehensive configuration check, .


### Running a configuration check from the CLI 
Use the following command to check if the configuration is valid. The command line configuration check validates the YAMLYAML is a human-readable data serialization language. It is used to store and transmit data in a structured format. In Home Assistant, YAML is used for configuration, for example in the configuration.yaml or automations.yaml files. [Learn more] files and checks for valid config structures, as well as some other elements.
```
ha core check
```

Bash
Copy
## Home Assistant versions 
To see which version your system is running, go to .
### Feature preview 
If you want to preview upcoming features, you can enable preview under .
Labs allows you to preview selected features that are stable but are still being fine-tuned. Preview is different from installing a beta or development version, which are used for development and testing.
For more information, refer to the .
### Running a beta version 
If you would like to test next release before anyone else, you can install the beta version.
From the UI
From the CLI
  1. In Home Assistant, go to .
  2. In the top-right corner, select the three dots menu.
  3. Select Join beta.
  4. Go to the panel.
  5. Install the update that is presented to you. 


  1. Join the beta channel.
```
ha supervisor options --channel beta
```

Bash
Copy
  2. Reload Home Assistant Supervisor.
```
ha supervisor reload
```

Bash
Copy
  3. Update Home Assistant Core to the latest beta version.
```
ha core update --backup
```

Bash
Copy
The --backup flag here ensures that you have a partial backup of your current setup in case you need to downgrade.


### Running a development version 
If you want to stay on the bleeding-edge Home Assistant Core development branch, you can upgrade to dev.
Caution
The dev branch is likely to be unstable. Potential consequences include loss of data and instance corruption.
  1. Join the dev channel.
```
ha supervisor options --channel dev
```

Bash
Copy
  2. Reload the Home Assistant SupervisorThe Home Assistant Supervisor is a program that manages a Home Assistant installation, taking care of installing and updating Home Assistant, add-ons, itself, and, if used, updating the Home Assistant Operating System..
```
ha supervisor reload
```

Bash
Copy
  3. Update Home Assistant CoreHome Assistant Core is the Python program at the heart of Home Assistant. It is part of all installation types. It can be installed standalone (without Home Assistant Supervisor) as a container using Docker (this is typically referred to as the Home Assistant Container installation type). For development, Core can also be run using a Virtual Environment (previously referred as the Home Assistant Core installation type). For production setup, the Home Assistant Core installation type is deprecated. to the latest dev version.
```
ha core update --backup
```

Bash
Copy
The --backup flag here ensures that you have a partial backup of your current setup incase you need to downgrade.


### Running a specific version 
To upgrade to a specific version, you can use the command line (CLI). The example below shows how to upgrade to 2025.12.4. To learn how to get started with the command line in Home Assistant, refer to the .
```
ha core update --version 2025.12.4 --backup
```

Bash
Copy
The --backup flag here ensures that you have a partial backup of your current setup in case you need to downgrade later.
To downgrade your installation, do a instead.
## Using external data disk 
Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. supports storing data on a secondary storage medium. For example, this can be a second internal SSD or HDD or a USB attached SSD or HDD. This data disk contains not only user data but also most of the Home Assistant software as well (Core, Supervisor, etc.). This means a fast data disk will make the system overall much faster.
The data disk feature can be used on an existing installation without losing data: The system will move existing data to the external data disk automatically. However, it is recommended to create and download a full before proceeding!
Caution
All data on the target disk will be overwritten!
Important
The storage capacity of the external data disk must be larger than the storage capacity of the existing (boot) disk.
Important
If you have been using a data disk previously with Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users., you need to use your host computer to delete all partitions before using it as a data disk again.
### Using UI to move the data partition 
  1. Connect the data disk to your system.
  2. Go to Settings > System > Storage in the UI.
  3. Select Move data disk.
  4. Select the data disk from the list of available devices.
  5. Select Move. 
     * Depending on the amount of data, this may take a while.


### Using CLI to move the data partition 
To see the current data disk use:
```
$ ha os info
...
data_disk: /dev/mmcblk1p4
...
```

Sh
Copy
To get a list of potential targets which can be used by datadisk:
```
ha os datadisk list
```

Sh
Copy
To initiate the move to the new data disk use the move command:
```
ha os datadisk move /dev/sdx
```

Sh
Copy
The system will prepare the data disk and immediately reboot. The reboot will take 10 minutes or more depending on the speed of the new data disk; please be patient!
Warning
Using an USB attached SSD can draw quite some power. For instance on Raspberry Pi 3 the official Raspberry Pi power supply (PSU) only provides 2.5A which can be too tight. Use a more powerful power supply if you experience issues. Alternatively use a powered USB hub. Connect the Hub to one of the USB slots of your Raspberry Pi, and connect the SSD to the Hub. In this setup the power supply of the Hub will power the attached device(s).
### Migrating an external data disk to another system 
This section shows how to move an external data disk from one system to another. This can be an option if the following elements apply to your use case:
  * You already have a functioning Home Assistant instance (system 1) that is using an external data disk.
  * You have another, new, Home Assistant instance (system 2).
  * You now want to use the data disk of system 1 on system 2 instead.


The aim is to migrate the data from system 1 to system 2. One way to do this is by . The other way is to move the data disk. This can be an interesting option if you have a large amount of data on your external disk or if your external disk has more storage capacity than your new system.
#### Prerequisites 
  * A Home Assistant instance using an external data disk (system 1)
  * A Home Assistant instance to which you want to move the external data disk (system 2)


#### To migrate an external data disk to another system 
To migrate an external data disk from one system to another, follow these steps:
  1. of both systems and store these backups on another system (not strictly necessary, but recommended just in case, at least for the important data).
  2. Shut down system 1 and remove the data disk.
  3. Make sure system 2 has Home Assistant OS installed, and Home Assistant is up and running. Home Assistant is using the data disk (partition) on the boot drive (e.g. SD card) at this point.
  4. Make sure system 2 has completed the basic steps, including the last steps where devices are discovered automatically.
  5. Plug the external disk into system 2 and go to the Settings > System. Select the three dots menu, and Restart Home Assistant > Reboot system. Result: A repair issue is displayed Multiple data disks detected. 
     * The repair issue comes up because system 2 now sees two file systems with an identical name. During a reboot, there is a name conflict with the existing data disk as it is undefined which file system should be used. This can lead to a random selection of the system you end up with. Hence you must make a decision.
  6. Open the repair issue and choose one of the options: 


## Home Assistant via the command line 
On the , you can use the ha command to retrieve logs, check the details of connected hardware, and more.
### Home Assistant 
```
ha core check
ha core info
ha core logs
ha core options
ha core rebuild
ha core restart
ha core restart --safe-mode
ha core start
ha core stats
ha core stop
ha core update
```

Bash
Copy
### Supervisor 
```
ha supervisor info
ha supervisor logs
ha supervisor reload
ha supervisor update
```

Bash
Copy
### Host 
```
ha host reboot
ha host shutdown
ha host update
```

Bash
Copy
### Hardware 
```
ha hardware info
ha hardware audio
```

Bash
Copy
### Usage examples 
To update Home Assistant to a specific version, use the command:
```
ha core update --version x.y.z
```

Bash
Copy
Replace x.y.z with the desired version like --version 2025.12.4
You can get a better description of the CLI capabilities by typing ha help:
```
The Home Assistant CLI is a small and simple command line utility that allows
you to control and configure different aspects of Home Assistant
Usage:
 ha [command]
Available Commands:
 addons     Install, update, remove and configure Home Assistant add-ons
 audio     Audio device handling.
 authentication Authentication for Home Assistant users.
 backups    Create, restore and remove backups
 banner     Prints the CLI Home Assistant banner along with some useful information
 cli      Get information, update or configure the Home Assistant cli backend
 core      Provides control of the Home Assistant Core
 dns      Get information, update or configure the Home Assistant DNS server
 docker     Docker backend specific for info and OCI configuration
 hardware    Provides hardware information about your system
 help      Help about any command
 host      Control the host/system that Home Assistant is running on
 info      Provides a general Home Assistant information overview
 jobs      Get information and manage running jobs
 multicast   Get information, update or configure the Home Assistant Multicast
 network    Network specific for updating, info and configuration imports
 observer    Get information, update or configure the Home Assistant observer
 os       Operating System specific for updating, info and configuration imports
 resolution   Resolution center of Supervisor, show issues and suggest solutions
 supervisor   Monitor, control and configure the Home Assistant Supervisor
Flags:
   --api-token string  Home Assistant Supervisor API token
   --config string   Optional config file (default is $HOME/.homeassistant.yaml)
   --endpoint string  Endpoint for Home Assistant Supervisor (default is 'supervisor')
 -h, --help        help for ha
   --log-level string  Log level (defaults to Warn)
   --no-progress    Disable the progress spinner
   --raw-json      Output raw JSON from the API
Use "ha [command] --help" for more information about a command.
```

Txt
Copy
### Console access 
You can also access the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. via a directly connected keyboard and monitor, the console.
#### Wiping the data disk from the command line 
In Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users., the ha os datadisk wipe command wipes the data disk. The command deletes all user data as well as Home Assistant Core, Supervisor, and any installed add-ons.
The command ha os datadisk wipe marks the data partition (either internal on the eMMC or the SD card, or on an external attached data disk) as to be cleared on the next reboot. The command automatically reboots the system. Upon reboot, the data is cleared. Then the system continues to boot and reinstalls the latest version of all Home Assistant components.
The ha os datadisk wipe command can only be run from the local terminal. Connect a display and keyboard and use the terminal.
Note, some systems have a reset button you can use to clear the data disk, instead of using the command line:
  * If you have a Home Assistant Yellow with a Raspberry Pi Compute Module 5, use the command line steps described above.
  * If you have a Home Assistant Yellow with a Raspberry Pi Compute Module 4, there is a red hardware button to wipe the data disk. Follow the procedure on .
  * If you have a Home Assistant Green, there is a black hardware button to wipe the data disk. Follow the procedure on .


#### Listing all users from the command line 
In Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users., the ha auth list command lists all users that are registered on your Home Assistant.
The ha auth list command can only be run from the local terminal. Connect a display and keyboard and use the terminal.
## Enable I2C 
Home Assistant using the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. which is a managed environment, which means you can’t use existing methods to enable the I2C bus on a Raspberry Pi. In order to use I2C devices you will have to
  * Enable I2C for the Home Assistant Operating System
  * Setup I2C devices e.g. sensors


### Enable I2C with an SD card reader 
#### Access the boot partition 
You will need:
  * SD card reader
  * SD card with Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users. flashed on it


Shutdown/turn-off your Home Assistant installation and unplug the SD card. Plug the SD card into an SD card reader and find a drive/file system named hassos-boot. The file system might be shown/mounted automatically. If not, use your operating systems disk management utility to find the SD card reader and make sure the first partition is available.
#### Add files to enable I2C 
#### Start with the new OS configuration 
  * Insert the SD card back into your Raspberry Pi.
  * On startup, the hassos-config.service will automatically pickup the new rpi-i2c.conf configuration.
  * Another reboot might be necessary to make sure the just imported rpi-i2c.conf is present at boot time.


### Enable I2C via Home Assistant Operating System Terminal 
Alternatively, by attaching a keyboard and screen to your device, you can access the physical terminal to the Home Assistant Operating SystemHome Assistant OS, the Home Assistant Operating System, is an embedded, minimalistic, operating system designed to run the Home Assistant ecosystem on single board computers (like the Raspberry Pi) or Virtual Machines. It includes Home Assistant Core, the Home Assistant Supervisor, and supports add-ons. Home Assistant Supervisor keeps it up to date, removing the need for you to manage an operating system. Home Assistant Operating System is the recommended installation type for most users..
You can enable I2C via this terminal:
  * Login as root.
  * Type login and press enter to access the shell.
  * Type the following to enable I2C, you may need to replace sda1 with sdb1 or mmcblk0p1 depending on your platform:
```
mkdir /tmp/mnt
mount /dev/sda1 /tmp/mnt
mkdir -p /tmp/mnt/modules
echo -ne i2c-dev>/tmp/mnt/modules/rpi-i2c.conf
echo dtparam=i2c_vc=on >> /tmp/mnt/config.txt
echo dtparam=i2c_arm=on >> /tmp/mnt/config.txt
sync
reboot
```

Bash
Copy


### Troubleshooting 
After rebooting the host there should be i2c-0 and similar device files in /dev. If such device files are missing, enabling I2C failed for some reason. You can check the status of I2C kernel modules by using lsmod | grep i2c in the terminal. If they are loaded, you should find at least the entry i2c_dev. Active usage of the modules is indicated by a number, e.g. i2c_dev 20480 2 would indicate two active I2C device files.
An active I2C can also be checked with a multi meter showing 3.3 V on the I2C pins GPIO2 and GPIO3.
## Related topics 


####  Help us improve our documentation 
Suggest an edit to this page, or provide/view feedback for this page. 
#  Documentation
#  On this page


