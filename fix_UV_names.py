""" rename the first uv map of each object to "UVMap"

Useful because joining objects with differently named UV maps gets weird.
"""

import bpy

D = bpy.data
 
for ob in D.objects:
    try:
        ob.data.uv_layers[0].name = "UVMap"
    except:
        pass