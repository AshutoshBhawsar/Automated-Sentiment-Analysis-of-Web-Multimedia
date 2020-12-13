
import you2mp3 as p
import extract_sub as e
import mp3_to_WAV as q
import wav_to_txt2 as r
import test3 as t

from directories import input_dir, output_dir, temp_dir, working_dir

#-----------------------------------

def start_project(media_url) :
	print('\n\nINPUT')
	print('\nGot URL as ' + media_url)
	p.download_mp3(media_url)

	print('\n\nPROCESSING\n')
	e.extract_sub()
	q.convert()
	r.convert()

	print('\n\nOUTPUT')
	t.perform_prediction()
	t.find_unique_words()

def get_url():
	f = open(working_dir + 'url.txt', 'r')
	for line in f :
		media_url = line
		break
	f.close()
	return media_url

#media_url = get_url()
#start_project(media_url)





















''' OUTPUT

Reading mp3 file.
mp3 to WAV done.

Opening WAV file...
Recognising...
Text: was i was also intent on following up our wives american tradition of ex presidents gracefully exiting the political stage and making room for new horses the new ideas that we have our first president george washington survivors of the matter to them actually let the goal is to venture as general washington are warm welcome spreads on really was gradually it got to those who would fall of women about there was no constitutional no democratic norms that guided would ensure that were put to make amends all powerful group made him so potentially present wife and said he resigned as commander in chief the move back to the coverage that in six years later he was elected president by met for two terms he was lying again the roar of themselves and whitewash an inmate the point that is essential to american democracy is that in a government of love and by and for the people there should be no permanent ruling class rowley says who through their elected and temporary representatives determined or course of the
WAV to txt done.

Features loaded.
Classifier loaded.

Reading test data...
Data:  was i was also intent on following up our wives american tradition of ex presidents gracefully exiting the political stage and making room for new horses the new ideas that we have our first president george washington survivors of the matter to them actually let the goal is to venture as general washington are warm welcome spreads on really was gradually it got to those who would fall of women about there was no constitutional no democratic norms that guided would ensure that were put to make amends all powerful group made him so potentially present wife and said he resigned as commander in chief the move back to the coverage that in six years later he was elected president by met for two terms he was lying again the roar of themselves and whitewash an inmate the point that is essential to american democracy is that in a government of love and by and for the people there should be no permanent ruling class rowley says who through their elected and temporary representatives determined or course of the

Probablities are...
joy: 0.04731787314647251
love: 0.11927838801566895
sadness: 0.061899116957923335
anger: 0.02242407830952746
surprise: 0.02222425861877652
fear: 0.024832184958290787
trust: 0.6873402878338469
disgust: 0.0146838121594936

PREDICTION:  trust
Prediction saved.

Unique words were...
['intent', 'following', 'wives', 'american', 'tradition', 'presidents', 'gracefully', 'exiting', 'political', 'stage', 'making', 'horses', 'ideas', 'first', 'president', 'george', 'washington', 'survivors', 'matter', 'actually', 'venture', 'general', 'welcome', 'spreads', 'really', 'gradually', 'those', 'would', 'women', 'about', 'there', 'constitutional', 'democratic', 'norms', 'guided', 'ensure', 'amends', 'powerful', 'group', 'potentially', 'present', 'resigned', 'commander', 'chief', 'coverage', 'years', 'later', 'elected', 'terms', 'lying', 'again', 'themselves', 'whitewash', 'inmate', 'point', 'essential', 'democracy', 'government', 'people', 'should', 'permanent', 'ruling', 'class', 'rowley', 'through', 'their', 'temporary', 'representatives', 'determined', 'course']

Unique words saved.
[Finished in 47.509s]
'''
