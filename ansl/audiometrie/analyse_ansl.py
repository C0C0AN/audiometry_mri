# import necessary dependencies
# %matplotlib inline
from __future__ import division #so 1/2 = 0.5, not 1/2=0

import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import scipy
import random
import os
import errno  # handy system and path functions
import sys  # to get file system encoding
import glob
import sklearn
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import seaborn as sns

###############################################################################
# main function to plot ansl results
###############################################################################
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(
            sys.getfilesystemencoding())
t1 = get_audio_data(_thisDir+'/plotting/t1w_spectrum.txt')
t2_tr1 = get_audio_data(_thisDir+'/plotting/t2_tr1_spectrum.txt')
t2_tr2 = get_audio_data(_thisDir+'/plotting/t2_tr2_spectrum.txt')

def main_func(_thisDir, expInfo):
    """
    function called in ansl.py, iterates over all files in subject directory
    and outputs different graphs containing results of ansl-experiment
    """
    print('####### starting analysis #########')

    #  get all tsv files in subject directory
    directory = _thisDir + '/data/'+expInfo['participant'] +'/*.tsv'
    os.chdir(_thisDir + '/data/'+expInfo['participant'] + '/')

    # create png directory to store plots in
    try:
        os.makedirs('pngs/')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    #  define directory to save plots in
    outdir = _thisDir + '/data/'+expInfo['participant'] + '/pngs/'
    #  get subject name
    subject = expInfo['participant']

    # create a counter to keep track of which loop-iteration we're in
    counter = 0

    #  iterate over all files in subject directory, exclude the ones we're not
    #  interested in
    for idx, filename in enumerate(glob.glob(directory)):
        if 'trial_start' in filename:
            #print('skipped')
            continue
        elif 'stimuli_onset' in filename:
            #print('skipped')
            continue
        elif '.json' in filename:
            #print('skipped')
            continue
        elif '.html' in filename:
            #print('skipped')
            continue
        elif '.png' in filename:
            #print('skipped')
            continue
        elif 'stats' in filename:
            #print('skipped')
            continue
        elif 'appended' in filename:
            #print('skipped')
            continue
        else:
            #  if we're at the first iteration of loop read Data into DataFrame
            if counter == 0:
                df = pd.read_csv(filename, sep='\t',
                                 encoding="utf8", engine='python')
            #  if we're in a sucessive loop read Data and append to DataFrame
            elif counter > 0:
                df2 = pd.read_csv(filename, sep='\t',
                                  encoding="utf8", engine='python')
                df = df.append(df2, ignore_index=True)
            counter += 1 # update counter

    #  get a overview of results
    plot_overview_linegraph(df, outdir, subject)

    #  divide DataFrame by acquisition_scheme
    df_base,df_tr1, df_tr2, df_t1w = plot_mri_settings_scatter(df, outdir, subject)

    #  if "epi fast" acquisition_scheme was in DataFrame plot results compared to
    #  frequency spectrum of acoustic scanner noise of specific acquisition_scheme
    if df_tr1 is not None:
        df_tr1 = rename_columns(df_tr1)
        df_tr1_mean = get_stats(df_tr1)

        x_coordinates, y_coordinates, coordinates, scaled = analyze_mri_noise(_thisDir+'/plotting/t2_tr1_spectrum.txt',
                                                                             half_height =False)
        plot_mri_overlay(x_coordinates, y_coordinates, coordinates, df_tr1, scaled, outdir, subject, setting='epi_fast(tr1)')

    #  if "epi_standard" acquisition_scheme was in DataFrame plot results compared to
    #  frequency spectrum of acoustic scanner noise of specific acquisition_scheme
    if df_tr2 is not None:
        df_tr2 = rename_columns(df_tr2)
        df_tr2_mean = get_stats(df_tr2)

        x_coordinates, y_coordinates, coordinates, scaled = analyze_mri_noise(_thisDir+'/plotting/t2_tr2_spectrum.txt',
                                                                             half_height =False)
        plot_mri_overlay(x_coordinates, y_coordinates, coordinates, df_tr2,scaled, outdir, subject, setting='epi_standard(tr2)')

    #  if "mprage" acquisition_scheme was in DataFrame plot results compared to
    #  frequency spectrum of acoustic scanner noise of specific acquisition_scheme
    if df_t1w is not None:
        df_t1w  = rename_columns(df_t1w)
        df_t1w_mean = get_stats(df_t1w)
        x_coordinates, y_coordinates, coordinates, scaled = analyze_mri_noise(_thisDir+'/plotting/t1w_spectrum.txt',
                                                                             half_height =False)
        plot_mri_overlay(x_coordinates, y_coordinates, coordinates, df_t1w,scaled, outdir, subject, setting='mprage(T1w)')

    html_name = outdir+subject+'.html'
    htmlFile = open(outdir+subject+'.html','w')

    message = """<html>
    <head><strong><font face = "helvetica" size = "19"><center>
    Aint no sound loud enough!</center></font></strong></head>
    <body>
    <p>
    <br><br>
    <font face = "helvetica" size = "17">Overview for subject</font>
    <br><br>
    <img src="outdir_overview_complete.png" alt="overview" height="400" width="2300">
    <br><br>
    <img src="outdir_mprage.png" alt="Lineplot-placeholder" height="400" width="2300">
    <br><br>
    <img src="outdir_baseline.png" alt="Lineplot-placeholder" height="400" width="2300">
    <br><br>
    <img src="outdir_epi_fast.png" alt="Lineplot-placeholder height="400" width="2300">
    <br><br>
    <img src="outdir_epi_standard.png" alt="Lineplot-placeholder"height="400" width="2300">
    <br><br>
    <br><br>
    <font face = "helvetica" size = "17"><center>
    Mri-noise vs. stimuli
    </center></font>
    <br><br>
    <img src="outdir_mprage(t1w)mri_noise_overlay.png" alt="Lineplot-placeholder" height="700" width="2300">
    <br><br>
    <img src="outdir_epi_fast(tr1)mri_noise_overlay.png" alt="Lineplot-placeholder" height="700" width="2300">
    <br><br>
    <img src="outdir_epi_standard(tr2)mri_noise_overlay.png" alt="Lineplot-placeholder" height="700" width="2300">
    <br><br>
    </p></body></html>"""

    htmlFile.write(message)
    htmlFile.close()

    with open(html_name) as html:
        text = html.read().replace('subject', subject)
        text2 = text.replace('outdir', outdir+subject)

    with open(html_name, "w") as html:
        html.write(text2)
