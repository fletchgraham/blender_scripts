import bpy

C = bpy.context
D = bpy.data

# user select source then the target

target = C.active_object
source = [o for o in C.selected_objects if o is not target][0]

loc = target.location.copy()
rot = target.rotation_euler.copy()

source.select_set(False)
bpy.ops.object.delete()

source.select_set(True)
bpy.ops.object.duplicate_move_linked()

source.location = loc
source.rotation_euler = rot

source.select_set(False)