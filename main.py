#IMPORTED PACKAGES
import os
import time
import logging

#IMPORTED CLASSES
import waveform as wf
import detect_silence as ds
import beat_detaction as bd
import key_detection as kd
import read_metadata as rmd
import structural_segmentation as sg
import source_seperation as ss
import melodyDetection as md
#import write_midi as wm
import write_midi2 as wm
import notation as nt
import filtering as fl
import quantization as qa

def try_until(cmd, timeout, err_handle="", err_type=0, err_opt=True, return_opt=False, log_opt=True):
    """FONKSIYON ACIKLAMA

       x (command) : denenecek islem komutu

       y (int) : timeout suresi

       err_handle (str) : raise value hata urettiginde ilgili hatanin bilgisi

       err_type (str) : raise value hata urettiginde ilgili hatanin tipidir.
                        0: tanimsiz hata
                        1,2,3... : is surecinde kullanilacak durumlara gore belirlenebilir.

       err_opt (bool) : hata durumundaki davranisi belirler
                        True -> olursa raise value yaparak hata uretir
                        False -> silence olarak devam eder

       return_opt (bool) : komutun calismasi sonucunda return olan birsey varsa onu try_until returnu olarak doner

       Ornek:
                try_until("driver.find_element_by_id('nss_tarih').text", WAIT_LONG,
                                                                         err_handle = 'tarih bilgisi okunamadi',
                                                                         err_type = '1',
                                                                         err_opt = True,
                                                                         return_opt = False )
       Ornek Aciklama:

                nss tarih bilgisi okunmaya calisirken hata alinmis olursa, "tarih okunamadi" bilgisi manuel gonderilecek kisiye verilmis olur,
                isin gonderilecegi yer (1 numarali istasyon) gonderimi yapacak robot icin belirlenmis olur. (Musteri hizmetleri)

                Bu bilgiler exception'da veritabanina yazilabilir ya da farklý aksiyonlar alinabilir

       """

    global elm
    cnt=0

    while 0 < timeout:
        try:
            if return_opt:
                elm = eval(cmd)
                return elm
            else:
                exec(cmd)
                print(cmd + "  -> ok")
                return True

        except Exception as err:
            err1 = err
            print(str(cnt) + " deniyor -> " + cmd)
            cnt = cnt + 1
            timeout = timeout - 1
            time.sleep(1)

    if err_opt:
        # raise ValueError (x + " ---> " + str(err1) + "<->" + err_type + "<->" + err_handle)
        raise ValueError({"msg": str(err1), "err_type": err_type, "err_handle": err_handle})
    else:
        if log_opt:
            #log("try_until basarisiz: " + cmd)
            return False

