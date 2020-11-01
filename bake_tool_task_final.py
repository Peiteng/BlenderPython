import bpy
 
import math

import os
import shutil
#clear the message in the system console
os.system("cls")
scene = bpy.context.scene
scene.tool_settings.use_uv_select_sync = True
 

print(list(bpy.context.scene.objects))

def checkBakeJobsNum():
    print("bake_jobs_num:",len(list(bpy.context.scene.BakeTool_Jobs.Jobs)))
def disp_all_meshes(all_meshes):
    all_meshes_list=list(bpy.data.meshes)
    print(all_meshes_list)
    num_meshes=len(all_meshes_list)

    #print(num_meshes)
    return all_meshes_list;
def clearAllJobs():
    all_jobs=bpy.context.scene.BakeTool_Jobs.Jobs;
    existing_jobs=list(all_jobs);
    if(len(existing_jobs)==0):
        print("No job avalibale")
    else:
        for job_i in range(len(existing_jobs)):
            #always remove the top one
            bpy.data.scenes["Scene"].BakeTool_Jobs.index=0
            bpy.ops.baketool.remove_job()
            print("remove one job")
            checkBakeJobsNum()
def removesuffix(my_str, suffix):
    # suffix='' should not call self[:-0].
    if suffix and my_str.endswith(suffix):
        return my_str[:-len(suffix)]
    else:
        return my_str[:]
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
print("clear all available jobs...")

clearAllJobs();

print("*****************************************")
print("add bake AO job...")
        
bpy.ops.baketool.add_job()

#rename the bake job
all_jobs=bpy.context.scene.BakeTool_Jobs.Jobs;
all_jobs[0].name="AO"
checkBakeJobsNum()
filepath = bpy.data.filepath
current_path = os.path.dirname(filepath)
current_file_name=os.path.basename(filepath)
current_file_name=removesuffix(current_file_name,".blend")
bake_data_save_path=current_path+"/bake_"+current_file_name;
if os.path.exists(bake_data_save_path):
    shutil.rmtree(bake_data_save_path)
os.mkdir(bake_data_save_path)

#
bake_tool_data=bpy.data.scenes["Scene"].BakeTool_Jobs;
bake_tool_data.Jobs[0].job_settings.path=bake_data_save_path;

print("*****************************************")
print("Add meshes...")
for i in range(len(mesh_list)):
    mesh=mesh_list[i];
   
    print("current mesh:",mesh.name)
    current_obj=bpy.data.objects[mesh.name]
    current_obj.select_set(True)
    bpy.ops.baketool.add_obj()
    print("Select object:",current_obj.name)
    #deselect the object, otherwise, it will be kept as selected status
    current_obj.select_set(False)
print("*****************************************")
print("Check UVMap...")
for i in range(len(mesh_list)):
    current_mesh=mesh_list[i];
   
    print("current mesh:",current_mesh.name)
    current_obj=bpy.data.objects[current_mesh.name]
    current_obj.select_set(True)
    #check if there is uv map for this object
    all_uv_maps=list(current_mesh.uv_layers);
    all_uv_maps_num=len(all_uv_maps);
    print("uv_map_num:",all_uv_maps_num)
    
    
    if(all_uv_maps_num==0):
        bpy.ops.mesh.uv_texture_add()
        #since there is only one uv map, so we can get the name
        current_uv_layers=current_mesh.uv_layers;
        print("currnet uv map name:",current_uv_layers[0].name)
        #set the name of the uv map
        #bpy.context.object.data.uv_layers["test_uv"].name = "ao_uv"

    current_obj.select_set(False)
    #
    
print("*****************************************")
print("Set UV Map ...")


   
bpy.context.scene.BakeTool_Jobs.Jobs[0].job_objs.coll 
        
 
#check whether each obj has uv coordinates

#bake ao for each obj

#export a new model