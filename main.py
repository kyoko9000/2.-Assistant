from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ScreenAI import Ui_MainWindow
import sys

import speech_recognition
import pyttsx3

Tom_ear = speech_recognition.Recognizer()
Tom_mouth = pyttsx3.init()

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.Start_Button.clicked.connect(lambda: self.Task_Gui())
        self.uic.Stop_Button.clicked.connect(lambda: self.main_win.close())

    def Task_Gui(self):
        while True:
            with speech_recognition.Microphone() as mic:
                audio = Tom_ear.listen(mic)
            try:
                you = Tom_ear.recognize_google(audio)
                self.uic.Me_Chat.setText(str(you))
            except:
                you = ""

            if you == "":
                Tom_brain = "i can't hear you, try again"
            elif "hello" in you:
                Tom_brain = "hello life"
            elif "doing" in you:
                Tom_brain = "i'm sleeping"
            elif "sure" in you:
                Tom_brain = "i'm not sure"
            elif "nice" in you:
                Tom_brain = "nice to see you too"
            elif "bye" in you:
                Tom_brain = "goodbye life"
                self.uic.Tom_Chat.setText(str(Tom_brain))
                Tom_mouth.say(Tom_brain)
                Tom_mouth.runAndWait()
                break
            else:
                Tom_brain = "oh thank you"
            self.uic.Tom_Chat.setText(str(Tom_brain))
            Tom_mouth.say(Tom_brain)
            Tom_mouth.runAndWait()

    def show(self):
        self.main_win.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())