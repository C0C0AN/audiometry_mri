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



################################################################################
# functions for plotting
################################################################################


def get_stats(dataframe):
    """
    function to calculate statistics of data and write them to df

    takes dataframe created by 'extract_data' function as input
    """
    # groupby frequency and calculate mean volume etc.
    stats = dataframe.groupby('Frequency (Hz)')['Level (dBFS)'].describe().unstack()

    stats = pd.Series.to_frame(stats)
    stats = stats.unstack()
    stats = stats[0]

    freqs = []
    counts = []
    means = []
    sds = []
    mins_ = []
    maxs_ = []
    medians = []
    per25s = []
    per75s = []

    # write values for each frequency into lists
    for item in stats:
        freq = item
        count = stats[item].iloc[0]
        mean = stats[item].iloc[1]
        sd = stats[item].iloc[2]
        min_ = stats[item].iloc[3]
        max_ = stats[item].iloc[4]
        per25 = stats[item].iloc[5]
        median = stats[item].iloc[6]
        per75 = stats[item].iloc[7]
        freqs.append(item)
        means.append(mean)
        counts.append(count)
        sds.append(sd)
        mins_.append(min_)
        maxs_.append(max_)
        medians.append(median)
        per25s.append(per25)
        per75s.append(per75)


    df_mean= pd.DataFrame({'Frequency (Hz)': freqs, 'mean_dBFS': means,
                           'standard_deviation': sds, 'min': mins_,
                           'max': maxs_, 'median': medians,
                           '25%': per25s, '75%': per75s})



    return df_mean


def plot_mri_settings_scatter(df, path, subject):
    """
    function to group data by mri_settings and plot data

    returns data for each mri setting as dataframe and plot as linegraph
    inclding scatterplot
    """
    df_base = None
    df_tr1 = None
    df_tr2 = None
    df_t1w = None

    grouped = df.groupby('acquisition_scheme')

    for name, group in grouped:
        print(name)
#         print(group)

        if 'baseline'in name:
            df_base = pd.DataFrame(group)

            plt.figure()
            print(0)

            g = sns.FacetGrid(df_base,hue='order_volume', height=6, aspect=6,palette='BuGn')
            g.map(sns.lineplot, "Frequency (Hz)", "Level (dBFS)", alpha=1, linewidth=1)
            g.map(plt.scatter, "Frequency (Hz)", "Level (dBFS)", s=50, alpha=1, linewidth=1)
            plt.title('Baseline')
            g.add_legend()
            sns.despine()
            g.savefig(path+subject+'_baseline.png')

        elif 'epi_fast' in name:
            df_tr1 = pd.DataFrame(group)

            plt.figure()
            print(1)
            g = sns.FacetGrid(df_tr1,hue='order_volume', height=6, aspect=6,palette='Blues_d')
            g.map(sns.lineplot, "Frequency (Hz)", "Level (dBFS)", alpha=1, linewidth=1)
            g.map(plt.scatter, "Frequency (Hz)", "Level (dBFS)", s=50, alpha=1, linewidth=1)
            plt.title('epi_fast')
            g.add_legend()
            sns.despine()
            g.savefig(path+subject+'_epi_fast.png')

        elif 'epi_standard'in name:
            df_tr2 = pd.DataFrame(group)

            plt.figure()
            print(2)

            g = sns.FacetGrid(df_tr2,hue='order_volume', height=6, aspect=6,palette=("ch:2.5,-.2,dark=.3"))
            g.map(sns.lineplot, "Frequency (Hz)", "Level (dBFS)", alpha=1, linewidth=1)
            g.map(plt.scatter, "Frequency (Hz)", "Level (dBFS)", s=50, alpha=1, linewidth=1)
            plt.title('epi_standard')
            g.add_legend()
            sns.despine()
            #plt.show()
            g.savefig(path+subject+'_epi_standard.png')

        elif 'T1w' in name:
            df_t1w = pd.DataFrame(group)

            plt.figure()
            print(3)

            g = sns.FacetGrid(df_t1w,hue='order_volume', height=6, aspect=6,palette='RdGy')
            g.map(sns.lineplot, "Frequency (Hz)", "Level (dBFS)", alpha=1, linewidth=1)
            g.map(plt.scatter, "Frequency (Hz)", "Level (dBFS)", s=50, alpha=1, linewidth=1)
            plt.title('mprage')
            g.add_legend()
            sns.despine()
            g.savefig(path+subject+'_mprage.png')

    return df_base,df_tr1, df_tr2, df_t1w


