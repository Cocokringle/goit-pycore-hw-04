def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if(name in contacts):
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact name {name} does not exist"
    
def show_phone(contacts):
    name = args[0]
    if(name in contacts):
        return f"{contacts[name]}"
    else:
        return f"Contact name {name} does not exist"

def show_all(contacts):
    return f"{contacts}"
