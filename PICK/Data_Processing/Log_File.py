try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import os
import speech_recognition as sr
import wavio
from os import path
from Data_Processing.cleanser import file_cleanse

class Log_File(object):
    def __init__(self,name,folder):
        self.folder = folder
        self.name = name
        self.cleansed = False
        self.validated = False
        self.acknowledged = False
        self.ingested = False

    def cleanseFile(self):
        #We must check here which type of file it is to turn it into text if image or if audio
        if(os.path.splitext(self.name)[1] == ".wav"):
            #Here is a wav file so we apply audio recognition
            # use the audio file as the audio source
            r = sr.Recognizer()
            with sr.AudioFile(self.folder + "/" + self.name) as source:
                audio = r.record(source)  # read the entire audio file
            # recognize speech using Sphinx
            try:
                file = open(self.folder+"/" + os.path.splitext(self.name)[0] + ".txt","w+")
                file.write(r.recognize_sphinx(audio))
                file.close()
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))
        elif(os.path.splitext(self.name)[1] == ".png"):
            #here is an image file so we apply ocr
            file = open(self.folder+"/" + os.path.splitext(self.name)[0] + ".txt","w+")
            file.write(pytesseract.image_to_string(Image.open(self.folder+"/" + self.name)))
            file.close()
        else:   
            file_cleanse(self.folder + "/" + self.name,self.folder + "/" + self.name)
        

        #If successfully cleansed
        self.cleansed = True
        self.validated = True
