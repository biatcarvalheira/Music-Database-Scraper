
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from listUrl import UrlList




from time import sleep
from random import randint



category = []
name = []
datePlace = []
otherInfo = []
works = []
itemList = []
relatedEvents = []
exhibits = []
bio = []
  
page = range (0,100)

count = 0

for pages in page :
    
    
    page = requests.get(UrlList[count])
   
    print (count)
   
    count +=1
    
    html_soup = BeautifulSoup(page.text, 'html.parser')
    
    artist_items = html_soup.find_all('main', class_= "container")
    
    sleep(randint(2,10))
    
    for container in artist_items:
    
        
    #category    
        cat = container.find ('div', class_="kicker").text
    
        if cat:    
            category.append(cat)
        else: 
            category.append("None")
        
        
    #name
        n = container.find ('h1', class_="border-top-5 mt-3 pt-3 pb-2 mb-0").text
        
        if n: 
            name.append(n)
        else: 
            name.append("None")
            
            
    #Date and Place of birth and death
        date = container.find ('div', class_="additional-information border-top-1 mt-3 pt-3")
        
        if date: 
            date = container.find ('div', class_="additional-information border-top-1 mt-3 pt-3").text

            datePlace.append(date)
        else: 
            datePlace.append("None")
       
        
    #Other information (Alias, Occupation, Family, Related Artists)
        other = container.find_all('aside', class_="col-sm-4 order-sm-2 border-top-5 pt-3")
        if other: 
            for secondContainer in other:
                    d = secondContainer.find('ul').text.strip()
                    otherInfo.append(d)  
        else: 
            otherInfo.append.append("None")  
          
            
    #Works
        w = container.find_all('article', class_="row no-gutters")
        itemList.clear()
        if w:
             for thirdContainer in w:
                 k = thirdContainer.find('h1', class_="mb-0").text.strip()
                 #print(k)
                 itemList.append(k + ",")
                 
        else:
            itemList.append("None")
        
        str1 = ''.join(itemList)
        works.append(str1)
        
        
        
    #Biography Text
        b = container.find ('section', class_="info").text
        
        if b:
            bio.append(b)
            print(b)
        else: 
            bio.append("None")


print(works)
artists = pd.DataFrame({
'Categoria': category,
'Nome': name,
'Data e Lugar': datePlace,
'Outra grafia, habilidades, familiares, artistas relacionados': otherInfo, 
'Works': works,
'Biography': bio
})



#print (artists)


artists.to_excel('artista_teste_100_v2.xlsx')