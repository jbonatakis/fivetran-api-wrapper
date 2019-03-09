# from .base import Fivetran

import base64

class Fivetran:
    """ Class to instantiate a Fivetran connection. """

    def __init__(self, key, secret):
        """ Break functionality of this __init__ function into separate functions? """

        self.key = key
        self.secret = secret

        combined_key_secret = self.key + ':' + self.secret
        key_secret_encoded = combined_key_secret.encode('UTF-8')
        key_secret_base_64 = base64.b64encode(key_secret_encoded)

        auth_header = 'Basic {}'.format(key_secret_base_64.decode('UTF-8'))

        self.headers = {
            "Accept": "application/json",
            "Authorization": auth_header
        }

    # Import methods
    from .users import list_all_users, user_details, invite_user, delete_user
