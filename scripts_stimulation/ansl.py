"""ANSL: aint no sound loud enough.

Experiment for audiometry and control for audible frequency, given
different volumes.

Michael Ernst, Christina Paula van Gemmern, Jacqueline Kittel
"""
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division
import os
import errno  # handy system and path functions
import sys  # to get file system encoding
import time
import pandas as pd
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED)
from psychopy import (locale_setup, sound, gui, visual,
                      core, data, event, logging)
import json

import analyse_ansl


reload(sys)
sys.setdefaultencoding('utf8')

###############################################################################
# Func to present the stimuli and collect participant responses
###############################################################################
def stimuli_presentation(subject, hz_list, acquisition_scheme, order_volume,
                         order_presentation, single_run):
    """function to present stimuli
    if single_run == True
        present a single trial with specified order of volume
        and frequency progression,

    if single_run == False
        presents all possible combinations of volume and frequency
        progression (2x2) for one specifies acquisition_scheme

    subject = subject code
    hz_list = list containing paths to stimuli
    acquisition_scheme = name of specified acq-scheme
    order_volume = volume progression either "increasing" or "decreasing"
    order_presentation = frequency progression either "ascending" or
                         "descending"
    """

# setup your screen specifications
    #hz_list = pd.read_csv('/home/michael/atom/stimuli.csv')
    run_list = hz_list.columns

    if single_run == True:
        # setup window for stimuli presentation
        # set fullscr=True for fullscree presentation
        win = visual.Window([800,600],monitor="testMonitor", units="deg",
                            fullscr=False)
        print(acquisition_scheme)
        content['acq']= str(acquisition_scheme)

        #  reverse stimuli list if different order of frequency presentation is specified
        if order_presentation == 'descending':
            run_list = reversed(list(run_list))

        #  get order of volume and in what range they should be presented
        if order_volume == 'increasing':
            order = list(range(0,9))

        elif order_volume == 'decreasing':
            order = list(reversed(range(0,9)))

        #  get instruction for increasing or decreasing volume condition
        if order_volume == 'increasing':
            instruction = 'Press the button, once you - DO - hear a tone.'
        elif order_volume == 'decreasing':
            instruction = 'Press the button, if you - DO NOT - hear the tone anymore'

        #  append order of volume and frequency presentation to json-file
        content.setdefault('volume_progression', []).append(order_volume)
        content.setdefault('frequency_progression', []).append(order_presentation)

        #  create lists to keep track what and when stimuli is presented
        result_list = []
        stim_start_type = []
        stim_onset_list = []
        rt_list = []
        trial_onset_list = []
        trial_end_list = []
        all_stim_list = []

        #  specify and present instrtuction
        win.clearBuffer()
        win.flip()  # update screen, display message
        message = visual.TextStim(win, text=instruction)
        win.flip()  # update screen, display message
        message.setAutoDraw(True)  # automatically draw every frame
        win.flip()  # update screen, display message
        core.wait(1.5)  # wait for given amount in seconds

        # wait for mri-trigger
        for i in range(3):
            while True:
                #  get timestamp for first trigger
                if i == 0:
                    trial_onset = time.time()

                #  get trigger as keyboard input, 't' is the standard input for
                #  our scanner, eventually needs to be changed for different
                #  scanner
                theseKeys = event.getKeys('t')  #
                if 't' in theseKeys:
                    event.clearEvents(eventType='keyboard')
                    print('trigger')
                    break
                #  end experiment by pressing "q"
                key_escape = event.getKeys('q')  # to end exp, if need be
                if 'q' in key_escape:
                        win.close()
                        core.quit()
        trial_onset_list.append(trial_onset)

        #  present msg indicating that trial begins
        message.setText('Run starts!')
        message.setAutoDraw(True)  # automatically draw every frame
        win.flip()  # update screen, display message

        #  end experiment by pressing "q"
        key_escape = event.getKeys('q')  # to end exp, if need be
        if 'q' in key_escape:
            win.close()
            core.quit()

        #  present fixation cross
        win.clearBuffer()
        win.flip()  # update screen, display message
        message.setText('+')
        win.flip()

        #######################################################################
        # stimuli presentation starts here
        #######################################################################
        #counter = 0  # counter
        #  iterate over list of stimuli
        for i in run_list:
            for j in order:
                core.wait(1)  # wait for one second before stimuli presentation
                #print(j)

                #  which stimuli to play
                hz = hz_list[i][j]

                # condition to break loop once participants responds to stimuli
                stop_loop = False

                # set stimuli as sound object
                stim = sound.Sound(_thisDir + '/stimuli/' + hz)

                win.clearBuffer()
                win.flip()  # update screen, display message

                #  end experiment by pressing "q"
                key_escape = event.getKeys('q')  # to end exp, if need be
                if 'q' in key_escape:
                    win.close()
                    core.quit()
                #core.wait(0.2)  # wait for 0.2s for system to settle
                #  clock object to keep track of presentation time
                trial_clock = core.Clock()

                stim.play()  # play stimuli
                #  get timestamp of stimuli presentation and append to list
                stim_start_absolute = time.time()
                stim_start = stim_start_absolute - trial_onset
                stim_start_type.append(hz)
                all_stim_list.append(stim_start)

                #  present stimuli for 2s and wait for participants response
                while trial_clock.getTime() < 2.0:  # clock times are in seconds
                    if 0.0 <= trial_clock.getTime() < 2.0:

                        #  if participant presses the "7" key stop volume volume
                        #  progression and jump to next stimuli
                        this_key = event.getKeys('7')
                        if '7' in this_key:
                            stim.stop()
                            stim_onset_list.append(stim_start)  #timestamp for stim onset
                            #counter += 1
                            #  get specific volume that was responded to
                            result_list.append(hz)

                            #  get timestamp for participant response
                            rt_absolute = time.time()
                            rt = rt_absolute - trial_onset
                            rt_list.append(rt)
                            stop_loop = True  # indicates that next stimuli should be picked
                            break
                        elif order_volume == 'decreasing' and j is 0 and '7' not in this_key and trial_clock.getTime() > 1.9:
                            print('not_discovered')
                            result_list.append(str(hz) + '/not_discovered')
                            stim_onset_list.append(stim_start)
                            #counter += 1
                            stim.stop()
                            rt_absolute = time.time()
                            rt = rt_absolute - trial_onset
                            rt_list.append(rt)
                            stop_loop = True
                            break


                        elif order_volume == 'increasing' and j is 8 and '7' not in this_key and trial_clock.getTime() > 1.9:
                            print('not_discovered')

                            result_list.append(str(hz) + '/not_discovered')
                            stim.stop()
                            stim_onset_list.append(stim_start)
                            #counter += 1
                            rt_absolute = time.time()
                            rt = rt_absolute - trial_onset
                            rt_list.append(rt)
                            stop_loop = True
                            break


                        key_escape = event.getKeys('q')  # to end exp, if need be
                        if 'q' in key_escape:
                            win.close()
                            core.quit()

                if stop_loop is True:
                    break
        #  close window for presentation
        win.close()

        #  create DataFrame to save results
        df_results = pd.DataFrame({'stimuli': result_list})

        order_presentation_list = []
        volumes = []
        frequencies = []
        acquisition_scheme_list = []
        order_volume_list = []
        subject_name = []

        for i in df_results.columns:
            for item in df_results[i]:
                subject_name.append(subject)
                # get info on acquisition_scheme
                if 'baseline' in acquisition_scheme:
                    acquisition_scheme_list.append('baseline')
                elif 'epi_fast(TR1s)' in acquisition_scheme:
                    acquisition_scheme_list.append('epi_fast(TR1s)')
                elif 'epi_standard(TR2s)' in acquisition_scheme:
                    acquisition_scheme_list.append('epi_standard(TR2s)')
                elif 'mprage(T1w)' in acquisition_scheme:
                    acquisition_scheme_list.append('mprage(T1w)')
                else:
                    acquisition_scheme_list.append('mprage(T1w)')


                # get info on volume order
                if 'decreasing' in order_volume:
                    order_volume_list.append('decreasing')
                elif 'increasing' in order_volume:
                    order_volume_list.append('increasing')
                # get info on stimuli order
                if 'ascending' in order_presentation:
                    order_presentation_list.append('ascending')
                elif 'descending' in order_presentation:
                    order_presentation_list.append('descending')

                # extract discovered volume
                if 'not_discovered' in item:
                    volumes.append('0')
                #elif '10dBFS' in item:
                #    volumes.append(-10)
                elif '20dBFS' in item:
                    volumes.append(-20)
                elif '30dBFS' in item:
                    volumes.append(-30)
                elif '40dBFS' in item:
                    volumes.append(-40)
                elif '50dBFS' in item:
                    volumes.append(-50)
                elif '60dBFS' in item:
                    volumes.append(-60)
                elif '70dBFS' in item:
                    volumes.append(-70)
                elif '80dBFS' in item:
                    volumes.append(-80)
                elif '90dBFS' in item:
                    volumes.append(-90)
                elif '100dBFS' in item:
                    volumes.append(-100)

                if '150hz' in item:
                    frequencies.append(150)
                elif '1000hz' in item:
                    frequencies.append(1000)
                elif '1500hz' in item:
                    frequencies.append(1500)
                elif '2000hz' in item:
                    frequencies.append(2000)
                elif '2250hz' in item:
                    frequencies.append(2250)
                elif '2500hz' in item:
                    frequencies.append(2500)
                elif '2750hz' in item:
                    frequencies.append(2750)
                elif '3000hz' in item:
                    frequencies.append(3000)
                elif '4000hz' in item:
                    frequencies.append(4000)
                elif '6000hz' in item:
                    frequencies.append(6000)
                elif '8000hz' in item:
                    frequencies.append(8000)
                elif '250hz' in item:
                    frequencies.append(250)
                elif '500hz' in item:
                    frequencies.append(500)

        # set datframe containing exp results
        date = data.getDateStr()  # get date
        df = pd.DataFrame({'stimuli': result_list,
                             'subject': subject_name,
                             'onset': stim_onset_list,
                             'reaction_time': rt_list,
                             'acquisition_scheme': acquisition_scheme_list,
                             'Level (dBFS)': volumes,
                             'Frequency (Hz)': frequencies,
                             'order_volume': order_volume_list,
                             'order_presentation': order_presentation_list})

        # save data as csv
        df.to_csv('{first}_{second}_{third}_{fourth}_{last}.tsv'.format(first=subject,
                                                        second=acquisition_scheme,
                                                        third=order_volume,
                                                        fourth=order_presentation,
                                                        last=str(date)),
                                                        encoding='utf-8', index=False,  sep='\t')

        # save trial_start times
        df_trial_start = pd.DataFrame({'trial_start': trial_onset_list})
        df_trial_start.to_csv('{first}_{second}_{third}_{fourth}_trial_start_{last}.tsv'.format(first=subject,
                                                        second=acquisition_scheme,
                                                        third=order_volume,
                                                        fourth=order_presentation,
                                                        last=str(date)),
                                                        encoding='utf-8', index=False,  sep='\t')
        # save all stimuli onsets
        df_stimuli_onsets = pd.DataFrame({'stimuli_onset': all_stim_list,
                                          'Frequency (Hz)': stim_start_type})
        df_stimuli_onsets.to_csv('{first}_{second}_{third}_{fourth}__stimuli_onsets_{last}.tsv'.format(first=subject,
                                                        second=acquisition_scheme,
                                                        third=order_volume,
                                                        fourth=order_presentation,
                                                        last=str(date)),
                                                        encoding='utf-8', index=False,  sep='\t')

        #  write json-summary-file for trial
        with open('{first}_{second}_{third}_{fourth}_{last}.json'.format(first=subject,
                                                        second=acquisition_scheme,
                                                        third=order_volume,
                                                        fourth=order_presentation,
                                                        last=str(date)),
                                                        'w') as f:
            json.dump(content, f, indent=4)

    ## if user specified to run all volume and presentation orders
    elif single_run == False:
        #  repeat loop for each possible combination of conditions
        for x in range(4):
            content['acq']= acquisition_scheme

            list_volume = ['increasing', 'decreasing']
            list_order = ['ascending', 'descending']

            if x == 0:
                # setup window for stimuli presentation
                # set fullscr=True for fullscree presentation
                win = visual.Window([800,600],monitor="testMonitor", units="deg")

                #  create lists to keep track what and when stimuli is presented
                result_list = []
                stim_start_type = []
                stim_onset_list = []
                rt_list = []
                trial_onset_list = []
                trial_end_list = []
                order_presentation_list = []
                order_volume_list = []
                all_stim_list = []

            #  x = how often loop was performed; which trial we're in
            if x == 0:
                #  get presentation conditions for first trial
                order_volume = list_volume[0]
                order_presentation = list_order[0]
                instruction = 'Press the button, once you - DO - hear a tone.'

            elif x == 1:
                #  get presentation conditions for second trial
                order_volume = list_volume[1]
                order_presentation = list_order[0]
                instruction = 'Press the button, if you - DO NOT - hear the tone anymore'

            elif x == 2:
                #  get presentation conditions for third trial

                order_volume = list_volume[0]
                order_presentation = list_order[1]
                instruction = 'Press the button, once you - DO - hear a tone.'

            elif x == 3:
                #  get presentation conditions for second trial
                order_volume = list_volume[1]
                order_presentation = list_order[1]
                instruction = 'Press the button, if you - DO NOT - hear the tone anymore'

            #  list containing stimuli categories (e.g. 150hz, 250hz, etc.)
            run_list = hz_list.columns

            #  reverse stimuli list if different order of frequency presentation is specified
            if order_presentation == 'descending':
                run_list = reversed(list(hz_list))

            #  get order of volume and in what range they should be presented
            if order_volume == 'increasing':
                order = list(range(0, 9))

            elif order_volume == 'decreasing':
                order = list(reversed(range(0, 9)))

            #  append order of volume and frequency presentation to json-file
            content.setdefault('volume_progression', []).append(order_volume)
            content.setdefault('frequency_progression', []).append(order_presentation)

            #  to avoid overlap of different instructions on screen
            if x is not 0:
                message.setAutoDraw(False)  # automatically draw every frame
                win.flip()

            #  specify and present instrtuction
            message = visual.TextStim(win, text=instruction)
            message.setAutoDraw(True)  # automatically draw every frame
            win.flip()  # update screen, display message
            core.wait(1.5)  # wait for given amount in seconds

            # wait for mri-trigger
            for i in range(3):
                while True:
                    #  get timestamp for first trigger
                    if i == 0:
                        trial_onset = time.time()

                    #  get trigger as keyboard input, 't' is the standard input for
                    #  our scanner, eventually needs to be changed for different
                    #  scanner
                    theseKeys = event.getKeys('t')
                    if 't' in theseKeys:
                        event.clearEvents(eventType='keyboard')
                        print('trigger')
                        break
                    key_escape = event.getKeys('q')  # to end exp, if need be
                    if 'q' in key_escape:
                            win.close()
                            core.quit()

            trial_onset_list.append(trial_onset)

            key_escape = event.getKeys('q')  # to end exp, if need be
            if 'q' in key_escape:
                win.close()
                core.quit()

            #  present fixation cross
            message.setText('+')
            message.setAutoDraw(True)  # automatically draw every frame
            win.flip()

            #counter = 0
            #  iterate over list of stimuli
            for i in run_list:
                for j in order:
                    # wait for 1 sec, otherwise next trial is started to quick
                    core.wait(1)

                    #  which stimuli to play
                    hz = hz_list[i][j]

                    # condition to break loop once participants responds to stimuli
                    stop_loop = False

                    # set stimuli as sound object
                    stim = sound.Sound(_thisDir + '/stimuli/' + hz)

                    key_escape = event.getKeys('q')  # to end exp, if need be
                    if 'q' in key_escape:
                        win.close()
                        core.quit()
                    #core.wait(0.2)
                    trial_clock = core.Clock()

                    stim.play()  # play stimuli
                    #  get timestamp of stimuli presentation and append to list
                    stim_start_absolute = time.time()
                    stim_start = stim_start_absolute - trial_onset
                    stim_start_type.append(hz)
                    all_stim_list.append(stim_start)

                    #  present stimuli for 2s and wait for participants response
                    while trial_clock.getTime() < 2.0:  # clock times are in seconds

                        if 0.0 <= trial_clock.getTime() < 2.0:

                            #  if participant presses the "7" key stop volume volume
                            #  progression and jump to next stimuli
                            this_key = event.getKeys('7')
                            if '7' in this_key:
                                stim.stop()
                                stim_onset_list.append(stim_start)
                                #counter += 1

                                #  get specific volume that was responded to
                                result_list.append(hz)

                                #  get timestamp for participant response
                                rt_absolute = time.time()
                                rt = rt_absolute - trial_onset
                                rt_list.append(rt)
                                order_presentation_list.append(order_presentation)
                                order_volume_list.append(order_volume)
                                stop_loop = True  # indicates that next stimuli should be picked
                                break
                            elif order_volume == 'decreasing' and j is 0 and '7' not in this_key and trial_clock.getTime() > 1.9:
                                result_list.append(str(hz) + '/not_discovered')
                                stim_onset_list.append(stim_start)
                                #counter += 1
                                stim.stop()
                                rt_absolute = time.time()
                                rt = rt_absolute - trial_onset
                                rt_list.append(rt)
                                order_presentation_list.append(order_presentation)
                                order_volume_list.append(order_volume)
                                stop_loop = True
                                break

                            elif order_volume == 'increasing' and j is 8 and '7' not in this_key and trial_clock.getTime() > 1.9:
                                result_list.append(str(hz) + '/not_discovered')
                                stim.stop()
                                stim_onset_list.append(stim_start)
                                #counter += 1
                                rt_absolute = time.time()
                                rt = rt_absolute - trial_onset
                                rt_list.append(rt)
                                order_presentation_list.append(order_presentation)
                                order_volume_list.append(order_volume)

                                stop_loop = True
                                break


                            key_escape = event.getKeys('q')  # to end exp, if need be
                            if 'q' in key_escape:
                                win.close()
                                core.quit()

                    if stop_loop is True:
                        break
        #  if fourth trial is done
        if x == 3:

            #  create DataFrame to save results
            df_results = pd.DataFrame({'stimuli': result_list})

            volumes = []
            frequencies = []
            acquisition_scheme_list = []
            subject_name = []

            for i in df_results.columns:
                for item in df_results[i]:
                    subject_name.append(subject)
                    # get info on acquisition_scheme
                    if 'baseline' in acquisition_scheme:
                        acquisition_scheme_list.append('baseline')
                    elif 'epi_fast(TR1s)' in acquisition_scheme:
                        acquisition_scheme_list.append('epi_fast(TR1s)')
                    elif 'epi_standard(TR2s)' in acquisition_scheme:
                        acquisition_scheme_list.append('epi_standard(TR2s)')
                    elif 'mprage(T1w)' in acquisition_scheme:
                        acquisition_scheme_list.append('mprage(T1w)')
                    else:
                        acquisition_scheme_list.append('mprage(T1w)')

                    # extract discovered volume
                    if 'not_discovered' in item:
                        volumes.append('0')
                    #elif '10dBFS' in item:
                    #volumes.append(-10)
                    elif '20dBFS' in item:
                        volumes.append(-20)
                    elif '30dBFS' in item:
                        volumes.append(-30)
                    elif '40dBFS' in item:
                        volumes.append(-40)
                    elif '50dBFS' in item:
                        volumes.append(-50)
                    elif '60dBFS' in item:
                        volumes.append(-60)
                    elif '70dBFS' in item:
                        volumes.append(-70)
                    elif '80dBFS' in item:
                        volumes.append(-80)
                    elif '90dBFS' in item:
                        volumes.append(-90)
                    elif '100dBFS' in item:
                        volumes.append(-100)

                    # print(volumes)
                    if '150hz' in item:
                        frequencies.append(150)
                    elif '1000hz' in item:
                        frequencies.append(1000)
                    elif '1500hz' in item:
                        frequencies.append(1500)
                    elif '2000hz' in item:
                        frequencies.append(2000)
                    elif '2250hz' in item:
                        frequencies.append(2250)
                    elif '2500hz' in item:
                        frequencies.append(2500)
                    elif '2750hz' in item:
                        frequencies.append(2750)
                    elif '3000hz' in item:
                        frequencies.append(3000)
                    elif '4000hz' in item:
                        frequencies.append(4000)
                    elif '6000hz' in item:
                        frequencies.append(6000)
                    elif '8000hz' in item:
                        frequencies.append(8000)
                    elif '250hz' in item:
                        frequencies.append(250)
                    elif '500hz' in item:
                        frequencies.append(500)

                # set datframe containing exp results
                date = data.getDateStr()  # get date
                df = pd.DataFrame({'stimuli': result_list,
                                     'subject': subject_name,
                                     'onset': stim_onset_list,
                                     'reaction_time': rt_list,
                                     'acquisition_scheme': acquisition_scheme_list,
                                     'Level (dBFS)': volumes,
                                     'Frequency (Hz)': frequencies,
                                     'order_volume': order_volume_list,
                                     'order_presentation': order_presentation_list})

                # save data as tsv
                df.to_csv('{first}_{second}_{last}.tsv'.format(first=subject,
                                                                second=acquisition_scheme,
                                                                last=str(date)),
                                                                encoding='utf-8', index=False,  sep='\t')

                # save trial_start times
                df_trial_start = pd.DataFrame({'trial_start': trial_onset_list})
                df_trial_start.to_csv('{first}_{second}_trial_start_{last}.tsv'.format(first=subject,
                                                                second=acquisition_scheme,
                                                                last=str(date)),
                                                                encoding='utf-8', index=False,  sep='\t')

                # save all stimuli onsets
                df_stimuli_onsets = pd.DataFrame({'stimuli_onset': all_stim_list,
                                                  'Frequency (Hz)': stim_start_type})
                df_stimuli_onsets.to_csv('{first}_{second}__stimuli_onsets_{last}.tsv'.format(first=subject,
                                                                second=acquisition_scheme,
                                                                last=str(date)),
                                                                encoding='utf-8', index=False,  sep='\t')

                #  write json-summary-file for trial
                with open('{first}_{second}_{last}.json'.format(first=subject,
                                                                second=acquisition_scheme,
                                                                last=str(date)),
                                                                'w') as f:
                    json.dump(content, f, indent=4)
        #  close window for presentation
        win.close()
