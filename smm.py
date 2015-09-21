# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open n the template in the editor.

__author__ = "Owner"
__date__ = "$12 Sep, 2015 5:17:25 PM$"


import nltk, re, pprint
'''if __name__ == "__main__":
    print "Hello World"'''
from nltk.book import *


from nltk import word_tokenize
fneg=open("C:\\Users\\Owner\\Documents\\NetBeansProjects\\SMM\\src\\neg.wn","r")
neg=fneg.readlines()
negwordlist=[]
for i in neg:
    i=i.rstrip("\n")
    #i=i.decode('utf-8')
    negword=i.split("_")
    #print negword
    negwordlist.append(negword)
#print negwordlist
negstringlist=[]
for x in negwordlist:
    substring=' '.join(x)
    negstringlist.append(substring)
for x in negstringlist:
    print x

fpos=open("C:\\Users\\Owner\\Documents\\NetBeansProjects\\SMM\\src\\pos.wn","r")
pos=fpos.readlines()
poswordlist=[]
for i in pos:
    i=i.rstrip("\n")
    #i=i.decode('utf-8')
    posword=i.split("_")
 #   print posword
    poswordlist.append(posword)
#print poswordlist
posstringlist=[]
for x in poswordlist:
    substring=' '.join(x)
    posstringlist.append(substring)
for x in posstringlist:
    print x

#from nltk.book import *
#print text1
#print type(text1)
fnegt=open("C:\\Users\\Owner\\Documents\\NetBeansProjects\\SMM\\src\\negTweets.txt","r")
negt=fnegt.readlines()
justcounter=1
for i in negt:
    #i=i.decode('utf8')
    print "\n\n", justcounter
    justcounter=justcounter+1
    print i
    print "character length", len(i)
    j=i.decode('utf8')
    tokensnegt = word_tokenize(j)
    #print tokensnegt
    textnegt = nltk.Text(tokensnegt)
    #print textnegt
    print "word count", len(textnegt)
    count=0
    for x in negstringlist:
        if x in i:
            print x
            count=count+1
    print "negative words ", count 
    count=0
    for x in posstringlist:
        if x in i:
            print x
            count=count+1
    print "positive words ", count 
    print "Lexical diversity", (float(len(set(textnegt))) / float(len(textnegt)))
    
fpost=open("C:\\Users\\Owner\\Documents\\NetBeansProjects\\SMM\\src\\posTweets.txt","r")
post=fpost.readlines()
justcounter=1
for i in post:
    #i=i.decode('utf8')
    print "\n\n", justcounter
    justcounter=justcounter+1
    print i
    print "character length", len(i)
    j=i.decode('utf8')
    tokenspost = word_tokenize(j)
    #print tokensnegt
    textpost = nltk.Text(tokenspost)
    #print textnegt
    print "word count", len(textpost)
    count=0
    for x in negstringlist:
        if x in i:
            print x
            count=count+1
    print "negative words ", count 
    count=0
    for x in posstringlist:
        if x in i:
            print x
            count=count+1
    print "positive words ", count 
    print "Lexical diversity", (float(len(set(textpost))) / float(len(textpost)))


    #i=i.decode('utf8')
print "For text1"
strtext1=' '.join(text1)
#print "character length", len(i)



print "char count", len(strtext1)

print "word count", len(text1)
textset1=set(text1)
count=0
for x in negstringlist:
    if x in textset1:
        print x
        count=count+1
print "negative words ", count 
count = 0


for x in posstringlist:
    if x in textset1:
        print x
        count=count+1
print "positive words ", count 
print "Lexical diversity", (float(len(set(text1))) / float(len(text1)))

'''
#print negt
#print post
#print ("heya")

#print neg

#print pos
#print heya
tokenspost = word_tokenize(post)
print type(tokenspost)
tokensnegt = word_tokenize(negt)
print type(tokensnegt)
postweet = nltk.Text(tokenspost)
print type(postweet)
negtweet = nltk.Text(tokensnegt)
print type(negtweet)
print ("hey")
print '''

fnegt.close()
fpost.close()
fneg.close()
fpos.close()