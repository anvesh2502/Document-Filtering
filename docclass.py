import re
import math

def getwords(doc) :

    splitter=re.compile('\\W*')
    #Split the words by non-alpha characters
    words=[s.lower() for s in splitter.split(doc) if len(s)>2 and len(s)<20]

    # Return the unique set of words only
    return dict([(w,1) for w in words])


class classifier :

    def __init__(self,getfeatures,filename=None) :
        # Counts of feature/category combinations
        self.fc={}
        # Counts of documents in each category
        self.cc={}
        self.getfeatures=getfeatures
