import pandas as pd
import sklearn

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
