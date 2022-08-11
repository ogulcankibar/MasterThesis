
import essentia.standard as es

filename = '/home/ogulcan/PycharmProjects/MasterThesis/Thesis Code/Why Moody D Sharp.wav'

audio = es.MonoLoader(filename=filename)()
print(audio.shape)

audio, _, _, _, _, _ = es.AudioLoader(filename=filename)()
print(audio.shape)

audio = es.MonoLoader(filename=filename, sampleRate=16000)()
print(audio.shape)

audio = es.EasyLoader(filename=filename, sampleRate=44100, startTime=60, endTime=70)()
print(audio.shape)




