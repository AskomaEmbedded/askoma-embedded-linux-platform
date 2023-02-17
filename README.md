# Askoma Embedded Linux Platform

This is an "ready to use" platform for Yocto Project. The intent of this platform is to make the project easier to handle, reliable and faster to use and mantain, automating some tasks that would be manually done.
Clone this repository using `repo` tool (which wee will step in later) and you will be able to build your own Yocto Project image in a few steps!

## Setup instructions

These instructions initialize an embedded Yocto platform to use the [meta-askoma-bsp](https://github.com/AskomaEmbedded/meta-askoma-bsp) layer.

## Getting the `repo` tool

The first step is to download and prepare all the Yocto Project environment, you need to have the `repo` tool installed in your host machine.

For Debian/Ubuntu Linux distro you can install it running:

```bash
sudo apt install repo
```

If you're using other Linux distro or the `repo` tools is not in the repository, you can download directly from upstream and set your distro as shown below:

```bash
mkdir ~/bin
curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
PATH=${PATH}:~/bin
```

## Download the platform source

The next step is to download the BSP source code, we have a platform to fetch all files that is necessary to build the project.

To download all sources run the following commands:

```bash
mkdir askoma-platform
cd askoma-platform
repo init -u git@github.com:AskomaEmbedded/askoma-embedded-linux-platform.git 
repo sync
```

At the end of the commands, you'll have every metadata you need to start work with.

### Supported hardware

This platform includes a BSP that supports the following hardware:

| Yocto Project Machine  | Askoma Hardware                                     |
|------------------------|-----------------------------------------------------|
| imx6ull-em-r1          | Energy Manager 1.2 and 1.3 (based on NXP i.MX 6ULL) |
| imx8mm-em-r1           | Energy Manager 2.0 (based on NXP i.MX 8MM)          |

## Preparing the environment

Before starting to work you need to load the Yocto variables to run `bitbake` command.

Example:

```bash
MACHINE=imx6ull-em-r1 source setup-environment build
```

Note that you need to run the command above for all new terminal, the
loaded variables are only visible to the terminal that you source the
`setup-environment` script.

## Images availables

### `askoma-image-base`

This is a basic image which contains simple resources and an SSH server to access the system as it doesn't have a graphical UI.

The image can run directly from the SD Card or internal storage.

### `askoma-image-base-installer`

This image has the only purpose to install the `askoma-image-base` into the internal storage (eMMC or NAND).

### Building the image

See all available images in the [#images](#images) section and check the
[Preparing the environment](#preparing-the-environment) section.

To build the image use `bitbake <image-name>`. Example:

```bash
bitbake askoma-image-base
```

This process **can take a long time** depending on your host machine.

When the image is ready, the resulted files are available in the `deploy` directory. By default it is located at `build/tmp/deploy/images/<machine-name>/` (where `<machine-name>` will depend on the choosen Yocto Machine).

### Writing the SD card

To use this image you need to flash it to a *SD card* using the following command:

``` bash
sudo bmaptool copy build/tmp/deploy/images/<machine-name>/<image-name>.wic.gz /dev/sd<X>
```

Note that the file extension of the image may vary according the compression method applied.

The `sd<X>` is the device that *SD card* was addressed in you host machine, you can check your using the `dmesg` command.

Example:
``` bash
sudo bmaptool copy build/tmp/deploy/images/imx6ull-em-r1/askoma-image-base.wic.gz /dev/sde
```

#### Installing the `askoma-image-base-installer`

You can install `askoma-image-base` into the internal storage, instead booting from SD card. To achieve this, follow these steps:

1. Generate a `askoma-image-base-installer`;
2. Burn a micro SD card with the image and insert into micro SD card slot;
3. Turn on the board and you will see a LED blinking;
4. When it get ready the LED will stop blinking and stay on;
5. Reboot the board without the SD card;
6. Ready. The image will boot automatically from internal storage.

## References

-   [Heading for the Yocto Project](https://github.com/CollaborativeWritersHub/heading-for-the-yocto-project/releases/download/18.10.0/Heading-for-the-Yocto-Project.pdf)
-   [Embedded Linux Development using Yocto Projects - Second Edition](https://www.amazon.com/dp/B0751HKPB4)
-   [Yocto Project Reference Manual](https://docs.yoctoproject.org/ref-manual/index.html)
