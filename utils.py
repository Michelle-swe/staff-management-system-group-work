import json
import uuid

"""Utility functions for the application."""


def save_db(staff):
    """
    Save the staff list into db.json file.
    Overwrites the file with the latest data.
    """
    try:
        with open("db.json", "w") as f:
            json.dump(staff, f, indent=4)
        print("Database saved successfully.")
    except Exception as e:
        print(f"Error saving database: {e}")

def validate_role():
    valid_roles = [
        "Cook",
        "Driver",
        "Cleaner",
        "Housekeeper",
        "Gardener",
        "Nanny",
        "Security",
        "Admin",
        "Laundry",
        "Manager",
        "Maintenance",
        "Personal_Assistant",
    ]

    valid_lower = {r.lower() for r in valid_roles}

    while True:
        role_input = input(f"Enter role ({', '.join(sorted(valid_roles))}): ").strip()
        if role_input.lower() in valid_lower:
            # return the role in the original capitalization from valid_roles
            for r in valid_roles:
                if r.lower() == role_input.lower():
                    return r
        else:
            print(f"Invalid role: '{role_input}'. Please choose one of: {', '.join(sorted(valid_roles))}")






def load_db():
    """Load and return all staff data from db.json."""
    try:
        with open("db.json", "r+") as f:
            data = json.load(f)
            
            return data
    except FileNotFoundError:
        print("db.json not found. Creating an empty one...")
        with open("db.json", "r+") as f:
            json.dump([], f, indent=4)
        return []
    except json.JSONDecodeError:
        print("db.json is corrupted. Resetting...")
        with open("db.json", "w") as f:
            json.dump([], f, indent=4)
        return []


def get_all_staff():
    """Retrieve all staff members from the database."""
    staff = load_db()
    return staff


def clear_db():
    with open("db.json", "r+") as f:
        json.dump([], f, indent=4)

def add_staff_member():
    """Add a new staff member to the database."""
    staff = load_db()
    name = input("Enter name: ").strip()
    role = validate_role()
    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()

    new_id =str(uuid.uuid4())

    new_staff = {
        "id": new_id,
        "role": role,
        "name": name,
        "email": email,
        "password": password,
        "salary": None,
        "hire_date": None,
        "is_active": True,
        "age": None,
        "address": None,
        "phone_number": None
    }

    staff.append(new_staff)
    save_db(staff)

    print(f"Staff member '{name}' added successfully with ID {new_id}.")


    


def update_staff_member(id,**kwargs):
    """Update details of a staff member."""
    
    if not id:
        print("Error: Staff ID cannot be empty.")
        return
    
    name = kwargs.get("name", None)
    role = kwargs.get("role", None)
    email = kwargs.get("email", None)
    password = kwargs.get("password", None)
    is_active = kwargs.get("is_active", None)

    db_data = get_all_staff()  # load all staff members
    new_db = []
    found = False

    for data in db_data:
        if data["id"] == id:
            found = True
            updated_info = {
                "id": data["id"],  # preserve the ID
                "name": name if name is not None else data["name"],
                "role": role if role is not None else data["role"],
                "email": email if email is not None else data["email"],
                "password": password if password is not None else data["password"],
                "is_active": is_active if is_active is not None else data["is_active"],
                "salary": data.get("salary"),
                "hire_date": data.get("hire_date"),
                "age": data.get("age"),
                "address": data.get("address"),
                "phone_number": data.get("phone_number")
            }
            new_db.append(updated_info)
        else:
            new_db.append(data)

    if not found:
        print(f"Error: Staff member with ID {id} not found.")
        return

    # Save all staff back to the DB
    with open("db.json", "w") as f:
        json.dump(new_db, f, indent=4)

    print(f"Staff member with ID {id} updated successfully.")


    
def delete_staff_member():
    """Delete a staff member by their ID."""
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
    print("5. get_single_staff_member\n")
    print("6. filter_staff_by_role\n")
    
user_resp = input("What would you like to do? ")

try:
    resp = int(user_resp)

    if resp == 1:
        add_staff_member()
    elif resp == 2:
        while True:
            staff_id = input("Enter staff ID to update (or type 'quit' to exit): ")
            if staff_id.lower() == "quit":
                print("Exiting update mode.")
                break
            if not staff_id:
                print("Error: Staff ID cannot be empty.")
                continue
            print("Enter new details (leave blank to keep current value):")
            name = input("Name: ")
            role = input("Role: ")
            email = input("Email: ")
            password = input("Password: ")
            is_active_input = input("Is Active (True/False): ").lower()
            is_active = None
            if is_active_input:
                is_active = is_active_input == "true"
            update_staff_member(staff_id, name=name if name else None, role=role if role else None, email=email if email else None, password=password if password else None, is_active=is_active)
            print(f"Staff member {staff_id} has been updated successfully")
            break


    elif resp == 3:
        pass
    elif resp == 4:
        print(get_all_staff()) 
    elif resp == 5:
        pass
    elif resp == 6:
        pass
    else:
        print("Choose a correct option.")
except Exception as e:
    print("Invalid input:", e)
