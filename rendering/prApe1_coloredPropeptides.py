import __main__
__main__.pymol_argv = [ "pymol" ] # Quiet and no GUI "-qc"

import sys, time, os
import pymol
import pymol.cmd as cmd

pymol.finish_launching()

##
# Read User Input
#spath = os.path.abspath(sys.argv[1])
#sname = spath.split("/")[-1].split(".")[0]

ENABLE_RAYTRACING = False

spath = "../PDB/prApe1/5jh9.cif"
sname = "prApe1"

img = [1920,1080]

fileName = "./" + sname + ".png"

# Load Structures
cmd.set("assembly", "1")
cmd.load(spath, sname)
cmd.disable("all")
cmd.enable(sname)

pymol.util.performance(0)
cmd.hide("everything")
cmd.show("cartoon"   , sname)
#cmd.show("ribbon"    , sname)

cmd.color("gray50", sname)
#cmd.show("surface"   , sname)
#cmd.set("cartoon_smooth_loops",1,"",0)
#cmd.set("volume_layers",1000.0,"",0)
#cmd.set("volume_mode",1,"",0)
#cmd.set("hash_max",300,"",0)
cmd.set("surface_type",2,"",0)
cmd.set("transparency",0.8,"",0)
#cmd.set("surface_color",4236,"",0)


#cmd.hide("(solvent and (prApe1))")
#cmd.hide("(prApe1 and hydro)")


#cmd.extend("new_command",new_command)

#cmd.set("line_smooth", "on")
#cmd.set('depth_cue',1,'',0)

cmd.color("yellow", "resi 1-45")

# # render high resolution image
# # Set transparent background
cmd.set("ray_opaque_background", 0)

if ENABLE_RAYTRACING:
    # # 2: structure, 1: only outline, 3: both
    cmd.set("ray_trace_mode",  3)

    # # A setting that alters the outline thickness when using ray_trace_mode=1 
    # # (full color with black outline). 
    # set ray_trace_gain, 0.0
    cmd.set("ray_trace_gain",0.5)
    cmd.set("ray_trace_color", 0x000000)

    #print("starting ray tracing...")
    cmd.ray(img[0],img[1],antialias=2)


cmd.rebuild


# Exporting the final view
print("exporting file")
cmd.png(fileName,img[0],img[1])
# Get out!
#cmd.quit()