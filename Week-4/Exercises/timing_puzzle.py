from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")
stims = [fixation]

def draw(stims):
# Clear first, update last
    for i, stim in enumerate(stims):
        stim.present(clear=(i == 0), update=(i == len(stims) - 1))

t0 = exp.clock.time
fixation.present()
dt = exp.clock.time - t0
exp.clock.wait(1000 - dt)

t2 = exp.clock.time
text.present()
t1 = exp.clock.time

dt = exp.clock.time - t2
exp.clock.wait(1000 - dt)
fix_duration = (t2-t0)/1000

units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()