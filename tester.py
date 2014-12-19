# -*- coding: utf-8 -*-
import os
import nltk
import pickle

# loading the classifier object
f = open("classifier_object.pickle")
classifier = pickle.load(f)
f.close()


# tesing our classifier
tweet = 'انا بااكره الشخص ده'
print classifier.classify(tweet.split())