#Implementation of program 1 and 2 from page 413.
#String manipulation

from string import ascii_lowercase
def fixSentence(sentence):

    sentence.strip()
    sentence = sentence.lower()
    sentence = sentence.capitalize()
    sentence = " ".join(sentence.split())
    return sentence
        
def countLetters(sentence):
    wordCount = len(sentence.split())
    sentence = sentence.lower()
    letters = [[]]
    for c in ascii_lowercase:
        letters.append([c, 0])
    letters.pop(0)
    for x in range(len(sentence)):
        for y in range(len(ascii_lowercase)):
            if(sentence[x] == ascii_lowercase[y]):
                temp = int(letters[y][1]) + 1
                letters[y][1] = temp
    print(str(wordCount) + " words")
    for y in range(len(ascii_lowercase)):
        if(letters[y][1] > 0):
            print(str(letters[y][1]) + " " + letters[y][0])

testSentence = "the    Answer to life, the Universe, and everything IS 42."
testSentence = fixSentence(testSentence)
testSentence = "I say Hi."
countLetters(testSentence)