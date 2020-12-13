import youtube_dl
import os

from directories import input_dir, output_dir, temp_dir, working_dir

#------------------------------------

def ensure_clean():
	# Remove old source.mp3 and source.txt
	for filename in os.listdir(input_dir) :
		if "source.mp3" in filename :
			print("Deleting old source.mp3")
			os.remove(input_dir + "source.mp3")
		if "source.txt" in filename :
			print("Deleting old source.txt")
			os.remove(input_dir + "source.txt")

	# Remove old source.srt
	for filename in os.listdir(temp_dir) :
		if "source.vtt" in filename :
			print("Deleting old source.vtt")
			os.remove(temp_dir + "source.vtt")


def download_mp3(media_url):
	ydl_opts = {
		'format': 'bestaudio/best',
		"outtmpl" : working_dir+'a.%(ext)s',
		'writeautomaticsub': True,
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
	}

	print("\nDownloading mp3...")
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([media_url])
	print("Download complete.")

	ensure_clean()

	# Copy downloaded mp3
	for filename in os.listdir(working_dir) :
		if ".mp3" in filename:
			os.rename(working_dir + filename, input_dir + "source.mp3")
		if ".vtt" in filename:
			os.rename(working_dir + filename, temp_dir + "source.vtt")
	print("Renaming and Moving complete.")
