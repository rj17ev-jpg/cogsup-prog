# labeled_shapes_function

from expyriment import design, control, stimuli, misc
control.set_develop_mode(on=True)

exp = design.Experiment(name="labeled shapes function")
control.initialize(exp)

def polygon(n,length,colour,position):
    a = misc.geometry.vertices_regular_polygon(n, length)
    poly = stimuli.Shape(vertex_list=a,colour=misc.Colour(f"{colour}"),position=position)
    return poly


triangle = polygon(3,50,"purple",(-100,0))
hexagon = polygon(6,25,"yellow",(100,0))


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