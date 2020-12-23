# -*- encoding: utf-8 -*-
from django.test import TestCase
import requests

def api_connector():
    headers = {'Content-Type': 'application/json',
               'credential': 'ZGpzOTAzaWZuc2Zpb25kZnNubm5u',}
    servername = "api.moni.com.ar"

    return servername, headers

def get_prestamo(dni):
    servername, headers = api_connector()
    URL = "https://" + servername + "/api/v4/scoring/pre-score/" + str(dni)
    
    response = requests.request("GET",URL, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        has_error = response_json.get("has_error")
        status = response_json.get("status")

    return status, has_error