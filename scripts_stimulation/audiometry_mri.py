#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.6),
    on Wed Feb 14 11:58:11 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
reload(sys)  
sys.setdefaultencoding('utf8')
import csv
import pandas as pd
from collections import OrderedDict
from datetime import date


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'aint_no_sound_loud_enough'  # from the Builder filename that created this script
expInfo = {u'participant': u'', 'setting':['T1','sparse','functional', 'baseline']}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
setting = expInfo['setting']
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
print (setting)


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s7' % (expInfo['participant'], expInfo['setting'], expName, expInfo['date'])


import csv

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Applications/PsychoPy2.app/Contents/Resources/untitled.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0, #changed size from 1440 900 to 1920, 1080
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, units = 'norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


# Initialize components for Routine "trial"
trialClock = core.Clock()
Hz1000 = sound.Sound('1000.wav')
Hz1000.setVolume(0.0)
Hz1500 = sound.Sound('1500.wav')
Hz1500.setVolume(0.0)
Hz2000 = sound.Sound('2000.wav')
Hz2000.setVolume(0.0)
Hz2250 = sound.Sound('2250.wav')
Hz2250.setVolume(0.0)
Hz2500 = sound.Sound('2500.wav')
Hz2500.setVolume(0.0)
Hz2750 = sound.Sound('2750.wav')
Hz2750.setVolume(0.0)
Hz3000 = sound.Sound('3000.wav')
Hz3000.setVolume(0.0)
Hz4000 = sound.Sound('4000.wav')
Hz4000.setVolume(0.0)
Hz6000 = sound.Sound('6000.wav')
Hz6000.setVolume(0.0)
Hz8000 = sound.Sound('8000.wav')
Hz8000.setVolume(0.0)
Hz1000 = sound.Sound('1000.wav')
Hz1000.setVolume(0.0)
Hz500 = sound.Sound('500.wav')
Hz500.setVolume(0.0)
Hz250 = sound.Sound('250.wav')
Hz250.setVolume(0.0)
Hz150 = sound.Sound('150.wav')
Hz150.setVolume(0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(32.000000)
# update component parameters for each repeat
# keep track of which components have finished
frequency_list = [Hz1000, Hz1500, Hz2000, Hz2250, Hz2500, Hz2750, Hz3000, Hz4000, Hz6000, Hz8000, Hz1000, Hz500, Hz250, Hz150]
for thisComponent in frequency_list:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
        
from psychopy import visual, core

# -------Start Routine "trial"-------
result_list_increase1 = [0] * 14
result_list_increase2 = [0] * 14

if setting == 'baseline':
    message = visual.TextStim(win, text='Druecke, wenn du einen Ton hoerst.')
    message.setAutoDraw(True)  # automatically draw every frame
    win.flip()
    core.wait(4.0)
    message.setText('Jetzt geht es los!')  # change properties of existing stim
    win.flip()
    core.wait(3.0)
    message.setText('+') 
    win.flip()
    for i in range(0,13):
        frequency = frequency_list[i]
        if frequency.status == NOT_STARTED: # keep track of start time/frame for later
            total_vol_inc = 0.0
            frequency.tStart = t
            frequency.frameNStart = frameN  # exact frame index
            frequency.play()  # start the sound (it finishes automatically)
            counter = 0
            key_pressed = False
            while (counter <= 12 and not key_pressed ): 
                frequency.stop()
                vol_inc = frequency.getVolume()
                if counter > 0:
                    total_vol_inc = vol_inc + 0.05
                frequency.setVolume(total_vol_inc)
                frequency.play()
                core.wait(2)
                t = core.CountdownTimer(2)
                key_escape = event.getKeys('q')
                if 'q' in key_escape:
                    win.close()
                    core.quit()
                while t > 0:
                    this_key = event.getKeys('7')
                    if '7' in this_key:
                        global key_pressed
                        key_pressed = True
                    else:
                        break
                counter += 1
             
            frequency.stop()
            result_list_increase1[i] = total_vol_inc            
    continue_pressed = False
    core.wait(5)
    win.flip()
    message.setText('Druecke, wenn du einen Ton hoerst.')
    win.flip()
    core.wait(2.0)
    message.setText('Jetzt geht es los!')  # change properties of existing stim
    win.flip()
    core.wait(2.0)
    message.setText('+') 
    win.flip()       
    for i in reversed(range(0,13)):
        frequency = frequency_list[i]
        frequency.tStart = t
        frequency.frameNStart = frameN  # exact frame index
        frequency.play()  # start the sound (it finishes automatically)
        counter = 0
        key_pressed = False
        frequency.setVolume(0.0)
        total_vol_dec = 0.0
        while (counter <= 12 and not key_pressed ): 
            frequency.stop()
            vol_dec = frequency.getVolume()
            if counter > 0:
                total_vol_dec = vol_dec + 0.05
            frequency.setVolume(total_vol_dec)
            frequency.play()
            core.wait(2)
            t = core.CountdownTimer(2)
            key_escape = event.getKeys('q')
            if 'q' in key_escape:
                win.close()
                core.quit()
            while t > 0:
                this_key = event.getKeys('7')
                print(this_key)
                if '7' in this_key:
                    key_pressed = True
                else:
                    break
            counter += 1
        frequency.stop()
        result_list_increase2[i] = total_vol_dec

if setting == "T1" or setting == "sparse":
    
    message = visual.TextStim(win, text='Druecke, wenn du einen Ton hoerst.')
    message.setAutoDraw(True)  # automatically draw every frame
    win.flip()
    core.wait(4.0)
    message.setText('Jetzt geht es los!')  # change properties of existing stim
    win.flip()
    core.wait(3.0)
    message.setText('+') 
    win.flip()
    for i in range(0,13):
        frequency = frequency_list[i]
        if frequency.status == NOT_STARTED: # keep track of start time/frame for later
            total_vol_inc = 0.0
            frequency.tStart = t
            frequency.frameNStart = frameN  # exact frame index
            frequency.play()  # start the sound (it finishes automatically)
            counter = 0
            key_pressed = False
            while (counter <= 12 and not key_pressed ): 
                frequency.stop()
                vol_inc = frequency.getVolume()
                if counter > 0:
                    total_vol_inc = vol_inc + 0.05
                frequency.setVolume(total_vol_inc)
                frequency.play()
                core.wait(2)
                t = core.CountdownTimer(2)
                key_escape = event.getKeys('q')
                if 'q' in key_escape:
                    win.close()
                    core.quit()
                while t > 0:
                    this_key = event.getKeys('7')
                    if '7' in this_key:
                        global key_pressed
                        key_pressed = True
                    else:
                        break
                counter += 1
             
            frequency.stop()
            result_list_increase1[i] = total_vol_inc            
    continue_pressed = False
    core.wait(5)
    win.flip()
    message.setText('Druecke, wenn du einen Ton hoerst.')
    win.flip()
    core.wait(2.0)
    message.setText('Jetzt geht es los!')  # change properties of existing stim
    win.flip()
    core.wait(2.0)
    message.setText('+') 
    win.flip()       
    for i in reversed(range(0,13)):
        frequency = frequency_list[i]
        frequency.tStart = t
        frequency.frameNStart = frameN  # exact frame index
        frequency.play()  # start the sound (it finishes automatically)
        counter = 0
        key_pressed = False
        frequency.setVolume(0.0)
        total_vol_dec = 0.0
        while (counter <= 12 and not key_pressed ): 
            frequency.stop()
            vol_dec = frequency.getVolume()
            if counter > 0:
                total_vol_dec = vol_dec + 0.05
            frequency.setVolume(total_vol_dec)
            frequency.play()
            core.wait(2)
            t = core.CountdownTimer(2)
            key_escape = event.getKeys('q')
            if 'q' in key_escape:
                win.close()
                core.quit()
            while t > 0:
                this_key = event.getKeys('7')
                print(this_key)
                if '7' in this_key:
                    key_pressed = True
                else:
                    break
            counter += 1
        frequency.stop()
        result_list_increase2[i] = total_vol_dec
            
if setting == "functional": 
    message = visual.TextStim(win, text='Druecke, wenn du einen Ton hoerst.')
    message.setAutoDraw(True)  # automatically draw every frame
    win.flip()
    core.wait(2.0)
    message.setText('Jetzt geht es los!')  # change properties of existing stim
    win.flip()
    core.wait(2.0)
    message.setText('+') 
    win.flip()
    for i in range(0,13):
        frequency = frequency_list[i]
        if frequency.status == NOT_STARTED: # keep track of start time/frame for later
            total_vol_inc = 0.0
            frequency.tStart = t
            frequency.frameNStart = frameN  # exact frame index
            frequency.play()  # start the sound (it finishes automatically)
            counter = 0
            key_pressed = False
            while (counter <= 12 and not key_pressed ): 
                frequency.stop()
                vol_inc = frequency.getVolume()
                if counter > 0:
                    total_vol_inc = vol_inc + 0.05
                frequency.setVolume(total_vol_inc)
                frequency.play()
                core.wait(2)
                t = core.CountdownTimer(2)
                key_escape = event.getKeys('q')
                if 'q' in key_escape:
                    win.close()
                    core.quit()
                while t > 0:
                    this_key = event.getKeys('7')
                    if '7' in this_key:
                        global key_pressed
                        key_pressed = True
                    else:
                        break
                counter += 1
             
            frequency.stop()
            result_list_increase1[i] = total_vol_inc        
    continue_pressed = False
    core.wait(5)
    win.flip()
    message.setText('Druecke, wenn du einen Ton hoerst.')
    win.flip()
    core.wait(2.0)
    message.setText('Jetzt geht es los!')  # change properties of existing stim
    win.flip()
    core.wait(2.0)
    message.setText('+') 
    win.flip()       
    for i in reversed(range(0,13)):
        frequency = frequency_list[i]
        #insert here: write down current frequency in file
        frequency.tStart = t
        frequency.frameNStart = frameN  # exact frame index
        frequency.play()  # start the sound (it finishes automatically)
        counter = 0
        key_pressed = False
        frequency.setVolume(0.0)
        total_vol_dec = 0.0
        while (counter <= 12 and not key_pressed ): 
            frequency.stop()
            vol_dec = frequency.getVolume()
            if counter > 0:
                total_vol_dec = vol_dec + 0.05
            frequency.setVolume(total_vol_dec)
            frequency.play()
            core.wait(2)
            t = core.CountdownTimer(2)
            key_escape = event.getKeys('q')
            if 'q' in key_escape:
                win.close()
                core.quit()
            while t > 0:
                this_key = event.getKeys('7')
                print(this_key)
                if '7' in this_key:
                    global key_pressed
                    key_pressed = True
                else:
                    break
            counter += 1
             
    frequency.stop()
    result_list_increase2[i] = total_vol_dec
    frequency.stop()
    frequency.status == NOT_STARTED
    # check if all components have finished
       
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in frequency_list:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
     
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        
# -------Ending Routine "trial"-------
for thisComponent in frequency_list:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
Hz1000.stop()
Hz1500.stop()
Hz2000.stop()  # ensure sound has stopped at end of routine
Hz2250.stop()  # ensure sound has stopped at end of routine
Hz2500.stop()  # ensure sound has stopped at end of routine
Hz2750.stop()  # ensure sound has stopped at end of routine
Hz3000.stop()  # ensure sound has stopped at end of routine
Hz4000.stop()
Hz6000.stop()
Hz8000.stop()
Hz1000.stop()
Hz500.stop()
Hz250.stop()
Hz150.stop()

#write lists to file
frequencypandas = [1000,1500,2000,2250,2500,2750,3000,4000,6000,8000,1000,500,250,150]
frequencypandas2 = [150,250,500,1000,8000,6000,4000,3000,2750,2500,2250,2000,1500,1000]
#to-do: in output-file seperate columns manually (excel) 
data = pd.DataFrame({'(1)frequency': frequencypandas,'(2)increase1': result_list_increase1, '(3)frequency-reversed': frequencypandas2, '(4)increase2': result_list_increase2})
print (data)
data.to_csv(filename +'.csv', sep='\t', encoding= 'utf-8', index = False)
x = trialClock.getTime()
print (x)

#end text
message.setText('Dieser Durchgang ist vorbei.')
win.flip()
core.wait(4.0)
message.setText('Jetzt kommt eine kurze Pause!')  # change properties of existing stim
win.flip()
core.wait(4.0)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
