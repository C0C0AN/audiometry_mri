import pandas as pd
import seaborn as sns
import numpy as np

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

    g = sns.FacetGrid(df, hue="acquisition_scheme", row='order_presentation', col='order_volume', palette='colorblind', height=5, aspect=6)
    g.map(plt.scatter, "Frequency (Hz)", "Level (dBFS)", s=50, alpha=.7,
          linewidth=1, edgecolor="white")
    g.map(sns.lineplot, "Frequency (Hz)", "Level (dBFS)", alpha=1,
          linewidth=1,palette='BuGn')
    g.add_legend();
    g.savefig(path+subject +'_overview_complete.png')



def plot_comparision(df1,df2):
    """
    function to plot volume per frequency for mri audio data
    and mean volume of frequency by ansl
    """
    g = sns.FacetGrid(df1, height=5, aspect=6,palette=("ch:2.5,-.2,dark=.3"),sharex=True,sharey=True)
    plt.xlim(0,-100)
    plt.xlim(0,8000)
    g.map(sns.lineplot, "Frequency (Hz)", "Level (dBFS)", alpha=1, linewidth=1)
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
