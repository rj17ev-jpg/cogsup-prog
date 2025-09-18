#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 15:56:24 2025

@author: riyajain
"""

from expyriment import design, control, stimuli

exp = design.Experiment(name="Two Squares")
control.initialize(exp)

square1 = stimuli.Rectangle((50,50),colour=(255,0,0),position=(-100,0)) # create tstimulus
square2 = stimuli.Rectangle((50,50),colour=(0,128,0),position=(100,0))
# preload stimulus into memory
square1.preload()
square2.preload()

control.start()

#  present on screen
square1.present(clear=True,update=False)
square2.present(clear=False,update=True)


exp.clock.wait(5000)

control.end()