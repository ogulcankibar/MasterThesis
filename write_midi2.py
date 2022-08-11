import pretty_midi

def WRITEMIDI(bpm, onsets, durations, notes, midi_file_location, time_signature):

    songNumerator = int(time_signature.split("/")[0])
    songDenominator = int(time_signature.split("/")[1])
    songTime = 0

    instrument_name_chord = pretty_midi.PrettyMIDI(initial_tempo=bpm)
    instrument_name_chord.time_signature_changes.append(pretty_midi.TimeSignature(songNumerator, songDenominator, songTime))
    instrument_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    instrument_name = pretty_midi.Instrument(program=instrument_program)

    for index in range(len(notes)):
        note_name = pretty_midi.note_number_to_name(notes[index])
        note_number = pretty_midi.note_name_to_number(note_name)
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=onsets[index], end=onsets[index] + durations[index])
        instrument_name.notes.append(note)

    instrument_name_chord.instruments.append(instrument_name)
    instrument_name_chord.write(midi_file_location)
    #print("Finish!!!")
