Troubleshooting
===============

In this section there are some tips to solve known problems.
This section will be updated over time based on the major problems encountered by users.
Problems related to HDRi Maker bugs are usually solved. Here are some of the most common problems.
Question and answer

------------------------------------------------------------------------------------------------------------------------

Find Options Menu
------------------

To go to the HDRi Maker options, you have to go to the addon preferences. But to make this process easier there is
a button directly in the HDRi Maker interface:

.. image:: _static/_images/troubleshooting/options_button_01.png
    :align: center
    :width: 200
    :alt: Options Button 01


------------------------------------------------------------------------------------------------------------------------


Pink Background
---------------

If you find yourself in a situation of background or Dome with Pink color, this means in 99% of cases that the image
to which the background refers is no longer linked to the project.

.. image:: _static/_images/troubleshooting/pink_background_01.png
    :align: center
    :width: 600
    :alt: Pink Background 01


To solve the problem, go to the HDRi Maker options and click on the "Find Lost Images" button

.. image:: _static/_images/troubleshooting/find_lost_images_01.png
    :align: center
    :width: 600
    :alt: Find Lost Images 01

A file search window will open. Indicate the path where the HDRi Maker library is located or where you think
that the file you are looking for may be. Once the path is indicated, click on "Find Missing Files".

The search will be performed in the indicated path and in all subfolders.

**Note**: The process may take a while, depending on the number of files in the library.


.. image:: _static/_images/troubleshooting/find_missing_files_01.png
    :align: center
    :width: 600
    :alt: Find Missing Files 01


------------------------------------------------------------------------------------------------------------------------


Black Background
----------------

In this case there may be a problem when creating a file in a newer version of Blender, and then after saving the project
it is opened in a previous version of Blender.

Sometimes Blender updates its nodes, so it may be that the nodes are no longer retro compatible with the previous version.
To solve this I have provided a function that tries to replace the "Unknown" nodes

You can find it in the HDRi Maker Options menu:

.. image:: _static/_images/troubleshooting/fix_unknown_nodes_01.png
    :align: center
    :width: 600
    :alt: Fix Unknown Nodes 01



------------------------------------------------------------------------------------------------------------------------

Projection distorted
--------------------

The projection of the dome is a great feature but not all images can be projected correctly.

First of all, keep in mind that the image is 2D and does not have the characteristics of the parallax, for example:
**Everything behind a tree in reality can be seen by turning around the tree, In an image No**

Keep this rule in mind.

The same thing applies to an object like a "Stick", the stick could result "Splamato" on the floor especially if the image
the stick is very close to the camera.

Another example is that the image is taken in a point of the grass. Obviously you will only see the grass from one direction, that is
from the center to the outside of the imaginary circle that forms the grass. But if you look at the image from another point.
If in the projections you try to frame the grass from the outside point to the center, you will see that the grass is "Splamato" on the floor.


These are the most typical limitations of the projection





