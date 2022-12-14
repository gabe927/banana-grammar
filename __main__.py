from english_words import english_words_set
import itertools

charCount = {
    'a':13,
    'b':3,
    'c':3,
    'd':6,
    'e':18,
    'f':3,
    'g':4,
    'h':3,
    'i':12,
    'j':2,
    'k':2,
    'l':5,
    'm':3,
    'n':8,
    'o':11,
    'p':3,
    'q':2,
    'r':9,
    's':6,
    't':9,
    'u':6,
    'v':3,
    'w':3,
    'x':2,
    'y':3,
    'z':2
}

playableWords = []
unplayableWords = []

def checkWord(w):
    counts = charCount.copy()
    for i in w:
        if (counts[i] == 0):
            return False
        else:
            counts[i] -= 1
    return True

for w in english_words_set:
    lw = w.lower()
    try:
        if checkWord(lw):
            playableWords.append(lw)
        else:
            unplayableWords.append(lw)     
    except KeyError:
        unplayableWords.append(lw)

print(unplayableWords)
print(f"Number of words in dictionary: {len(english_words_set)}")
print(f"Number of playable words: {len(playableWords)}")
print(f"Number of un-playable words: {len(english_words_set) - len(playableWords)}")