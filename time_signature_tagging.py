import pandas as pd
import taglib

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

df_readed = pd.read_excel("/home/ogulcan/PycharmProjects/MasterThesis/Dataset/Veri Kümesi (Wav)/Veri Kümesi.xlsx")
df = pd.DataFrame(df_readed, columns=['Sanatçı', 'Müzikal Eser', 'Ölçü İşareti'])

for song in songs:
    songTag = taglib.File(song)
    songDict = songTag.tags
    #print(songDict)
    musicianName = song.split("/")[8].split("-")[0][0:-1]
    songName = song.split("/")[8].split("-")[1][1:]
    if not("TIME SIGNATURE" in songDict.keys()):
        print("If'teyim")
        #print(f"Song Tag : {songTag}, song Dict: {songDict}, Musician: {musicianName}, Song Name: {songName} ")
        songDict["Time Signature"] = df.loc[df["Sanatçı"] == musicianName].loc[df["Müzikal Eser"] == songName]["Ölçü İşareti"]
        songTag.save()

print("Bitti")




