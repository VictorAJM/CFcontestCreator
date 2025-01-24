import requests
from abc import ABC, abstractmethod

class APICall:
  def __init__(self):
    self.requestBase = "https://codeforces.com/api/"
    self.request = self.requestBase

  @abstractmethod
  def responseObject(self, response):
    pass

  def requester(self):
    response = requests.get(self.request)
    if response.status_code == 200:
      return self.responseObject(response.json())
    else:
      print(f"Failed with status code {response.status_code}")
  
  @abstractmethod
  def setRequest(self):
    pass