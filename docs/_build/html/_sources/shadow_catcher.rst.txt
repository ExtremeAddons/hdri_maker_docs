.. _shadow_catcher:

Shadow Catcher
==============


.. Figure:: _static/_images/shadow_catcher/shadow_catcher_800x300.png
            :align: center

.. class:: center

    This model "Lightning Mage (Free Download)" comes from sketchfab and was created by **Adipriatna** under license **CC BY**,
    you can find it at this link:https://sketchfab.com/3d-models/lightning-mage-free-download-f89b591b51cb42c98f84606999e4ec89


.. Important:: In Eevee the shadow catcher need a light source to work because the background in Eevee does not produce shadows
               unlike Cycles.

The shadow catcher in HDRi Maker works also in Eevee as well as in Cycles.
This tool is used to create shadows and reflections of objects in the scene on an Invisible plane.
This technique is very suitable when you want an image with a transparent background, in order to apply another background
in post-production, keeping the original shadows and reflections.

.. Note:: The shadow catcher components automatically adapt by switching between Cycles and Eevee.

.. |sc_i| image:: _static/_images/shadow_catcher/shadow_catcher_panel_inactive_01.png
              :width: 400
              :alt: Shadow Catcher Panel Inactive

.. |sc_a| image:: _static/_images/shadow_catcher/shadow_catcher_panel_active_01.png
                :width: 400
                :alt: Shadow Catcher Panel Active

+------------------------------------+------------------------------------+
|  **Panel Without Shadow Catcher**  |  **Panel With Shadow Catcher**     |
+------------------------------------+------------------------------------+
| |sc_i|                             | |sc_a|                             |
+------------------------------------+------------------------------------+



Add Shadow Catcher
------------------

- Pressing the "Add Shadow Catcher" button, a plane is added at the 3D cursor in the scene.
  When it is present in the scene, the "Shadow Catcher" panel will be activated.

.. image:: _static/_images/shadow_catcher/shadow_catcher_plane_eevee_01.png
              :width: 800
              :alt: Shadow Catcher Panel Active



.. |sc_p_legenda| image:: _static/_images/shadow_catcher/shadow_catcher_panel_legenda_01.png
                      :width: 800
                      :alt: Shadow Catcher Panel Legenda


+--------------------------------------------+-------------------------------------------------------------------------+
|   **The shadow catcher panel activated**                                                                             |
+--------------------------------------------+-------------------------------------------------------------------------+
| 1. :ref:`remove_shadow_catcher`            | |sc_p_legenda|                                                          |
| 2. :ref:`shadow_catcher_node_group_inputs` |                                                                         |
| 3. :ref:`shadow_catcher_normals`           |                                                                         |
| 4. :ref:`shadow_catcher_options`           |                                                                         |
+--------------------------------------------+-------------------------------------------------------------------------+



.. _remove_shadow_catcher:

Remove Shadow Catcher
---------------------

- Pressing the "Remove Shadow Catcher" button, the plane is removed from the scene.
  If you have manually removed the shadow catcher
  from the scene, there will certainly be components of it in the scene (Like the reflection plane)
  To remove them, use this button that will remove all the components of the shadow catcher from the scene.

.. _shadow_catcher_node_group_inputs:

Shadow Catcher Node Group inputs
--------------------------------

.. Tip:: In Eevee Shadow Strength is very important and must be dosed well to get a shadow, this is never the same
         as it must be manually adjusted, depending on the illumination of the scene. In some cases the plane
         may result Completely black or completely without shadows, in this case it is necessary to adjust the
         value of Shadow Strength.

- The panel allows you to control the input values of the "Shadow Catcher" node group.

    1. **Shadow Color  (Rgba)**

     - Adjust color of the shadow

    **Eevee Only:**

    2. **Shadow Strength  (Value)**

     - Adjusts the amount of shadow to cast. Attention, the shadow will only be shown if a light is placed in the scene. World Background does not cast shadows (Affects Eevee only)

    3. **From Min  (Value)**

     - Adjust the minimum shadow range (Eevee only)

    4. **From Max  (Value)**

     - Adjust the maximum shadow range (Eevee only)

    **Cycles & Eevee:**

    5. **Reflection Strength  (Value)**

     - Adjust the strength of the reflection

    6. **Reflection Range  (Value)**

     - Adjusts the range of the (Circular) area of the reflection. The greater the value, the smaller the area

    7. **Reflection Smooth  (Value)**

     - Adjusts the hue from reflection to non-reflection, from the center to the outside. A larger value increases the hue more

    8. **Roughness  (Value)**

     - Strength of Roughness, has visible effect only if "Reflection Strength" is greater than 0


.. _shadow_catcher_normals:

Shadow Catcher Normals
----------------------

- With the selector you can apply some normals map, you can choose between 3 types of normals, or none.

  An example with the "water" normals:

  .. image:: _static/_images/shadow_catcher/shadow_catcher_water_plane_eevee_01.png
              :width: 600
              :alt: Shadow Catcher Normals Water


.. _shadow_catcher_options:

Shadow Catcher Options
----------------------

.. |sc_p_options| image:: _static/_images/shadow_catcher/shadow_catcher_options_01.png
                      :width: 800
                      :alt: Shadow Catcher Options

+------------------------------------+---------------------------------------------------------------------------------+
| 1. :ref:`film_transparent`         |                                                                                 |
| 2. :ref:`hide_sc_reflection_plane` |              |sc_p_options|                                                     |
| 3. :ref:`hide_cycles_plane`        |                                                                                 |
| 4. :ref:`shadow_details_sc`        |                                                                                 |
+------------------------------------+---------------------------------------------------------------------------------+


.. _film_transparent:

Film Transparent
****************

- As already explained Here :ref:`transparent_background`, this box, if active, render the background Transparent

.. _hide_sc_reflection_plane:

Hide SC Reflection Plane
************************

- If active, the reflection plane will not be visible in the viewport, the reflection plane is only used for Eevee engine,
  in Cycles the reflection is done by the "Shadow Catcher" node group directly on the object. (It is an Eevee limitation)

.. _hide_cycles_plane:

Hide Cycles Plane
*****************

- If active, the plane used for Cycles will not be visible in the viewport, the plane is only used for Cycles engine,
  in Eevee the reflection is done by the "Shadow Catcher" node group directly on the object. (It is an Eevee limitation)

  .. Note:: This is managed automatically by the addon, you do not need to activate it manually


.. _shadow_details_sc:

Shadow Details (SC)
*******************

- **Shadow detail** (Only in Eevee) allows you to change between 6 options:


  - **Very Low**: Shadows are very undefined, consumes very little resources (Useful during the editing phase)

  - **Low**: Shadows are undefined, consumes few resources

  - **Default**: Shadows are as in Blender by default

  - **High**: Shadows are defined, consumes many resources

  - **Very High**: Shadows are very defined, consumes many resources

  - **Ultra**: Shadows are very defined, consumes many resources (This setting is very heavy, it takes full advantage of Eevee's capabilities, but it is very heavy, not recommended for computers not very powerful)










