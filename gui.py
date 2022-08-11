#IMPORTED PACKAGES
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

#IMPORTED CLASSES
import waveform as wf
import detect_silence as ds
import beat_detaction as bd
import key_detection as kd
"""
import structural_segmentation as sg
import source_seperation as ss
import melodyDetection as md
import write_midi as wm
import notation as nt
import filtering as fl
import quantization as qa
"""
class Worker(QObject):
   worker_result_bpm = pyqtSignal(int)
   worker_result_key = pyqtSignal(str)
   worker_progress_result = pyqtSignal(int)

   finished = pyqtSignal()

   song_path = ""

   def setSongPath(self, path):
      self.song_path = path

   def run(self):
      self.worker_progress_result.emit(0)
      print("Worker Thread started!!!!")
      songName = self.song_path
      songNameTrimmed = songName.split(".")[0] + "Trimmed.wav"
      self.worker_progress_result.emit(10)

      sourceSeperationLocation = ""
      for i in songNameTrimmed.split("/")[1:-1]:
         sourceSeperationLocation = sourceSeperationLocation + "/" + i
      sourceSeperationLocation = sourceSeperationLocation + "/SeperationLocation"
      self.worker_progress_result.emit(20)

      ProcessedLocation = ""
      for i in songNameTrimmed.split("/")[1:-1]:
         ProcessedLocation = ProcessedLocation + "/" + i
      ProcessedLocation = ProcessedLocation + "/ProcessedLocation"
      self.worker_progress_result.emit(30)

      midiLocation = ""
      for i in songNameTrimmed.split("/")[1:-1]:
         midiLocation = midiLocation + "/" + i
      midiLocation = midiLocation + "/MidiLocation"
      self.worker_progress_result.emit(40)

      xmlLocation = ""
      for i in songNameTrimmed.split("/")[1:-1]:
         xmlLocation = xmlLocation + "/" + i
      xmlLocation = xmlLocation + "/XMLLocation"

      ds.remove_sil(songName, songNameTrimmed)
      wf.waveformfunction(songNameTrimmed)

      samplerate = wf.samplerate_function(songNameTrimmed)
      song_BPM = round(bd.BPM_CALCULATION(songNameTrimmed))

      song_KeyandScale = kd.Key_Detection_Function(songNameTrimmed)

      print("bpm", song_BPM)
      print("song_keyandscale", song_KeyandScale)
      self.worker_result_bpm.emit(song_BPM)
      self.worker_result_key.emit(song_KeyandScale)

      print("Worker thread finished!!!")
      self.finished.emit()

