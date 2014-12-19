import os

pos_tweets = []

for path, subdirs, files  in os.walk('/home/mohamed/Twitter/Positive'):
	for filename in files:
		f = os.path.join(path, filename)
		file_data = open(f, 'r')
		pos_tweets.append((file_data.read(), 'positive'))

		
