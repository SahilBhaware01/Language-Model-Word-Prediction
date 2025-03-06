Objectives:       

  1.Perform basic word frequency distribution analysis for a text corpus.
                   
  2.Calculate probability of a sentence.
  
  3.Build Language Model word prediction.


Coupara Used:     

  1.Brown Corpus
  
  2.Reuters Corpus

1.Displayed a top ten (ranks 1 through 10) words for BOTH corpora on screen 
2.Generated log(rank) vs log(frequency) plots for the first 1000 (ranks 1 through 1000) words for BOTH corpora 
3.Used frequency counts obtained earlier to calculate the unigram occurrence probability for the TWO (“technical” and not technical) words



TASK 1: Building a Bigram Language Model

1.Enter a Sentence:
  •When prompted, type a sentence of your choice and press Enter.
  •Ensure the sentence has at least two words for bigram analysis.

2.Understand Preprocessing:
  •Your sentence will be automatically converted to lowercase to maintain consistency.
  •This step ensures that words like "Hello" and "hello" are treated the same.

3.How Probabilities are Calculated:
  •The program will split your sentence into pairs of consecutive words, called bigrams (e.g., "I am" and "am happy").
  •Each bigram’s probability is calculated based on a predefined rule:
    •0.25 for bigrams that start or end the sentence.
  •The final probability P(S) of the sentence is the product of all bigram probabilities.

4.The program will display:
  •Your original sentence
  •All bigrams created from your sentence
  •Probability of each bigram
  •Final probability P(S) of the entire sentence (even if it is zero).



TASK 2: Building a Sentence with a 2-Gram Language Model

1.Start with the First Word (W1):
  •When prompted, enter an initial word (W1) and press Enter.
  •The word will be automatically converted to lowercase for uniformity.
  •If the entered word is not in the corpus, you will get two options:
    a. Enter a different word.
    b. Type QUIT to exit the program.

2.Choose the Next Word:
  •Based on your first word (W1), the program will display a menu with the TOP 3 words most likely to follow along with their probabilities.
  •Select an option by typing the corresponding number (1, 2, 3, or 4) and press Enter.

3.Handling Incorrect Choices:
  •If you type a number other than 1, 2, 3, or 4, the program will automatically choose option (1) for you.
  •The newly chosen word will be added to your sentence.

4.Continue or Quit:
  •The menu will reappear with the next set of words based on your last choice.
  •Repeat the process to build your sentence until you choose option (4) QUIT.
  •After quitting, the program will display your final sentence and exit.
