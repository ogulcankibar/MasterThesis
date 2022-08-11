import pretty_midi
import pandas as pd
pd.options.mode.chained_assignment = None
from music21 import *

def MIDI_to_NOTATION(audiofile, songBPM, outputDirectory, time_signature):
    midi_data = pretty_midi.PrettyMIDI(audiofile)
    midi_list = []

    for instrument in midi_data.instruments:
        for notes in instrument.notes:
            start = notes.start
            end = notes.end
            pitch = notes.pitch
            velocity = notes.velocity
            midi_list.append([start, end, pitch, velocity, instrument.name])

    midi_list = sorted(midi_list, key=lambda x: (x[0], x[2]))
    df = pd.DataFrame(midi_list, columns=['Start', 'End', 'Pitch', 'Velocity', 'Instrument'])
    #print(df)

    midi_df = pd.read_excel("/home/ogulcan/PycharmProjects/MasterThesis/MIDI Note to Frequency Conversion Table.xlsx")
    #print(midi_df)
    midi_df_note = midi_df[["Pitch","note"]]
    #print(midi_df_note)

    merge = pd.merge(df, midi_df_note, on = "Pitch")
    #print(merge)
    sorted_merge = merge.sort_values(by=['Start']).reset_index().drop(columns=["index"])
    #print(sorted_merge)

    sorted_merge["Length"] = sorted_merge["End"] - sorted_merge["Start"]
    last_note_df = sorted_merge[["note","Length"]]
    #last_note_df["Duration Name"] = ""
    #print(last_note_df)

    nduration_df = pd.read_excel("/home/ogulcan/PycharmProjects/MasterThesis/Duration Formula.xlsx")
    nduration_df["Length"] = round(nduration_df.Formula / songBPM,6)
    #print(nduration_df)

    last_note_df["Duration Name"] = " "

    for index, row in last_note_df.iterrows():
        time = round(row['Length'], 6)
        #print(f"time {time}")

        result_index = nduration_df['Length'].sub(time).abs().idxmin()
        #print(result_index)

        last_note_df.at[index, 'Duration Name'] = nduration_df["Name"][result_index]

    #print(last_note_df)
    #return last_note_df

    s = stream.Stream()
    songTempo = tempo.MetronomeMark(number=songBPM, referent="16th")
    s.append(songTempo)
    songTimeSignature = meter.TimeSignature(time_signature)
    s.append(songTimeSignature)

    for index, row in last_note_df.iterrows():
        t_note = note.Note(row['note'])
        t_note.duration = duration.Duration(row['Duration Name'])
        #t_note.duration = duration.Duration(row['Length'])
        s.append(t_note)

    #s.plot()
    environment.set('musicxmlPath', '/usr/bin/musescore3')
    #s.show()

    s.write("musicxml", outputDirectory)

    #environment.set('musicxmlPath', '/usr/bin/timidity')
    #s.show("midi")

    del df
    del midi_df
    del midi_df_note
    del merge
    del sorted_merge
    del last_note_df
    del nduration_df

