url = "https://www.covid-19.pk/"
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
# dd/mm/YY H:M:S
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y \nTime: %H:%M:%S")
print("\nLast Updated on: ", dt_string)	

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
pak_covid19 = html_soup.find_all('div', id="maincounter-wrap")
total = html_soup.find_all('div', class_ = "maincounter-number")
Total_pk_raw = total[0].text
Total_pk_raw = Total_pk_raw.replace(',', '')
Total_pk = [int(i) for i in Total_pk_raw.split() if i.isdigit()] 
Death_pk_raw = total[1].text
Death_pk = [int(i) for i in Death_pk_raw.split() if i.isdigit()] 
Recovered_pk_raw = total[2].text
Recovered_pk = [int(i) for i in Recovered_pk_raw.split() if i.isdigit()] 
Total_pk = str(Total_pk).replace('[', '')
Death_pk = str(Death_pk).replace('[', '')
Recovered_pk = str(Recovered_pk).replace('[', '')
Total_pk = str(Total_pk).replace(']', '')
Death_pk = str(Death_pk).replace(']', '')
Recovered_pk = str(Recovered_pk).replace(']', '')
print("Total Cases: " + str(Total_pk))
print("Deaths: " + str(Death_pk))
print("Recovered Cases: " + str(Recovered_pk))