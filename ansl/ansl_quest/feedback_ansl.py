"""created by Michael Ernst (https://github.com/M-earnest)

feedback questionnaire for ansl pilot
"""


from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
import os  # handy system and path functions
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import pandas as pd


def update(list_1,firsttrial,check):
# function to display Dialogue
    # assign gui to variable and define title

    if check == 0:

    #gUI_1
    #added and list_1[] == '' in red condition --> resolved
        print(str(firsttrial)+'trial')
        myDlg1 = gui.Dlg(title="Nachbefragung")
        # quest 1
        myDlg1.addField('Which tones were audible?:',choices= ['low','high','both','none'],initial=list_1[0])
        # quest 2
        myDlg1.addField('Which tones were not audible?:', choices=['low','high','both','none'],initial=list_1[1])
        # quest 3 and 4
        myDlg1.addField('Do you were distracted during the audiometry / could you not concentrate?'
                        ,choices= ['J','N'],initial=list_1[2])
        if list_1[2] == '' and firsttrial==0:
            myDlg1.addField('If yes: why?:',initial=list_1[3])
        elif list_1[2] == 'y'  and list_1[3] == '' and firsttrial==1:
            myDlg1.addField('If yes: why?:',initial=list_1[3], color='red')
        elif list_1[2] == 'N'  and firsttrial==1:
            myDlg1.addField('If yes: why?:',initial=list_1[3])
        elif list_1[2] == 'Y'  and not list_1[3] == ''and firsttrial==1:
            myDlg1.addField('If yes: why?:',initial=list_1[3])

        # quest 5 and 6
        myDlg1.addField('Konntest du deine Konzentration gut auf das Hoeren der Toene richten?',choices= ['J','N'],initial=list_1[4])
        if list_1[4] == '' and firsttrial==0:
            myDlg1.addField('Wenn Nein: Warum?:',initial=list_1[5])
        elif list_1[4] == 'N'  and list_1[5] == '' and firsttrial==1:
            myDlg1.addField('Wenn Nein: Warum?:',initial=list_1[5], color='red')
        elif list_1[4] == 'J'  and firsttrial==1:
            myDlg1.addField('Wenn Nein: Warum?:',initial=list_1[5])
        elif list_1[4] == 'N'  and not list_1[5] == '' and firsttrial==1:
            myDlg1.addField('Wenn Nein: Warum?:',initial=list_1[5])
        # quest 6 and 7
        myDlg1.addField('Hattest du bestimmte Strategien, um die Toene besser wahrzunehmen?',choices= ['J','N'],initial=list_1[6])
        if list_1[6] == '' or firsttrial==0:
            myDlg1.addField('Wenn Ja: Welche?',initial=list_1[7])
        elif list_1[6] == 'J' and list_1[7] == ''  and firsttrial==1:
            myDlg1.addField('Wenn Ja: Welche?',initial=list_1[7], color='red')
        elif list_1[6] == 'N'  and firsttrial==1:
            myDlg1.addField('Wenn Ja: Welche?',initial=list_1[7])
        elif list_1[6] == 'J' and not list_1[7] == ''  and firsttrial==1:
            myDlg1.addField('Wenn Ja: Welche?',initial=list_1[7])

        # quest 8
        if list_1[8] == '' or firsttrial==1:
            myDlg1.addField('Zusaetzlichen Anmerkungen zum Experiment?',initial=list_1[8])
        elif not list_1[8] == '' and firsttrial == 1:
            myDlg1.addField('Zusaetzlichen Anmerkungen zum Experiment?',initial=list_1[8])

        myDlg1.show()
        myDlg1 = myDlg1.data
        return list_1, myDlg1


def savecsv(list_1,filename):
  # function to add data to experiment handler and save as csv
  # add column + data

    print('list')
    data = {'gut_hoerbar': list_1[0],
            'schlecht_hoerbar': list_1[1],
            'aufmerksamkeit': list_1[2],
            'problematik_aufmerksamkeit': list_1[3],
            'konzentartion_toene': list_1[4],
            'problematik_konzentration': list_1[5],
            'strategienutzung': list_1[6],
            'genutzte Strategie': list_1[7],
            'zusaetzliche_anmerkungen': list_1[8]}

    df = pd.Series(data).to_frame()
    df.to_csv(filename+'.csv',header=False)


def check_values(list_1, check):
    print(list_1)
    if check == 0:
        if list_1[2] == 'J' and list_1[3] == '':
            print('01 is the problem')
            return 0
        elif list_1[4] == 'N' and list_1[5] == '':
            print('q2')
            return 0
        elif list_1[6] == 'J' and list_1[7] == '':
            print('q3')
            return 0
        else:
            return 4




def main_func(expInfo, save_path):
    # main function
    # Ensure that relative paths start from the same directory as this script
    _thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
    os.chdir(_thisDir)

    expName = u'feedback_ansl'

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename =save_path + os.sep + u'%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='', runtimeInfo=None,
      originPath=None,
      savePickle=True, saveWideText=True,
      dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)

    # create empty list to store data and help determine status of question
    list_1 = [''] * 9

    # create variable which ensures that the first run of the test has now questions marked as unanswered
    firsttrial = 0
    # create variable to check if question has been answered
    check = 0


    # while loop calls update function, then checks for missing values, then update trialstatus and call save func
    while check is not 4:
        temp_Dlg = update(list_1,firsttrial,check)
        temp_check = check
        print(str(temp_check)+'check')
        print(temp_Dlg)
        check = check_values(temp_Dlg[1], check)
        print(str(check)+'check')
        # compare check values before and after check function and assign either 1 or 0 tp trial number
        if temp_check == check:
            firsttrial=1
        else:
            firsttrial=0

        list_1 = temp_Dlg[1]
    # save values in csv
    savecsv(temp_Dlg[1],filename)


    thisExp.abort()  # or data files will save again on exit
