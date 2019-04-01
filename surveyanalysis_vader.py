from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

neutcount = 0
neutcorrect = 0
negcount = 0
negcorrect = 0
poscount = 0
poscorrect = 0

with open("EECommentsOnly.txt", "r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs['compound'] >= 0.05:
            poscorrect += 1
        poscount +=1

with open("EECommentsOnly.txt", "r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs['compound'] <= -0.05:
            negcorrect += 1
        negcount +=1

with open("EECommentsOnly.txt", "r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs['compound'] > -0.05 and vs['compound'] < 0.05:
            neutcorrect += 1
        neutcount +=1

print("Vader = {}% positive results via {} samples".format(poscorrect/poscount*100.0, poscount))
print("Vader = {}% negative results via {} samples".format(negcorrect/negcount*100.0, negcount))
print("Vader = {}% neutral results via {} samples".format(neutcorrect/neutcount*100.0, neutcount))

