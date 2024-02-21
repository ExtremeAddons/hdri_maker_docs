Updates Log
===========

3.0.117
-------

**Release date: 21-02-2024 (D/M/Y)**

- **Fix - Update for Blender 4.1 API**

    Update to the new Blender 4.1 API and various fixes for the addon to work on Blender 4.1

- **Fix - Asset Browser Creation Popup Message**

    Regardless of the library you wanted to create, the text relating to the creation of the Default Library was always shown, in truth it was just a code error, as the selected library was actually created with the button, it was just a misleading message. Fixed, now shows the right text

3.0.116
-------

**Release date: 02-11-2023 (D/M/Y)**

- **BugFix - Reuse images**

    The texture image loading script analyzed whether the image was already present in the project and checked whether the image had the data via image.has_data, this could happen if the image did not have has_data an error was raised in the texture loading. The script has been improved and if there is no has_data, the image is now reloaded correctly

- **BugFix - Add Dome-Hooks Error**

    It happened that if the VIEW_3D windows were more than one, trying to add a Dome or adding the Hooks to the Dome raised an error 'TypeError: Region not found in area', this because the function that did the override did not take into account the Region, but only the area, so everything worked fine only if the 3D windows was only one.

3.0.115
-------

**Release date: 12-10-2023 (D/M/Y)**

- **Improvement - Support For Blender 4.0**

    Now HDRi Maker also works on Blender 4.0 maintaining backward compatibility with previous versions from 3.0 onwards

- **BugFix - Export Image**

    From the Save Menu, Export image did not work well, the Blender image.has_data APIs always returned False, now I have solved it by updating the image before checking if image.has_data with image.update()

- **BugFix - Batch Save**

    If the batch save contained a .blend file and the .blend file for some reason did not have a world, this created an error, now it is bypassed, in addition at the end of the operation. In addition, now the preview icons are redrawn in order to make the backgrounds immediately available from the HDRi Maker Browser menu

- **BugFix - Add Diffuse/Light Bug (Convert World to HDRi Maker World)**

    If you added a Diffuse or Light, from the 'World' panel if the World nodes had not been created with HDRi Maker, they were no longer added to a Group (Which had to be created) now, the group will be created and positioned correctly both as Diffuse and as Light

- **Improve - Restore Node Value**

    The confirmation method has been improved with a new popup

3.0.114
-------

**Release date: 30-09-2023 (D/M/Y)**

- **Bugfix - Add light during paint mode error**

    If you were in paint mode and tried to add a light, an error occurred, this has now been fixed by adding the object mode check

- **Improvement - Link Unlink World-Dome Rotation Buttons**

    A depress state has been added to the respective buttons for the synchronization of the dome and background rotation, now when the respective driver is activated, the button lights up, to indicate that it has been activated, and turns off in case of unlink or activation of the opposite driver

- **Patch - Regeneration of Preview Icons**

    A button named 'Regenerate Previews and Icons' has been added in the options section, this button regenerates the icons and the preview icons of the backgrounds, now also regenerates the icons damaged by the Beta-Alpha versions of Blender, so they are regenerated simply by copying and deleting the damaged icons and reloading the Background Previews

- **Added - Purge Cache Button into Options Section**

    HDRi Maker uses Json files that store library paths, so that whenever the addon is installed in a new version of Blender, the addon itself recognizes the library paths set by another version of Blender, this is also useful for update the addon, which in fact, once updated and started Blender, will automatically recognize the library paths. There have been some cases, however, that the addon stored paths that no longer existed, and for some reason they were not removed automatically, for this reason this button has been added, which in addition also removes all the .json files present in the addon folder called 'online_utility', these files are for updates and other online functions, these are always deleted via this button

- **Fix - Library paths storage**

    It has been reported to us that the library paths stored in the .json file present in the ExtremeAddons folder (As explained in the previous point) may no longer exist, so if this is the case, they will be ignored and no longer set to the default and user libraries so as to avoid confusion

3.0.113
-------

**Release date: 29-07-2023 (D/M/Y)**

