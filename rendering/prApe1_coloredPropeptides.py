import __main__

from pkg_resources import load_entry_point


__main__.pymol_argv = [ "pymol" ] # Quiet and no GUI "-qc"

import sys, time, os
import pymol
import pymol.cmd as cmd

from pathlib import Path

stdout = sys.stdout
stderr = sys.stderr
pymol.finish_launching()
sys.stdout = stdout
sys.stderr = stderr

##
# Read User Input
#spath = os.path.abspath(sys.argv[1])
#sname = spath.split("/")[-1].split(".")[0]

#ENABLE_RAYTRACING = False

img = [1920,1080]



# Load Structures
def loadStructure(spath, sname, assembly = True):
    if assembly:
        cmd.set("assembly", "1")
    cmd.load(spath, sname)
    cmd.disable("all")
    cmd.enable(sname)    
    Path("./Output").mkdir(parents=True, exist_ok=True)
    return "./Output/" + sname + ".png"

def create_prApe1():
    spath = "../PDB/prApe1/5jh9.cif"
    sname = "prApe1"
    fileName = loadStructure(spath, sname)    
    cmd.hide("everything")
    cmd.color("gray40", sname)
    cmd.color("yellow", "resi 1-45")
    cmd.show("cartoon", sname)        
    cmd.set("surface_type",2,"",0)
    cmd.set("transparency",0.8,"",0)
    outputPicture(fileName)


def create_mApe1():
    spath = "../PDB/mApe1/5jgf-sf.cif"
    sname = "mApe1"    
    fileName = loadStructure(spath, sname)
    cmd.hide("everything")
    cmd.color("grey60", sname)
    cmd.show("cartoon", sname)        
    cmd.set("surface_type",2,sname,0)
    cmd.set("transparency",0.8,sname,0)
    cmd.set("surface_color", "gray80", sname, quiet=0)
    outputPicture(fileName)

def create_Ams1():
    spath = "../PDB/Ams1/5jm0.cif"
    sname = "Ams1"    
    fileName = loadStructure(spath, sname)
    cmd.hide("everything")
    cmd.color("forest", sname)
    cmd.show("cartoon", sname)        
    cmd.set("surface_type",2,sname,0)
    cmd.set("transparency",0.8,sname,0)
    cmd.set("surface_color", "gray80", sname, quiet=0)
    cmd.show("surface", sname)
    outputPicture(fileName)


def outputPicture(fileName):    
    print("exporting file")
    cmd.set('ray_opaque_background', 0)
    cmd.ray(img[0],img[1])
    cmd.png(fileName,img[0],img[1])

create_Ams1()
#cmd.reinitialize
#create_mApe1
#cmd.reinitialize
#create_prApe1

# Get out!
#cmd.quit()


#pymol.util.performance(0)
#cmd.color("yellow", "resi 1-45")
#cmd.show("surface"   , sname)
#cmd.set("cartoon_smooth_loops",1,"",0)
#cmd.set("volume_layers",1000.0,"",0)
#cmd.set("volume_mode",1,"",0)
#cmd.set("hash_max",300,"",0)
#cmd.set("surface_type",2,"",0)
#cmd.set("transparency",0.8,"",0)
#cmd.set("surface_color",4236,"",0)


#cmd.hide("(solvent and (prApe1))")
#cmd.hide("(prApe1 and hydro)")


#cmd.extend("new_command",new_command)

#cmd.set("line_smooth", "on")
#cmd.set('depth_cue',1,'',0)


# # render high resolution image

#if ENABLE_RAYTRACING:    
    # # Set transparent background
    #cmd.set("ray_opaque_background", 0)

    # # 2: structure, 1: only outline, 3: both
    #cmd.set("ray_trace_mode",  3)

    # # A setting that alters the outline thickness when using ray_trace_mode=1 
    # # (full color with black outline). 
    # set ray_trace_gain, 0.0
    #cmd.set("ray_trace_gain",0.5)
    #cmd.set("ray_trace_color", 0x000000)

    #print("starting ray tracing...")
    #cmd.ray(img[0],img[1],antialias=2)


#cmd.rebuild