from api.repositories.repos import Repos
from api.issues.issues import Issues
from api.checks.checks import Checks
from api.interactions.interactions import Interactions
from api.apps.apps import Apps
from api.orgs.orgs import Orgs
from operations.orgs import create_org_and_repo
import json


class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "https://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)
        self.issues = Issues(self.api_root_url, **kwargs)
        self.checks = Checks(self.api_root_url, **kwargs)
        self.interactions = Interactions(self.api_root_url, **kwargs)
        self.apps = Apps(self.api_root_url, **kwargs)
        self.orgs = Orgs(self.api_root_url, **kwargs)



if __name__ == '__main__':
    g = Github(username="namelaowang", password ="ghl6032069")

    result =g.repos.list_user_repos("namelaowang" ,json={'type':'all'})
    r = result.json()
    print(r)
    for i in r:
        print(i['name'])

    print("---------")

    # result = g.repos.delete_a_repo('namelaowang','repos')
    # print(result.status_code)



