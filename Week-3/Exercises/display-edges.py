

from expyriment import design, control, stimuli, misc
# control.set_develop_mode(on=True)

exp = design.Experiment(name="display-edges")
control.initialize(exp)


def squares_contours(length,colour,position):
    a = misc.geometry.vertices_frame((length,length),1)
    poly = stimuli.Shape(vertex_list=a,colour=misc.Colour(f"{colour}"),position=position)
    return poly

def at_edges(n,colour):
    squares = {}
    positions = []
    w_screen,l_screen = exp.screen.size
    square_length = w_screen *0.05
    w = w_screen- square_length
    l = l_screen - square_length
    positions.extend([(-w//2,-l//2),(-w//2,l//2),(w//2,-l//2),(w//2,l//2)])
    
    for i in range(1,n+1):
        squares.setdefault(i)
    for x,p in list(enumerate(positions, start=1)):
        squares[x] = squares_contours(square_length,colour,p)
    return squares

control.start()

n = 4
sq = at_edges(n,"red")

exp.clock.wait(1000)

for i in range(1,n):
    sq[i].present(clear=False,update=False)
sq[n].present(clear=False, update=True)
    

exp.keyboard.wait()
control.end()