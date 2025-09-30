#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 21:31:27 2025

@author: riyajain
"""

# HERMAN GRID

from expyriment import design, control, stimuli, misc

sq_size = 50
sq_colour = misc.constants.C_BLACK
space = 10
rows, cols = 5,5

x_edge = 0 - (cols//2)*sq_size
y_edge = 0 - (rows//2)*sq_size

exp = design.Experiment(name="Kanisza Square Experiment")

control.initialize(exp)
control.set_develop_mode(on=True)
control.defaults.window_mode = True

# specify background color
exp.screen.colour = misc.constants.C_WHITE

control.start(exp,skip_ready_screen=True)

for row in range(rows):
    for col in range(cols):
        x = x_edge + col * (sq_size + space)
        y = y_edge + row * (sq_size + space)
        s = stimuli.Rectangle((sq_size,sq_size),colour=sq_colour,position=(x,y))
        s.preload()
        s.present(clear=False,update=False)

exp.screen.update()

exp.keyboard.wait()

control.end()

