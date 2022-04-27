from re import M
from PyQt5 import QtWidgets, QtGui, QtCore, uic

from asrInterface import Ui_MainWindow
from PyQt5.QtCore import QThread, pyqtSignal
import sys

import speech_recognition as sr

import os
import difflib
import time

class myWindow(QtWidgets.QMainWindow, QtWidgets.QWidget):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.work = RecognizeThread()

    def exectue(self):
        self.work.start()
        self.work.trigger.connect(self.show_message)

    def show_message(self,message):
        self.ui.mes_box.setText(message)
        self.ui.mes_box.show()
        
class RecognizeThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self):
        super(RecognizeThread, self).__init__()

    def recognize_speech_from_mic(self,recognizer, microphone):
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        try:
            response["transcription"] = recognizer.recognize_sphinx(audio)
        except sr.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            response["error"] = "Unable to recognize speech"

        return response
    
    def get_similarity(self,s1,s2):
        return difflib.SequenceMatcher(None,s1,s2).ratio()

    def run(self):
        COMMANDS = ["play music", "open notepad", "open canvas"]
        OPEN = [r"res\Mozart.mp3","notepad.exe","mspaint.exe"]
        
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        while True:
            guess = self.recognize_speech_from_mic(recognizer,microphone)

            if guess["error"]:
                self.trigger.emit("ERROR: {}".format(guess["error"]))
                break

            self.trigger.emit("You said {}".format(guess["transcription"]))

            similarity = [self.get_similarity(guess["transcription"],command) for command in COMMANDS]

            if max(similarity) < 0.4 :
                self.trigger.emit("I didn't catch that. What did you say?\n")   
                continue

            idx = similarity.index(max(similarity))
            os.system(OPEN[idx])
            time.sleep(5)
    

app = QtWidgets.QApplication([])
application = myWindow()
application.show()
application.exectue()
sys.exit(app.exec())

