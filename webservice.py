import requests
import json
#url = "http://172.16.1.13/webservice-php-json/index.php"
url = "https://bot.movatec.cl/webservice-php-json/index.php"
payload={'action': 'get','id': '143'}
files=[
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

#print(response.text)
my_bytes_value = response.content
my_new_string = my_bytes_value.decode("utf-8").replace("'", '"')
data = json.loads(my_new_string)
s = json.dumps(data, indent=4, sort_keys=True)
print(s)
print(data["data"])
##UPDATE DATOS



"""
import requests

url = "http://172.16.1.72/webservice-php-json/index.php"
motivo = "Sin Trabajo"

payload={'action': 'update',
'tipo_contacto': '4',
'motivo': 'sin trabajo',
'compromiso_p': '4',
'derivacion': 'None',
'fecha_com': 'None',
'entrega_info': 'Si',
'lead_id': '134'}
files=[

]
headers = {}
response = requests.request("POST", url, headers=headers, data=payload, files=files)
print(payload)
print(response.text)
"""

