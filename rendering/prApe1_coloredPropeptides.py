import __main__

from pkg_resources import load_entry_point


__main__.pymol_argv = [ "pymol"]#, "-qc" ] # Quiet and no GUI "-qc"

import sys, time, os
import pymol
import pymol.cmd as cmd

#from pathlib import Path

#stdout = sys.stdout
#stderr = sys.stderr
pymol.finish_launching()
#sys.stdout = stdout
#sys.stderr = stderr

##
# Read User Input
#spath = os.path.abspath(sys.argv[1])
#sname = spath.split("/")[-1].split(".")[0]

#ENABLE_RAYTRACING = False

img = [1920,1080]
cmd.util.performance(100)
cmd.rebuild()
cmd.viewport(img[0],img[1])


# Load Structures
def loadStructure(spath, sname, assembly = True):
    if assembly:
        cmd.set("assembly", "1")
    cmd.load(spath, sname)
    cmd.disable("all")
    cmd.enable(sname)    
    #Path("./Output").mkdir(parents=True, exist_ok=True)
    return "./Output/" + sname + ".png"

def outputPicture(fileName):   
    cmd.set('ray_opaque_background', 0)
     
    print("Starting Ray tracing")
    #cmd.ray(img[0],img[1])
     
    print("Exporting to {}".format(fileName))
    cmd.png(fileName, width =img[0],height= img[1],dpi = 300, ray = 1)

def create_prApe1():
    spath = "../PDB/prApe1/5jh9.cif"
    sname = "test_prApe1"
    fileName = loadStructure(spath, sname)    
    cmd.hide("everything")
    cmd.color("gray20", sname)
    cmd.color("yellow", "resi 1-45")
    cmd.show("cartoon", sname)        
    cmd.set("surface_type","2")
    cmd.set("transparency",0.6)    
    cmd.set("surface_color",4236)
    cmd.show("surface", sname)
    outputPicture(fileName)

def create_single_prApe1():
    spath = "../PDB/prApe1/5jh9.cif"
    sname = "single_prApe1"
    fileName = loadStructure(spath, sname,assembly=False)    
    cmd.hide("everything")
    cmd.color("gray40", sname)
    cmd.color("yellow", "resi 1-45")
    cmd.show("cartoon", sname)        
    cmd.set("surface_type","2")
    cmd.set("transparency",0.4)
    cmd.show("surface", sname)
    outputPicture(fileName)

def create_mApe1():
    spath = "../PDB/mApe1/5jgf.cif"
    sname = "mApe1"    
    fileName = loadStructure(spath, sname)
    cmd.hide("everything")
    cmd.color("grey60", sname)
    cmd.show("cartoon", sname)        
    cmd.set("surface_type","2")
    cmd.set("transparency",0.50000)
    cmd.set("surface_color", "gray80")
    cmd.show("surface", sname)
    outputPicture(fileName)

def create_Ams1():
    spath = "../PDB/Ams1/5jm0.cif"
    sname = "Ams1"    
    fileName = loadStructure(spath, sname)
    cmd.hide("everything")
    cmd.color("forest", sname)
    cmd.show("cartoon", sname)        
    cmd.set("surface_type","2")
    cmd.set("transparency",0.800)
    cmd.set("surface_color", "tv_orange")
    cmd.show("surface", sname)
    outputPicture(fileName)

def create_Atg8():
    spath = "../PDB/Atg8/6wy6.cif"
    sname = "Atg8"    
    fileName = loadStructure(spath, sname)
    cmd.hide("everything")
    cmd.color("lime", sname)
    cmd.show("cartoon", sname)        
    cmd.set("surface_type","2")
    cmd.set("transparency",0.800)
    cmd.set("surface_color", "lime")
    cmd.show("surface", sname)
    outputPicture(fileName)

def create_Atg11():
    spath = "../PDB/Atg11/AF-Q12527-F1-model_v2.pdb"
    sname = "Atg11"    
    fileName = loadStructure(spath, sname, assembly=False)
    cmd.hide("everything")
    cmd.color("marine", sname)
    cmd.show("cartoon", sname)        
    cmd.set("surface_type","2")
    cmd.set("transparency",0.800)
    cmd.set("surface_color", "marine")
    cmd.show("surface", sname)
    outputPicture(fileName)

def create_Atg19():
    spath = "../PDB/Atg19/AF-P35193-F1-model_v2.pdb"
    sname = "Atg19"    
    fileName = loadStructure(spath, sname, assembly=False)
    cmd.hide("everything")
    cmd.color("aquamarine", sname)
    cmd.show("cartoon", sname)        
    cmd.set("surface_type","2")
    cmd.set("transparency",0.800)
    cmd.set("surface_color", "aquamarine")
    cmd.show("surface", sname)
    outputPicture(fileName)





#create_single_prApe1()
#cmd.reinitialize()
#create_Ams1()
#cmd.reinitialize()
#create_mApe1()
#cmd.reinitialize()
create_prApe1()

# create_Atg8()
# cmd.reinitialize()
# create_Atg11()
# cmd.reinitialize()
# create_Atg19()



# Get out!
cmd.quit()


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