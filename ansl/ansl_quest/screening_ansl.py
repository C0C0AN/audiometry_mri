"""created by Michael Ernst (https://github.com/M-earnest)

screening questionnaire for ansl pilot
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
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import pandas as pd


def update(list_,list_1,list_2,list_3,firsttrial,check):
# function to display Dialogue
    # assign gui to variable and define title

    if check ==0:
        myDlg = gui.Dlg(title="Screening-Fragebogen")
        myDlg.addText('\nSubject info')
        myDlg.addField(u'Haendigkeit(eigene Einschaetzung):',choices=['R','L'],initial=list_[0])
        myDlg.addField('Geschlecht:',choices=['male','female','other'],initial=list_[1])

        # check if questions are unanswered - or define other condition
        if not list_[2] == '' or firsttrial==0:
            # when string not empty or first run - assign answer to question, if already provided
            myDlg.addField('Alter:',initial=list_[2])
            # mark question red, if second run and question unanswered
        else:
            myDlg.addField('Alter:',initial=list_[2], color='red')

        if not list_[3] == ''or firsttrial==0:
            myDlg.addField('Geburtsdatum:',initial=list_[3])
        else:
            myDlg.addField('Geburtsdatum:',initial=list_[3],color='red')

        if not list_[4] == ''or firsttrial==0:
            myDlg.addField('Schulabschluss:',initial=list_[4])
        else:
            myDlg.addField('Schulabschluss:',initial=list_[4],color='red')


        # show content in output and return data to main func
        myDlg.show()
        myDlg = myDlg.data
        return myDlg,list_1,list_2,list_3

    #gUI_1
    #added and list_1[] == '' in red condition --> resolved
    #inserr #nein# in first string to test if it resolves the problem of repeating the selected answer without a following empty field

    elif check ==1:
        print(firsttrial)
        myDlg1 = gui.Dlg(title="Screening-Fragebogen")
        myDlg1.addText(u'\nKrankheitsgeschichte')
        myDlg1.addField('Diabetes:', choices=['J','N'],initial=list_1[0])
        myDlg1.addField(u'erhoehter Blutdruck:', choices=['J','N'],initial=list_1[1])



        myDlg1.addField('Herzinfarkt:',choices= ['J','N'],initial=list_1[2])
        if list_1[2] == '' or firsttrial==0:
            myDlg1.addField(u'Alter bei Herzinfarkt?:',initial=list_1[3])
        elif list_1[2] == 'J' and list_1[3] == '' and firsttrial==1:
            myDlg1.addField('Alter bei Herzinfarkt?:',initial=list_1[3], color='red')
        elif list_1[2] == 'N'  and firsttrial==1:
            myDlg1.addField('Alter bei Herzinfarkt?:',initial=list_1[3])
        elif list_1[2] == 'J' and not list_1[3]=='' and firsttrial==1:
            myDlg1.addField('Alter bei Herzinfarkt?:',initial=list_1[3])


        myDlg1.addField('Gicht:', choices=['J','N'],initial=list_1[4])
        myDlg1.addField('Asthma:', choices=['J','N'],initial=list_1[5])
        myDlg1.addField('Gallen/Nierensteine:',choices=['J','N'],initial=list_1[6])

        myDlg1.addField('Krebsleiden:',choices= ['J','N'],initial=list_1[7])
        if list_1[7] == '' and firsttrial==0:
            myDlg1.addField('Krebs: betroffenes Organ?:',initial=list_1[8])
        elif list_1[7] == 'J'  and list_1[8] == '' and firsttrial==1:
            myDlg1.addField('Krebs: betroffenes Organ?:',initial=list_1[8], color='red')
        elif list_1[7] == 'N'  and firsttrial==1:
            myDlg1.addField('Krebs: betroffenes Organ?:',initial=list_1[8])
        elif list_1[7] == 'J'  and not list_1[8] == ''and firsttrial==1:
            myDlg1.addField('Krebs: betroffenes Organ?:',initial=list_1[8])


        myDlg1.addField('Alzheimer:', choices=['J','N'],initial=list_1[9])



        myDlg1.addField('Allergien:',choices= ['J','N'],initial=list_1[10])
        if list_1[10] == '' and firsttrial==0:
            myDlg1.addField('Worauf reagieren Sie allergisch?:',initial=list_1[11])
        elif list_1[10] == 'J'  and list_1[11] == '' and firsttrial==1:
            myDlg1.addField('Worauf reagieren Sie allergisch?',initial=list_1[11], color='red')
        elif list_1[10] == 'N'  and firsttrial==1:
            myDlg1.addField('Worauf reagieren Sie allergisch?',initial=list_1[11])
        elif list_1[10] == 'J'  and not list_1[11] == '' and firsttrial==1:
            myDlg1.addField('Worauf reagieren Sie allergisch?:',initial=list_1[11])



        myDlg1.addField('psychische Erkrankungen\n(z.B. Depressionen, Schizophrenie):',choices= ['J','N'],initial=list_1[12])
        if list_1[12] == '' or firsttrial==0:
            myDlg1.addField('psychische Erkankungen - bitte erlaeutern Sie naeher:',initial=list_1[13])
        elif list_1[12] == 'J' and list_1[13] == ''  and firsttrial==1:
                myDlg1.addField('psychische Erkankungen - bitte erlaeutern Sie naeher:',initial=list_1[13], color='red')
        elif list_1[12] == 'N'  and firsttrial==1:
            myDlg1.addField('psychische Erkankungen  - bitte erlaeutern Sie naeher:',initial=list_1[13])
        elif list_1[12] == 'J' and not list_1[13] == ''  and firsttrial==1:
            myDlg1.addField('psychische Erkankungen - bitte erlaeutern Sie naeher:',initial=list_1[13])



        myDlg1.addField('Sprachstoerungen:',choices= ['J','N'],initial=list_1[14])
        if list_1[14] == '' or firsttrial==0:
            myDlg1.addField('Sprachstoerungen - bitte erlaeutern Sie naeher:',initial=list_1[15])
        elif list_1[14] == 'J' and list_1[15] == ''  and firsttrial==1:
            myDlg1.addField('Sprachstoerungen - bitte erlaeutern Sie naeher:',initial=list_1[15], color='red')
        elif list_1[14] == 'N'  and firsttrial==1:
            myDlg1.addField('Sprachstoerungen  - bitte erlaeutern Sie naeher:',initial=list_1[15])
        elif list_1[14] == 'J' and not list_1[15] == ''  and firsttrial==1:
            myDlg1.addField('Sprachstoerungen - bitte erlaeutern Sie naeher:',initial=list_1[15])


        myDlg1.addField('Gehoerstoerungen:',choices= ['J','N'],initial=list_1[16])
        if list_1[16] == '' or firsttrial==0:
            myDlg1.addField('Gehoerstoerungen - bitte erlaeutern Sie naeher:',initial=list_1[17])
        elif list_1[16] == 'J' and list_1[17] == ''and firsttrial==1:
            myDlg1.addField('Gehoerstoerungen - bitte erlaeutern Sie naeher:',initial=list_1[17], color='red')
        elif list_1[16] == 'N'  and firsttrial==1:
            myDlg1.addField('Gehoerstoerungen - bitte erlaeutern Sie naeher:',initial=list_1[17])
        elif list_1[16] == 'J' and not list_1[17] == ''  and firsttrial==1:
            myDlg1.addField('Gehoerstoerungen - bitte erlaeutern Sie naeher:',initial=list_1[17])

        myDlg1.addField(u'Legasthenie(Lese-Rechtschreibstoerung):', choices=['J','N'],initial=list_1[18])

        myDlg1.addField('genetische Erkrankungen:',choices= ['J','N'],initial=list_1[19])
        if list_1[19] == '' or firsttrial==0:
            myDlg1.addField('genetische Erkrankungen - bitte erlaeutern Sie naeher:',initial=list_1[20])
        elif list_1[19] == 'N'  and firsttrial==1:
            myDlg1.addField('genetische Erkrankungen  - bitte erlaeutern Sie naeher:',initial=list_1[20])
        elif list_1[19] == 'J' and list_1[20] == '' and firsttrial==1:
            myDlg1.addField('genetische Erkrankungen - bitte erlaeutern Sie naeher:',initial=list_1[20], color='red')
        elif list_1[19] == 'J' and not list_1[20] == ''  and firsttrial==1:
            myDlg1.addField('genetische Erkrankungen - bitte erlaeutern Sie naeher:',initial=list_1[20])


        myDlg1.show()
        myDlg1 = myDlg1.data
        return list_,myDlg1,list_2,list_3

    #GUI

    elif check ==2:
        myDlg2= gui.Dlg(title=u'Screening-Fragebogen - Krankheitsgeschichte')

        myDlg2.addText('\nHatten oder haben Sie eine der folgenden Erkrankungen?')
        myDlg2.addText('Kinderkrankheiten')
        myDlg2.addField(u'Roeteln:', choices=['J','N'], initial=list_2[0])


        myDlg2.addField('Keuchhusten:', choices=['J','N'], initial=list_2[1])
        myDlg2.addField('Windpocken:', choices=['J','N'], initial=list_2[2])
        myDlg2.addField('Mumps:', choices=['J','N'], initial=list_2[3])
        myDlg2.addField('Masern:', choices=['J','N'], initial=list_2[4])
        myDlg2.addField(u'Pfeiffersches Druesenfieber:', choices=['J','N'], initial=list_2[5])
        myDlg2.addField('sonstige:',choices=['J','N'], initial=list_2[6])
        if list_2[6] == '' or firsttrial==0:
            myDlg2.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_2[7])
        elif list_2[6] == 'J' and list_2[7] == '' and firsttrial==1:
            myDlg2.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_2[7],color='red')
        elif list_2[6] == 'N'  and firsttrial==1:
            myDlg2.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_2[7])
        elif list_2[6] == 'J' and not list_2[7]=='' and firsttrial==1:
            myDlg2.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_2[7])

        myDlg2.addText(u'\nHerz- und Gefaesserkrankungen')
        myDlg2.addField('Thrombosen:', choices=['J','N'], initial=list_2[8])
        myDlg2.addField('Schlaganfall:', choices=['J','N'], initial=list_2[9])
        myDlg2.addField('Krampfadern:', choices=['J','N'], initial=list_2[10])
        myDlg2.addField(u'Durchblutungsstoerungen:', choices=['J','N'], initial=list_2[11])
        myDlg2.addField('sonstige:',choices=['J','N'], initial=list_2[12])
        if list_2[12] == '' or firsttrial==0:
            myDlg2.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_2[13])
        elif list_2[12] == 'J' and list_2[13] == '' and firsttrial==1:
            myDlg2.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_2[13],color='red')
        elif list_2[12] == 'N'  and firsttrial==1:
            myDlg2.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_2[13])
        elif list_2[12] == 'J' and not list_2[13]=='' and firsttrial==1:
            myDlg2.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_2[13])

        myDlg2.show()
        myDlg2 = myDlg2.data
        return list_,list_1,myDlg2,list_3

    ###gui
    elif check ==3:
        myDlg3 = gui.Dlg(title=u'Screening-Fragebogen - Krankheitsgeschichte')
        myDlg3.addText('\nStoffwechselerkrankungen')
        myDlg3.addField(u'Schilddruesenerkrankungen:', choices=['J','N'],initial=list_3[0])


        myDlg3.addField('sonstige:',choices=['J','N'], initial=list_3[1])
        if list_3[1] == '' or firsttrial==0:
            myDlg3.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_3[2])
        elif list_3[1] == 'J' and list_3[2] == '' and firsttrial==1:
            myDlg3.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_3[2],color='red')
        elif list_3[1] == 'N'  and firsttrial==1:
            myDlg3.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_3[2])
        elif list_3[1] == 'J' and not list_3[2]=='' and firsttrial==1:
            myDlg3.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_3[2])

        myDlg3.addText('\nsonstige Fragen')
        myDlg3.addField('Tragen Sie eine Brille oder Kontaktlinsen?',choices= ['J','N'],initial=list_3[3])
        if list_3[3] == '' or firsttrial==0:
            myDlg3.addField('Brille oder Kontaktlinsen: Dioptrie?',initial=list_3[4])
        elif list_3[3] == 'J' and list_3[4] == '' and firsttrial==1:
            myDlg3.addField('Brille oder Kontaktlinsen: Dioptrie?',initial=list_3[4],color='red')
        elif list_3[3] == 'N'  and firsttrial==1:
            myDlg3.addField('Brille oder Kontaktlinsen: Dioptrie?',initial=list_3[4])
        elif list_3[3] == 'J' and not list_3[4]=='' and firsttrial==1:
            myDlg3.addField('Brille oder Kontaktlinsen: Dioptrie?',initial=list_3[4])


        myDlg3.addField(u'Haben Sie einmal wegen persoenlicher oder psychischer Probleme\n einen Sozialarbeiter, Psychologen oder Psychiater aufgesucht?:',choices= ['J','N'],initial=list_3[5])
        if list_3[5] == '' or firsttrial==0:
            myDlg3.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_3[6])
        elif list_3[5] == 'J' and list_3[6] == '' and firsttrial==1:
            myDlg3.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_3[6],color='red')
        elif list_3[5] == 'N'  and firsttrial==1:
            myDlg3.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_3[6])
        elif list_3[5] == 'J' and not list_3[6]=='' and firsttrial==1:
            myDlg3.addField(u'wenn Ja: bitte erlaeutern Sie:',initial=list_3[6])

        myDlg3.addField('Rauchen Sie?', choices=['J','N'],initial=list_3[7])
        if list_3[7] == '' or firsttrial==0:
            myDlg3.addField(u'wenn Ja: Wie viel rauchen Sie an einem Tag?:',initial=list_3[8])
        elif list_3[7] == 'J' and list_3[8] == '' and firsttrial==1:
            myDlg3.addField(u'wenn Ja: Wie viel rauchen Sie an einem Tag?:',initial=list_3[8],color='red')
        elif list_3[7] == 'N'  and firsttrial==1:
            myDlg3.addField(u'wenn Ja: Wie viel rauchen Sie an einem Tag?:',initial=list_3[8])
        elif list_3[7] == 'J' and not list_3[8]=='' and firsttrial==1:
            myDlg3.addField(u'wenn Ja: Wie viel rauchen Sie an einem Tag?:',initial=list_3[8])

        myDlg3.addField('Haben Sie Geschwister?:', choices=['J','N'],initial=list_3[9])
        myDlg3.addField('Haben Sie eine Zwillingsschwester bzw. einen Zwillingsbruder:', choices=['J','N'],initial=list_3[10])
        myDlg3.addField(u'Litten oder Leiden Sie unter neurologischen Erkrankungen(z.B. Migraene)?:', choices=['J','N'],initial=list_3[11])
        if list_3[11] == '' or firsttrial==0:
            myDlg3.addField(u'wenn Ja: bitte spezifizieren Sie:',initial=list_3[12])
        elif list_3[11] == 'J' and list_3[12] == '' and firsttrial==1:
            myDlg3.addField(u'wenn Ja: bitte spezifizieren Sie:',initial=list_3[12],color='red')
        elif list_3[11] == 'N'  and firsttrial==1:
            myDlg3.addField(u'wenn Ja: bitte spezifizieren Sie:',initial=list_3[12])
        elif list_3[11] == 'J' and not list_3[12]=='' and firsttrial==1:
            myDlg3.addField(u'wenn Ja: bitte spezifizieren Sie:',initial=list_3[12])


        myDlg3.addField(u'Nehmen Sie regelmaessig Medikamente ein? :', choices=['J','N'],initial=list_3[13])
        if list_3[13] == '' or firsttrial==0:
            myDlg3.addField(u'wenn Ja: Welche Medikamente nehmen Sie zur Zeit?:',initial=list_3[14])
        elif list_3[13] == 'J' and list_3[14] == '' and firsttrial==1:
            myDlg3.addField(u'wenn Ja: Welche Medikamente nehmen Sie zur Zeit?:',initial=list_3[14],color='red')
        elif list_3[13] == 'N'  and firsttrial==1:
            myDlg3.addField(u'wenn Ja: Welche Medikamente nehmen Sie zur Zeit?:',initial=list_3[14])
        elif list_3[13] == 'J' and not list_3[14]=='' and firsttrial==1:
            myDlg3.addField(u'wenn Ja: Welche Medikamente nehmen Sie zur Zeit?:',initial=list_3[14])
        myDlg3.addField(u'Fuer Frauen: Nehmen Sie die Pille?:', choices=['J','N'])


        myDlg3.show()
        myDlg3 = myDlg3.data
        return list_,list_1,list_2,myDlg3



def savecvs(list_,list_1,list_2,list_3,filename, num_items,num_items_1,num_items_2,num_items_3):
  # function to add data to experiment handler and save as csv
  # add column + data

    keys = [''] * num_items
    keys1 = ['']*num_items_1
    keys2 = ['']*num_items_2
    keys3 = ['']*num_items_3

    keys[0] = 'Haendigkeit'
    keys[1] = 'Geschlecht'
    keys[2] = 'Alter'
    keys[3] = 'Geburtsdatum'
    keys[4] = 'Schulabschluss'


    keys1[0] = 'Diabetes'
    keys1[1] = 'Blutdruck'
    keys1[2] = 'Herzinfarkt'
    keys1[3] = 'Alter Herzinfarkt'
    keys1[4] = 'Gicht'
    keys1[5] = 'Asthma'
    keys1[6] = 'Gallen/Nierensteine'
    keys1[7] = 'Krebs'
    keys1[8] = 'krebsbefallenes organ'
    keys1[9] = 'Alzheimer'
    keys1[10] = 'Allergien'
    keys1[11] = 'Allergien spezifisch'
    keys1[12] = 'psych Erkrankungen'
    keys1[13] = 'psych Erkrankungen spezifisch'
    keys1[14] = 'Sprachstoerungen'
    keys1[15] = 'Sprachstoerungen spezifisch'
    keys1[16] = 'Gehoerstoerungen'
    keys1[17] = 'Gehoerstoerungen spezifisch'
    keys1[18] = 'Legasthenie'
    keys1[19] = 'genetische Erkrankungen'
    keys1[20] = 'gen Erkankrungen spezifisch'

    keys2[0] = 'roeteln'
    keys2[1] = 'keuchhusten'
    keys2[2] = 'windpocken'
    keys2[3] = 'mumps'
    keys2[4] = 'masern'
    keys2[5] = 'pfeiffersches druesenfieber'
    keys2[6] = 'sosntige kinderkrankheiten'
    keys2[7] = 'sosntige kinderkrankheiten spezifisch'
    keys2[8] = 'thrombosen'
    keys2[9] = 'schlaganfall'
    keys2[10] = 'krampfadern'
    keys2[11] = 'durchblutungsstoerungen'
    keys2[12] = 'sonstige Herz-kreislauf'
    keys2[13] = 'sonstige herz-kreislauf spezifisch'


    keys3[0] = 'Schilddruesenerkrankungen'
    keys3[1] = 'sonstige stoffwechselerkrankungen'
    keys3[2] = 'sonstige stoffwechselerkrankungen spezifisch'
    keys3[3] = 'Sehhilfe'
    keys3[4] = 'Dioptrie'
    keys3[5] = 'psychiatrisch/psychologische beratung'
    keys3[6] = 'psychiatrische/psychologische beratung spezifisch'
    keys3[7] = 'raucher'
    keys3[8] = 'menge zigaretten/tag'
    keys3[9] = 'geschwister'
    keys3[10] ='zwillingsgeschwister'
    keys3[11] = 'neurologische erkrankungen'
    keys3[12] = 'neurologische erkrankungen spezifisch'
    keys3[13] = 'medikamente'
    keys3[14] = 'medikamente spezifisch'
    keys3[15] = 'verhuetung pille'



    file_open = open(filename + '.csv','w')
    for i in range(num_items):
        file_open.write(keys[i]+',')
    for i in range(num_items_1):
        file_open.write(keys1[i]+',')
    for i in range(num_items_2):
        file_open.write(keys2[i]+',')
    for i in range(num_items_3):
        if i == num_items_3-1:
            file_open.write(keys3[i])
        else:
            file_open.write(keys3[i]+',')
    file_open.write('\n')


    for i in range(len(list_)):
        list_[i] = list_[i].replace(',',':')
        file_open.write(list_[i]+',')

    for i in range(len(list_1)):
        list_1[i] = list_1[i].replace(',',':')
        file_open.write(list_1[i]+',')

    for i in range(len(list_2)):
        list_2[i] = list_2[i].replace(',',':')
        file_open.write(list_2[i]+',')

    for i in range(len(list_3)):
        list_3[i] = list_3[i].replace(',',':')
        file_open.write(list_3[i]+',')

    file_open.close()

def check_values(list_,list_1,list_2,list_3,check):

    if check ==0:
        if list_[2] == '' or list_[2] == 'J':
            return 0
        elif list_[3] == ''or list_[3] == 'J':
            return 0
        elif list_[4] == ''or list_[4] == 'J':
            return 0
        else:
            return 1


    elif check==1:
        if list_1[2] == 'J' and  list_1[3] == '':
            return 1
        elif list_1[7] == 'J' and list_1[8] == '':
            return 1
        elif list_1[10] == 'J' and list_1[11] == '':
            return 1
        elif list_1[12] == 'J ' and list_1[13] == '':
            return 1
        elif list_1[14] == 'J' and list_1[15]== '':
            return 1
        elif list_1[16] == 'J' and list_1[17]== '':
            return 1
        elif list_1[19] == 'J' and list_1[20]== '':
            return 1
        else:
            return 2

    elif check==2:
        if list_2[6] == 'J' and list_2[7] == '':
            return 2
        if list_2[12] == 'J' and list_2[13] == '':
            return 2
        else:
            return 3

    elif check==3:
        if list_3[1] == 'J' and  list_3[2] == '':
            return 3
        elif list_3[3] == 'J' and list_3[4] == '':
            return 3
        elif list_3[5] == 'J' and list_3[6] == '':
            return 3
        elif list_3[7] == 'J ' and list_3[8] == '':
            return 3
        elif list_3[11] == 'J' and list_3[12]== '':
            return 3
        elif list_3[13] == 'J' and list_3[14]== '':
            return 3


        else:
            return 4



def main_func(expInfo,save_path):
  # main function
# Ensure that relative paths start from the same directory as this script
    _thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
    os.chdir(_thisDir)

    # Store info about the experiment session
    expName = u'Screening_demographisch' # from the Builder filename that created this script

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename =save_path + os.sep + u'%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='', runtimeInfo=None,
      originPath=None,
      savePickle=True, saveWideText=True,
      dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file


    # create empty list to store data and help determine status of question
    num_items = 5
    list_ = [''] * num_items
    print list_

    num_items_1 = 21
    list_1 = [''] * num_items_1
    print list_1

    num_items_2 = 14
    list_2 = [''] * num_items_2
    print list_2

    num_items_3 = 16
    list_3 = [''] * num_items_3
    print list_3


    # create variable which ensures that the first run of the test has now questions marked as unanswered
    firsttrial=0
    # create variable to check if question has been answered
    check = 0

    temp_Dlg = []
    # while loop calls update function, then checks for missing values, then update trialstatus and call save func
    while check <4:
        temp_Dlg = update (list_,list_1,list_2,list_3,firsttrial,check)
        temp_check = check
        print(temp_check)
        check = check_values(temp_Dlg[0],temp_Dlg[1],temp_Dlg[2],temp_Dlg[3],check)
        print(check)
        # compare check values before and after check function and assign either 1 or 0 tp trial number
        if temp_check == check:
            firsttrial=1
        else:
            firsttrial=0
        list_ = temp_Dlg[0]
        list_1= temp_Dlg[1]
        list_2= temp_Dlg[2]
        list_3= temp_Dlg[3]


    # save values in csv
    savecvs(list_,list_1,list_2,list_3,filename, num_items, num_items_1, num_items_2, num_items_3)


    thisExp.abort()  # or data files will save again on exit
