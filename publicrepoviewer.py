import requests

from bs4 import BeautifulSoup

def printAllRepo(x):
	for i in x:
		if(i.get("itemprop") == "name codeRepository"):
			i = i.text
			i=i.strip()
			i=i.replace("\t","")
			print(i)


githubprofilename = input("Enter github profile name: ")

url = "https://github.com/"+githubprofilename+"?tab=repositories"

while(True):
	response = requests.get(url)

	html_content = response.content

	soup = BeautifulSoup(html_content,"html.parser")

	x = soup.find_all("a")
	
	printAllRepo(x)
	nextPage = 0
	for i in soup.find_all("a"):
		if(i.text == "Next"):
			nextPage = 1
			url=i.get("href")
			
	if(nextPage == 0):
		break
	
		
