
import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier
import pickle

from directories import input_dir, output_dir, temp_dir, working_dir

#------------------REQUIRED-FUNCTIONS------------------------

def get_words_in_dataset(dataset):
	all_words = []
	for (words, sentiment) in dataset:
		all_words.extend(words)
	return all_words

def read_datasets(fname, t_type):
	data = []
	f = open(fname, 'r')
	line = f.readline()
	while line != '':
		data.append([line, t_type])
		line = f.readline()
	f.close()
	return data

def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features

def extract_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

def prob_classify_dataset(data):
	return classifier.prob_classify(extract_features(nltk.word_tokenize(data)))

def maximum_value(pdist):
	return pdist.max()

#-------------------------------------------------------

# Create global variables to load classifier
f = open(input_dir + 'word_features3.pickle', 'rb')
word_features = pickle.load(f)
f.close()
f = open(input_dir + 'my_classifier3.pickle', 'rb')
classifier = pickle.load(f)
f.close()

#------------------------PREDICTION------------------------------
def perform_prediction():

	# read in the data to classify
	print("\n\nReading test data...")
	f = open(temp_dir + "file.txt")
	test_data = f.read()
	print("\nData: ", test_data)

	pdist = prob_classify_dataset(test_data)

	print("\n\nProbablities are...")
	total = pdist.prob('joy') + pdist.prob('love') + pdist.prob('sadness') + pdist.prob('anger') +  + pdist.prob('surprise') + pdist.prob('fear') + pdist.prob('trust') + pdist.prob('disgust')
	pJoy = pdist.prob('joy') / total;
	pLove = pdist.prob('love') / total;
	pSadness = pdist.prob('sadness') / total;
	pAnger = pdist.prob('anger') / total;
	pSurprise = pdist.prob('surprise') / total;
	pFear = pdist.prob('fear') / total;
	pTrust = pdist.prob('trust') / total;
	pDisgust = pdist.prob('disgust') / total;

	print("joy:", pJoy)
	print("love:", pLove)
	print("sadness:", pSadness)
	print("anger:", pAnger)
	print("surprise:", pSurprise)
	print("fear:", pFear)
	print("trust:", pTrust)
	print("disgust:", pDisgust)

	print("\nPREDICTION: ", maximum_value(pdist))

	# first we create blank prediction file and then append our prediction to it
	f = open(output_dir + 'predict.txt', "w")
	f.write("joy,"+ str(pJoy))
	f.write("\nlove,"+ str(pLove))
	f.write("\nsadness,"+ str(pSadness))
	f.write("\nanger,"+ str(pAnger))
	f.write("\nsurprise,"+ str(pSurprise))
	f.write("\nfear,"+ str(pFear))
	f.write("\ntrust,"+ str(pTrust))
	f.write("\ndisgust,"+ str(pDisgust))
	f.close()

	print("\n\nPrediction saved.")


#---------------------EXTRACTING WORDS------------------------------------
def find_unique_words():
	# read input file
	data_file = read_datasets(temp_dir + 'file.txt', '?')

	# filter away words that are less than 'n' letters
	n = 8
	data2 = []
	for (words, sentiment) in data_file:
		words_filtered = [e.lower() for e in words.split() if len(e) >= n]
		data2.append((words_filtered, sentiment))

	# extract useful words from input
	word_features2 = get_word_features(get_words_in_dataset(data2))
	print("\n\nUnique words were...")
	print(list(word_features2))

	# save unique words
	f = open(output_dir + 'unique_words.txt', "w")
	str1 = ','.join(list(word_features2))
	f.write(str1)
	print("\nUnique words saved.")

''' OUTPUT
Features loaded.
Classifier loaded.

Reading test data...

Data:  it the world is bad worse i don't want to live in it and had it there but venice and so they tend to have a fifth have it if it plan that need that bad things and have the phone and who have be a tied behind it and then they don't think they can of the things that you have a bit of that and don't know if i can prove that if the vanity and that if one and one hundred and when he and what

Probablities are...
joy: 0.2820808574700056
love: 0.002233612170801628
sadness: 0.622438987904567
anger: 0.035531859328029124
surprise: 3.9394371200652964e-08
fear: 0.018100861581301433
trust: 0.001877789815439354
disgust: 0.037735992335484664

PREDICTION: sadness

Prediction saved.


Unique words were...
['world', 'worse', "don't", 'want', 'live', 'there', 'venice', 'they', 'tend', 'have', 'fifth', 'plan', 'that', 'need', 'things', 'phone', 'tied', 'behind', 'then', 'think', 'know', 'prove', 'vanity', 'hundred', 'when', 'what']

Unique words saved.
'''
