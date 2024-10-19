import requests
import json

class XataApi:
    def __init__(self, WorkSpace_slug, region, database, branch, tableName, api_key):
        self.WorkSpace_slug = WorkSpace_slug
        self.region = region
        self.database = database
        self.branch = branch
        self.tableName = tableName
        self.api_key = api_key


    def Max_id(self):
        url =  f"https://{self.WorkSpace_slug}.{self.region}.xata.sh/db/{self.database}:{self.branch}/sql"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "statement": "SELECT max(xata_id) FROM videos;",
            "params": None,
            "consistency": "strong",
            "responseType": "json"
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            details = (result["records"][0])
            return int(details["max"])
        else:
            return {
                "error": response.status_code,
                "message": response.text
            }


    def isEmailPresent(self, email):
        url =  f"https://{self.WorkSpace_slug}.{self.region}.xata.sh/db/{self.database}:{self.branch}/sql"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "statement": f"SELECT email FROM users WHERE email = '{email}';",
            "params": None,
            "consistency": "strong",
            "responseType": "json"
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if len(result['records']) >= 1:
                if email == result['records'][0]["email"]:
                    return True
            else:
                return False    
        else:
            return {
                "error": response.status_code,
                "message": response.text
            }

    def isUserNamePresent(self,username):
        url =  f"https://{self.WorkSpace_slug}.{self.region}.xata.sh/db/{self.database}:{self.branch}/sql"
        headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
        }
        payload = {
            "statement": f"SELECT username FROM users WHERE username = '{username}';",
            "params": None,
            "consistency": "strong",
            "responseType": "json"
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if len(result['records']) >= 1:
                if username == result['records'][0]["username"]:
                    return True
            else:
                return False    
        else:
            return {
                "error": response.status_code,
                "message": response.text
            }
        
    
    def insert_xata_record(self,data):
        url = f"https://{self.WorkSpace_slug}.{self.region}.xata.sh/db/{self.database}:{self.branch}/tables/{self.tableName}/data"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        payload = json.dumps(data)
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 201:
            print("Record inserted successfully!")
        else:
            print(f"Failed to insert record. Status code: {response.status_code}, Response: {response.text}")
        
        return response.json()
    
    def password_check(self,password):
        url =  f"https://{self.WorkSpace_slug}.{self.region}.xata.sh/db/{self.database}:{self.branch}/sql"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "statement": f"SELECT password FROM users WHERE password = '{password}';",
            "params": None,
            "consistency": "strong",
            "responseType": "json"
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if len(result['records']) >= 1:
                if password == result['records'][0]["password"]:
                    return True
            else:
                return False    
        else:
            return {
                "error": response.status_code,
                "message": response.text
            }

# data = {
#     "username" : "rohit",
#     "email" : "rohit@gmail.com",
#     "password" : "Rohit@1"
# }

obj = XataApi("L-earn-Hub-s-workspace-3rj5i6", "us-east-1", "learnhub", "main","users", "xau_jIRNNlavLZ7IvkDYCPq3NwlAU4p15pR13")
# obj.insert_xata_record(data)
# result = obj.password_check('NarendraKumar')s
# print(result)
result=obj.isEmailPresent("narendra@gmail.com")
print(result)