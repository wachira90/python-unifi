from ubiquiti.unifi import API as Unifi_API
import json
import urllib3
urllib3.disable_warnings()

# Example with context manager

# with Unifi_API(username="wachiradd", password="Mst001Admin", baseurl="https://192.168.4.170:8443", verify_ssl=False) as api:
#     device_list = (api.list_clients(filters={'hostname': 'Chromecast.*'}, order_by="ip"))
#     print(json.dumps(device_list, indent=4))


# Example without contextmanager

api = Unifi_API(username="user1", password="pass1", baseurl="https://192.168.4.170:8443", verify_ssl=False)
api.login()
device_list = (api.list_clients(order_by="ip"))
print(json.dumps(device_list, indent=4))
api.logout()
