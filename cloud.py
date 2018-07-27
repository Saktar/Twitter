'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import wordCloud

# Search term used for this tweet
# We want to filter this out
tweetSearch ="automation"

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
# Combine all the tweet texts
combinedTweets = ""
for tweet in tweetData:
    combinedTweets += tweet["text"]

# Create  combined tweet Tweet Blob
tweetblock = TextBlob(combinedTweets)

# Filter Words
worldsToFilter = ["about", "https", "in", "the", "thing", "will", "cloud", tweetSearch]
filterDictionary = dict()

for word in tweetblob.words:
    # Skip tiny Words
    if len(word) < 2:
        continue

    # skip words with random characters or numbers
    if not word.isalpha():
        continue

    # Skip words in our filterDictionar
    if word.lower() in worldsToFilter:
        continue

    # Don't want lowercase words smaller than 5 characters
    if len(word) < 5 and word.upper() != word:
        continue

# create the word Cloud
wordcloud = WordCloud().generate_from_frequencies(filterDictionary)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()


# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)
