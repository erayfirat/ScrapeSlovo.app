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
    secondTable =[]
    line=[]
    
    for td in soup.find_all('td'):
        firstTable.append(td.text);
    
    for i in range(0, len(firstTable)):
        line.append(firstTable[i])
        if(i%4==3):
            secondTable.append(' '.join(line))
            line=[]
    
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
    # print(len(verblist))
    # print(len(secondTable))
    # print(len(presens))
    # print(len(imperfectum))
    # print(len(perfectum))
    df=pd.DataFrame({'Verb':verblist,'General':secondTable, 'Presens':presens,'Imperfectum':imperfectum,'Perfectum':perfectum})
    # print(verb)
    return df
    
    


my_file = open("verbum0.txt", "r") 
  
# reading the file 
data = my_file.read() 
  
# replacing end splitting the text  
# when newline ('\n') is seen. 
data_into_list = data.split("\n") 
# print(data_into_list) 
my_file.close() 

result=[]
for verb in data_into_list:
    
    try:
        result.append(GetSentence(verb))
    except Exception:
        print(verb)
        continue


df=pd.concat(result)
# verb='praten'

#df1=pd.DataFrame(result,columns=['verb','Presens','Imperfectum','Perfectum','-'])

# sentences=[]
# for row in soup.select('table.lister-list tr'):
#     title = row.find('td', class_='titleColumn').find('a').get_text()
#     year = row.find('td', class_='titleColumn').find('span', class_='secondaryInfo').get_text()[1:-1]
#     rating = row.find('td', class_='ratingColumn imdbRating').find('strong').get_text()
#     sentences.append([title, year, rating])



# Extract the relevant information from the HTML code
# movies = []
# for row in soup.select('tbody.lister-list tr'):
#     title = row.find('td', class_='titleColumn').find('a').get_text()
#     year = row.find('td', class_='titleColumn').find('span', class_='secondaryInfo').get_text()[1:-1]
#     rating = row.find('td', class_='ratingColumn imdbRating').find('strong').get_text()
#     movies.append([title, year, rating])

# # Store the information in a pandas dataframe
# df = pd.DataFrame(movies, columns=['Title', 'Year', 'Rating'])

# # Add a delay between requests to avoid overwhelming the website with requests
# time.sleep(1)
