import requests
import os
from dotenv import load_dotenv
from validation import get_id, get_name, get_phone, get_email, handle_error

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("MOCKAPI_PROJECT_ID is not configured.")

headers = {
    "Authorization" : f"bearer {api_key}"
}

BASE_URL = f"https://{api_key}.mockapi.io/api/v1"


        
def get_all_users():
    
    try:
        response = requests.get(f'{BASE_URL}/users', headers=headers, timeout=5)
    
        response.raise_for_status()
    
        users = response.json()
        
        if len(users) == 0:
            print("No data found.")
        
        print()
        for user in users:
            print(f"ID: {user['id']} | Name: {user['name']} | Phone: {user['phone']} | Email: {user['email']}")
            print("-"*90)
        print()
        
    except requests.exceptions.RequestException as e:
        handle_error(e)
        
        
def get_user():
    
    user_id = get_id()
    
    try:
        response = requests.get(f'{BASE_URL}/users/{int(user_id)}', headers=headers, timeout=5)
    
        response.raise_for_status()
    
        user = response.json()
    
        print("\nID: ",user['id'])
        print("Name: ",user['name'])
        print("Phone: ",user['phone'])
        print("Email: ",user['email'])
        print("-"*30)
        print()
        
    except requests.exceptions.RequestException as e:
        handle_error(e)



def post_user():
  
    name = get_name()
    
    phone = get_phone()       
    
    email = get_email()
    
    data = {
        "name" : name,
        "phone" : phone,
        "email" : email
    }
    
    try:
        response = requests.post(f'{BASE_URL}/users', json=data, timeout=5)
        
        response.raise_for_status()
        user = response.json()
        
        print(f"\n{user}")
        print("User added successfully!\n")
    
    except requests.exceptions.RequestException as e:
        handle_error(e)


def put_user():
    
    user_id = get_id()
        
    name = get_name()
    
    phone = get_phone()
    
    email = get_email()
    
    data = {
        "name" : name,
        "phone" : phone,
        "email" : email
    }
        
    try:
        check = requests.get(f"{BASE_URL}/users/{int(user_id)}",timeout=5)
        
        
        if check.status_code == 404:
            print("\nUser not found!\n")
            return
        
        check.raise_for_status()        
        
        response = requests.put(f"{BASE_URL}/users/{int(user_id)}",json=data,timeout=5)
        
        response.raise_for_status()
    
        print(f"\n{response.json()}")
        print("User updated successfully.\n")
            
    except requests.exceptions.RequestException as e:
        handle_error(e)


def delete_user():
    
    user_id = get_id()            
       
    try:
        check = requests.get(f"{BASE_URL}/users/{int(user_id)}", timeout=5)
        
        if check.status_code == 404:
            print("\nUser not found!\n")
            return
        
        check.raise_for_status()
                
        response = requests.delete(f"{BASE_URL}/users/{int(user_id)}", timeout=5)
        
        response.raise_for_status()
        
        if response.status_code in [200, 204]:
            print("\nUser deleted successfully!\n")
         
    except requests.exceptions.RequestException as e:
        handle_error(e)
        


def main_menu():
    while True:
        print(f'---===--- USER API ---===---')
        print()
        print("1. Show All Users")
        print("2. Show One User")
        print("3. Create User")
        print("4. Update User")
        print("5. Delete User")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            get_all_users()
        elif choice == "2":
            get_user()
        elif choice == "3":
            post_user()
        elif choice == "4":
            put_user()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            print("---Thank You---\n")
            break
        else:
            print("Invalid choice.\n")


main_menu()