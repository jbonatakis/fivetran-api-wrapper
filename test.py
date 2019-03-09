from wrapper import Fivetran
import json
import os


f = Fivetran(key=os.environ["FIVETRAN_KEY"], secret=os.environ["FIVETRAN_SECRET"])

users = f.list_all_users() # listAllUsers function dumps json. To prettyprint, use load.json then redump with indent
users_json = json.loads(users)
users_json = json.dumps(users_json, indent=4)
print(users_json)

# print(f.listAllUsers())

# print(f.headers)

# print(f.userDetails("medication_blip"))

# print(f.inviteUser("jack+test@das42.com", "Jack", "Bonat", "ReadOnly"))

# print(f.listAllUsers())

# print(f.deleteUser(""))
