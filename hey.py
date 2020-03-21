from bs4 import BeautifulSoup
import requests

s = 'https://www.worldometers.info/coronavirus/#countries'
r = requests.get(s)
hi = r.text
soup = BeautifulSoup(hi,"html.parser")
count = 0
a = []
b = []
x = soup.find('table').text
x = x.replace(" ","")
x = x.replace("+","")
x = x.replace(",","")
a = x.split('\n')
for i in range(16,len(a)-11,11):
	b.append(a[i:i+9])
	

#Country  Name:0	Total Cases:1	Cases Registered Today:2	Total Deaths:3	%of People Died of Infected(index3/index1*100)	   	
c = ["Country  Name","Total Cases","Cases Registered Today","Total Deaths","Percentage of victims Died"]
for i in b:
	if(i[3] == ""):
		i[3] = 0
	if(i[1] == ""):
		i[1] = 1	
	c.append([i[0],i[1],i[2],i[3],int(i[3])/int(i[1])*100])

def search(Country,c):
	for k in c:
		if(k[0] == Country):
			return k
c = c[1:-1]					
for i in c:
	print(*i)
