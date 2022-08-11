from pedalboard import Pedalboard, HighpassFilter, LowpassFilter, Gain, Chorus, Distortion
from pedalboard.io import AudioFile

#file = "/home/ogulcan/PycharmProjects/MasterThesis/Songs/SeperationLocation/NafileTrimmed/bass.wav"

def filtering(instrument, file, outputLocation):
  # Read in a whole audio file:
  with AudioFile(file, 'r') as f:
    audio = f.read(f.frames)
    samplerate = f.samplerate

  board = Pedalboard([Distortion(), Gain(gain_db=12)])
  """
  # Make a Pedalboard object, containing multiple plugins:
  if (instrument == "piano"):
    board = Pedalboard([Gain(gain_db=12)])
  elif (instrument == "vocals"):
    board = Pedalboard([HighpassFilter(cutoff_frequency_hz=200), LowpassFilter(cutoff_frequency_hz=1000), Gain(gain_db=12)])
  elif (instrument == "bass"):
    board = Pedalboard([LowpassFilter(cutoff_frequency_hz=400), Gain(gain_db=12)])
  elif (instrument == "drums"):
    board = Pedalboard([Gain(gain_db=12)])
  elif (instrument == "other"):
    board = Pedalboard([Gain(gain_db=12)])
  """
  # Run the audio through this pedalboard!
  effected = board(audio, samplerate)

  #processed = file.split(".")[0][:-4] + "processed_" + file.split(".")[0].split("/")[-1] + "." + file.split(".")[1]
  # Write the audio back as a wav file:
  with AudioFile(outputLocation, 'w', samplerate, effected.shape[0]) as f:
    f.write(effected)