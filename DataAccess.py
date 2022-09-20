"""
Accessing data from one of the top website - CricInfo.
The data am using here is only* for Test Matches.(You can use of any format.)
The prediction is against all the opponent team. (You can go for any particular team as well.)
Record is from 1932 to 2016/2017
"""

# Import Request Package
import requests
from bs4 import BeautifulSoup

# Url Access - Test Matches
url = 'http://stats.espncricinfo.com/ci/engine/team/6.html?class=1;template=results;type=team;view=results'
"""
For Other formats use any of the below URL -
For ODI's - http://stats.espncricinfo.com/ci/engine/team/6.html?class=2;template=results;type=team;view=results
For T20's - http://stats.espncricinfo.com/ci/engine/team/6.html?class=3;template=results;type=team;view=results
"""

r = requests.get(url)
html = r.text

# Create Soup Object
soup = BeautifulSoup(html,'lxml')
recs = soup.select('tbody > .data1')

# Data Access
file = open('India_in_Tests.csv', "w")
for i in range(2,len(recs)):
        single = recs[i].findAll('td')
        file.write(single[0].text + ','+single[1].text+ ','+single[2].text+ ','+single[3].text+ ','+ single[4].text+ ','+single[6].text+ ','+ single[7].text+'\n')

file.close()

