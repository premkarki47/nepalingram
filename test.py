# test.py
# test the ngram model creator
# by anup pokhrel
# http://virtualanup.com/nepali-ngram-models/

from makengram import ngrammodel
import re

model = ngrammodel(1)
model.readfile(open('test'))
model.saveoutput(open('testoutput','w+'))
#Data = 'उल्लेख गरिएको छ । दस्तावेजमा एमाओवादीसँग? कार्यगत एकत! is ther'
#print(Data.replace("।",' ').split())
