Python
======================


Add the background with python
----------------------------------

Example python code:


.. code-block:: python

    import bpy
    import os


    default_lib_path = "\\HDRI_MAKER_DEFAULT_LIB" # Path to your folder, you need to get your full path, this is only an example path

    for root, dirs, files in os.walk(default_lib_path):
        for fn in files:
            if fn.endswith(".hdr") or fn.endswith(".exr"):
                fp = os.path.join(root, fn)
                bpy.ops.hdrimaker.addbackground(filepath=fp, invoke_browser=True)



In this case all hdr and exr backgrounds present in the specified folder will be added.
Make sure to enter the code: ``invoke_browser=True`` otherwise it will not work.




