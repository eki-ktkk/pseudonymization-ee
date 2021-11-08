from mspresidio import anonymize, hide_names, hide_dates

text = []

with open("karis.txt") as f:
    text = f.readlines()[:1000]

text = [anonymize(t) for t in text]
text = [t.text for t in text]
text = [hide_dates(t, '<DATE>') for t in text]
text = [hide_names(t, '<PERSON>') for t in text]

print(text[0])

with open("../anonymized.txt", 'w') as f:
    f.writelines(text)
