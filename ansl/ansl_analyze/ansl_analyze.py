import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from matplotlib.lines import Line2D
import scipy
import random
import os
import glob
import sklearn
from sklearn.preprocessing import MinMaxScaler
from __future__ import division #so 1/2 = 0.5, not 1/2=0

import pandas as pd

def extract_ansl_data(file, outpath):
    """ function to extract data from ansl output csv

    takes path to directory as input"""
    # necessary lists for data extraction
    conditions = []
    items = []
    volumes = []
    frequencies = []
    orders = []
    settings = []
    subjects = []

    for filename in glob.iglob(file): # all specified files in directory
        df = pd.read_csv(filename)

        for i in df.columns:
            for item in df[i]:

                # get subject info
                subject = filename.split('/')
                subject = subject[6]
                subject = subject[:5]
                subjects.append(subject)


                item= item.split('/')
                item= item[2]
                items.append(item)

                # get info on setting
                setting = filename.split('/')
                if 'baseline' in filename:
                    settings.append('baseline')
                elif 'epi_fast(TR1s)' in filename:
                    settings.append('epi_fast(TR1s)')
                elif 'epi_standard(TR2s)' in filename:
                    settings.append('epi_standard(TR2s)')
                else:
                    settings.append('structural(T1w)')

                # get info on stimuli order
                if 'order1' in i:
                    orders.append('1')
                elif 'order2' in i:
                    orders.append('2')

                # get info on volume condition
                if 'decrease' in i:
                    conditions.append('decrease')
                elif 'increase' in i:
                    conditions.append('increase')

                # extract discovered volume
                if '10dBFS' in item:
                    volumes.append(-10)
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
                elif 'not_discovered' in item:
                    volumes.append('0')

                if '150hz' in item:
                    frequencies.append(150)
                elif '250hz' in item:
                    frequencies.append(250)
                elif '500hz' in item:
                    frequencies.append(500)
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

    # write to dataframe
    df= pd.DataFrame({'subject': subjects,
                       'setting': settings,
                       'condition': conditions,
                       'order': orders,
                       'item' : items,
                       'Level (dBFS)' : volumes,
                       'Frequency (Hz)': frequencies})

    df.to_csv(opj(path, 'ansl_output.csv'), index=False)

    return df


def convert_ansl_data_dbfs(file, outpath):

    df = pd.read_csv(file)

    df_dBFS = df.groupby(['subject','setting','condition','order','Frequency (Hz)']).aggregate('mean')

    df_dBFS = df_dBFS.unstack()
    df_dBFS = df_dBFS['Level (dBFS)']

    df_dBFS.to_csv(opj(path, 'ansl_output_dbfs.csv'), index=False)

    return df_dBFS


def group_ansl_data_dbfs(file, outpath):


    grouped = df.groupby('condition')

    for name, group in grouped:
        if name == 'increase':
            df_increase = pd.DataFrame(group)
        else:
            df_decrease = pd.DataFrame(group)

    df_increase.to_csv(opj(path, 'ansl_output_dbfs_increase.csv'), index=False)
    df_decrease.to_csv(opj(path, 'ansl_output_dbfs_increase.csv'), index=False)

    return df_increase, df_decrease


def get_stats(file, outpath):
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

    df_mean.to_csv(opj(path, 'ansl_output_dbfs_mean.csv'), index=False)


    return df_mean
