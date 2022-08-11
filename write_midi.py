import mido

def WRITEMIDI(bpm, onsets, durations, notes, midi_file_location):

    PPQ = 480 # Pulses per quarter note.
    #BPM = 76 # Assuming a default tempo in Ableton to build a MIDI clip.
    tempo = mido.bpm2tempo(bpm) # Microseconds per beat.

    # Compute onsets and offsets for all MIDI notes in ticks.
    # Relative tick positions start from time 0.
    offsets = onsets + durations
    silence_durations = list(onsets[1:] - offsets[:-1]) + [0]

    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)

    for note, onset, duration, silence_duration in zip(list(notes), list(onsets), list(durations), silence_durations):
        track.append(mido.Message('note_on', note=int(note), velocity=64, time=int(mido.second2tick(duration, PPQ, tempo))))
        track.append(mido.Message('note_off', note=int(note), time=int(mido.second2tick(silence_duration, PPQ, tempo))))

    #midi_file_location = "/home/ogulcan/PycharmProjects/MasterThesis/testdirectory" + '/myimmortaltest3.mid'
    mid.save(midi_file_location)
    print("MIDI file location:", midi_file_location)