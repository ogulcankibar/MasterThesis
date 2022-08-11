import librosa


def BPM_CALCULATION(songName):

    x, sr = librosa.load(songName)
    bpm = librosa.beat.beat_track(x, sr)[0]

    return bpm


