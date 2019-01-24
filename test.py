import requests
import sys
from prettytable import PrettyTable

user = sys.argv[1]
URL = "https://api.github.com/users/{0}/repos".format(user)


def get_user_data(URL):
    try:
        r = requests.get(url = URL)
        data = r.json()
        return data
    except requests.exceptions.RequestException as e: 
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    rtr_data = get_user_data(URL)

    if 'message' in rtr_data and rtr_data['message'] == 'Not Found':
        print("User not found")
        sys.exit(1)

    cnt = 1
    t = PrettyTable(['SNo', 'Name', 'Fork', 'Archived'])
    for repo in rtr_data:
        if not repo['private']:
            toAdd = [cnt, repo['name'], repo['fork'], repo['archived']]
            t.add_row(toAdd)
            cnt+=1

    if cnt == 1:
        print("No Public Repositories found for: {}".format(user))
    else:
        print(t)