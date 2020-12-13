
from directories import output_dir

#-----------------------------------

def read_prediction():
	file = open(output_dir + "predict.txt")
	for line in file:
		line = line.split(',')
		arr2.append(float(line[1]))

def get_max(num):
	arr3 = arr2.copy()
	arr3.sort()
	for i in range (0,8):
		if arr3[7-(num-1)] == arr2[i]:
			return arr[i]

def get_prediction():
	read_prediction()
	print(get_max(1))
	print(get_max(2))
	print(get_max(3))

	return get_max(1), get_max(2), get_max(3)


#-----------------------------------


arr = ['joy', 'love', 'sadness', 'anger', 'surprise', 'fear', 'trust', 'disgust']
arr2 = []

love = '♥'

#get_prediction()

#import emoji
#print ('♥‿♥')
#print(emoji.emojize('Python is :pensive:'))
#print(emoji.emojize('Python is :cookie:'))
