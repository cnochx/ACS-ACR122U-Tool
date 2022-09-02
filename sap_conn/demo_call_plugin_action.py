""""
Demo how to use the BA Toolbox Basic Plugin call api from python
Jörg Müller 01.09.2022
"""
import json

from pydeen.auth import AuthBasic
from pydeen.sap_abap import SAPAbapHttpBackend
from pydeen.http import HTTPConnector


# define sap backend
sap_name = "S4D100"
sap_client = "100"
sap_url = "http://s4d.17.ucc.md"

# load auth
auth = AuthBasic()
auth.set_menu_context(name=sap_name, path="../sec")
if auth.load_config(auth.get_menu_filename()) == False:
    auth.menu()

# init request
backend = SAPAbapHttpBackend(sap_name, sap_url, sap_client, auth=auth)
connector = HTTPConnector(backend)
request = connector.create_request()

# build params
params = {
    "sap-client": sap_client,
    "action": "/BAB/BLB_PCD_USR_ROLES",
    "variant": "",
    "trace": "true",
    "background": "false"
}

# build payload
payload = {
                "USER": "JMR",
                "VALID_DATE": "",
                "PARAMETERS": [],
                "BACKGROUND": {
                        "EXT_CLIENT_ID": "",
                        "ONLY_PRIVATE": ""
                }
            }

http_code = request.post(json.dumps(payload), "/sap/bc/bsp/bab/atb_pi_srv/call_action", params)
print("HTTP Status:", http_code)

text = request.get_response_text()
print(text)