

from mspresidio import anonymize

text = []

with open("data/news.2017.et.shuffled") as f:
    text = f.readlines()[:1000]



text = [anonymize(t) for t in text]

with open("anonymized.txt",'w') as f:
    f.writelines(text)



def correct_mispelling():
    pass

def substitute_locs():
    pass

def substitute_people():
    pass

def substitute_dates():
    pass
