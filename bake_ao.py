import bpy
 
import math

import os
#clear the message in the system console
os.system("cls")
scene = bpy.context.scene
scene.tool_settings.use_uv_select_sync = True
 

print(list(bpy.context.scene.objects))

 
def disp_all_meshes(all_meshes):
    all_meshes_list=list(bpy.data.meshes)
    print(all_meshes_list)
    num_meshes=len(all_meshes_list)

    #print(num_meshes)
    return all_meshes_list;

#get all the objs
all_meshes_list=list(bpy.data.meshes)
print(all_meshes_list)
num_meshes=len(all_meshes_list)

print(num_meshes)

all_meshes=bpy.data.meshes;
print("before remove")
disp_all_meshes(all_meshes)

# remove mesh Cube
if "Cube" in bpy.data.meshes:
    mesh = bpy.data.meshes["Cube"]
    print("removing mesh", mesh)
    bpy.data.meshes.remove(mesh)
    
print("after remove")
mesh_list=disp_all_meshes(all_meshes)
print("*****************************************")
print("check the uv coordinates of each mesh...")
for i in range(len(mesh_list)):
    mesh=mesh_list[i];
     #mesh.set_select(state = True);
    print("current mesh:",mesh.name)
    current_obj=bpy.data.objects[mesh.name]
        
    bpy.context.view_layer.objects.active =current_obj
    
    print(bpy.data.objects[mesh.name])
 

    all_uv_maps=list(mesh.uv_layers);
    all_uv_maps_num=len(all_uv_maps);
    if(all_uv_maps_num>0):
        print("UVMaps Number:",all_uv_maps_num)
    else:
        print("Creating UVMap...")
        bpy.ops.mesh.uv_texture_add()
        bpy.ops.uv.smart_project()
    #check whether this obj has UV Maps
    print()
        
 
#check whether each obj has uv coordinates

#bake ao for each obj

#export a new model