import json
import uuid

"""Utility functions for the application."""


def clear_db():
    
    with open("db.json", "w") as f:
        json.dump([], f, indent=4)

def add_staff_member():
    """Add a new staff member to the database."""
    
    pass

def update_staff_member(id,**kwargs):
    """Update details of a staff member."""
    pass
    
def delete_staff_member():
    """Delete a staff member by their ID."""
    pass

def get_all_staff():
    """Retrieve all staff members from the database."""
    pass

def get_single_staff_member():
    """Retrieve a single staff member by their ID."""
    pass

def filter_staff_by_role():
    """Filter staff members by their role."""
    pass

if __name__ == "__main__":
    print("1. add_staff_member\n")
    print("2. update_staff_member\n")
    print("3. delete_staff_member\n")
    print("4. get_all_staff\n")
    print("5. get_single_staff_membe\n")
    print("6. filter_staff_by_role\n")
    
user_resp = input("what would you like to do")
resp = int(user_resp)

try:

    if user_resp == 1:
        pass
    elif user_resp == 2 :
        pass
    elif user_resp == 3 :
        pass
    elif user_resp == 4:
        pass
    elif user_resp == 5:
        pass
    elif user_resp == 6:
        pass
    else:
        print("Choose between 1 and 2.")
except Exception as e:
            print("Invalid input:", e)

    


        

