import requests

from bs4 import BeautifulSoup
import pandas as pd

def GetSentence(verb):
    # URL of the website to scrape
    url = "https://www.slovo.app/nl/"+verb
    
    # Send an HTTP GET request to the website
    response = requests.get(url)
    
    # Parse the HTML code using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    
    firstTable =[]
    
    subject=[]
    presensVerbum=[]
    imperfectumVerbum=[]
    perfectumVerbum=[]
    
    for td in soup.find_all('td'):
        firstTable.append(td.text);
        
    for i in range(0, len(firstTable)):
        if(i%4==0):
            subject.append(firstTable[i])
        elif(i%4==1):
            presensVerbum.append(firstTable[i])
        elif(i%4==2):
            imperfectumVerbum.append(firstTable[i])
        elif(i%4==3):
            perfectumVerbum.append(firstTable[i])
 

    liList=soup.find_all('li')
    liLen=len(liList)
    verblist=[]
    presens=[]
    imperfectum=[]
    perfectum=[]
    for x in range(0,liLen):
        if x<5:
            presens.append(liList[x].text)
        elif x<10:
            imperfectum.append(liList[x].text)
        else:            
            perfectum.append(liList[x].text)
            verblist.append(verb)

   
    
    presens.append('')
    imperfectum.append('')           
    perfectum.append('')
    verblist.append(verb)

    df=pd.DataFrame({'Verb':verblist,'Subject':subject,'PresensVerbum':presensVerbum,'ImperfectumVerbum':imperfectumVerbum,'PerfectumVerbum':perfectumVerbum, 'Presens':presens,'Imperfectum':imperfectum,'Perfectum':perfectum})
    # print(verb)
    return df
    
    


my_file = open("verbum0.txt", "r") 
  
# reading the file 
data = my_file.read() 
  
# replacing end splitting the text  
data_into_list = data.split("\n") 
# print(data_into_list) 
my_file.close() 

result=[]
# example
# result.append(GetSentence('beginnen'))
for verb in data_into_list:    
    try:
        result.append(GetSentence(verb))
    except Exception:
        print(verb)
        continue


df=pd.concat(result)

df.to_csv('out.csv', index=False)  