import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()
save_to_file = open('corpora/clean_neg/neg61.txt', 'w')
with open('corpora/neg/neg61.txt', 'r') as fileinput:
    for line in fileinput:
        line = line.lower()#lowercase
        table = str.maketrans({key: None for key in string.punctuation}) ##Cleansing(tanda baca)
        line = line.translate(table)
        line = line.strip()
        line = stemmer.stem(line) ##Normalisasi/
        save_to_file.write(line)
