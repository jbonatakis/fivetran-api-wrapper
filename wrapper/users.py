import json
import requests

def list_all_users(self):
    """ List details about all users """

    response = requests.get('https://api.fivetran.com/v1/users', headers=self.headers)
    j = response.json()

    return json.dumps(j["data"]["items"])


def user_details(self, user_id):
    """ List details about a specific user """

    response = requests.get(f'https://api.fivetran.com/v1/users/{user_id}', headers=self.headers)
    j = response.json()

    return json.dumps(j["data"])


def invite_user(self, email, first_name, last_name, role):
    """ *args or **kwargs for optional parameters?     """

    payload = {
        'email': email,
        'given_name': first_name,
        'family_name': last_name,
        'role': role
    }

    response = requests.post('https://api.fivetran.com/v1/users', headers=self.headers, \
    	                  json=payload)
    j = response.json()

    return json.dumps(j)


def delete_user(self, user_id):

    payload = {
        'user_id': user_id
    }

    response = requests.delete(f'https://api.fivetran.com/v1/users/{user_id}', \
    	                   headers=self.headers, \
    	                   json=payload)

    j = response.json()

    return json.dumps(j)


""" Add 'modifyUser' method here """
