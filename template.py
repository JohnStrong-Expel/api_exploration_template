import html
import json
import os
import re
import urllib.parse
from wsgiref import headers
import requests
import pprint
from datetime import datetime

provider = "{url_to_receive_call}"
current_datetime = datetime.now()
current_date_time = str(current_datetime)
integration = "{integration_name_here}"
file_name = integration + current_date_time + ".json"
file = open(file_name, 'w')

resp = requests.post(
  url = provider,
  headers = {}, #headers
  data = {}, #body
  params = {}, #URL parameters
  allow_redirects=False
)
pprint.pprint(resp.json())
file.write(str(resp.json()))
file.close()