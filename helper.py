import requests


def result():
    pass

def requester(request):
    response = requests.get(request)
    if response.status_code == 200:
        print("Success Call!")
        print(response.json())
    else: 
        print(f"Failed with status code {response.status_code}")