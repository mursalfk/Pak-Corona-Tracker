url = "https://www.covid-19.pk/"
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
# dd/mm/YY H:M:S
now = datetime.now()
dt_string = now.strftime("Date: %d/%m/%Y Time: %H:%M:%S")
print("Last Updated on: ", dt_string)	

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

#Province Wise Cases
province_table = html_soup.find_all('tr')
province_table

Punjab_cases_raw = province_table[1].text
Punjab_cases = [int(i) for i in Punjab_cases_raw.split() if i.isdigit()] 
Punjab_cases
Sindh_cases_raw = province_table[2].text
Sindh_cases = [int(i) for i in Sindh_cases_raw.split() if i.isdigit()] 
Sindh_cases
KPK_cases_raw = province_table[3].text
KPK_cases = [int(i) for i in KPK_cases_raw.split() if i.isdigit()] 
KPK_cases
GB_cases_raw = province_table[4].text
GB_cases = [int(i) for i in GB_cases_raw.split() if i.isdigit()] 
GB_cases
Balochistan_cases_raw = province_table[5].text
Balochistan_cases = [int(i) for i in Balochistan_cases_raw.split() if i.isdigit()] 
Balochistan_cases
FC_cases_raw = province_table[6].text
FC_cases = [int(i) for i in FC_cases_raw.split() if i.isdigit()] 
FC_cases
AJK_cases_raw = province_table[7].text
AJK_cases = [int(i) for i in AJK_cases_raw.split() if i.isdigit()] 
AJK_cases
print("\nTotal Cases: " + str(Total_pk))
print("Deaths: " + str(Death_pk))
print("Recovered Cases: " + str(Recovered_pk))
print("=====================")
print("Province-Wise Details")
print("=====================")
print("\n1. Punjab:")
print("\tTotal Cases: " + str(Punjab_cases[0]))
print("\tRecovered Cases: " + str(Punjab_cases[1]))
print("\tDeaths Cases: " + str(Punjab_cases[2]))
print("\n2. Sindh:")
print("\tTotal Cases: " + str(Sindh_cases[0]))
print("\tRecovered Cases: " + str(Sindh_cases[1]))
print("\tDeaths Cases: " + str(Sindh_cases[2]))
print("\n3. Khyber Pakhtunkhwa:")
print("\tTotal Cases: " + str(KPK_cases[0]))
print("\tRecovered Cases: " + str(KPK_cases[1]))
print("\tDeaths Cases: " + str(KPK_cases[2]))
print("\n4. Gilgit Baltistan:")
print("\tTotal Cases: " + str(GB_cases[0]))
print("\tRecovered Cases: " + str(GB_cases[1]))
print("\tDeaths Cases: " + str(GB_cases[2]))
print("\n5. Balochistan:")
print("\tTotal Cases: " + str(Balochistan_cases[0]))
print("\tRecovered Cases: " + str(Balochistan_cases[1]))
print("\tDeaths Cases: " + str(Balochistan_cases[2]))
print("\n6. Federal Capital:")
print("\tTotal Cases: " + str(FC_cases[0]))
print("\tRecovered Cases: " + str(FC_cases[1]))
try:  
    print("\tDeaths Cases: " + str(FC_cases[2]))  
except IndexError:  
    print ("\tDeaths Cases: No Deaths Yet")
else:  
    print("\tDeaths Cases: " + str(FC_cases[2]))
print("\n7. Azad Jammu & Kashmir:")
print("\tTotal Cases: " + str(AJK_cases[0]))
print("\tRecovered Cases: " + str(AJK_cases[1]))
try:  
    print("\tDeaths Cases: " + str(AJK_cases[2]))  
except IndexError:  
    print ("\tDeaths Cases: No Deaths Yet")
else:  
    print("\tDeaths Cases: " + str(AJK_cases[2]))
