''' created by Michael Ernst (https://github.com/M-earnest)

main gui - allowing access to questionnaires'''
from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functionspart of the Dlg object has been deleted, attribute access no longer allowed.

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import pandas as pd

import feedback_ansl as feedback
import screening_ansl as screening
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)
expInfo = {'participant':'', 'directory':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title='questionaire')
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp

save_path = expInfo['directory']
print(save_path)

# defines layout of hui gui and updates status of questionnaires after each run
def update(field1, field2):
    # creates starting gui
    myDlg = gui.Dlg(title=u'questionaires')
    myDlg.addText(u'status: o = not completed  x = completed\n')
    # prompts static text field showing the status of each questionaire
    myDlg.addText(field1 + ' demographisch')
    myDlg.addText(field2 + ' feedback')

    # create empty list to append to
    list_ = []
    # check status of each questionaire and add still open questionaires to drop down menu
    if field1 == 'o':
        list_.append('demographics')
    if field2 == 'o':
        list_.append('feedback')


    # prompt message when all questionaires are done, else print basic prompt and create drop down menu
    if len(list_) == 0 :
        myDlg.addText(u'\n Thank you very much, you have finished this questionnaire.')
    else:
        myDlg.addText(u'\n   Please choose the questionnaire you want to conduct:')
        myDlg.addField(u'',choices=list_)
    myDlg.show()
    return myDlg

# main func - defines starting values of each questionaire and feeds the questionaire modules into the gui
def questionaires_func():
    # create status icons/values for each questionaire
    field1 = 'o'
    field2 = 'o'
    # call update function and add all open questionaires to menu
    myDlg = update(field1, field2)

    # while loop allows updating the starting gui with new status
    while not field1 == 'x' or not field2 == 'x':

        for i in myDlg.data:
            if 'demographics' in myDlg.data:
                screening.main_func(expInfo, save_path)
                field1 = 'x'
                myDlg = update(field1, field2)

            elif 'feedback' in myDlg.data:
                feedback.main_func(expInfo, save_path)
                field2 = 'x'
                myDlg = update(field1, field2)

#  call function
questionaires_func()
core.quit()
