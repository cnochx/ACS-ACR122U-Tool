"""
Demo Setzen von Attributwerten im BA Universum via BA Plugin API
Beispiel erkanntes Tag vom NFCScanner an Universum als Attribut übergeben
Jörg Müller, 01.09.2022
"""

import json

from pydeen.auth import AuthBasic
from pydeen.sap_abap import SAPAbapHttpBackend
from pydeen.http import HTTPConnector
from pydeen.menu import UserInput


# define sap backend
sap_name = "S4D100"
sap_client = "100"
sap_url = "http://s4d.17.ucc.md"

# define universe context
guv_key = 'BAH3Demo'
guv_obj_type = 'NfcScanner'
guv_obj_key = 'NFC0002'
guv_atr_type = 'NfcTag'

# get user input for simulation
guv_atr_value_text = "1234567890"
guv_atr_value_text = UserInput("Enter a Tag ID", guv_atr_value_text).get_input()
if not guv_atr_value_text:
    exit(0)

# load auth
auth = AuthBasic()
auth.set_menu_context(name=sap_name)
if not auth.load_config(auth.get_menu_filename()):
    auth.menu()

# init request
backend = SAPAbapHttpBackend(sap_name, sap_url, sap_client, auth=auth)
connector = HTTPConnector(backend)
request = connector.create_request()

# build params
params = {
    "sap-client": sap_client,
    "action": "/BAB/IGK_BAF_INS_ATR_PUT",
    "variant": "",
    "trace": "true",
    "background": "false"
}

# build payload
payload = {
    "GUV_KEY": guv_key,
    "ASS_TYPE_KEY": guv_obj_type,
    "ASS_INST_KEY": guv_obj_key,
    "TAGR_KEY": "",
    "TATR_KEY": guv_atr_type,
    "IATR_GUID": "",
    "DATA": {
        "GUV_GUID": "",
        "TATR_GUID": "",
        "TAGR_GUID": "",
        "ASSIGNED_TYPE": "IOBJ",
        "ASSIGNED_GUID": "",
        "INSTANCE_KEY": "",
        "INSTANCE_GROUP": "",
        "TITLE": "",
        "STATUS": "",
        "VERSION": "",
        "VERSION_DATE": "0000-00-00",
        "DESCRIPTION": "",
        "HASHTAGS": "",
        "RESPONSIBLE": "",
        "RESPONSIBLE_GROUP": "",
        "VALID_FROM": 0,
        "VALID_TO": 0,
        "COMMITTED_AT": 0,
        "COMMITTED_BY": "",
        "COMMITTED_COUNT": 0,
        "REC_INDEX": 0,
        "VALUE_NUMERIC": 0,
        "VALUE_TEXT": guv_atr_value_text,
        "VALUE_BOOL": "",
        "VALUE_TIMESTAMP": 0,
        "VALUE_STRING": "",
        "VALUE_CONTENT_TYPE": "",
        "VALUE_HASH": ""
    },
    "FIELDS": [],
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


