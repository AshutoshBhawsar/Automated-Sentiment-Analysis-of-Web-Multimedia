
from MAIN import *
from get_predict import get_prediction


print("Classifying...")
t.perform_prediction()
t.find_unique_words()

a, b, c = get_prediction()
print("The media contains "+a+", "+b+", "+c)
