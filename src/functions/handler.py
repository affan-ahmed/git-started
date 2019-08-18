import requests

def create_repo(token, options):
    url = "https://api.github.com/user/repos"
    headers = {
        'content-type': 'application/json',
        'Authorization': f'token {token}'
    }
    response = requests.post(url, data=options, headers=headers)
    print(response.content)