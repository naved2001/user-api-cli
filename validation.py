import requests

def get_id():
    while True:
        user_id = input("Enter ID: ").strip()
        
        if not user_id:
            print("ID cannot be empty.")
            continue
        
        if not user_id.isdigit():
            print("ID must contain digits only.")
            continue
        break
    
    return user_id

def get_name():
    while True:
        name = input("Enter name: ").strip()
        
        if not name:
            print("Name cannot be empty.")
            continue
       
        if not all(word.isalpha() for word in name.split()):
            print("Name must contain letters and spaces only.")
            continue

        break
    return name
    
def get_phone():
    while True:
        phone = input("Enter phone number: ").strip()
        
        if not phone:
            print("Phone number cannot be empty.")
            continue
        
        if not phone.isdigit():
            print("Phone number must contain digits only.")
            continue
        
        if len(phone) != 10:
            print("Phone number must be 10 digits only")
            continue 
        break
    
    return phone

def get_email():
    while True:
        email = input("Enter email: ")
        
        if not email:
            print("Email cannot be empty.")
            continue
        
        if "@" not in email or "." not in email:
            print("Please enter a valid email.")
            continue
    
        break
    
    return email


def handle_error(e):
    if isinstance(e, requests.exceptions.Timeout):
        print("Request timed out.")

    elif isinstance(e, requests.exceptions.ConnectionError):
        print("Could not connect to the API.")

    elif isinstance(e, requests.exceptions.HTTPError):
        print("HTTP error:", e)

    elif isinstance(e, requests.exceptions.RequestException):
        print("Request error:", e)

    else:
        print("Unexpected error:", e)