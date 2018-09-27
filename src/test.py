#import nltk
from nltk.corpus import twitter_samples

print(twitter_samples.fileids())
# The below results in extra long string in the console
#print(twitter_samples.strings('tweets.20150430-223406.json'))


print("Done.")