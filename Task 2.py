import nltk
from nltk import bigrams
from nltk.probability import FreqDist, ConditionalFreqDist

browns=nltk.corpus.brown.words()
refined_brown=[x.lower() for x in browns]


user_sentence = input("Enter a sentence: ").strip()

user_sentence = user_sentence.lower()

def NGrams(sentence):
    start_symbol = '<s> '
    end_symbol = ' </s>'
    start_probability = 0.25
    end_probability = 0.25
    probability = start_probability

    tokens = nltk.word_tokenize(sentence)
    bigrams_list = list(bigrams(refined_brown)) 

    unigram_freq = FreqDist(refined_brown)
    cfd = ConditionalFreqDist(bigrams_list)
    print('{:<22}|{:>22}'.format('Bigram', 'Probability'))
    for i in range(len(tokens) - 1):
        current_bigram = (tokens[i], tokens[i + 1])
        print(cfd[tokens[i]][tokens[i + 1]], unigram_freq[tokens[i]])
        if not unigram_freq[tokens[i]]:
            bigram_probability=0
        else:
            bigram_probability = cfd[tokens[i]][tokens[i + 1]]/ unigram_freq[tokens[i]]
        print(bigram_probability)
        probability *= bigram_probability
        print('{:<22}|{:>22}'.format(str(current_bigram), bigram_probability))
    print("===============================")  
    probability *= end_probability
    
    print("Sentence:",user_sentence)
    print("\nLowercase sentence:",user_sentence)
    print("Probability:", probability)

NGrams(user_sentence)

