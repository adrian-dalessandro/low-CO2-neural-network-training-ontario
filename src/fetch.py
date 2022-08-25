import xml.etree.ElementTree as ET
import requests

prod_url = "http://reports.ieso.ca/public/GenOutputCapability/PUB_GenOutputCapability.xml" 
prod_xml = requests.get(prod_url)

