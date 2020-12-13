
import os
import webvtt

from directories import input_dir, output_dir, temp_dir, working_dir

def check_subtitles():
	for filename in os.listdir(temp_dir) :
		if "source.vtt" in filename :
			return True
	return False

def extract_sub() :
	if (check_subtitles()==True):
		print ('\nSubtitles found!')

		temp = ' '
		for line in webvtt.read(temp_dir + "source.vtt") :
			temp = temp + line.text + ' ';

		str2 = temp.replace('\n',' ')
		f = open (input_dir + 'source.txt', 'w')
		f.write(str(str2))
		f.close()
		print ('Subtitles saved!')
