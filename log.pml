cmd.hide("(solvent and (prApe1))")
cmd.hide("(solvent and (prApe1))")
cmd.hide("(prApe1 and hydro)")
cmd.show("ribbon"    ,"prApe1")
cmd.hide("everything","all")
cmd.show("cartoon"   ,"prApe1")
cmd.show("surface"   ,"prApe1")
color("yellow", "resi 1-45")

/cmd.set('depth_cue',1,'',0)
/cmd.set('ray_trace_frames',1,'',0)
/cmd.set('ray_trace_frames',0,'',0)
util.performance(0)
rebuild
/cmd.set('surface_cavity_mode',1,'',0)
cmd.show("surface"   ,"prApe1")
/cmd.set('surface_cavity_mode',0,'',0)
ray 800 600
ray 800,600
