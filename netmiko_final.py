from netmiko import ConnectHandler
from pprint import pprint

device_ip = "<!!!REPLACEME with router IP address!!!>"
username = "admin"
password = "cisco"

device_params = {
    "device_type": "<!!!REPLACEME with device type for netmiko!!!>",
    "ip": device_ip,
    "username": username,
    "password": password,
}


def desc():

    with ConnectHandler(**device_params) as ssh:
    <!!!Write code here!!!>
        return <!!!Write code here!!!>