# ----------------------------------------------------------------------------


def gui_func1(field1, field2, field3, field4):
    """Define layout and create gui to specify
    acquisition_scheme.
    """
    # create empty list to append to
    list_ = []

    # check status of each stting and add unused settings to drop down menu
    if field1 == 'o':
        list_.append('mprage(T1w)')
    if field2 == 'o':
        list_.append('epi_standard(TR2s)')
    if field3 == 'o':
        list_.append('epi_fast(TR1s)')
    if field4 == 'o':
        list_.append('baseline')


    myDlg = gui.Dlg(title=expName)

    # prompts static text field showing the status of each run
    myDlg.addText('\t')
    myDlg.addText(field1 + '\tmprage(T1w)')
    myDlg.addText(field2 + '\tepi_standard(TR2s)')
    myDlg.addText(field3 + '\tepi_fast(TR1s)')
    myDlg.addText(field4 + '\tbaseline')

    #if len(list_) == 0:
    #    myDlg.addText(u"\n Thanks, you're done.")
    #else:
    myDlg.addText(u'\n   Choose acquisition_scheme:')
    myDlg.addField(u'', choices=list_)

    myDlg.show()  # output gui to screen
    if myDlg.OK == False:
        analyse_ansl.main_func(_thisDir, expInfo)  # call analysis script once exp is closed
        core.quit()  # user pressed cancel

    #  get info on acquisition_scheme
    myDlg = myDlg.data
    return myDlg

