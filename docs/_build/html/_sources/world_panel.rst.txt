.. _standard_hdri_maker_background:

World
=====

Qui poi trovare un video tutorial di questa sezione all'opera:


.. Tip::
    Here you can find a video tutorial of this section at work: :ref:`world_manipulation`


Here below the World Panel is shown as it is usually when a new world is added, from the HDRi Maker library:


.. |wp_01| image:: _static/_images/world/world_panel_simple_01.png
              :width: 400
              :alt: Tools Category Light Studio

+------------------------------+------------------------------------------------------------+
|  **Example With HDRi Maker Standard Background**                                          |
+------------------------------+------------------------------------------------------------+
| 1. :ref:`add_diffuse_light`  |  |wp_01|                                                   |
| 2. :ref:`color_properties`   |                                                            |
| 3. :ref:`vector_properties`  |                                                            |
| 4. :ref:`other_properties`   |                                                            |
+------------------------------+------------------------------------------------------------+




The World panel is the one that allows you to adjust the World Background, it is consistent with the nodes that are
found in the world node tree, so it is drawn based on the various situations.

- Example of the simple HDRi Maker Node Tree setup:


  .. image:: _static/_images/world/world_node_complete_01.png
          :width: 600
          :align: center
          :alt: World Node Tree Example Complete




.. _add_diffuse_light:

Add Diffuse/Light
*****************

- Depending on the situation, it may happen that you want to show a solid color visually as a background and keep the HDR image
  lighting. Here below the 2 buttons that allow you to do this:

Add Diffuse
###########

- If you want to add a solid color and keep the current background, this button will add a new background on the
  left of the panel, it will be visible, but it will not have any effect on the scene, so it will not affect the light.


Add Light
#########

- If you add the background through this button, the current background will be visible, but it will not affect the light,
    while the new background will not be visible and will affect the light.


.. _color_properties:

Color Properties (Inputs)
*************************


1. **Use Solid Color  (Button)**

 - If on, it will use a solid color instead of the image. The color property will appear once activated.

2. **Solid Color  (Rgba)**

 - The color of the solid background. (Only visible if Use Solid Color is on)

3. **Emission  (Value)**

 - Adjust the emissivity of the background world. If at 0 no emissivity (therefore completely black/dark background). Attention, on Eevee at the moment the background does not produce shadows, to add shadows, it is advisable to add a 'SUN' light

4. **Exposure  (Value)**

 - Adjust background exposure

5. **Hue  (Value)**

 - Adjust the HUE of the background

6. **Saturation  (Value)**

 - Adjust the Saturation of the background

7. **Colorize  (Rgba)**

 - Colorize the background without completely replacing the image with color.

8. **C. Strength  (Value)**

 - Adjust the amount of colorization



.. _vector_properties:

Vector Properties (Inputs)
**************************

1. **Blur Strength  (Value)**

 - The strength of the blur applied to the background image, 0 = no blur, 1 = full blur

2. **Angle  (Value)**

 - The rotation angle of the background image


.. _other_properties:

Other Properties
****************

- Depending on the situation, additional properties may be displayed.


.. _transparent_background:

Transparent Background
######################


- If on, the background will be transparent, this is useful to make rendering with transparent background, or to use the
  background as a mask for compositing.

   .. Note:: Make sure you render with RGBA otherwise the transparency will not be displayed, in this example, the rendering is set as PNG (Which supports the Alpha channel, i.e. transparency)



      .. image:: _static/_images/world/render_png_rgba_01.png
              :width: 300
              :align: center
              :alt: Render PNG RGBA


Solve Node Problems
###################

- In some cases (If for example the node tree has been manually manipulated) this should solve any problems with the node tree, so that it can be used again.

------------------------------------------------------------------------------------------------------------------------

Diffuse and Light Situation
---------------------------

- If you have added a Diffuse or Light node, the World panel will change in this way:

.. |diffuse_and_light| image:: _static/_images/world/world_panel_diffuse_light_01.png
                        :width: 400
                        :alt: World Panel Diffuse and Light



+---------------------------------+------------------------------------------------------------+
|  **Example With HDRi Maker Diffuse + Light Background**                                      |
+---------------------------------+------------------------------------------------------------+
| 1. :ref:`remove_diffuse`        |  |diffuse_and_light|                                       |
| 2. :ref:`change_diffuse`        |                                                            |
| 3. :ref:`invert_diffuse_light`  |                                                            |
| 4. :ref:`change_light`          |                                                            |
| 5. :ref:`remove_light`          |                                                            |
+---------------------------------+------------------------------------------------------------+


.. _remove_diffuse:

Remove Diffuse
**************

- This button removes the diffuse node group from the node tree. Once removed, the "Light" node takes the role of the
  diffuse and light, so the color of the diffuse will be that of the Light, and the Light will be visible.
  (You return to the initial state) See here: :ref:`standard_hdri_maker_background`



.. _change_diffuse:

Change Diffuse
**************

- This button is used to load a background for the Diffuse **Press SHIFT+Click to import a Background**.
  (If SHIFT is not pressed, it will be loaded from the current preview of the HDRi Maker library)


.. _invert_diffuse_light:

Invert Diffuse/Light
********************

- This button inverts the Diffuse with the Light, and vice versa. Once pressed, in the interface, the left column moves
  to the right, and the right column to the left.


.. _change_light:

Change Light
************

- This button is used to load a background for the Light **Press SHIFT+Click to import a Background**.
  (If SHIFT is not pressed, it will be loaded from the current preview of the HDRi Maker library)


.. _remove_light:

Remove Light
************

- This button removes the Light node group from the node tree. Once removed, the "Diffuse" node takes the role of the
  diffuse and light, so the color of the diffuse will be that of the Diffuse, and the Diffuse will be visible.
  (You return to the initial state) See here: :ref:`standard_hdri_maker_background`


.. _change_light_path:

Change Light Path
*****************

- This selector allows you to choose which type of blend to use between Diffuse and Light, there are 2 options

  - **Is camera ray**
     - Allows you to view the Diffuse only in the camera and point of view, but it will have no effect on the light.

  - **Is Reflection Ray**
     - Excludes the Light in reflections, this in some cases is useful for the shadow catcher, when you add a reflection
       on the shadowcatcher, it will reflect only the objects in the scene, but not the Light, so you will not see
       any image of the background reflected on the shadowcatcher here: :ref:`shadow_catcher`





Unknown world Situation
***********************

When a World is not recognized as an HDRi Maker world, the panel draws an interface similar to the native
of Blender, this is good, but it is not optimal, because with it it is not possible to use some advanced functions of HDRi Maker.

Here is an example of the situation that can occur:

.. image:: _static/_images/world/unknown_world_01.png
        :width: 400
        :align: center
        :alt: Unknown World 01 IT


This situation occurs in 2 occasions:

1. When the World present in the scene was not created with HDRi Maker
2. When you remove a World with HDRi Maker, and a Default World "Gray" is created automatically (By the way, if you don't want it to happen, press "Shift" + Remove)


So the "Try To convert" button will try to recover an HDR/EXR image from the World, if present, the image will be taken
and transported into an HDRi Maker World, then it will be applied to the scene. This is useful to fully exploit the
HDRi Maker functions.

.. Note:: It will only work if there is an HDR/EXR image. The script analyzes all Group nodes and Subgroup nodes,
          so in most cases it should work.


If you want to use this configuration as "Light" or "Diffuse" you can do it, just press one of the 2 buttons (+) at the top of the panel
this will try to use the current nodes as if they were those of HDRi Maker to configure a "Diffuse" or a "Light" As explained here: :ref:`add_diffuse_light`

