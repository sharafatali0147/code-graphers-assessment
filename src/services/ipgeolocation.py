from django.conf import settings
# from requests import request

# class BanxicoService:
    
#     def getConversionRate(self):
#         response = request('GET', 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno', headers={
#             'accept': 'application/json',
#             'Bmx-Token': settings.BANXICO_TOKEN
#         })
#         obj = response.json()
#         print(obj)
#         return float(obj['bmx']['series'][0]['datos'][0]['dato'])

import requests

class   IPGeolocationService:
    def getIPGeolocation(self, ip_address):
        url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={settings.IP_GEOLOCATION_API_KEY}&ip_address={ip_address}"

        response = requests.get(url)
        print(response.status_code)
        print(response.content)
        return response

# https://ipgeolocation.abstractapi.com/v1/
#     ? api_key = settings.IP_GEOLOCATION_API_KEY
#     & ip_address = 166.171.248.255