songs = ["/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Almora - Kaf Dağının Ardında/kaf_daginin_ardinda.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Anonim - Kürdilihicazkâr/Anonim - Kurdili Hicazkar Sirto.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Apocalyptica - I Don't Care/apocalyptica_i_dont_care.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/B.B. King - Help The Poor/B.B. King - Help The Poor.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Beethoven - Moonlight Sonata/Beethoven - Moonlight Sonata.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Black Sabbath - NIB/black_sabbath_nib.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Blind Guardian - The Bards Song/Blind Guardian - The Bards Song (guitar pro).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Bon Jovi - Its My Life (guitar pro)/Bon Jovi - Its My Life (guitar pro).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Chris Rea - The Road To Hell/Chris Rea - The Road To Hell.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Chuck Berry - Johnny B Goode/Chuck Berry - Johnny B Goode (ver 6).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Dave Brubeck - Take Five/The Dave Brubeck Quartet - Take Five.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Deep Purple - Smoke On The Water/Deep Purple - Smoke On The Water (Pro).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Dr. Feelgood - She Does It Right/Dr. Feelgood - She Does It Right.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Dream Evil - The Book Of Heavy Metal/dream_evil_the_book_of_heavy_metal.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Duke Ellington - Take The “A” Train/Duke Ellington - Take The A Train.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Five Finger Death Punch - Canto 34/five_finger_death_punch_canto_34.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Gary Moore - Still Got The Blues/Gary Moore - Still Got The Blues (ver 2).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Green Day - Holiday/Green Day - Holiday (guitar pro).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Halk Türküsü - Çökertme/çökertme.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Herbie Hancock - Cantaloupe Island/Herbie Hancock - Cantaloupe Island (ver 2).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Inna - India/INNdiA (KcrA).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Iron Maiden - Dance Of Death/iron_maiden_dance_of_death.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Johann Sebastian Bach - Prelude/Johann Sebastian Bach - Cello Suite No 1 - Prelude (ver 4 by thelordofdarkch).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/John Coltrane - My Favorite Things/John Coltrane - My Favorite Things.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Ludwig van Beethoven - Sonata Opus 31/Ludwig van Beethoven - Sonata Opus 31.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Malt - Aşkın Gözü/Malt - Askin Gozu (guitar pro).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Megadeth - Trust/Megadeth - Trust (guitar pro).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Metallica - Orion/metallica_orion.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Miles Davis - So What/Miles Davis - So What.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Nightwish - The Islander/nightwish_the_islander.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Nirvana - Something In The Way/Nirvana - Something In The Way (ver 2 by dont_fall_asl1).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/P!nk - Just Like a Pill/P!nk - Just Like A Pill (ver 2 by hxc_emo).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Pentagram - F.T.W.D.A/mezarkabul_ftwda.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Red Hot Chili Peppers - Californication/Red Hot Chili Peppers - Californication (guitar pro).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Rise Against - Prayer of the Refugee/rise_against_prayer_of_the_refugee.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Skillet - Awake and Alive/skillet_awake_and_alive.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Slash - Anastasia/Slash - Anastasia (Pro).wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Styx - Renegade/styx_renegade.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/The Eagles - Hotel California/eagles_hotel_california.wav",
         "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Şarkılar/Wolfgang Amadeus Mozart - Rondo Alla Turca/Wolfgang Amadeus Mozart - Rondo Alla Turca (ver 8 by AwokenDEMON).wav"]

songsTimeSignature = ['3/4', '4/4', '4/4', '4/4', '3/4', '4/4', '3/4', '4/4', '4/4', '4/4', '5/4', '4/4', '4/4', '4/4', '4/4', '4/4', '12/8', '6/4', '4/4', '4/4', '4/4', '3/4', '4/4', '6/8', '3/8', '4/4', '4/4', '4/4', '4/4', '3/4', '4/4', '4/4', '4/4', '4/4', '4/4', '4/4', '4/4', '4/4', '4/4', '1/4']

times = 0

songName = songs[times]
songArtist = songName.split("/")[8].split(" - ")[0]
songMW = songName.split("/")[8].split(" - ")[1]

directory = songName[:-4].split("/")[-1]
parent_dir = "/home/ogulcan/PycharmProjects/MasterThesis/Dataset/System Output"
path = os.path.join(parent_dir, directory)
os.mkdir(path)

logging.basicConfig(filename=path + "/log.txt", level=logging.INFO ,format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filemode="w")
logging.info("Started!!!")
logging.info(f"Artist: {songArtist}")
logging.info(f"Musical Work: {songMW}")

TrimmedLocation = path + "/TrimmedLocation/"
os.mkdir(TrimmedLocation)
songNameTrimmed = TrimmedLocation + songName[:-4].split("/")[-1] + " Trimmed.wav"

sourceSeperationLocation = ""
for i in songNameTrimmed.split("/")[1:-2]:
    sourceSeperationLocation = sourceSeperationLocation + "/" + i
sourceSeperationLocation = sourceSeperationLocation + "/SeperationLocation"
os.mkdir(sourceSeperationLocation)

#ProcessedLocation = ""
#for i in songNameTrimmed.split("/")[1:-1]:
#    ProcessedLocation = ProcessedLocation + "/" + i
#ProcessedLocation = ProcessedLocation + "/ProcessedLocation/" + songName.split(".")[0].split("/")[-1]

midiLocation = ""
for i in songNameTrimmed.split("/")[1:-2]:
    midiLocation = midiLocation + "/" + i
midiLocation = midiLocation + "/MidiLocation"
os.mkdir(midiLocation)

xmlLocation = ""
for i in songNameTrimmed.split("/")[1:-2]:
    xmlLocation = xmlLocation + "/" + i