def plot_overview_linegraph(df, path, subject):
    """ simple function to plot data

    show overview of data as linegraph including scatterplot
    """
    plt.figure(figsize=(50,15))
    sns.set_context('poster')
    sns.set_style('darkgrid')
    #sns.barplot(y = dfx['dBFS'], x = dfx['frequency'])
    sns.despine()
    sns.lineplot(y = df['Level (dBFS)'], x = df['Frequency (Hz)'],
                 hue = df['acquisition_scheme'], palette='colorblind', alpha = 1)


    #g = sns.FacetGrid(df, hue="acquisition_scheme", row='order_volume', palette='colorblind', height=5, aspect=6)
    #g.map(plt.scatter, "Frequency (Hz)", "Level (dBFS)", s=50, alpha=.7,
    #      linewidth=1, edgecolor="white")
    #g.map(sns.lineplot, "Frequency (Hz)", "Level (dBFS)", alpha=1,
    #      linewidth=1,palette='BuGn')
    #g.add_legend();

    #g = sns.FacetGrid(df, hue="acquisition_scheme", row='order_presentation', palette='colorblind', height=5, aspect=6)
    #g.map(plt.scatter, "Frequency (Hz)", "Level (dBFS)", s=50, alpha=.7,
    #      linewidth=1, edgecolor="white")
    #g.map(sns.lineplot, "Frequency (Hz)", "Level (dBFS)", alpha=1,
    #      linewidth=1,palette='BuGn')
    #g.add_legend();


    g = sns.FacetGrid(df, hue="acquisition_scheme", row='order_presentation', col='order_volume', palette='colorblind', height=5, aspect=6)
    g.map(plt.scatter, "Frequency (Hz)", "Level (dBFS)", s=50, alpha=.7,
          linewidth=1, edgecolor="white")
    g.map(sns.lineplot, "Frequency (Hz)", "Level (dBFS)", alpha=1,
          linewidth=1,palette='BuGn')
    g.add_legend();
    g.savefig(path+subject +'_overview_complete.png')


def get_audio_data(file):
    """
    function to extract and clean audio file

    returns dataframe including volume for each frequency
    in data
    """
    audio = pd.read_csv(file, sep='\t')
    audio = audio[audio["Frequency (Hz)"] < 8000]
    audio.rename(columns={'Level (dB)':'Level (dBFS)'}, inplace=True)

    return audio


def rename_columns(df):
    """
    function to rename columns to allow for easier plotting
    of mri  audio recordings compared to ansl output
    """
    df.rename(columns={'dBFS':'Level (dBFS)'}, inplace=True)
    df['Frequency (Hz)'].astype(float)
    return df


def plot_comparision(df1,df2):
    """
    function to plot volume per frequency for mri audio data
    and mean volume of frequency by ansl
    """
    g = sns.FacetGrid(df1, height=5, aspect=6,palette=("ch:2.5,-.2,dark=.3"),sharex=True,sharey=True)
    plt.xlim(0,-100)
    plt.xlim(0,8000)
    g.map(sns.lineplot, "Frequency (Hz)", "Level (dBFS)", alpha=1, linewidth=1)
    #g.map(plt.scatter, "Frequency (Hz)", "Level (dBFS)", s=50, alpha=1, linewidth=1)
    plt.title('t1_noise')
    plt.ylim(-100, 0)

    plt.xlim(0,10000)
    g.add_legend()
    sns.despine()



    g = sns.FacetGrid(df2,hue='order_volume', height=5, aspect=6)
    g.map(sns.lineplot, "Frequency (Hz)", "Level (dBFS)", alpha=1, linewidth=1)
    g.map(plt.scatter, "Frequency (Hz)", "Level (dBFS)", s=50, alpha=1, linewidth=1)
    plt.title('mpRage')
    g.add_legend()
    plt.ylim(-100, 0)

    plt.xlim(0,10000)
    sns.despine()


