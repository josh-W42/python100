# Generally Speaking
"""
    Response Status Codes Guidelines: See MDN if you want more info.
    1XX: Hold on
    2XX: Here you go
    3XX: Go Away
    4XX: You Screwed up
    5XX: I Screwed up
"""

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() # Can use this to raise an exception anytime we get a response that is not 200

