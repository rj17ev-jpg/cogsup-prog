
from expyriment import design, control, stimuli, misc
# control.set_develop_mode(on=True)

BACKGROUND_COLOR = misc.constants.C_GREY  # Gray background
exp = design.Experiment(name="Kanisza Square Experiment",background_colour=BACKGROUND_COLOR)

control.initialize(exp)
control.set_develop_mode(on=True)
# exp.screen.colour = misc.constants.C_GREY

def circle(circle_radius, positions):
    circles = []
    for p in range(2):
        circles.append(stimuli.Circle(circle_radius, colour=misc.constants.C_BLACK, position=positions[p]))
    for p in range(2, 4):
        circles.append(stimuli.Circle(circle_radius, colour=misc.constants.C_WHITE, position=positions[p]))
    return circles

def sizes(aspect_ratio,rectangle_sf=1,circle_sf=1):
    k = []
    screen_width, _ = exp.screen.size
    r_height = screen_width * 0.25
    r_width = r_height*aspect_ratio

    rect = stimuli.Rectangle((r_width,r_height),colour=misc.constants.C_GREY)
    rect.scale((rectangle_sf,rectangle_sf))
    k.append(rect)

    circle_radius = screen_width * 0.05
    c = r_height//2
    d = r_width//2

    positions = [(-d, -c),(-d, c), (d, c), (d, -c)]

    for d in circle(circle_radius,positions):
        d.scale((circle_sf,circle_sf))
        k.append(d)


    return k


control.start(exp)

k = sizes(2)

for x in k[1:]:
    x.present(clear=False,update=False)

k[0].present(clear=False,update=True)

exp.keyboard.wait()

control.end()

