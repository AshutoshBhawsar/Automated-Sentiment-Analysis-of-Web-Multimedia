import os
import speech_recognition as sr
import pocketsphinx

from directories import input_dir, output_dir, temp_dir, working_dir

def check_subtitles():
	for filename in os.listdir(input_dir) :
		if "source.txt" in filename :
			return True
	return False

def convert():

	if (check_subtitles()==True) :
		print("\nSubtitles.txt found! Bypassing WAV to txt conversion")

		file = open (input_dir + 'source.txt')
		f = open(temp_dir + "file.txt", "w")
		for s in file :
			f.write("" + s)
		f.close()
		print("Subtitles.txt copied.")
		return

	else :
		print("Opening WAV file...")
		r = sr.Recognizer()
		file = sr.AudioFile(temp_dir + "sound1.wav")
		with file as source:
			r.adjust_for_ambient_noise(source)

			#audio = r.record(source, offset = 1)
			audio = r.record(source, offset = 1, duration = 50)

		print("Recognising...")
		try:
			#s = r.recognize_google(audio)
			s = r.recognize_sphinx(audio)
			print("Text: " + s)

			f = open(temp_dir + "file.txt", "w")
			f.write("" + s)
			print("WAV to txt done.")

		except Exception as e:
			print("Exception: " + str(e))