class MainWindow(QMainWindow):

   def __init__(self):
      super().__init__()

      self.thread = QThread()
      self.worker = Worker()

      self.worker.moveToThread(self.thread)

      self.thread.started.connect(self.worker.run)
      self.worker.finished.connect(self.thread.quit)
      self.worker.finished.connect(self.worker.deleteLater)
      self.thread.finished.connect(self.thread.deleteLater)
      self.worker.worker_result_bpm.connect(self.print_bpm)
      self.worker.worker_result_key.connect(self.print_key)
      self.worker.worker_progress_result.connect(self.set_progress_bar)

      #self.p = None  # Default empty value.

      # calling initUI method
      #self.initUI()

   # method for creating widgets
   #def initUI(self):

      self.lineEdit_browser = QLineEdit(self)
      self.lineEdit_browser.setGeometry(30, 40, 380, 25)

      self.searchBtn = QPushButton('Browse Song', self)
      self.searchBtn.setGeometry(30, 40, 100, 25)
      self.searchBtn.move(430, 40)
      self.searchBtn.clicked.connect(self.browsefiles)

      self.pbar = QProgressBar(self)
      self.pbar.setGeometry(30, 80, 500, 25)

      #TODO fonksiyon yazılıp update edilecek
      self.pbar.setValue(0)

      self.anlysbtn = QPushButton("Analyse", self)
      self.anlysbtn.setGeometry(550, 40, 190, 65)
      self.anlysbtn.clicked.connect(self.button_click)
      self.anlysbtn.clicked.connect(self.thread.start)

      self.bpmLabel = QLabel('BPM: ' + bpm, self)
      self.bpmLabel.setGeometry(550, 120, 150, 20)

      self.scaleLabel = QLabel('Key & Scale: ' + scale, self)
      self.scaleLabel.setGeometry(550, 160, 150, 20)

      self.wavefromPicture = QPixmap(waveform)
      self.wfLbl = QLabel(self)
      self.wfLbl.setGeometry(30, 120, 500, 400)
      self.wfLbl.setPixmap(self.wavefromPicture)
      self.wfLbl.setScaledContents(True)

      self.btnM1 = QPushButton('Piano Midi', self)
      self.btnM1.setGeometry(550, 200, 90, 25)
      self.btnM1.clicked.connect(self.openFile)

      self.btnM2 = QPushButton('Vocals Midi', self)
      self.btnM2.setGeometry(550, 240, 90, 25)
      self.btnM2.clicked.connect(self.openFile)

      self.btnM3 = QPushButton('Bass Midi', self)
      self.btnM3.setGeometry(550, 280, 90, 25)
      self.btnM3.clicked.connect(self.openFile)

      self.btnM4 = QPushButton('Drums Midi', self)
      self.btnM4.setGeometry(550, 320, 90, 25)
      self.btnM4.clicked.connect(self.openFile)

      self.btnM5 = QPushButton('Other Midi', self)
      self.btnM5.setGeometry(550, 360, 90, 25)
      self.btnM5.clicked.connect(self.openFile)

      self.btnX1 = QPushButton('Piano XML', self)
      self.btnX1.setGeometry(650, 200, 90, 25)
      self.btnX1.clicked.connect(self.openFile)

      self.btnX2 = QPushButton('Vocals XML', self)
      self.btnX2.setGeometry(650, 240, 90, 25)
      self.btnX2.clicked.connect(self.openFile)

      self.btnX3 = QPushButton('Bass XML', self)
      self.btnX3.setGeometry(650, 280, 90, 25)
      self.btnX3.clicked.connect(self.openFile)

      self.btnX4 = QPushButton('Drums XML', self)
      self.btnX4.setGeometry(650, 320, 90, 25)
      self.btnX4.clicked.connect(self.openFile)

      self.btnX5 = QPushButton('Other XML', self)
      self.btnX5.setGeometry(650, 360, 90, 25)
      self.btnX5.clicked.connect(self.openFile)

      # setting window geometry
      self.setGeometry(300, 300, 750, 550)
      # setting window action
      self.setWindowTitle("ARAYÜZ")
      # showing all the widgets
      self.show()

   def browsefiles(self):
      fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/ogulcan/PycharmProjects/MasterThesis/Songs/TestDirectory','All files (*.*)')
      self.lineEdit_browser.setText(fname[0])

   def print_bpm(self, bpm_input):
      #print("The calculated bpm: " + str(bpm_input))
      self.bpmLabel.setText("BPM: " + str(bpm_input))

   def print_key(self, key_input):
      #print("The calculated bpm: " + str(bpm_input))
      self.scaleLabel.setText("Key & Scale: " + str(key_input))

   def openFile(self):
      text = self.sender().text()
      format = text.split(" ")[1]
      instrument = text.split(" ")[0]

      if(format == "Midi"):
         path = "/home/ogulcan/PycharmProjects/MasterThesis/Songs/MidiLocation/"
         frmt = ".mid"
      elif(format == "XML"):
         path = "/home/ogulcan/PycharmProjects/MasterThesis/Songs/XMLLocation/"
         frmt = ".xml"

      filePath = path + instrument.lower() + frmt
      url = QUrl.fromLocalFile(filePath)
      QDesktopServices.openUrl(url)
      pass

   def set_progress_bar(self, int):
      self.pbar.setValue(int)

   #Take Directory
   def button_click(self,s):
      shost = self.lineEdit_browser.text()

      print("Shot: " + shost)
      self.worker.setSongPath(shost)
      self.thread.start()
      # Worker.run(self,shost)

   #TODO butona basıldığında program tetiklenecek
   def doAnalyse(self):
      print("Analyse")
      pass

# main method
if __name__ == '__main__':
   # create pyqt5 app
   App = QApplication(sys.argv)

   bpm = str(" ")
   scale = str(" ")
   waveform = "/home/ogulcan/PycharmProjects/MasterThesis/waveform.png"

   # create the instance of our Window
   window = MainWindow()



   # start the app
   sys.exit(App.exec())
