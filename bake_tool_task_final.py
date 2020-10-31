import bpy
 
import math

import os
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

os.mkdir("bake")
#for i in range(len(mesh_list)):
#    mesh=mesh_list[i];
#     #mesh.set_select(state = True);
#    print("current mesh:",mesh.name)
#    current_obj=bpy.data.objects[mesh.name]
#        
#    bpy.context.view_layer.objects.active =current_obj
#    bpy.ops.baketool.add_job()
#    print(bpy.data.objects[mesh.name])
# 

   
        
 
#check whether each obj has uv coordinates

#bake ao for each obj

#export a new model