- **Bugfix Json Save**

    During the saving of json files, it could happen that if blender stopped abnormally, the json file would be corrupted. Now a temporary saving system has been implemented, only if the writing is successful, the file is then converted to json. This to avoid corrupted files

- **Bugfix - Error during the creation of the Asset Browser**

    In some cases (Probably still to be fully understood) the process was blocked by an error if the background file was not present in the library folder, so an exception was put, in case it occurred, the process bypasses the background and continues

- **Improvement - Added additional warning if the background file is not present**

    As described in the previous point, if the preview file is not present, by pressing the 'Add' button an additional message will now be shown informing in which exapack volume the missing background is present, so that you can download only that package

3.0.112
-------

**Release date: 14-07-2023 (D/M/Y)**

- **Alpha - Beta Version Alert Message added**

    If the version of Blender used is a Beta or Alpha version, a message will be displayed in the main interface of the addon, a confirmation button will hide the message until the next start of Blender, this has been added because many users try the new unstable versions of Blender and sometimes the addons don't work, I hope this message is useful

- **Node Alignment improved**

    Added a function that better calculates the size of the nodes, even in conditions where the nodes are not displayed, the node.dimensions property does not work until the nodes are displayed, a log with the dimensions of the nodes has been added via file.json

- **Bugfix - Add background reset the orientation and the other properties**

    If you add an HDR in version 1k and then replace it with the same background at another resolution (For example 4k) the background rotation was reset, this no longer happens, the rotation remains unchanged and also the other properties

- **Improvement - Library paths updated when the addon is activated**

    When the addon is activated with the checkbox, if it was already activated before, it now updates the library paths and you don't have to reassign the paths. This only happens if HDRi Maker was already installed and with the library paths already assigned (It only works if the paths were assigned in the previous 3.x version)

- **Bugfix - Error Index negative during Add Hooks in Blender 3.6**

    For some reason, the vertex indices of the Dome, changed to negative indices during the compilation of the vertex list and the assignment of a Modifier for each Hook. Now the list is compiled in a further step and the indices no longer change.

3.0.111
-------

**Release date: 08-05-2023 (D/M/Y)**

- **Bugfix - Error During Asset Browser Creation**

    In some cases (Probably still to be fully understood) it showed a mat_info.get() error, this is because an exception had not been set to check if mat_info really existed. It has now been fixed and the error will no longer appear

- **Added - Remind me later button**

    In order to hide the update message (If the addon need update) a new button has been added to the message, this button will hide the message in the current Blender Session

- **Bugfix - check_existing Error**

    During the creation of the Asset Browser In versions prior to Blender 3.4 an error (check_existing) occurred, this was due to the fact that the check_existing parameter was not present in the bpy.ops.preferences.asset_library_add operator, now this parameter has been removed if the Blender version is prior to 3.4

3.0.110
-------

**Release date: 29-03-2023 (D/M/Y)**

- **Added - Creation of library in Asset Browser**

    For now it is limited to Worlds only, if drag and drop is done, only the world is added. All other features need to be added via the HDRi Maker panel. This python API limitation of Asset Browser.

- **Added - Convert World to HDRi Maker World**

    Now if the World is not of type HDRi Maker, the usual menu appears in the HDRi Maker World panel, with a button called TRY TO CONVERT, this operator, attempts to convert any World to an HDRi Maker Wordl. This will only work if there is an HDR/EXR File in the World. This for obvious reasons, first of all, will allow you to use some functions present only if the group nodes are recognized by HDRi maker.

- **Added - Reload Dome Image**

    A new Reload Image button has been added to the Dome menu. This is useful if you work with asset browsers, once any World (even of a non-HDRi Maker type) has been added, it can also be added to the dome, without necessarily having to add a new dome. This works provided that in the World Added to the scene, there is an HDR or EXR image inside the World nodes.

3.0.105
-------

**Release date: 16-03-2023 (D/M/Y)**

- **Bugfix - Pose Mode Bug**

    If in Pose Mode, trying to add Backgrouns-Dome-Lamps, an error occurred. This has now been fixed, if you are in pose mode and do one of the above operations, the object goes back to Edit Mode, and the script executes correctly.

