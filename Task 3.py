import nltk
from nltk.corpus import brown,stopwords
from nltk import bigrams, FreqDist,ConditionalFreqDist

words_in_brown=brown.words()
eng_stopwords=set(stopwords.words())
filtered_brown_words=[x.lower() for x in words_in_brown if x.lower() not in eng_stopwords and str(x).isalpha()]

bigram_model=list(bigrams(filtered_brown_words))
bigram_frequency=FreqDist(filtered_brown_words)
conditional_frequency=ConditionalFreqDist(bigram_model)


final_sentence=''

def Retry():
    global final_sentence
    user_word = input("Enter a word: ")
    user_word = user_word.lower()
    print(user_word)
    if user_word not in filtered_brown_words:
        t=int(input(print("\n'1' to try again\n'2' to quit")))
        match t:
            case 1:	Retry()
            case 2:	Quit()
    else:
        final_sentence+=user_word
        builtSentence(user_word)

def builtSentence(user_word):
    global final_sentence
    most_likely_follwing_3=get_most_likely_follwing_words(user_word)
    # print(probs)
    # print(most_likely_follwing_3)
    print("Which word should follow:?\n") 

    for i, (word, prob) in enumerate(most_likely_follwing_3, start=1):
        probability = prob / conditional_frequency[user_word].N()
        print(f"{i}. {word} P({user_word} {word}): {probability}")
    t2 = int(input("\nSelect '1', '2', '3' or '4' to quit: "))

    while(1):
        if t2==2:
            final_sentence =final_sentence+ " "+most_likely_follwing_3[1][0]   
            print("\nSentence:",final_sentence,"...")
            builtSentence(most_likely_follwing_3[1][0])
        elif t2==3: 
            final_sentence =final_sentence+" "+most_likely_follwing_3[2][0]
            print("\nSentence:",final_sentence,"...")
            builtSentence(most_likely_follwing_3[2][0]) 
        elif t2==4: 
            Quit()   
        else:
            final_sentence =final_sentence+" "+ most_likely_follwing_3[0][0]  
            print("\nSentence:",final_sentence,"...")
            builtSentence(most_likely_follwing_3[0][0])

def get_most_likely_follwing_words(user_word):
    most_likely_follwing_3=conditional_frequency[user_word].most_common(3)
    return most_likely_follwing_3
    
def Quit():
    global final_sentence
    if final_sentence=='':
        print("Empty string")
    else:
        print("Generated sentence:",final_sentence)
    quit()

Retry()

