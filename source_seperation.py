from spleeter.audio.adapter import AudioAdapter
from spleeter.separator import Separator
import shutil
import os

def SOURCE_SEPERATION_FUNCTION(audiofile, outputdirectory,sample_rate):

    #audiofile = '/home/ogulcan/PycharmProjects/MasterThesis/Dataset/System Output/Dr. Feelgood - She Does It Right/TrimmedLocation/Dr. Feelgood - She Does It Right Trimmed.wav'
    #outputdirectory = '/home/ogulcan/PycharmProjects/MasterThesis/Dataset/System Output/Dr. Feelgood - She Does It Right/SeperationLocation'
    #sample_rate = 44100

    audio_loader = AudioAdapter.default()
    waveform, _ = audio_loader.load(audiofile, sample_rate=sample_rate)

    separator = Separator('spleeter:5stems')

    separator.separate_to_file(audiofile, outputdirectory)

    path = ""
    for i in audiofile.split(".")[0].split("/")[:-1]:
        path = path +  "/" + i
    path = path[1:]
    path = path[:-16] + "/SeperationLocation/" + audiofile.split(".")[0].split("/")[-1]
    files = os.listdir(path)
    files_list = []
    for root, directories, files in os.walk(path):
        for name in files:
            if name.endswith('.wav'):
                files_list.append(os.path.join(root, name))

    for i in range(len(files_list)):
        shutil.copy2(files_list[i], outputdirectory)

    shutil.rmtree(path, ignore_errors=False, onerror=None)
