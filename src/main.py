

# script Jörg

from src import nfc
from pydeen.auth import AuthBasic
from pydeen.http import HTTPConnector, HTTPBackend
from pydeen.service import ServiceCommand, ServiceContext
from pydeen.websocket import WebSocketService


# define sap backend
sap_name = "S4D100"
sap_client = "100"
sap_url = "ws://10.17.1.12/extern/api/atbrtc?sap-client=100"


# define call back command
class MyCommand(ServiceCommand):
    def handle(self, command, payload, service) -> bool:
        reader = nfc.Reader()
        payload = reader.print_data(reader.get_uid())
        print(f"MY COMMAND CALLED: payload {payload}")
        return True


# load auth
auth = AuthBasic()
auth.set_menu_context(name=sap_name)
if not auth.load_config(auth.get_menu_filename()):
    auth.menu()

# init sap backend
backend = HTTPBackend(sap_name, sap_url, auth=auth)
connector = HTTPConnector(backend)
service = WebSocketService(backend)

# ======== configure service
# optional: set external Client ID - must be unique
# default: auto generated ID via service.generate_client_id
service.set_client_id("MY_UNIQUE_PYTHON_CLIENT_ID")

# optional: set different backend channel/app
# service.set_header("amc_channel", "/pcp")
# service.set_header("amc_channel", "/events")

# activate command mode and register custom command handler
service.set_command_mode()
service_command = MyCommand("custom_cmd", "My Custom Command Handler")
service.register_command(service_command)

# optional: subscribe to group(s)
service.register_group("testgroup")
service.register_group("production")
service.register_group("logistic")

# start the service now in an endless loop
service.run()




