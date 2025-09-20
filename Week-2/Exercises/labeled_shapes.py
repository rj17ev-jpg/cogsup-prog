# labeled_shapes

from expyriment import design, control, stimuli, misc
control.set_develop_mode(on=True)

exp = design.Experiment(name="labeled shapes")
control.initialize(exp)

tr = misc.geometry.vertices_triangle(60,50,50)
triangle = stimuli.Shape(vertex_list=tr,colour=misc.Colour("purple"),position=(-100,0))
hex = misc.geometry.vertices_regular_polygon(6, 25)
hexagon = stimuli.Shape(vertex_list=hex,colour=misc.Colour("yellow"),position=(100,0))

line1 = stimuli.Line([-100,50],[-100,100],3,colour=misc.Colour("white"))
line2 = stimuli.Line([100,50],[100,100],3,colour=misc.Colour("white"))

tl1 = stimuli.TextLine("triangle",[-100,120],text_colour=misc.Colour("white"))
tl2 = stimuli.TextLine("hexagon",[100,120],text_colour=misc.Colour("white"))
                       
# preload stimulus into memory
triangle.preload()
hexagon.preload()

control.start()

#  present on screen
triangle.present(clear=True,update=False)
hexagon.present(clear=False,update=False)
line1.present(clear=False, update=False)
line2.present(clear=False, update=False)
tl1.present(clear=False, update=False)
tl2.present(clear=False, update=True)

exp.keyboard.wait()


control.end()