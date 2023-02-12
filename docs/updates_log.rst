Updates Log
===========

3.0.100
-------

**Release date: 20-02-2023 (D/M/Y)**

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

    From this version, it is possible to add Expansion, 1 Expansion is already provided with the addon, this Expansion, contains more than 100 new backgrounds from HdrMaps.com, the owner of this site has approved with pleasure the use of his backgrounds, for this reason, it was decided to add this Expansion

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