def alpha_scaling(df):
    """
    function to scale extracted volume in a range from 0 (lowest volume in data)
    and 1 (highest volume in data)

    returns scaled (scaled volume per frequency as df) and
    xyz_shape (dimensions of df)
    """
    xyz = (df['Level (dBFS)'])
    xyz = pd.DataFrame(xyz)
    xyz_shape = xyz.shape
    scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1), copy=True)
    scaled = scaler.fit(xyz)
    scaled = scaler.transform(xyz)
    scaled = scaled.reshape(xyz_shape[0])
    scaled.shape
    scaled = pd.DataFrame({'db_transformed':scaled})
    return scaled, xyz, xyz_shape

def draw_lines(dataframe, xyz_shape, position_lines, half_height):
    """
    function to draw lines to overlay over plot for each frequency in input data

    takes df, xyz_shape (dimensions of df), the position(from where to where the lines
    should be drawn, and half_height (if lines should be drawn over the complete plot
    or just half of it))

    returns coordinates for plotting
    """
    counter = 0
    coordinates = []
    lines = []

    for item in t1['Frequency (Hz)']:
        frequency_coordinates = tuple([t1['Frequency (Hz)'].iloc[counter],t1['Frequency (Hz)'].iloc[counter]])

        if half_height is True:
            line_coordinates = position_lines

        if half_height is False:
            line_coordinates = tuple([-100,0])

        coordinates.append(frequency_coordinates)
        lines.append(line_coordinates)
        counter +=1
    coordinates_array = np.array(coordinates)
    coordinates= pd.DataFrame({'x_coordinates': coordinates, 'y_coordinates': lines})

    x_coordinates = np.array(coordinates['x_coordinates'])
    x = x_coordinates.shape
    x[0]
    x_coordinates = x_coordinates.reshape(xyz_shape[0])

    y_coordinates = np.array(coordinates['y_coordinates'])
    y = y_coordinates.shape
    y[0]
    y_coordinates= y_coordinates.reshape(xyz_shape[0])
    return x_coordinates, y_coordinates, coordinates


def analyze_mri_noise(item, half_height):
    """
    function to analyze mri audio recording

    takes path to audio data as input and half_height(if lines should be
    drawn over the complete plot or just half of it))

    returns coordinates for plotting"""
    df = get_audio_data(item)
    scaled, xyz, xyz_shape = alpha_scaling(df)
    position_lines = tuple([-50,0])
    x_coordinates, y_coordinates, coordinates = draw_lines(df,xyz_shape, position_lines, half_height)

    return x_coordinates, y_coordinates, coordinates, scaled

def analyze_stimuli(item):
    """
    function to analyze data of stimuli recording

    takes path to audio data as input and half_height(if lines should be
    drawn over the complete plot or just half of it))

    returns coordinates for plotting"""
    stimuli = get_audio_data(item)
    scaled, xyz, xyz_shape = alpha_scaling(stimuli)
    position_lines = tuple([-100,-50])
    x_coordinates_stimuli, y_coordinates_stimuli, coordinates_stimuli = draw_lines(stimuli, xyz_shape,
                                                                                   position_lines,
                                                                                   half_height = True)
    return x_coordinates_stimuli, y_coordinates_stimuli, coordinates_stimuli, scaled



def alpha_scaling(df):
    """
    function to scale extracted volume in a range from 0 (lowest volume in data)
    and 1 (highest volume in data)

    returns scaled (scaled volume per frequency as df) and
    xyz_shape (dimensions of df)
    """
    xyz = (df['Level (dBFS)'])
    xyz = pd.DataFrame(xyz)
    xyz_shape = xyz.shape
    scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1), copy=True)
    scaled = scaler.fit(xyz)
    scaled = scaler.transform(xyz)
    scaled = scaled.reshape(xyz_shape[0])
    scaled.shape
    scaled = pd.DataFrame({'db_transformed':scaled})
    return scaled, xyz, xyz_shape

