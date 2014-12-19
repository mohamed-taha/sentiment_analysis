# -*- coding: utf-8 -*-
import os
import nltk
import pickle

#positive tweets will be used for training
pos_tweets = []
for path, subdirs, files  in os.walk('/home/mohamed/Twitter/Positive'):
	for filename in files:
		f = os.path.join(path, filename)
		file_data = open(f, 'r')
		pos_tweets.append((file_data.read(), 'positive'))


#negative tweets will be used for training
neg_tweets = []
for path, subdirs, files  in os.walk('/home/mohamed/Twitter/Negative'):
	for filename in files:
		f = os.path.join(path, filename)
		file_data = open(f, 'r')
		pos_tweets.append((file_data.read(), 'negative'))


tweets = []
for(words, sentiment) in pos_tweets + neg_tweets:
	words_filtered = [e.lower() for e in words.split() if len(e) >=3]
	tweets.append((words_filtered, sentiment))

def get_words_in_tweets(tweets):
	all_words = []
	for(words, sentiment) in tweets:
		all_words.extend(words)
	return all_words
	
def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys() #usch that worrlist is a dictionary
									# of key(word) and value(frequency)
	return word_features

word_features = get_word_features(get_words_in_tweets(tweets))	

#handling the input
def extract_features(document):
	document_words = set(document) #eliminate duplicates
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features
	
	
# define the training set
training_set = nltk.classify.apply_features(extract_features, tweets)
#training our classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)

# saving the classifier object
f = open("classifier_object.pickle", 'wb')
pickle.dump(classifier, f)
f.close()