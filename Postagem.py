import requests
import json

def postar():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=31d49c4bec438e1e41cc7eec111fb4153ae67647'
    file = {'answer': open("answer.json", 'rb')}
    response = requests.post(url, files=file)

    print(response.status_code)
    print(response.text)

    
postar()