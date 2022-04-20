from django.conf import settings
import requests
import json


def get_IP_geolocation(ip_address):
    ip_address = '37.111.141.5' # replacing for testing purose
    url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={settings.IP_GEOLOCATION_API_KEY}&ip_address={ip_address}"

    response = requests.get(url)
    print(response.status_code)
    data_dict = json.loads(response.content)
    print(data_dict)
    return data_dict