def gui_func2():
    """Define layout and create gui to specify if single or multiple trial
    should be run.
    """

    myDlg2 = gui.Dlg(title=expName)
    myDlg2.addText(u'\n   Run stimuli in all orders of frequency presentation and volume progression?:')
    myDlg2.addField(u'', choices=['yes', 'no'])


    myDlg2.show()

    if myDlg2.OK == False:
        analyse_ansl.main_func(_thisDir, expInfo)
        core.quit()  # user pressed cancel

    #  get info if single or multiple trial should be run
    myDlg2 = myDlg2.data
    return myDlg2


def gui_func3():
    """Define layout and create gui to specify specific conditions if
    presenting a single trial was specified in previous gui
    """
    list_volume = ['increasing', 'decreasing']
    list_order = ['ascending', 'descending']

    myDlg3 = gui.Dlg(title=expName)
    myDlg3.addText(u'\n   Choose volume order:')
    myDlg3.addField(u'', choices=list_volume)
    myDlg3.addText(u'\n   Choose presentation order:')
    myDlg3.addField(u'', choices=list_order)

    myDlg3.show()
    if myDlg3.OK == False:
        analyse_ansl.main_func(_thisDir, expInfo)
        core.quit()  # user pressed cancel

    #  get info on combination of conditions
    myDlg3 = myDlg3.data
    return myDlg3

