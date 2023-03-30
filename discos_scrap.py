
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from discos_lista import UrlList




from time import sleep
from random import randint



category = []
name = []


valueList1 = []
labelList1 = []

labelList2 = []
valueList2 = []

labelList3 = []
valueList3 = []


labelList4 = []
valueList4 = []


labelList5 = []
valueList5 = []


linkList = []

lbList = []


idList = []
idLComplete = []



  
page = range (0,2807)

count = 550

for pages in page :
    
    page = requests.get(UrlList[count])
    
    
    check = str(page)
    
    print(count)
     
    count +=1  
    
        
    
    html_soup = BeautifulSoup(page.text, 'html.parser')
    
    
    
    disc_IndvItems = html_soup.find_all('div', class_= "col-12-xs-12 col-12-sm-8 col-12-md-7")
    
    
    
   
    sleep(randint(2,10))
    
    
    for container in disc_IndvItems:
        
    
   #counting the number of labels and finding the labels
        
        firstLabel_list = container.find_all('div', class_="col-12-xs-4 col-12-sm-3 col-12-sm-3 property-label")

        
        flabel_list_length = len(firstLabel_list)
               
        label_list = container.find_all ('div', class_="col-12-xs-4 col-12-sm-3 property-label")
        
        label_list_length = len(label_list)
        
        totalLength = flabel_list_length + label_list_length
        
        #finding the values
        
        firstValue_list = container.find_all ('div', class_="col-12-xs-8 col-12-sm-9 col-12-sm-9 property-value")
        
        
        value_list = container.find_all('div', class_="col-12-xs-8 col-12-sm-9 property-value")




#N O  L A B E L 

    if totalLength == 0: 
                
      #CATEGORY
        cat = container.find('h3').text
        category.append(cat)
    
    
    
        #NAME
        n = container.find('h1', class_="color1").text
        name.append(n)
        
        
        #LABELS        
       
    
        label1 = "None"
        label2 = "None"
        label3 = "None"
        label4 = "None"
        label5 = "None"
        labelList1.append(label1)
        labelList2.append(label2)
        labelList3.append(label3)
        labelList4.append(label4)
        labelList5.append(label5)
            
        
        
        
        #VALUES
        
        value1 = "None"
        value2 = "None"
        value3 = "None"
        value4 = "None"
        value5 = "None"
        valueList1.append(value1)
        valueList2.append(value2)
        valueList3.append(value3)
        valueList4.append(value4)
        valueList5.append(value5)






#1 L A B E L 

    if totalLength == 1: 
                
      #CATEGORY
        cat = container.find('h3').text
        category.append(cat)
    
    
    
        #NAME
        n = container.find('h1', class_="color1").text
        name.append(n)
        
        
        #LABELS        
       
        marker3 = 1
        
        while marker3 <= 1:
            if flabel_list_length == 0: 
                label1 = label_list[0].text
            else:
                label1 = firstLabel_list[0].text
            label2 = "None"
            label3 = "None"
            label4 = "None"
            label5 = "None"
            labelList1.append(label1)
            labelList2.append(label2)
            labelList3.append(label3)
            labelList4.append(label4)
            labelList5.append(label5)
            marker3 +=1
        
        
        
        #VALUES
        
        marker4 = 1
        
        while marker4 <=1:
            if flabel_list_length == 0:
                value1 = value_list[0].text
            else: 
                value1 = firstValue_list[0].text
            value2 = "None"
            value3 = "None"
            value4 = "None"
            value5 = "None"
            valueList1.append(value1)
            valueList2.append(value2)
            valueList3.append(value3)
            valueList4.append(value4)
            valueList5.append(value5)
            marker4 +=1
    
    
#2 L A B E L S
    
    if totalLength == 2: 
        
        #CATEGORY
        cat = container.find('h3').text
        category.append(cat)
       
    
    
    
        #NAME
        n = container.find('h1', class_="color1").text
        name.append(n)
        
        
        #LABELS        
       
        marker3 = 1
        
        while marker3 <= 1:
            if flabel_list_length == 0: 
                label1 = label_list[0].text
                label2 = label_list[1].text
            else:
                label1 = firstLabel_list[0].text
                label2 = label_list[0].text
            label3 = "None"
            label4 = "None"
            label5 = "None"
            labelList1.append(label1)
            labelList2.append(label2)
            labelList3.append(label3)
            labelList4.append(label4)
            labelList5.append(label5)
            marker3 +=1
        
        
        
        #VALUES
        
        marker4 = 1
        
        while marker4 <=1:
            if flabel_list_length == 0: 
                value1 = value_list[0].text
                value2 = value_list[1].text
            else: 
                value1 = firstValue_list[0].text
                value2 = value_list[0].text
            value3 = "None"
            value4 = "None"
            value5 = "None"
            valueList1.append(value1)
            valueList2.append(value2)
            valueList3.append(value3)
            valueList4.append(value4)
            valueList5.append(value5)
            marker4 +=1
 
            
 
