
from MAIN import *
from get_predict import get_prediction

media_url = get_url()

print("Fetching...")
p.download_mp3(media_url)
e.extract_sub()

print("Processing...")
q.convert()
r.convert()

print("Classifying...")
t.perform_prediction()
t.find_unique_words()
print("Done!")

a, b, c = get_prediction()
#print("The media contains "+a+", "+b+", "+c)
print(""+a+", "+b+", "+c)