- **New feature - Dome Rotation**

    A property has been added to rotate the Dome, this is useful, because when the Hooks are applied, now the Hook will rotate with the dome, in order not to have to rotate the objects in the scene

- **Bug Fix - Installation User Library Missing**

    It could happen that during the first installation, the user chose the USER_LIBRARY directory, in a non-existent location, this did not start HDRi Maker and had to be removed, then add the USER LIBRARY, now this is solved, The addon if it sees that there is no USER Library In the chosen path, it will create it automatically during installation (Exapack installation) This already happened, but only if no User Library path was selected

- **Improvement - Save the Expansion Library directories**

    When you update the addon from version 3.x and up of HDRi Maker, the addon now also saves the directories and names of the Expansion Library, so that if you update the addon, you do not have to re-indicate the paths of the Expansion Library. Now all directories are stored in a json file, in order to simplify the update phase of the addon. Even when you switch to a later version of Blender, the addon always recognizes the directories, as long as they still exist and have not been moved on the computer to another location

3.0.104
-------

**Release date: 03-03-2023 (D/M/Y)**

- **Bugfix - Retrocompatibility Dome Material**

    Dome material was reflective on Blender versions 3.0 to 3.3 (Not on 3.4) Fixed issue, it was the Mix nodes that didn't have proper input and black was grayed out, causing reflection to always be on, and also the metallic. Now everything should work from Blender 3.0 and up. Previous versions have been abandoned, as they are now obsolete. a positive note for the support of Blender 3.3 which is an LTS release, so it is necessary to make HDRi Maker workable on it.

3.0.103
-------

**Release date: 03-03-2023 (D/M/Y)**

- **Bugfix - (Choose path) For Mac and Linux**

    For some reason, it was no longer possible to select the library paths. I had used the ntpath.normpath module to make sure I normalized the paths. It worked during testing, but now it doesn't work anymore on Mac and Linux. Maybe I missed something. The new version checks the path with os.path.normpath. You should now be able to select the path to the libraries correctly

3.0.102
-------

**Release date: 02-03-2023 (D/M/Y)**

- **Bugfix when installing expansions**

    It could happen that during the installation of Expansions, if they were already present on the disk and not in the list of HDRi Maker expansions, they were installed in the Default library. This could rarely happen, only if they had already been installed before. I fixed this to avoid potential confusion in some rare cases.

- **Bugfix: Removes files of expansion volumes**

    Expansion volumes were not removed from the Updates menu, they can now be removed.

3.0.101
-------

**Release date: 01-03-2023 (D/M/Y)**

- **Installation Bugfix for Mac-Linux**

    For some reason, using os.path.realpath didn't work well on Mac and Linux. It has been replaced with ntpath.normpath module, this blocked the installation of files.exapack now it's back it works on Win-Mac-Linux

3.0.100
-------

**Release date: 28-02-2023 (D/M/Y)**

- **Completely redesigned interface**

    The new interface has been completely redesigned to be simpler and more intuitive, we have inserted custom menus for each functionality of the addon, now the menus are sortable

- **Addon rewritten almost from new**

    All the code has been reviewed and structurally improved

- **New panel structure**

    The panel has been completely revised and improved, now it is divided into sections that can be moved open and close at will

- **Tag system added**

    Now all backgrounds have tags that allow you to filter the search

- **New Volumetric system**

    Now the Volumetric is managed by a group node system, this simplifies the addition in the future of new volumetric nodes, this for the simulation of fog and dust

- **Diffuse and Light management added**

    You can now add a solid background with HDR lighting, for example, you can add a completely Black background, using the lighting of an HDRi

- **Shadow Catcher Eevee**

    The Eevee Shadow Catcher has been revised and improved. But the support for the displacement of the shadow catcher has been removed, this was not very functional

- **Lights (Light studio)**

    A new panel dedicated to lighting functions. Here you can manage the lights or the sun, and the lighting settings

- **Ability to animate all (or almost all the sliders)**

    Previously HDRi Maker did not allow you to animate the sliders, this because the properties did a callback to the main property, now this problem has been solved, because I adopted the same drawing technique of the panel, thanks to the experience gained with Extreme PBR, All sliders (Or Almost) can be animated with keyframes

