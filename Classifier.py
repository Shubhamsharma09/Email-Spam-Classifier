#Implementation of Email spam Classifier Using Naive Bayes 
import os
import io
#import tkinter as tk
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB



#root=tk.Tk()
def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)

def checkingmail(example):
    example_counts = vectorizer.transform(example)
    predictions = classifier.predict(example_counts)
    return predictions

data = DataFrame({'message': [], 'class': []})

data = data.append(dataFrameFromDirectory('F:/project/emails/spam', 'spam'))
data = data.append(dataFrameFromDirectory('F:/project/emails/ham', 'ham'))


#print(data.describe())
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)
#print(vectorizer.get_feature_names())
print(counts.toarray())
classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)