def ansl_main_func(subject):
    """Define starting values of each string.

    Feed experiment info into the gui.
    """
    # create status icons/values for each run
    field1 = 'o'
    field2 = 'o'
    field3 = 'o'
    field4 = 'o'


    # call gui function one afther another
    myDlg = gui_func1(field1, field2, field3, field4)  # first gui
    myDlg2 = gui_func2()  # second gui

    # if single run was selected call third gui
    if myDlg2[0] == 'no':
        myDlg3 = gui_func3()


    # while loop: enables updating of gui
    while (not field1 == 'x'
           or not field2 == 'x'
           or not field3 == 'x'
           or not field4 == 'x'):

        for i in myDlg:
            #  if mprage acq-schme was selected
            if 'mprage(T1w)' in myDlg:
                acquisition_scheme = 'mprage(T1w)'

                #  if multiple trial presentation was selected
                if myDlg2[0] == 'yes':
                    single_run = False
                    order_volume = None
                    order_presentation = None
                    stimuli_presentation(subject, hz_list, acquisition_scheme,
                                         order_volume, order_presentation,
                                         single_run)

                #  if single trial presentation was selected
                if myDlg2[0] == 'no':
                    # specified order of volume_progression
                    order_volume = myDlg3[0]

                    # specified order of frequency_progression
                    order_presentation = myDlg3[1]
                    single_run = True
                    stimuli_presentation(subject, hz_list, acquisition_scheme,
                                         order_volume, order_presentation,
                                         single_run)
                # call gui function one afther another
                myDlg = gui_func1(field1, field2, field3, field4)
                myDlg2 = gui_func2()

                # if single run was selected call third gui
                if myDlg2[0] == 'no':
                    myDlg3 = gui_func3()

            #  if epi_standard acq-schme was selected
            elif 'epi_standard(TR2s)' in myDlg:
                acquisition_scheme = 'epi_standard(TR2s)'

                #  if multiple trial presentation was selected
                if myDlg2[0] == 'yes':
                    single_run = False
                    order_volume = None
                    order_presentation = None
                    stimuli_presentation(subject, hz_list, acquisition_scheme,
                                         order_volume, order_presentation,
                                         single_run)

                #  if single trial presentation was selected
                if myDlg2[0] == 'no':
                    # specified order of volume_progression
                    order_volume = myDlg3[0]

                    # specified order of frequency_progression
                    order_presentation = myDlg3[1]
                    single_run = True
                    stimuli_presentation(subject, hz_list, acquisition_scheme,
                                         order_volume, order_presentation,
                                         single_run)
                # call gui function one afther another
                myDlg = gui_func1(field1, field2, field3, field4)
                myDlg2 = gui_func2()

                # if single run was selected call third gui
                if myDlg2[0] == 'no':
                    myDlg3 = gui_func3()

            #  if epi_fast acq-schme was selected
            elif 'epi_fast(TR1s)' in myDlg:
                acquisition_scheme = 'epi_fast(TR1s)'

                #  if multiple trial presentation was selected
                if myDlg2[0] == 'yes':
                    single_run = False
                    order_volume = None
                    order_presentation = None
                    stimuli_presentation(subject, hz_list, acquisition_scheme,
                                         order_volume, order_presentation,
                                         single_run)

                #  if single trial presentation was selected
                if myDlg2[0] == 'no':
                    # specified order of volume_progression
                    order_volume = myDlg3[0]

                    # specified order of frequency_progression
                    order_presentation = myDlg3[1]
                    single_run = True
                    stimuli_presentation(subject, hz_list, acquisition_scheme,
                                         order_volume, order_presentation,
                                         single_run)
                # call gui function one afther another
                myDlg = gui_func1(field1, field2, field3, field4)
                myDlg2 = gui_func2()

                # if single run was selected call third gui
                if myDlg2[0] == 'no':
                    myDlg3 = gui_func3()

            #  if baseline condition was selected
            elif 'baseline' in myDlg:
                acquisition_scheme = 'baseline'

                #  if multiple trial presentation was selected
                if myDlg2[0] == 'yes':
                    single_run = False
                    order_volume = None
                    order_presentation = None
                    stimuli_presentation(subject, hz_list, acquisition_scheme,
                                         order_volume, order_presentation,
                                         single_run)

                #  if single trial presentation was selected
                if myDlg2[0] == 'no':
                    # specified order of volume_progression
                    order_volume = myDlg3[0]

                    # specified order of frequency_progression
                    order_presentation = myDlg3[1]
                    single_run = True
                    stimuli_presentation(subject, hz_list, acquisition_scheme,
                                         order_volume, order_presentation,
                                         single_run)
                # call gui function one afther another
                myDlg = gui_func1(field1, field2, field3, field4)
                myDlg2 = gui_func2()

                # if single run was selected call third gui
                if myDlg2[0] == 'no':
                    myDlg3 = gui_func3()


###############################################################################
# setup
###############################################################################

# clock for keeping time of routines from beginning of script
absolute_clock = time.time()

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(
            sys.getfilesystemencoding())
os.chdir(_thisDir)
print(_thisDir)

# Store info about the experiment session
expName = 'aint_no_sound_loud_enough'
expInfo = {u'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)

if dlg.OK is False:
    core.quit()  # user pressed cancel

expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'],
                                                    expName,
                                                    expInfo['date'])

# create subject directory
try:
    os.makedirs('data/'+expInfo['participant'])
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

os.chdir(_thisDir + '/data/' + expInfo['participant'] + '/')

# setup dict for json sidecar
content = {}
content['subject'] = expInfo['participant']
content['date'] = expInfo['date']

file_id = expName + '_' + expInfo['participant']


# get dataframe containing paths to stimuli
hz_list = pd.read_csv('/home/michael/atom/stimuli.csv')


#  call function
subject = expInfo['participant']  # get subject code
ansl_main_func(subject)


core.quit()  # quit session
