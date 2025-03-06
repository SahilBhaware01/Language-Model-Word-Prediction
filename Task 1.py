import nltk
from nltk.corpus import reuters, brown, stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

eng_stopwords=set(stopwords.words('english'))
words_brown=brown.words()
words_reuters=reuters.words()

filtered_brown=[]
for i in words_brown:
    if i not in eng_stopwords:
        filtered_brown.append(i)

filtered_reuters=[]
for i in words_reuters:
    if i not in eng_stopwords:
        filtered_reuters.append(i)        

words_freq_brown=FreqDist(filtered_brown)
words_freq_reuters=FreqDist(filtered_reuters)

# Part 1============================================================
print("\nPart 1")
print("word freq distribution brown:\t",words_freq_brown)
print("word freq distribution reuters:\t",words_freq_reuters)

# Part 2============================================================
print("\nPart 2")
most_common_words_brown=words_freq_brown.most_common(10)
most_common_words_reuters=words_freq_reuters.most_common(10)
print("\nmost_common_words_brown:")
for word, frequency in most_common_words_brown:
    print(f"\t[{word}]: {frequency}")
print("\nmost_common_words_reuters:")    
for word, frequency in most_common_words_reuters:
    print(f"\t[{word}]: {frequency}")    

# Part 3============================================================
print("\nPart 3")
# Brown----
print("\nBrown")
frequencies_brown=np.array(list(words_freq_brown.values()))
log_frequencies_brown=np.log(frequencies_brown)
log_frequencies_brown=np.sort(log_frequencies_brown)[::-1]
ranks_brown = np.arange(1,len(frequencies_brown)+1, +1)

print(log_frequencies_brown)
data_brown=list(zip(ranks_brown,log_frequencies_brown))
df=pd.DataFrame(data_brown,columns=['log(ranks)','log(frequencies)'])
import plotly.express as px

fig = px.line(df.head(100),x='log(frequencies)',y='log(ranks)',title="log(rank) vs log(frequency) for the first 1000 words of Brown Corpus ")
fig.show()

# Reuters----------------------------------------------------------------------------
print("\nReuters")
frequencies_reuters=np.array(list(words_freq_reuters.values()))
log_frequencies_reuters=np.log(frequencies_reuters)
log_frequencies_reuters=np.sort(log_frequencies_reuters)[::-1]
ranks_reuters= np.arange(1,len(frequencies_reuters)+1, +1)

data_reuters=list(zip(ranks_reuters,log_frequencies_reuters))
df2=pd.DataFrame(data_reuters,columns=['log(ranks)','log(frequencies)'])
import plotly.express as px

fig = px.line(df2.head(100),x='log(frequencies)',y='log(ranks)',title="log(rank) vs log(frequency) for the first 1000 words of Reuters Corpus ")
fig.show()

