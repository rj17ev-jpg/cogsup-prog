#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 15:35:20 2025

@author: riyajain
"""
from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")
control.initialize(exp)

fixation = stimuli.FixCross()

square = stimuli.Rectangle((50,50),colour=(65,105,225)) # create tstimulus
# preload stimulus into memory
square.preload()

control.start()

#  present on screen
square.present(clear=True,update=False)
fixation.present(clear=False,update=True)
exp.clock.wait(500)
square.present(clear=True,update=True)
exp.clock.wait()


control.end()