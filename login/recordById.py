import requests

def get_record_by_id():
    # Construct the URL
    url = f"https://L-earn-Hub-s-workspace-3rj5i6.us-east-1.xata.sh/db/main/tables/users/data/email"

    # Set the headers with the Authorization Bearer token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer xau_jIRNNlavLZ7IvkDYCPq3NwlAU4p15pR13"
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check for different status codes and handle accordingly
    if response.status_code == 200:
        # Success, return the record data
        return response.json()
    elif response.status_code == 400:
        raise Exception("Bad Request: The request was invalid.")
    elif response.status_code == 401:
        raise Exception("Unauthorized: Check your API key.")
    elif response.status_code == 404:
        raise Exception(f"Not Found: No record found with ID email.")
    else:
        raise Exception(f"Error: Received status code {response.status_code}.")

# Example usage
workspace_slug = "L-earn-Hub-s-workspace-3rj5i6"
region = "us-east-1"
db_branch_name = "main"
table_name = "users"
record_id = "email"
api_key = "xau_jIRNNlavLZ7IvkDYCPq3NwlAU4p15pR13"

try:
    record = get_record_by_id(workspace_slug, region, db_branch_name, table_name, record_id, api_key)
    print("Record retrieved:", record)
except Exception as e:
    print(e)