def draw_lines(dataframe, xyz_shape, position_lines, half_height):
    """
    function to draw lines to overlay over plot for each frequency in input data

    takes df, xyz_shape (dimensions of df), the position(from where to where the lines
    should be drawn, and half_height (if lines should be drawn over the complete plot
    or just half of it))

    returns coordinates for plotting
    """
    counter = 0
    coordinates = []
    lines = []

    for item in t1['Frequency (Hz)']:
        frequency_coordinates = tuple([t1['Frequency (Hz)'].iloc[counter],t1['Frequency (Hz)'].iloc[counter]])

        if half_height is True:
            line_coordinates = position_lines

        if half_height is False:
            line_coordinates = tuple([-100,0])

        coordinates.append(frequency_coordinates)
        lines.append(line_coordinates)
        counter +=1
    coordinates_array = np.array(coordinates)
    coordinates= pd.DataFrame({'x_coordinates': coordinates, 'y_coordinates': lines})

    x_coordinates = np.array(coordinates['x_coordinates'])
    x = x_coordinates.shape
    x[0]
    x_coordinates = x_coordinates.reshape(xyz_shape[0])

    y_coordinates = np.array(coordinates['y_coordinates'])
    y = y_coordinates.shape
    y[0]
    y_coordinates= y_coordinates.reshape(xyz_shape[0])
    return x_coordinates, y_coordinates, coordinates


def plot_mri_overlay(x_coordinates, y_coordinates, coordinates, df, scaled, outdir, subject, setting):
    """
    function to plot results of ansl (mean volume per frequency)
    overlayed with mri frequencies with their respective volumes
    represented by the transparency of the overlayed lines

    takes coorinates of 'analyze_mri_noise' as input
    """
    sns.set_style('whitegrid')
    sns.set_context("poster")
    plt.figure(figsize=(30,10))
    plt.xlim(0,8050)
    plt.ylim(-100, 0)

    counter = 0
    for i in x_coordinates:
        plt.plot(x_coordinates[counter],y_coordinates[counter], 'k-', color="lightsteelblue",
                 alpha=scaled['db_transformed'].iloc[counter])
        counter +=1
    mean = get_stats(df)
    sns.lineplot((df["Frequency (Hz)"]), (df["Level (dBFS)"]), alpha=1, linewidth=1, color='r')
    plt.scatter(mean["Frequency (Hz)"], mean["mean_dBFS"], s=50, alpha=1, linewidth=1,color='r',zorder=5)
    plt.title(setting)
    plt.savefig(outdir+subject+'_'+setting+'_mri_noise_overlay.png')



#x_coordinates_stimuli, y_coordinates_stimuli, coordinates_stimuli, scaled_stimuli = analyse_stimuli('/home/michael/Documents/metal_spectrum_4000.txt')

def plot_mri_stimuli_comparision(x_coordinates, y_coordinates, coordinates, scaled,
                                 x_coordinates_stimuli, y_coordinates_stimuli,
                                 coordinates_stimuli, scaled_stimuli, df):
    """
    function to plot results of ansl (mean volume per frequency)
    overlayed with mri frequencies and stimuli frequencies with their respective volumes
    represented by the transparency of the overlayed lines

    takes coorinates of 'analyze_mri_noise' as input
    """
    sns.set_style('whitegrid')
    sns.set_context("poster")
    plt.figure(figsize=(20,6))
    plt.xlim(0,8050)
    plt.ylim(-100, 0)

    counter = 0
    for i in x_coordinates:
        plt.plot(x_coordinates[counter],y_coordinates[counter], 'k-', color="steelblue",
                 alpha=scaled['db_transformed'].iloc[counter])
        counter +=1

    counter = 0

    for i in x_coordinates_stimuli:
        plt.plot(x_coordinates_stimuli[counter],y_coordinates_stimuli[counter], 'k-', color="darkgreen",
                 alpha=scaled_stimuli['db_transformed'].iloc[counter])
        counter +=1

    mean = get_stats(df)
    sns.lineplot((df["Frequency (Hz)"]), (df["Level (dBFS)"]),
                 alpha=1, linewidth=1, color='firebrick')
    plt.scatter(mean["Frequency (Hz)"], mean["mean_dBFS"],
                s=50, alpha=1, linewidth=1,color='firebrick',zorder=5)

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