- **Library link management improved**

    The library management system is simpler, the paths to the libraries are opened via button, this to avoid the problem of relative paths, same system adopted in Extreme PBR

- **Additions of Expansion Packs**

    From this version, it is possible to add Expansion, 1 Expansion is already provided with the addon, this Expansion, contains more than 100+ new backgrounds from HdrMaps.com, the owner of this site has approved with pleasure the use of his backgrounds, for this reason, it was decided to add this Expansion

- **Import on the fly**

    By pressing the SHIFT key and the ADD button, you can import a background on the fly, this allows you to use your Background, without having to add it to the library

- **Dome (Classic) Improved**

    I recreated the dome with care, paying attention to its topology. This to be able to divide the dome with a modifier, in order to improve the experience with the Wrap system already present in the past

- **Wrap system improved**

    Now the Wrap system, has the possibility to decide the direction of the Wrap on the ground, (Negative or Positive), in addition now the Wrap objects are listed in the dedicated panel

- **Ground Material system improved**

    Now the addition of the Ground material has been improved, every object to which the Ground material is applied, is now listed in the dedicated panel, in addition it is possible to choose the function of this material in 2 options, the first assumes the ground projection, the second assumes the Top dome projection, this allows you to project on the object the same projection of the dome in the upper part

- **Dome Material Improved**

    Now the dome material and all its nodes, have been improved and revised, this now allows greater control on the projection of the dome, allowing to adjust and stretch the upper or lower part (Ground) of the dome

- **Dome Cube Added**

    A new dome in the shape of a cube has been added, the projection now also takes place on a cube

- **Dome Cylinder Added**

    A new dome in the shape of a cylinder has been added, the projection now also takes place on a cylinder

- **Two variants to the classic Dome Added**

    Another 2 versions of the classic dome have been added, these 2 versions are similar, but the curvature that is between the ground part and the top part changes

- **Dome Hooks Added**

    The new Hooks system allows you to modify the shape of the dome, to modify the shape of the dome, and adapt it to the projected image, for example you can recreate the angle of a wall present in the image (This only works on dome Cube and dome Cylinder at the moment)

- **Reflection Plane On the dome**

    When you add a dome, now a reflection plane is added on the ground, in order to be able to add realistic reflections on the ground in Eevee mode

- **Dome With Bump Map**

    Now on the ground of the dome it is possible to add a Bump Map effect, this is simulated by the same image projected on the dome, in order to be able to create a roughness effect on the ground

- **Shadows on the Ground**

    Now the area where the dome receives shadows has been improved and faded, you can now decide how far the ground receives shadows (In the previous version this detachment was almost sharp, and created a color change problem between the ground and the rest of the dome)

- **Reflections on the Ground**

    As mentioned earlier, now it is possible to add reflections on the ground, metallic and roughness effect 

- **Sun, Background, Dome Synchronization**

    Now you can choose whether to synchronize the sun, the dome with the background. This thanks to the addition of drivers if needed

- **Improved Blur background effect**

    The Blur effect of the background has been improved, in the previous version there were graphical errors in some points of the background, now this has been solved

- **Blur effect in the dome**

    Now it is possible to add a Blur effect in the dome, The effect can be managed based on the distance of the observation point and be inverted (Similar to the effect of the camera depth of field)

- **New installation system**

    From this version the installation of the libraries takes place through packages with .exapack extension this format is recognized by the addon and is managed by the new installer

- **Improved update control**

    Now the update check takes place on an online json file. Before the check system was obsolete and took place on the Blendermarket page

- **New documentation**

    Now the online documentation has been improved, now throughout the addon it is possible to access it through the buttons with the (?) icon, this opens directly the online documentation page to the corresponding page

- **Improved the import of Backgrounds**

    Now you can Try to import World Backgrounds from your .blend files, the addon tries to recover the first Background from the .blend project, this is not guaranteed to work every time, but in most cases if your .blend file contains a Background, it will be imported correctly

