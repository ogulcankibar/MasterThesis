from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np

#song = "/home/ogulcan/PycharmProjects/MasterThesis/Songs/TestDirectory/Malt - DepremTrimmed.wav"

def waveformfunction(song):
    samplerate, data = read(song)

    # print("Data: ",data)

    duration = len(data) / samplerate
    time = np.arange(0, duration, 1 / samplerate)  # time vector

    title = song.split(".")[0].split("/")[-1][:-7]

    plt.plot(time, data)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.savefig("waveform" + song.split(".")[0].split("/")[-1] + ".png")

def samplerate_function(song):
    samplerate, data = read(song)
    return samplerate
