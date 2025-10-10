#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 11:24:04 2025

@author: riyajain
"""

from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_RED, C_GREEN, C_BLUE, C_EXPYRIMENT_ORANGE
from expyriment.misc.constants import K_LEFT, K_RIGHT, K_SPACE

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)
exp.data_variable_names = ['trial block','trial number','trial type','word meaning','text color','RTs','accuracy']

color_names = ['RED','GREEN','BLUE','ORANGE']
colors = [C_RED, C_GREEN, C_BLUE, C_EXPYRIMENT_ORANGE]
d = dict(zip(color_names,colors))
TRIALS = 10
BLOCKS = 2
TYPE = {'MISMATCH':K_LEFT,'MATCH':K_RIGHT}
feedback_text = ['Correct!','Incorrect']

blocks = [design.Block() for i in range(BLOCKS)]
for b in blocks:
    for i in range(TRIALS):
        t = design.Trial()
        b.add_trial(t)
    exp.add_block(b)

"""STIMULI"""
def fixation():
    fixation = stimuli.FixCross(size=(10,10))
    fixation.preload()
    return fixation

def stimulus(t_type):
    name = design.randomize.rand_element((color_names))
    if t_type == 'MATCH':
        color = d.get(name)
    else:
        color = design.randomize.rand_element([c for c in colors if c !=d[name]])
    # name = design.randomize.rand_element(color_names)
    s = stimuli.TextScreen('', name,text_colour=color,position=(0,-60),text_size=60)
    return s

instructions = stimuli.TextScreen('Instructions','If the color matches the word, press the RIGHT arrow key.\n If the color does not match the word, press the LEFT arrow key.\n Press SPACE to move on to the next trial.\n \nAt the end of the blocks press any key to end the experiment.')

""" Experiment """
def feedback(key, t_type):
    if key == TYPE[t_type]:
        f = stimuli.TextScreen('',feedback_text[0])
        accuracy = 1
    else:
        f = stimuli.TextScreen('',feedback_text[1])
        accuracy = 0
    return f,accuracy


def run_trial():
    t_type = design.randomize.rand_element(TYPE)

    fixation().present()
    exp.clock.wait(500)

    s = stimulus(t_type)
    s.present()
    key, rt = exp.keyboard.wait(keys=[K_LEFT, K_RIGHT])

    screen, accuracy = feedback(key,t_type)
    screen.present()
    exp.clock.wait(1000)

    exp.data.add([t_type,s.text,s.text_colour,rt,accuracy])


"""START"""
control.start(subject_id=1)

for b,block in enumerate(exp.blocks):
    instructions.present()
    exp.keyboard.wait()
    for t,trial in enumerate(block.trials):
        exp.data.add([b,t])
        run_trial()


exp.keyboard.wait()

control.end()