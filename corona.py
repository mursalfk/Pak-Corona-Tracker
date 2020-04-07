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
total = html_soup.find_all('div', class_ = "maincounter-number")
Total_pk = total[0].text
Total_pk = Total_pk.strip()
Total_pk
Recovered_pk = total[1].text
Recovered_pk = Recovered_pk.strip()
Recovered_pk
Deaths_pk = total[2].text
Deaths_pk = Deaths_pk.strip()
Deaths_pk
print("\nTotal Cases:" + str(Total_pk))
print("Recovered Cases:" + str(Recovered_pk))
print("Deaths: " + str(Deaths_pk))

#Province Wise Cases
province_table = html_soup.find_all('tr')
province_table

#Function for Calling Provinces
def province_cases(province_name, ind):
    province_name = province_table[ind].text
    province_name = province_name.strip()
    province_name = province_name.split()
    return province_name

Punjab_cases = province_cases("Punjab_cases",1)
Sindh_cases = province_cases("Sindh_cases",2)
KPK_cases = province_cases("KPK_cases",3)
GB_cases = province_cases("GB_cases",4)
Balochistan_cases = province_cases("Balochistan_cases",5)
FC_cases = province_cases("FC_cases",6)
AJK_cases = province_cases("AJK_cases",7)

print("=====================")
print("Province-Wise Details")
print("=====================")

print("\n1. Punjab:")
print("\t--Today--")
print("\t\tTotal Cases: " + str(Punjab_cases[1]) + " " + str(Punjab_cases[2]))
print("\t\tRecovered : " + str(Punjab_cases[4]) + " " + str(Punjab_cases[5]))
print("\t\tDeaths : " + str(Punjab_cases[7]) + " " + str(Punjab_cases[8]))
print("\n\t--Overall--")
print("\t\tTotal Cases: " + str(Punjab_cases[3]))
print("\t\tRecovered: " + str(Punjab_cases[6]))
print("\t\tDeaths Cases: " + str(Punjab_cases[9]))

print("\n2. Sindh:")
print("\t--Today--")
print("\t\tTotal Cases: " + str(Sindh_cases[1] + " " + Sindh_cases[2]))
print("\t\tRecovered : " + str(Sindh_cases[4] + " " + Sindh_cases[5]))
print("\t\tDeaths : " + str(Sindh_cases[7] + " " + Sindh_cases[8]))
print("\n\t--Overall--")
print("\t\tTotal Cases: " + str(Sindh_cases[3]))
print("\t\tRecovered: " + str(Sindh_cases[6]))
print("\t\tDeaths Cases: " + str(Sindh_cases[9]))

print("\n3. Khyber Pakhtunkhwa:")
print("\t--Today--")
print("\t\tTotal Cases: " + str(KPK_cases[2] + " " + KPK_cases[3]))
print("\t\tRecovered : " + str(KPK_cases[5] + " " + KPK_cases[6]))
print("\t\tDeaths : " + str(KPK_cases[8] + " " + KPK_cases[9]))
print("\n\t--Overall--")
print("\t\tTotal Cases: " + str(KPK_cases[4]))
print("\t\tRecovered: " + str(KPK_cases[7]))
print("\t\tDeaths Cases: " + str(KPK_cases[10]))

print("\n4. Gilgit Baltistan:")
print("\t--Today--")
print("\t\tTotal Cases: " + str(GB_cases[2] + " " + GB_cases[3]))
print("\t\tRecovered : " + str(GB_cases[5] + " " + GB_cases[6]))
print("\t\tDeaths : " + str(GB_cases[8] + " " + GB_cases[9]))
print("\n\t--Overall--")
print("\t\tTotal Cases: " + str(GB_cases[4]))
print("\t\tRecovered: " + str(GB_cases[7]))
print("\t\tDeaths Cases: " + str(GB_cases[10]))

print("\n5. Balochistan:")
print("\t--Today--")
print("\t\tTotal Cases: " + str(Balochistan_cases[1] + " " + Balochistan_cases[2]))
print("\t\tRecovered : " + str(Balochistan_cases[4] + " " + Balochistan_cases[5]))
print("\t\tDeaths : " + str(Balochistan_cases[7] + " " + Balochistan_cases[8]))
print("\n\t--Overall--")
print("\t\tTotal Cases: " + str(Balochistan_cases[3]))
print("\t\tRecovered: " + str(Balochistan_cases[6]))
print("\t\tDeaths Cases: " + str(Balochistan_cases[9]))

print("\n6. Federal Capital:")
print("\t--Today--")
print("\t\tTotal Cases: " + str(FC_cases[2] + " " + FC_cases[3]))
print("\t\tRecovered : " + str(FC_cases[5] + " " + FC_cases[6]))
print("\t\tDeaths : " + str(FC_cases[8] + " " + FC_cases[9]))
print("\n\t--Overall--")
print("\t\tTotal Cases: " + str(FC_cases[4]))
print("\t\tRecovered: " + str(FC_cases[7]))
print("\t\tDeaths Cases: " + str(FC_cases[10]))

print("\n7. Azad Jammu & Kashmir:")
print("\t--Today--")
print("\t\tTotal Cases: " + str(AJK_cases[2] + " " + AJK_cases[3]))
print("\t\tRecovered : " + str(AJK_cases[5] + " " + AJK_cases[6]))
try:  
    print("\t\tDeaths : " + str(AJK_cases[8] + " " + AJK_cases[9]))
except IndexError:  
    print ("\t\tDeaths Cases: No Deaths Yet")
else:  
    print("\t\tDeaths : " + str(AJK_cases[8] + " " + AJK_cases[9]))
print("\n\t--Overall--")
print("\t\tTotal Cases: " + str(AJK_cases[4]))
print("\t\tRecovered: " + str(AJK_cases[7]))
try:  
    print("\t\tDeaths Cases: " + str(AJK_cases[10]))  
except IndexError:  
    print ("\t\tDeaths Cases: No Deaths Yet")
else:  
    print("\t\tDeaths Cases: " + str(AJK_cases[10]))