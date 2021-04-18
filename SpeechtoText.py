#Must install this libraries
#pip install speechrecognition
#pip install pyttsx3
#for next library there's 2 different ways to install it  "for me the 2nd way worked"
#1st
#pip install pyaudio
#2nd
#pip install pipwin
#pipwin install pyaudio
import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()

def SpeakText(command):
	
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

while(1):	
	
	try:
		
		with sr.Microphone() as source2:
			
			r.adjust_for_ambient_noise(source2, duration=0.2)
			audio2 = r.listen(source2)
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say "+MyText)
			SpeakText(MyText)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occured")
