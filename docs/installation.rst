Installation
============

.. Note:: If you are already a HDRi Maker user and you currently have a version prior to 3.0.100, please
          uninstall it and proceed with the installation of this new version.
          If you already have a version 3.0.100 or higher, you do not need to uninstall the previous one.


Instal the addon
-------------------------

.. _mac_safari_zip:

Download the files
******************

In your product page, you can find various files, the main ones for the installation are the following:


- **hdri_maker_v301##.zip** is the addon for blender, While the
- **HDRiMkr_##_Vol_#.exapack** are the files of the library. and they are divided with increasing number.

The **.exapack** files are installed by the addon, they are not installed manually, the HDRi Maker addon
once installed manages your exapack packages.


.. Note:: For Mac users, it often happens that Safari Browser is set to decompress .zip files, make sure this does not happen,
          otherwise the .zip file will no longer be a .zip file and you will not be able to install the addon as follows.

.. Tip:: Just go to the Safari menu bar at the top left and click on Safari>Preferences, then remove the check mark from
         "Open safe files after download" in the "General" window. Done, if in the future you download zipped files with safari,
         they will no longer be unzipped.


Install Into Blender
********************

Now, download the addon and install it in Blender, the procedure is as follows:

**1)** Download the addon (Remember that you must be logged in):

    - If you purchased on Blendermarket you can find the addon here:

       - https://blendermarket.com/account/orders


    - If you purchased on Gumroad you can find the addon here:

       - https://app.gumroad.com/library

    - Addon name Example: **hdri_maker_v30100.zip** (The number can be different, it depends on the version you are downloading)


   .. Important:: The addon file must remain in zip format! Do not unzip the file, otherwise you will not be able to install it correctly.
                  This note is especially for Mac users. If you do not know how to prevent Safari from decompressing zip files, take a look here :ref:`mac_safari_zip`

2) Once the addon is downloaded, open Blender and go to:

   ``Edit > Preferences > Add-ons > Install``

.. image:: _static/_images/installation/install_addon_in_blender_01.png
    :width: 800
    :alt: Main Panel

3) Select the downloaded file (**hdri_maker_v30100.zip** <-- !This name is only an example!) and click on "Install Addon" (The name of the file can be different from version to version)

.. image:: _static/_images/installation/install_addon_zip_blender_01.png
    :width: 800
    :alt: Main Panel

4) If everything went well, the addon is in the list of installed addons, you can also search for it by typing "HDRi Maker"
   Mark the checkbox to activate it.

.. image:: _static/_images/installation/install_addon_zip_blender_02.png
    :width: 800
    :alt: Main Panel


5) Now in the 3D view window of Blender you should already be able to see the HDRi Maker Welcome panel, click on
   "Go to install", the HDRi Maker Preferences window will open on the "Install Libraries" section (TAB)

.. image:: _static/_images/installation/go_to_install_libraries_01.png
    :width: 800
    :alt: Main Panel

.. Tip:: If you do not see the HDRi Maker Welcome panel, you can open it by pressing the "N" key on the keyboard.


.. _how_to_install_libraries:

Install The library
-------------------

- Se hai installato correttamente l'addon, ora puoi passare all'installazione della libreria.

1. Download the file HDRiMkr_1k_vol_1.exapack, this is the package containing the 1k resolution files,
   it is also the smallest package in terms of MB, so it is easy and fast. You can download the others at any time.









New exapack library
-------------------

As for the libraries, from version 3.0.100 onwards, they will be distributed in the form of exapack packages.
All new packages will be in the form of numbered volumes Here is an example of nomenclature:

- **HDRiMkr_1k_vol_1.exapack**: HDRiMkr 1k Volume 1: Contains files from 1k, previews, and data files
- **HDRiMkr_2k_vol_1.exapack**: HDRiMkr 1k Volume 2: Contains files from 2k, previews, and data files
- **HDRiMkr_4k_vol_1.exapack**: HDRiMkr 1k Volume 3: Contains files from 4k, previews, and data files
- **HDRiMkr_8k_vol_1.exapack**: HDRiMkr 1k Volume 4: Contains files from 8k, previews, and data files
- **HDRiMkr_16k_vol_1.exapack**: HDRiMkr 1k Volume 5: Contains files from 16k, previews, and data files

The packages are consecutive, Vol_1, Vol_2, Vol_3, The maximum weight of each package is 2.5 GB, this limit is not exceeded
this limit to avoid download and installation problems, since those who have a slower connection, could
encounter timeout problems.

.. Note:: The 2k packages are more, because the individual files contained in them are much larger.
          For example, the 2k package is about 4 times the size of the 1k package, so it needs more Volumes in order to
          not exceed the maximum weight of 2.5 GB.










