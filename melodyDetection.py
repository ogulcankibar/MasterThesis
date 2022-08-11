import numpy
import essentia.standard as es

#audiofile = "/home/ogulcan/PycharmProjects/MasterThesis/Songs/SeperationLocation/NafileTrimmed/vocals.wav"
def MELODY_DETECTION(audiofile, sampleRate):

    # Load audio file.
    # It is recommended to apply equal-loudness filter for PredominantPitchMelodia.
    loader = es.EqloudLoader(filename=audiofile, sampleRate=sampleRate)
    audio = loader()
    #print("Duration of the audio sample [sec]:", len(audio)/sampleRate)

    # Extract the pitch curve
    # PitchMelodia takes the entire audio signal as input (no frame-wise processing is required).

    pitch_extractor = es.PredominantPitchMelodia(frameSize=2048, hopSize=1024)
    pitch_values, pitch_confidence = pitch_extractor(audio)

    # Pitch is estimated on frames. Compute frame time positions.
    pitch_times = numpy.linspace(0.0,len(audio)/sampleRate,len(pitch_values))

    #todo sonic visualizer text kodu
    #with open("sonic_viz_results_last.txt", 'w') as f:
    #    for i in range(len(pitch_times)):
    #        f.write(str(pitch_times[i]) + "\t" + str(pitch_values[i]) + "\n")


    # Plot the estimated pitch contour and confidence over time.
    #f, axarr = plt.subplots(2, sharex=True)
    #axarr[0].plot(pitch_times, pitch_values)
    #axarr[0].set_title('estimated pitch [Hz]')
    #axarr[1].plot(pitch_times, pitch_confidence)
    #axarr[1].set_title('pitch confidence')
    #plt.show()


    onsets, durations, notes = es.PitchContourSegmentation(hopSize=1024)(pitch_values, audio)
    return onsets, durations, notes

    #print("MIDI notes:", notes) # Midi pitch number
    #print("MIDI note onsets:", onsets)
    #print("MIDI note durations:", durations)





