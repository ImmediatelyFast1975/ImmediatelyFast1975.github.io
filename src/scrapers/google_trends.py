# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET
def get_data():
    try:
        res = requests.get("https://trends.google.com/trending/rss?geo=US", timeout=5)
        root = ET.fromstring(res.text)
        return [i.find('title').text for i in root.findall('.//item')][:15]
    except: return []