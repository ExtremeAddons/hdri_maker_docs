.. _standard_hdri_maker_background:

World
=====


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

- In Base alla necessità, può capitare che tu voglia Mostrare un colore solido visivamente come sfondo e mantenere l'illuminazione
  dell'HDR immagine. Qui di seguito i 2 bottoni che ti permettono di fare questo:

Add Diffuse
###########

- Se vuoi aggiungere un colore solido e mantenere lo sfondo attuale, questo bottone aggiungerà un nuovo sfondo sulla
  sinistra del pannello, esso sarà visibile, ma non avrà effetto sulla scena, quindi non influenzerà la luce.


Add Light
#########

- Se aggiungerai lo sfondo tramite questo bottone, l'attuale sfondo sarà visibile, ma non influenzerà la luce, mentre il nuovo
  sfondo non sarà visibile e influenzerà la luce.


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
