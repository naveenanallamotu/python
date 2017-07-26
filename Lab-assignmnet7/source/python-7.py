import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import string
refined_text = ""
#reading the file
file_reader = open("big.txt").read()
#stop words
st = set(stopwords.words('english'))
for Z in file_reader.lower().split():
    if Z not in st:
        refined_text = refined_text + ' ' + Z
print ("***********refined_text************")
print (refined_text)
#punction removal
NOPUNCT = set(string.punctuation)
texted = ''.join(k for k in refined_text if k not in NOPUNCT)
print ("**********text with no punctions**********")
print texted
#tokenzing the data
token_1 = word_tokenize(texted)
removing_verb = nltk.pos_tag(token_1)
removing_verb = nltk.pos_tag(token_1)
purifiedtext = []
for p in removing_verb:
    if 'VB' not in p[1]:
        purifiedtext.append(p[0])
print ("*************text after removing verbs****************")
print (purifiedtext)
#counting the frequency
summary = ""
freq = Counter(purifiedtext).most_common(5)
print "************freqeuncy*********"
print freq
# summarizing the text
for most in freq:
    for rew in sent_tokenize(file_reader.lower()):
        if rew not in summary:
            if most[0] in word_tokenize(rew):
                summary = summary + rew
print "*********summary********************"
print summary