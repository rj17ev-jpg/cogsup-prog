# kanisza squares draft

from expyriment import design, control, stimuli, misc
control.set_develop_mode(on=True)

exp = design.Experiment(name="kanisza-square",background_colour=misc.constants.C_GREY)
control.initialize(exp)


screen_width, _ = exp.screen.size
sq_length = screen_width * 0.25
circle_radius = screen_width * 0.05

c = sq_length//2


def square():
    a = misc.geometry.vertices_regular_polygon(4, sq_length)
    poly = stimuli.Shape(vertex_list=a,colour=misc.constants.C_GREY,position=(0,0))
    return poly

positions = [(-c,-c),(c,-c),(-c,c),(c,c)]

def circle():
    circles = []
    for p in range(2):
        circles.append(stimuli.Circle(circle_radius,colour=misc.constants.C_BLACK,position=positions[p]))
    for p in range(2,4):
        circles.append(stimuli.Circle(circle_radius,colour=misc.constants.C_WHITE,position=positions[p]))
    return circles


control.start()

for x in circle():
    x.present(clear=False,update=False)

square().present(clear=False, update=True)

exp.keyboard.wait()

control.end()