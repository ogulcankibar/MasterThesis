import time

from music21 import *

note1 = note.Note("C4")
note1.duration.type = 'half'
note2 = note.Note("F#4")
note2.duration.dots = 1.5
note3 = note.Note("B-2")

s = stream.Stream()
s.append(note1)
s.append(note2)
s.append(note3)

s.plot()
environment.set('musicxmlPath', '/usr/bin/musescore3')
s.show()







import music21
from .KeyStrikes import KeyStrikes
from mingus.midi import midi_file_in

midi_file_in.MIDI_to_Composition(midifilename)

def midi2keystrikes(filename, tracknum=0):
    """
    Reads a midifile (thanks to the package music21), returns a list
    of the keys hits:  [{'time':15, 'note':50} ,{... ]
    """

    mf = music21.midi.MidiFile()
    mf.open(filename)
    mf.read()
    mf.close()
    events = mf.tracks[tracknum].events
    result = []
    t = 0

    for e in events:

        if e.isDeltaTime and (e.time is not None):

            t += e.time

        elif (e.isNoteOn and (e.pitch is not None) and
              (e.velocity != 0) and (e.pitch > 11)):

            result.append({'time': t, 'note': e.pitch})

    if (len(result) == 0) and (tracknum < 5):
        # if it didn't work, scan another track.
        return midi2keystrikes(filename, tracknum + 1)

    return KeyStrikes(result)

midifilename = "/home/ogulcan/PycharmProjects/MasterThesis/testdirectory/extracted_melody6.mid"

midi2keystrikes(midifilename,0)

"""
from mingus.containers import NoteContainer
from mingus.midi import midi_file_out

nc = NoteContainer(["A", "C", "E"])
midi_file_out.write_NoteContainer("test.mid", nc)

from mido import MidiFile
import time
import midi

mid = MidiFile("/home/ogulcan/PycharmProjects/MasterThesis/testdirectory/extracted_melody6.mid", clip=True)
print(mid)

for track in mid.tracks:
    print(track)

for msg in mid.tracks[0]:
    yazı = str(msg)
    note = yazı.split(" ")[2].split("=")[1]
    print(f"Note is {note}")
    time = yazı.split(" ")[4].split("=")[1]
    print(f"Time is {time}")
"""