import os
from os import path
from pydub import AudioSegment

from directories import input_dir, output_dir, temp_dir, working_dir

def check_subtitles():
	for filename in os.listdir(input_dir) :
		if "source.txt" in filename :
			return True
	return False

def convert():

	if (check_subtitles()==True):
		print("\nSubtitles.txt found! Bypassing mp3 to WAV conversion")
		return

	else:
		print("Reading mp3 file.")
		# files
		src = input_dir + "source.mp3"
		dst = temp_dir + "sound1.wav"

		# convert wav to mp3
		sound = AudioSegment.from_mp3(src)
		sound.export(dst, format = "wav")

		print("mp3 to WAV done.")
