import nltk
from nltk.corpus import stopwords
import operator
from wordcloud import WordCloud
import matplotlib.pyplot as plt 
import csv
 
 
file_ob = open(r"jobTitle.csv", encoding="utf8") 
  
reader_ob = csv.reader(file_ob) 
  
reader_contents = list(reader_ob) 
  
text = "" 
 
for row in reader_contents : 
      
   
    for word in row : 
  
        text = text + " " + word 
   
wordcloud = WordCloud(width=680, height=580, max_words=50,stopwords=stopwords.words('english'), background_color="white").generate(text) 

plt.figure() 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("on") 
plt.margins(x=0, y=0) 
plt.show()
