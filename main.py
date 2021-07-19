

from mspresidio import anonymize
import re
text = []

with open("data/news.2017.et.shuffled") as f:
    text = f.readlines()[:1000]



text = [anonymize(t) for t in text]

with open("anonymized.txt",'w') as f:
    f.writelines(text)

def hide_names():
    pass

def hide_capital_letters():
    pass


def correct_mispelling():
    pass

def substitute_locs():
    pass

def substitute_people():
    pass

def substitute_dates():
    pass
