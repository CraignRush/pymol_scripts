space rgb
/cmd.set('cartoon_smooth_loops',1,'',0)
/cmd.set('volume_layers',1000.0,'',0)
/cmd.set('volume_mode',1,'',0)
/cmd.set('hash_max',300,'',0)
cmd.disable('4r8f')
cmd.enable('4r8f',1)
cmd.show("surface"   ,"4r8f")
cmd.show_as("nonbonded" ,"4r8f")
cmd.hide("everything","4r8f")
cmd.show("surface"   ,"4r8f")
cmd.color_deep("gray50", '4r8f', 0)
cmd.color_deep("gray90", 'sele', 0)
zoom animate=-1
zoom animate=-1
/cmd.set('overlay',1,'',0)
/cmd.set('surface_color',4236,'',0)
color yellow, resi 1-45
cmd.show("ribbon"    ,"4r8f")
cmd.show("cartoon"   ,"4r8f")
cmd.hide("surface"   ,"4r8f")
cmd.select('sele','none')
cmd.select('sele',"byresi((((sele) or byresi((5jh9`12694))) and not ((byresi((5jh9`12694))) and byresi(sele))))",enable=1)
cmd.disable('5jh9')
cmd.enable('5jh9',1)
cmd.disable('5jh9')
cmd.enable('5jh9',1)
cmd.disable('5jh9')
cmd.delete("5jh9")
set assembly, "1"
fetch 5jh9, async=0
fetch 5jh9, type=2fofc, async=0
fetch 5jh9, type=fofc, async=0
cmd.disable('4r8f')
color yellow, resi 1-45
/cmd.set('surface_type',2,'',0)
cmd.show("surface"   ,"5jh9")
/cmd.set('transparency',0.4,'',0)
/cmd.set('transparency',0.6,'',0)
scene new, store
scene new, store, color=0, rep=0

set assembly, "1"
fetch 5jh9, async=0
fetch 5jh9, type=2fofc, async=0
cmd.select('sele','none')
cmd.select('sele',"byresi((((sele) or byresi((5jh9`6307))) and not ((byresi((5jh9`6307))) and byresi(sele))))",enable=1)