xmlLocation = xmlLocation + "/XMLLocation"
os.mkdir(xmlLocation)

ds.remove_sil(songName,songNameTrimmed)
#wf.waveformfunction(songNameTrimmed)

samplerate = wf.samplerate_function(songNameTrimmed)
#print(f"Samplerate: {samplerate}")
logging.info(f"Samplerate: {str(samplerate)}")

song_BPM = round(bd.BPM_CALCULATION(songNameTrimmed))
logging.info(f"BPM: {str(song_BPM)}")
#print(f"BPM: {song_BPM}")

song_KeyandScale = kd.Key_Detection_Function(songNameTrimmed)
logging.info(f"Key and Scale: {str(song_KeyandScale)}")
#print(f"Key and Scale: {song_KeyandScale}")

#TODO time signature alamıyor
#song_Time_signature = str(rmd.read_time_signature(songNameTrimmed))
song_Time_signature = songsTimeSignature[times]
logging.info(f"Time Signature: {str(song_Time_signature)}")
#print(f"Time Signature: {song_Time_signature}")

"""
import musthe as m
s = m.Scale(m.Note(key), scale)
scaleArray = [str(s[i]) for i in range(len(s))]

scale_df = pd.DataFrame(scaleArray)

for notes in song_notes:
    for scale in scale_df:
        if song_notes[notes] not in scale_df:
            song_notes[notes] = 

xcoords = structural_segmentation.str_segmentation_function(songNameTrimmed)
for xc in xcoords:
    plt.axvline(x=xc)

lenght_arr = [j-i for i, j in zip(xcoords[:-1], xcoords[1:])]

index = 0
index_arr = []
for element in lenght_arr:
    if element < 1.0:
        index_arr.append(index)
        lenght_arr.remove(element)
    index = index + 1

index_arr = incr(index_arr,1)

xcoords = np.delete(xcoords, index_arr)
lenght_arr = [j-i for i, j in zip(xcoords[:-1], xcoords[1:])]
"""

ss.SOURCE_SEPERATION_FUNCTION(songNameTrimmed, sourceSeperationLocation, samplerate)
logging.info("Source Separation is done.")

files_seperation = os.listdir(sourceSeperationLocation)
files_list_seperation = []
for root, directories, files_seperation in os.walk(sourceSeperationLocation):
    for name in files_seperation:
        files_list_seperation.append(os.path.join(root, name))

"""
for instruments in files_list_seperation:
    instrument = instruments.split(".")[0].split("/")[-1]
    processOutput = ProcessedLocation + "/" + instrument + ".wav"
    fl.filtering(instrument, instruments, processOutput)
    print(f"{instrument} işlem yaptım")

files_processed = os.listdir(ProcessedLocation)
files_list_processed = []
for root, directories, files_processed in os.walk(ProcessedLocation):
    for name in files_processed:
        files_list_processed.append(os.path.join(root, name))
"""

for instruments in files_list_seperation:
    instrument = instruments.split("/")[-1].split(".")[0]
    #instrument = instruments.split(".")[0].split("/")[-1]
    #print(instrument)
    #print(instruments)

    song_onsets = []
    song_durations = []
    song_notes = []


    song_onsets, song_durations, song_notes = md.MELODY_DETECTION(instruments, samplerate)
    logging.info("The melody has been detected.")
    #print(f"{instrument} Melodi çıkarıldı")

    song_notes = qa.quantize_notes(song_notes, song_KeyandScale)
    song_durations = qa.quantize_durations(song_durations, song_BPM)

    tempMidiLocation = midiLocation + "/" + instrument + ".mid"
    wm.WRITEMIDI(song_BPM, song_onsets, song_durations, song_notes, tempMidiLocation, song_Time_signature)
    logging.info("Midi has been wrote.")
    #print(f"{instrument} Midi yazıldı")

    tempXmlLocation = xmlLocation + "/" + instrument + ".xml"
    nt.MIDI_to_NOTATION(tempMidiLocation, song_BPM, tempXmlLocation, song_Time_signature)
    logging.info("XML has been wrote.")
    #print(f"{instrument} XML yazıldı")

    song_onsets = []
    song_durations = []
    song_notes = []

    #print("----------------------------------")

logging.info("Finished!!!")

print("bitti")

