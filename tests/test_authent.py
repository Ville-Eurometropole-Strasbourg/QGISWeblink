# test de d'authent
import requests
from requests_negotiate_sspi import HttpNegotiateAuth
auth = HttpNegotiateAuth()
# a=requests.get('https://whsiglw.cus.fr')
a=requests.get('https://catalog.whsiglw.cus.fr',auth=auth)
print (a.text)
print (a.history)