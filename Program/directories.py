
import os

#--------------------------------

def ensure_dir(directory) :
	if not os.path.exists(directory) :
		os.makedirs(directory)

#--------------------------------

working_dir = str(os.path.dirname(os.path.realpath(__file__))) + '/'
input_dir = working_dir + 'input/'
temp_dir = working_dir + 'temp/'
output_dir = working_dir + 'output/'

ensure_dir(temp_dir)
ensure_dir(output_dir)

print('\nInitialised working directory as ' + working_dir)
