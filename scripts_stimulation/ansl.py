"""ANSL: aint no sound loud enough.

Experiment for audiometry and control for audible frequency, given
different volume.

Jacky, Chrissi, Michael Ernst
"""
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division
import os  # handy system and path functions
import sys  # to get file system encoding
reload(sys)
sys.setdefaultencoding('utf8')
import time
from datetime import date
from numpy.random import random, randint, normal, shuffle
import csv
import pandas as pd
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy import (locale_setup, sound, gui, visual,
                      core, data, event, logging)

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(
            sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'aint_no_sound_loud_enough'
expInfo = {u'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)

if dlg.OK == False:
    core.quit()  # user pressed cancel

expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log
filename = _thisDir + os.sep + u'data/%s_%s_%s7' % (expInfo['participant'],
                                                    expName,
                                                    expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath='/Applications/PsychoPy2.app/Contents/Resources/untitled.psyexp',
                                 savePickle=True, saveWideText=False,
                                 dataFileName=filename)

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)


def run_func(filename, expInfo, thisExp, setting):
    """
    Funtion to display stimuli.

    Sets up lists with stimuli paths to iterate over.
    Contains four conditions, differing in stimuli order and direction of
    volume change. Input parameters are
    setting(the specific mri sequence to be tested),
    filename(path containing current working directory,
    designated participant number, the experiment name, and the date
    as a string),
    expInfo(same parameters as filename, further used to control
    for monitor Framerate, if need be),
    and thisExp (an ExperimentHandler to
    create logfiles)
    """
# Setup the Window
    win = visual.Window(
        size=(1440, 900), fullscr=True, screen=0,
        allowGUI=False, allowStencil=False,
        monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
        blendMode='avg', useFBO=True, units='norm')
    # store frame rate of monitor if we can measure it
    expInfo['frameRate'] = win.getActualFrameRate()
    if expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess

    stimuli_duration = core.StaticPeriod(screenHz=60)

    # define paths to stimuli and arrange in lists
    hz150 = ['stimuli/audiosegment/150hz_minus_100dBFS.wav',
             'stimuli/audiosegment/150hz_minus_90dBFS.wav',
             'stimuli/audiosegment/150hz_minus_80dBFS.wav',
             'stimuli/audiosegment/150hz_minus_70dBFS.wav',
             'stimuli/audiosegment/150hz_minus_60dBFS.wav',
             'stimuli/audiosegment/150hz_minus_50dBFS.wav',
             'stimuli/audiosegment/150hz_minus_40dBFS.wav',
             'stimuli/audiosegment/150hz_minus_30dBFS.wav',
             'stimuli/audiosegment/150hz_minus_20dBFS.wav',
             'stimuli/audiosegment/150hz_minus_10dBFS.wav']

    hz250 = ['stimuli/audiosegment/250hz_minus_100dBFS.wav',
             'stimuli/audiosegment/250hz_minus_90dBFS.wav',
             'stimuli/audiosegment/250hz_minus_80dBFS.wav',
             'stimuli/audiosegment/250hz_minus_70dBFS.wav',
             'stimuli/audiosegment/250hz_minus_60dBFS.wav',
             'stimuli/audiosegment/250hz_minus_50dBFS.wav',
             'stimuli/audiosegment/250hz_minus_40dBFS.wav',
             'stimuli/audiosegment/250hz_minus_30dBFS.wav',
             'stimuli/audiosegment/250hz_minus_20dBFS.wav',
             'stimuli/audiosegment/250hz_minus_10dBFS.wav']

    hz500 = ['stimuli/audiosegment/500hz_minus_100dBFS.wav',
             'stimuli/audiosegment/500hz_minus_90dBFS.wav',
             'stimuli/audiosegment/500hz_minus_80dBFS.wav',
             'stimuli/audiosegment/500hz_minus_70dBFS.wav',
             'stimuli/audiosegment/500hz_minus_60dBFS.wav',
             'stimuli/audiosegment/500hz_minus_50dBFS.wav',
             'stimuli/audiosegment/500hz_minus_40dBFS.wav',
             'stimuli/audiosegment/500hz_minus_30dBFS.wav',
             'stimuli/audiosegment/500hz_minus_20dBFS.wav',
             'stimuli/audiosegment/500hz_minus_10dBFS.wav']

    hz1000 = ['stimuli/audiosegment/1000hz_minus_100dBFS.wav',
              'stimuli/audiosegment/1000hz_minus_90dBFS.wav',
              'stimuli/audiosegment/1000hz_minus_80dBFS.wav',
              'stimuli/audiosegment/1000hz_minus_70dBFS.wav',
              'stimuli/audiosegment/1000hz_minus_60dBFS.wav',
              'stimuli/audiosegment/1000hz_minus_50dBFS.wav',
              'stimuli/audiosegment/1000hz_minus_40dBFS.wav',
              'stimuli/audiosegment/1000hz_minus_30dBFS.wav',
              'stimuli/audiosegment/1000hz_minus_20dBFS.wav',
              'stimuli/audiosegment/1000hz_minus_10dBFS.wav']

    hz1500 = ['stimuli/audiosegment/1500hz_minus_100dBFS.wav',
              'stimuli/audiosegment/1500hz_minus_90dBFS.wav',
              'stimuli/audiosegment/1500hz_minus_80dBFS.wav',
              'stimuli/audiosegment/1500hz_minus_70dBFS.wav',
              'stimuli/audiosegment/1500hz_minus_60dBFS.wav',
              'stimuli/audiosegment/1500hz_minus_50dBFS.wav',
              'stimuli/audiosegment/1500hz_minus_40dBFS.wav',
              'stimuli/audiosegment/1500hz_minus_30dBFS.wav',
              'stimuli/audiosegment/1500hz_minus_20dBFS.wav',
              'stimuli/audiosegment/1500hz_minus_10dBFS.wav']

    hz2000 = ['stimuli/audiosegment/2000hz_minus_100dBFS.wav',
              'stimuli/audiosegment/2000hz_minus_90dBFS.wav',
              'stimuli/audiosegment/2000hz_minus_80dBFS.wav',
              'stimuli/audiosegment/2000hz_minus_70dBFS.wav',
              'stimuli/audiosegment/2000hz_minus_60dBFS.wav',
              'stimuli/audiosegment/2000hz_minus_50dBFS.wav',
              'stimuli/audiosegment/2000hz_minus_40dBFS.wav',
              'stimuli/audiosegment/2000hz_minus_30dBFS.wav',
              'stimuli/audiosegment/2000hz_minus_20dBFS.wav',
              'stimuli/audiosegment/2000hz_minus_10dBFS.wav']

    hz2250 = ['stimuli/audiosegment/2250hz_minus_100dBFS.wav',
              'stimuli/audiosegment/2250hz_minus_90dBFS.wav',
              'stimuli/audiosegment/2250hz_minus_80dBFS.wav',
              'stimuli/audiosegment/2250hz_minus_70dBFS.wav',
              'stimuli/audiosegment/2250hz_minus_60dBFS.wav',
              'stimuli/audiosegment/2250hz_minus_50dBFS.wav',
              'stimuli/audiosegment/2250hz_minus_40dBFS.wav',
              'stimuli/audiosegment/2250hz_minus_30dBFS.wav',
              'stimuli/audiosegment/2250hz_minus_20dBFS.wav',
              'stimuli/audiosegment/2250hz_minus_10dBFS.wav']

    hz2500 = ['stimuli/audiosegment/2500hz_minus_100dBFS.wav',
              'stimuli/audiosegment/2500hz_minus_90dBFS.wav',
              'stimuli/audiosegment/2500hz_minus_80dBFS.wav',
              'stimuli/audiosegment/2500hz_minus_70dBFS.wav',
              'stimuli/audiosegment/2500hz_minus_60dBFS.wav',
              'stimuli/audiosegment/2500hz_minus_50dBFS.wav',
              'stimuli/audiosegment/2500hz_minus_40dBFS.wav',
              'stimuli/audiosegment/2500hz_minus_30dBFS.wav',
              'stimuli/audiosegment/2500hz_minus_20dBFS.wav',
              'stimuli/audiosegment/2500hz_minus_10dBFS.wav']

    hz2750 = ['stimuli/audiosegment/2750hz_minus_100dBFS.wav',
              'stimuli/audiosegment/2750hz_minus_90dBFS.wav',
              'stimuli/audiosegment/2750hz_minus_80dBFS.wav',
              'stimuli/audiosegment/2750hz_minus_70dBFS.wav',
              'stimuli/audiosegment/2750hz_minus_60dBFS.wav',
              'stimuli/audiosegment/2750hz_minus_50dBFS.wav',
              'stimuli/audiosegment/2750hz_minus_40dBFS.wav',
              'stimuli/audiosegment/2750hz_minus_30dBFS.wav',
              'stimuli/audiosegment/2750hz_minus_20dBFS.wav',
              'stimuli/audiosegment/2750hz_minus_10dBFS.wav']

    hz3000 = ['stimuli/audiosegment/3000hz_minus_100dBFS.wav',
              'stimuli/audiosegment/3000hz_minus_90dBFS.wav',
              'stimuli/audiosegment/3000hz_minus_80dBFS.wav',
              'stimuli/audiosegment/3000hz_minus_70dBFS.wav',
              'stimuli/audiosegment/3000hz_minus_60dBFS.wav',
              'stimuli/audiosegment/3000hz_minus_50dBFS.wav',
              'stimuli/audiosegment/3000hz_minus_40dBFS.wav',
              'stimuli/audiosegment/3000hz_minus_30dBFS.wav',
              'stimuli/audiosegment/3000hz_minus_20dBFS.wav',
              'stimuli/audiosegment/3000hz_minus_10dBFS.wav']

    hz4000 = ['stimuli/audiosegment/4000hz_minus_100dBFS.wav',
              'stimuli/audiosegment/4000hz_minus_90dBFS.wav',
              'stimuli/audiosegment/4000hz_minus_80dBFS.wav',
              'stimuli/audiosegment/4000hz_minus_70dBFS.wav',
              'stimuli/audiosegment/4000hz_minus_60dBFS.wav',
              'stimuli/audiosegment/4000hz_minus_50dBFS.wav',
              'stimuli/audiosegment/4000hz_minus_40dBFS.wav',
              'stimuli/audiosegment/4000hz_minus_30dBFS.wav',
              'stimuli/audiosegment/4000hz_minus_20dBFS.wav',
              'stimuli/audiosegment/4000hz_minus_10dBFS.wav']

    hz6000 = ['stimuli/audiosegment/6000hz_minus_100dBFS.wav',
              'stimuli/audiosegment/6000hz_minus_90dBFS.wav',
              'stimuli/audiosegment/6000hz_minus_80dBFS.wav',
              'stimuli/audiosegment/6000hz_minus_70dBFS.wav',
              'stimuli/audiosegment/6000hz_minus_60dBFS.wav',
              'stimuli/audiosegment/6000hz_minus_50dBFS.wav',
              'stimuli/audiosegment/6000hz_minus_40dBFS.wav',
              'stimuli/audiosegment/6000hz_minus_30dBFS.wav',
              'stimuli/audiosegment/6000hz_minus_20dBFS.wav',
              'stimuli/audiosegment/6000hz_minus_10dBFS.wav']

    hz8000 = ['stimuli/audiosegment/8000hz_minus_100dBFS.wav',
              'stimuli/audiosegment/8000hz_minus_90dBFS.wav',
              'stimuli/audiosegment/8000hz_minus_80dBFS.wav',
              'stimuli/audiosegment/8000hz_minus_70dBFS.wav',
              'stimuli/audiosegment/8000hz_minus_60dBFS.wav',
              'stimuli/audiosegment/8000hz_minus_50dBFS.wav',
              'stimuli/audiosegment/8000hz_minus_40dBFS.wav',
              'stimuli/audiosegment/8000hz_minus_30dBFS.wav',
              'stimuli/audiosegment/8000hz_minus_20dBFS.wav',
              'stimuli/audiosegment/8000hz_minus_10dBFS.wav']

    # define list of stimuli in order of presentation
    hz_list = [hz1000, hz1500,
               hz2000, hz2250, hz2500,
               hz2750, hz3000, hz4000, hz6000,
               hz8000, hz500, hz250, hz150]

    # lists to append results to
    result_list_increase1 = []
    result_list_increase2 = []
    result_list_decrease1 = []
    result_list_decrease2 = []




    # start trial 1: increasing volume, regular order
    win.flip()  # update screen, display messagel
    message = visual.TextStim(win, text='Druecke, wenn du einen Ton hoerst.')
    message.setAutoDraw(True)  # automatically draw every frame
    win.flip()  # update screen, display message
    core.wait(4.0)  # wait for given amount in seconds
    message.setText('Jetzt geht es los!')
    win.flip()
    core.wait(2.0)
    message.setText('Durchgang beginnt!')
    message.setAutoDraw(True)  # automatically draw every frame
    win.flip()  # update screen, display message

    # wait for mri-trigger
    while True:

        theseKeys = event.getKeys('t')
        if 't' in theseKeys:
            event.clearEvents(eventType='keyboard')
            break
        key_escape = event.getKeys('q')  # to end exp, if need be
        if 'q' in key_escape:
                win.close()
                core.quit()


    block_start = time.time()  # get starting time

    win.flip()  # update screen, display message
    message.setText('+')
    win.flip()
    trial_1_inc_start = time.time()  # get starting time for trial

    for i in hz_list:
        for j in range(0, 9):
            hz = i[j]  # get stimuli for easier saving

            frequency = sound.Sound(i[j])  # set stimuli

            frequency.play()  # start the sound

            stimuli_duration.start(2)  # start a period of 2s for stim display
            stimuli_duration.complete()  # end period

            key_escape = event.getKeys('q')  # to end exp, if need be
            if 'q' in key_escape:
                win.close()
                core.quit()

            # # get participant response, break loop and save picked stimuli
            this_key = event.getKeys('7')
            if '7' in this_key:
                result_list_increase1.append(hz)
                break

            frequency.stop()  # stop sound

            # set value,
            # if participant did not react for any volume of one freq
            if j is 8:
                if '7' not in this_key:
                    result_list_increase1.append(str(hz) + '/not_discovered')

        frequency.stop()
        if 'q' in key_escape:
            win.close()

    trial_1_inc_end = time.time()  # get time for trial end

    # trial 2: increasing volume  -> reversed list starting at 150hz
    core.wait(2)
    win.flip()
    message.setText('Druecke, wenn du einen Ton hoerst.')
    win.flip()
    core.wait(4.0)
    message.setText('Jetzt geht es los!')
    win.flip()
    core.wait(2.0)
    message.setText('+')
    win.flip()
    trial_2_inc_start = time.time()

    for i in reversed(hz_list):
        for j in range(0, 9):
            hz = i[j]

            frequency = sound.Sound(i[j])

            frequency.play()  # start the sound (it finishes automatically)

            stimuli_duration.start(2)  # start a period of 2s for stim display
            stimuli_duration.complete()  # finish period

            key_escape = event.getKeys('q')
            if 'q' in key_escape:
                win.close()
                core.quit()

            this_key = event.getKeys('7')
            if '7' in this_key:
                result_list_increase2.append(hz)
                break

            frequency.stop()
            print(j)
            if j is 8:
                if '7' not in this_key:
                    result_list_increase2.append(str(hz) + '/not_discovered')

        frequency.stop()
        if 'q' in key_escape:
            win.close()

    trial_2_inc_end = time.time()

# trial 3: decreasing volume -> regular order
    core.wait(2)
    win.flip()
    message.setText('Druecke, wenn du keinen Ton mehr hoerst.')
    win.flip()
    core.wait(4.0)
    message.setText('Jetzt geht es los!')
    win.flip()
    core.wait(2.0)
    message.setText('+')
    win.flip()
    trial_1_dec_start = time.time()

    for i in hz_list:

        for j in reversed(range(0, 9)):
            hz = i[j]

            frequency = sound.Sound(i[j])

            frequency.play()  # start the sound (it finishes automatically)

            stimuli_duration.start(2)  # start a period of 2s for stim display
            stimuli_duration.complete()  # finish period

            key_escape = event.getKeys('q')
            if 'q' in key_escape:
                win.close()
                core.quit()

            this_key = event.getKeys('7')
            if '7' in this_key:
                result_list_decrease1.append(hz)
                break
            frequency.stop()
            if j is 0:
                if '7' not in this_key:
                    result_list_decrease1.append(str(hz) + '/not_discovered')

        frequency.stop()
        if 'q' in key_escape:
            win.close()

    trial_1_dec_end = time.time()

    # trial 4: decreasing volume -> reversed order
    core.wait(2)
    win.flip()
    message.setText('Druecke, wenn du keinen Ton mehr hoerst.')
    win.flip()
    core.wait(4.0)
    message.setText('Jetzt geht es los!')
    win.flip()
    core.wait(2.0)
    message.setText('+')
    win.flip()
    trial_2_dec_start = time.time()

    for i in reversed(hz_list):
        for j in reversed(range(0, 9)):
            hz = i[j]

            frequency = sound.Sound(i[j])

            frequency.play()  # start the sound (it finishes automatically)

            stimuli_duration.start(2)  # start a period of 2s for stim display
            stimuli_duration.complete()  # finish period

            key_escape = event.getKeys('q')
            if 'q' in key_escape:
                win.close()
                core.quit()

            this_key = event.getKeys('7')
            if '7' in this_key:
                result_list_decrease2.append(hz)

                break

            frequency.stop()
            print(j)
            if j is 0:
                if '7' not in this_key:
                    result_list_decrease2.append(str(hz) + '/not_discovered')

        frequency.stop()
        if 'q' in key_escape:
            win.close()

    frequency.stop()
    trial_2_dec_end = time.time()

    # end text
    win.flip
    message.setText('Dieser Durchgang ist vorbei.')
    win.flip()
    core.wait(4.0)
    message.setText('Jetzt kommt eine kurze Pause!')
    win.flip()
    core.wait(2.0)

    block_end = time.time()  # get time for end of block

    # set up list, calculate duration for trials and append values
    trial_1_inc_duration = []
    trial_2_inc_duration = []
    trial_1_dec_duration = []
    trial_2_dec_duration = []
    trial_1_inc_dur = trial_1_inc_end - trial_1_inc_start
    trial_2_inc_dur = trial_2_inc_end - trial_2_inc_start
    trial_1_dec_dur = trial_1_dec_end - trial_1_dec_start
    trial_2_dec_dur = trial_2_dec_end - trial_2_dec_start

    trial_1_inc_duration.append(trial_1_inc_dur)
    trial_2_inc_duration.append(trial_2_inc_dur)
    trial_1_dec_duration.append(trial_1_dec_dur)
    trial_2_dec_duration.append(trial_2_dec_dur)

    # set up list, calculate duration for block and append value
    block_duration = []
    block_dur = block_end - block_start
    block_duration.append(block_dur)
    print(result_list_increase1)
    print('increase1')
    print(result_list_increase2)
    print('decrease1')
    print(result_list_decrease1)
    print('decrease2')
    print(result_list_decrease2)
    # set datframe containing exp results
    data = pd.DataFrame({'freq_increase_order1': result_list_increase1,
                         'freq_increase_order2': result_list_increase2,
                         'freq_decrease_order1': result_list_decrease1,
                         'freq_decrease_order2': result_list_decrease2})

    # set dataframe containing durations
    data_time = pd.DataFrame({'block duration': block_duration,
                              'trial_1_inc_duration': trial_1_inc_duration,
                              'trial_2_inc_duration': trial_2_inc_duration,
                              'trial_1_dec_duration': trial_1_dec_duration,
                              'trial_2_dec_duration': trial_2_dec_duration})
    # save data as csv
    data.to_csv(filename+'_' + setting + '_.csv',
                encoding='utf-8', index=False)
    data_time.to_csv(filename+'_' + setting + '_time''.csv',
                     encoding='utf-8', index=[0])
    # save data as .psydat
    thisExp.saveAsPickle(filename+setting)

    win.close()


def gui_func(field1, field2, field3, field4):
    """Define layout and create gui.

    Update status of setting after each run.
    """
    myDlg = gui.Dlg(title=expName)

    myDlg.addText(u'status: o = noch ausstehend  x = erledigt\n')
    # prompts static text field showing the status of each run
    myDlg.addText(field1 + '\tstructural(T1w)')
    myDlg.addText(field2 + '\tepi_standard(TR2s)')
    myDlg.addText(field3 + '\tepi_fast(TR1s)')
    myDlg.addText(field4 + '\tbaseline')

    # create empty list to append to
    list_ = []
    # check status of each stting and add unused settings to drop down menu
    if field1 == 'o':
        list_.append('structural(T1w)')
    if field2 == 'o':
        list_.append('epi_standard(TR2s)')
    if field3 == 'o':
        list_.append('epi_fast(TR1s)')
    if field4 == 'o':
        list_.append('baseline')

    # prompt message when all runs are done,
    # else print basic prompt and create drop down menu
    if len(list_) == 0:
        myDlg.addText(u'\n Danke, sie sind nun fertig.')
    else:
        myDlg.addText(u'\n   Waehlen Sie das gewuenschte setting aus:')
        myDlg.addField(u'', choices=list_)
    myDlg.show()
    if myDlg.OK == False:
        core.quit()  # user pressed cancel
    return myDlg


def ansl_main_func():
    """Define starting values of each string.

    Feed experiment info into the gui.
    """
    # create status icons/values for each run
    field1 = 'o'
    field2 = 'o'
    field3 = 'o'
    field4 = 'o'

    # call update function and add runs to menu
    myDlg = gui_func(field1, field2, field3, field4)

    # while loop: enables updating of gui
    while (not field1 == 'x'
           or not field2 == 'x'
           or not field3 == 'x'
           or not field4 == 'x'):

        for i in myDlg.data:
            if 'structural(T1w)' in myDlg.data:
                # generate run files for this session
                setting = 'structural(T1w)'
                run_func(filename, expInfo, thisExp, setting)
                print('structural(T1w)')
                field1 = 'x'
                myDlg = gui_func(field1, field2, field3, field4)
            elif 'epi_standard(TR2s)' in myDlg.data:
                setting = 'epi_standard(TR2s)'
                run_func(filename, expInfo, thisExp, setting)
                print('epi_standard(TR2s)')
                field2 = 'x'
                myDlg = gui_func(field1, field2, field3, field4)
            elif 'epi_fast(TR1s)' in myDlg.data:
                setting = 'epi_fast(TR1s)'
                run_func(filename, expInfo, thisExp, setting)
                print('epi_fast(TR1s)')
                field3 = 'x'
                myDlg = gui_func(field1, field2, field3, field4)
            elif 'baseline' in myDlg.data:
                setting = 'baseline'
                run_func(filename, expInfo, thisExp, setting)
                print('baseline')
                field4 = 'x'
                myDlg = gui_func(field1, field2, field3, field4)

#  call function
ansl_main_func()

logging.flush()
core.quit()
