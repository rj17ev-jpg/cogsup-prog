

from expyriment import design, control, stimuli
control.set_develop_mode(on=True)

exp = design.Experiment(name="launching")
control.initialize(exp)
control.start()

s_length = 50
s = stimuli.Rectangle((s_length,s_length),colour=(255,0,0),position=(-400,0))
s2 = stimuli.Rectangle((s_length,s_length),colour=(0,128,0),position=(0,0))

s.present(clear=False,update=True)
s2.present(clear=False,update=True)
exp.clock.wait(100)

# exp.clock.reset_stopwatch()
while s.position[0] - s2.position[0]  < -(s_length):
    s.move([5,0])
    s2.present(clear=True, update=False)  # Clear screen and draw static square
    s.present(clear=False, update=True)  # Draw moving square without clearing
    # s.present(clear=True,update=False)
    # exp.clock.wait(200)

while s2.position[0] < 400:
    s2.move([5,0])
    s.present(clear=True, update=False)  # Clear screen and draw static square
    s2.present(clear=False, update=True)  # Draw moving square without clearing

exp.clock.wait(1000)
control.end()
