import bpy

ops = bpy.ops
scene = bpy.context.scene
mesh = bpy.ops.mesh

# Delete default scene objects
ops.object.select_all()
ops.object.select_all()
ops.object.delete()

# Import the model from our Three scene
ops.import_scene.obj(filepath="input.obj")

current_mesh = scene.objects[0]

# Set it to active and go into edit mode
scene.objects.active = current_mesh
ops.object.mode_set(mode='EDIT')

# Mesh cleanup step, since what's coming out of Three is mostly cubes laying side by side.

# Remove double verts...
mesh.select_mode(type="VERT")
mesh.remove_doubles()

# Merge tris into quads...
mesh.select_mode(type="FACE")
mesh.dissolve_limited()

# Remove interior faces
mesh.select_all()
mesh.select_interior_faces()
mesh.delete(type="FACE")

# Create a second UV layer for the ambient occlusion map
bpy.ops.mesh.uv_texture_add()
current_mesh.data.uv_layers[1].name = 'Shadows'

# Unwrap the mesh
mesh.select_all()
ops.uv.lightmap_pack(PREF_IMG_PX_SIZE=512)

# Create a new image to bake the lighting in to
bpy.ops.image.new(name="AO Map")
image = bpy.data.images['AO Map']

# Set the image to active (applies it to the object)
bpy.data.screens['UV Editing'].areas[1].spaces[0].image = image

# Bake the lightmap
bpy.data.scenes["Scene"].render.bake_margin = 4
bpy.data.worlds["World"].light_settings.use_ambient_occlusion = True
bpy.data.worlds["World"].light_settings.samples = 10
bpy.ops.object.bake_image()

# Save the baked image
image.filepath_raw = "output.png"
image.file_format = "PNG"
image.save()

# Save the new model with the new UV channel
ops.object.mode_set(mode='OBJECT')
bpy.ops.export.three(filepath="output.json")