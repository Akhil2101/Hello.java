from bs4 import BeautifulSoup
import requests
url="https://www.imdb.com/list/ls055592025/"
response=requests.get(url)
file=response.text
soup=BeautifulSoup(file,"html.parser")
greatest_movies=soup.find_all(name="h3",_class="lister-item-header")
movies=[movie.getText() for movie in greatest_movies]
#movies.reverse()
#movies[58]="59)The extra Terrestrial"
with open("movie.txt", mode="w") as f:
     for m in movies:
         f.write(f"{m}\n")

