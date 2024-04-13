import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/all/~cs-e4e13890860d1ca22d1230d34dffd153/pr?sid=jek,p31,trv&marketplace=FLIPKART&restrictLocale=true")
soup=BeautifulSoup(response.content,"html.parser")
names=soup.find_all('div',class_='_4rR01T')
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)

prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)

ratings=soup.find_all('div',class_='gUuXy-')
rate=[]
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(d)

reviews=soup.find_all('span',class_='_2_R_DZ')
review=[]
for i in reviews[0:20]:
    d=i.get_text()
    review.append(d)

features=soup.find_all('li',class_='rgWa7D')
feature=[]
for i in features[0:20]:
    d=i.get_text()
    feature.append(d)
   
links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com"+i['href']
    link.append(d)

images=soup.find_all('img',class_='_396cs4')
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
    
#print(image)

# df=pandas.DataFrame({"Names":pandas.Series(name),
#                      "Prices":price,
#                      "Rateing":rate,
#                      "Reviews":review,
#                      "Features":feature,
#                      "Images":image,
#                      "Links":link})

df=pandas.DataFrame({"Names":name,
                     "Prices":price,
                     "Rateing":rate,
                     "Reviews":review,
                     "Features":feature,
                     "Images":image,
                     "Links":link})  
print(df)

# df.to_csv("DSLR&mirrotless cams_data.csv")   
