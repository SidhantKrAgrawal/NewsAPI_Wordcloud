
import requests
import json
from wordcloud import WordCloud,STOPWORDS
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#endpoints
print("1. Everything") #retrieves every information


print("2. Top headlines based on a particular category") #retrieves top headlines from a particular news source
end=int(input("enter your choice:  "))
if end==1:
    api_url="https://newsapi.org/v2/everything"
    ct=input("enter name of desired topic:  ")
elif end==2:
    print("categories: ")
    print("1. Business")
    print("2. Entertainment")
    print("3. General")
    print("4. Health")
    print("5. Science")
    print("6. Sports")
    print("7. Technology")
    catg=int(input("enter your favorable category:  "))
    if catg==1:
        print("Bitcoin")
        print("Cryptocurrency")
        print("Stock market")
        print("GDP")
        print("Economy")
        print("Census")
        print("Startups")
        print("Entreprenuership")
        ct=input("enter your choice:  ")
    elif catg==2:
        print("Hollywood")
        print("Netflix")
        print("HBO")
        print("TV Shows")
        ct=input("enter your choice:  ")  
    elif catg==3:
        print("Headlines")
        print("Current affairs")
        ct=input("enter your choice:  ")
    elif catg==4:
        print("Covid 19")
        print("Heart")
        print("Exercises")   
        ct=input("enter your choice:  ")
    elif catg==5:
        print("Physics")
        print("Chemistry")
        ct=input("enter your choice:  ")         
     
    elif catg==6:
        print("Football")
        print("Cricket")
        print("Rugby")
        print("Soccer")
        print("Hockey")
        print("Athletics")
        print("Shooting")
        ct=input("enter your choice:  ")
     
           
    elif catg==7:
        ct=input("enter your choice:  ")
        

    
        
    api_url="https://newsapi.org/v2/top-headlines"



api_key="6045ea0c57c2405d8f756482c990b924"

query_parms={"q":ct,"from":"2022-04-03","sortBy":"relevance","apiKey":api_key}

resp=requests.get(api_url,params=query_parms)

data=resp.json()
n=3
file_words=""
for i in range(n):
#pprint.pp(data)
    x=data["articles"][i]["content"]
    #x=x-x[-10:] 
    file_words+=str(x)

stop_w=set(STOPWORDS)
print()
print("Enter the Shape :")
print("1. India map")
print("2. apple ")
print("3. africa map")

r=int(input())

if r==1:
    mask = np.array(Image.open('india.jpg'))
elif r==2:
    mask = np.array(Image.open('apple4.jpg'))    
elif r==3:
    mask = np.array(Image.open('africa.jpeg'))


w=mask.shape[1]
h=mask.shape[0]
word_cloud=WordCloud(stopwords=stop_w,background_color='white',mask=mask,width=(3*w),height=(3*h)).generate(file_words)



plt.imshow(word_cloud, interpolation="bilinear")
plt.axis('off')
plt.show()