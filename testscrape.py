from indeed import IndeedClient
import socket

client = IndeedClient(publisher = "insert publisher key here")

client_hostname = socket.gethostname()
client_ip_address = socket.gethostbyname(client_hostname)

keyword = input("What keyword would you like to search? > ")

params = {
    'q' : f"{keyword}",
    'l' : "austin",
    'userip' : f"{client_ip_address}",
    'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
}

search_response = client.search(**params)

print(json.dumps(search_response,indent=4))
