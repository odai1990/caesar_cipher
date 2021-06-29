import nltk

alphabet='abcdefghijklmnopqrstuvwxyz'

def encrypt(sentence,num):
    words=sentence.split()
    newWords=[]
    for word in words:
        newWord=''
        for i in word:
            number=(alphabet.index(i)+num) %26
            newWord+=(alphabet[number])
        newWords.append(newWord)
    return " ".join(newWords)


def decrypt(encrypted,key):
    return encrypt(encrypted,-key)


def count_valid_english_words(sentence):
    """
    returns number of valid English words in the sentence
    
    """
    nltk.download('words')

    english_words = nltk.corpus.words.words()

    words = sentence.split()
    counter = 0

    for word in words:
        if word in english_words or word.lower() in english_words or word.upper() in english_words:
            counter += 1
    return counter


def crack(encrypted):
    counter=[]
    maximum=0
    for i in range(0,26):
        sentence= decrypt(encrypted,i)
        counter.append(count_valid_english_words(sentence))
        if count_valid_english_words(sentence)>maximum:
            maximum=count_valid_english_words(sentence)
    key=counter.index(maximum)
    decrypted=decrypt(encrypted,key)
    return decrypted