#3 L A B E L S     
        
    if totalLength == 3: 
        
        
              #CATEGORY
        cat = container.find('h3').text
        category.append(cat)
    
    
    
        #NAME
        n = container.find('h1', class_="color1").text
        name.append(n)
        
        
        #LABELS        
       
        marker3 = 1
        
        while marker3 <= 1:
            
            if flabel_list_length == 0:
                label1 = label_list[0].text
                label2 = label_list[1].text
                label3 = label_list[2]
            else: 
                label1 = firstLabel_list[0].text
                label2 = label_list[0].text
                label3 = label_list[1].text
            label4 = "None"
            label5 = "None"
            labelList1.append(label1)
            labelList2.append(label2)
            labelList3.append(label3)
            labelList4.append(label4)
            labelList5.append(label5)
            marker3 +=1
        
        
        
        #VALUES
        
        marker4 = 1
        
        while marker4 <=1:
            if flabel_list_length == 0: 
                value1 = value_list[0].text
                value2 = value_list[1].text
                value3 = value_list[2].text
            else: 
                value1 = firstValue_list[0].text
                value2 = value_list[0].text
                value3 = value_list[1].text
            value4 = "None"
            value5 = "None"
            valueList1.append(value1)
            valueList2.append(value2)
            valueList3.append(value3)
            valueList4.append(value4)
            valueList5.append(value5)
            marker4 +=1
 
    

#4 L A B E L S
    
    if totalLength == 4: 
        
              #CATEGORY
        cat = container.find('h3').text
        category.append(cat)
    
    
    
        #NAME
        n = container.find('h1', class_="color1").text
        name.append(n)
        
        
        #LABELS        
       
        marker3 = 1
        
        while marker3 <= 1:
            if flabel_list_length == 0:
                label1 = label_list[0].text
                label2 = label_list[1].text
                label3 = label_list[2].text
                label4 = label_list[3].text
            else: 
                label1 = firstLabel_list[0].text
                label2 = label_list[0].text
                label3 = label_list[1].text
                label4 = label_list[2].text
            label5 = "None"
            labelList1.append(label1)
            labelList2.append(label2)
            labelList3.append(label3)
            labelList4.append(label4)
            labelList5.append(label5)
            marker3 +=1
        
        #VALUES
        
        marker4 = 1
        
        while marker4 <=1:
            if flabel_list_length == 0:
                value1 = value_list[0].text
                value2 = value_list[1].text
                value3 = value_list[2].text
                value4 = value_list[3].text
            else: 
                value1 = firstValue_list[0].text
                value2 = value_list[0].text
                value3 = value_list[1].text
                value4 = value_list[2].text
            value5 = "None"
            valueList1.append(value1)
            valueList2.append(value2)
            valueList3.append(value3)
            valueList4.append(value4)
            valueList5.append(value5)
            marker4 +=1
         
            
    #5 L A B E L S
    
    if totalLength == 5: 
        
              #CATEGORY
        cat = container.find('h3').text
        category.append(cat)
    
    
    
        #NAME
        n = container.find('h1', class_="color1").text
        name.append(n)
        
        
        #LABELS        
       
        marker3 = 1
        
        while marker3 <= 1:
            if flabel_list_length == 0:
                label1 = label_list[0].text
                label2 = label_list[1].text
                label3 = label_list[2].text
                label4 = label_list[3].text
                label5 = label_list[4].text
            else: 
                label1 = firstLabel_list[0].text
                label2 = label_list[0].text
                label3 = label_list[1].text
                label4 = label_list[2].text
                label5 = label_list[3].text
            labelList1.append(label1)
            labelList2.append(label2)
            labelList3.append(label3)
            labelList4.append(label4)
            labelList5.append(label5)
            marker3 +=1
        
        #VALUES
        
        marker4 = 1
        
        while marker4 <=1:
            if flabel_list_length == 0:
                value1 = value_list[0].text
                value2 = value_list[1].text
                value3 = value_list[2].text
                value4 = value_list[3].text
                value5 = value_list[4].text
            else: 
                value1 = firstValue_list[0].text
                value2 = value_list[0].text
                value3 = value_list[1].text
                value4 = value_list[2].text
                value5 = value_list[3].text
            valueList1.append(value1)
            valueList2.append(value2)
            valueList3.append(value3)
            valueList4.append(value4)
            valueList5.append(value5)
            marker4 +=1      
            
            
           
    
    #TRACKNAMES           
    
    trackListItems = html_soup.find_all('div', class_="shiro-content-box tracklist")  
    
    length = len(trackListItems)
    idList.clear()
    
    marker10 = 0
    
    if length == 0: 
        
        idLComplete.append("None")
    
    
    else:
        
        
        for secondContainer in trackListItems:
            
            i = str(trackListItems[marker10])
            
            fullItem = ("CODIGO:",i, ",")
            
            fIStr = str(fullItem)
            
            
            f = fIStr.find("data-list=")
       
            s = slice(f,(f+18))
        
        
            #print(fIStr[s])
        
            dI = fIStr[s] + ", "
         
            s2 = slice(11,17)
            
            data_list_ok = dI[s2] + ', '
            
            print(data_list_ok)
            
            idList.append(data_list_ok)
            
            marker10 +=1
            
    
        str1 = ''.join(idList)
        idLComplete.append(str1)
        
   
    
    
    fonograms = pd.DataFrame({
    'Categoria': category,
    'Titulo': name,
    'Label 1': labelList1,
    'Value 1': valueList1,
    'Label 2': labelList2, 
    'Value 2': valueList2, 
    'Label 3': labelList3,
    'Value 3': valueList3, 
    'Label 4': labelList4,
    'Value 4': valueList4,
    'Label 5': labelList5,
    'Value 5': valueList5,
    'Data-List': idLComplete,
    
        })   




    fonograms.to_excel('discos_dia1.xlsx')
   
    



   