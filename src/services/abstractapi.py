from django.conf import settings
import requests
import json
import datetime

def get_IP_geolocation(ip_address):
    ip_address = '37.111.141.5' # replacing for testing purose
    url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={settings.IP_GEOLOCATION_API_KEY}&ip_address={ip_address}"

    response = requests.get(url)
    # print(response.status_code)
    geolocation_dict = json.loads(response.content)
    # print(geolocation_dict)
    holiday = get_holidays(geolocation_dict['country_code'])
    return holiday, geolocation_dict

def email_validate(email):
    url = f"https://emailvalidation.abstractapi.com/v1/?api_key={settings.EMAIL_VALIDATION_API_KEY}&email={email}"

    response = requests.get(url)
    print(response.status_code)
    data_dict = json.loads(response.content)
    # print(data_dict)
    return data_dict

def get_holidays(country, year = None, month = None, day = None):
    if year is None:
        year = datetime.datetime.now().year
    if month is None:
        month = datetime.datetime.now().month
    if day is None:
        day = datetime.datetime.now().day
        
    url = f"https://holidays.abstractapi.com/v1/?api_key={settings.HOLIDAYS_API_KEY}&country={country}&year={year}&month={month}&day={day}"

    response = requests.get(url)
    print(response.status_code)
    data_dict = json.loads(response.content)
    # print(data_dict)
    return data_dict