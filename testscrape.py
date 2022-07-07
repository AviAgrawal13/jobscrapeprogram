from indeed import IndeedClient
from collections.abc import MutableMapping
import socket

client_hostname = socket.gethostname()
client_ip_address = socket.gethostbyname(client_hostname)

print(client_ip_address)
