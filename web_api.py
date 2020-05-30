url = "https://www.covid-19.pk/"
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
from flask import Flask,jsonify
# dd/mm/YY H:M:S
now = datetime.now()
dt_string = now.strftime("Date: %d/%m/%Y Time: %H:%M:%S")
print("Last Updated on: ", dt_string)	
app = Flask(__name__)

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


@app.route('/overall')
def overall():
    return jsonify({'Confirmed':Total_pk},{'Recovered':Recovered_pk},{'Deaths':Deaths_pk})

@app.route('/provinces')
def provinces():
    return jsonify({'Punjab':Punjab_cases},{'Sindh':Sindh_cases},{'KPK':KPK_cases},{'Federal':FC_cases},{'Gilgit':GB_cases},{'Balochistan':Balochistan_cases},{'AJK':AJK_cases})

if __name__ == '__main__':
    app.run()
