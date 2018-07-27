'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
# Create a sentiment lists
polarityList=[]

#Subjectivity
subjectivityList=[]

# Get sentiment data
for tweet in tweetData:
    tweetblob = TextBlob(tweet["text"])
    polarityList.append(tweetblob.polarity)

    subjectivityList.append(tweetblob.subjectivity)

'''print(polarityList)
print(subjectivityList)'''

# Create the graph
plt.hist(polarityList, bins=[-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
plt.xlabel('Polarities')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Tweets')
plt.axis([-1.1, .1, 0, 100])
plt.grid(True)
plt.show()

# Subjectivitiy
plt.plot(polarityList, subjectivityList, "ro")
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.title('Tweet Polarity vs Subjectivity')
plt.axis([-1.1, 1.1, -0.1, 1.1])
plt.grid(True)
plt.show()


# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)
