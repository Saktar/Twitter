import json

tweetFile = open("tweets_small.json", "r")

tweetData = json.load(tweetFile)

tweetFile.close()

print("Tweet ID: ", tweetData[0]["id"])

print("Tweet text: ", tweetData[0]["text"])

for idx in range(len(tweetData)):
    print("Tweet text: "+ tweetData[idx]["text"])