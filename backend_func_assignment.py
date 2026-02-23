
# 1. Write a function called login_user(username, password)
#    - If username is "admin" and password is "1234"
#      return "Login Successful"
#    - Else return "Invalid Credentials"

def login_user(username, password):
    # if username == "admin" and password == "1234":
    #    return "Login Successful"
    # else: 
    #     return "Invalid Credentials"
    return "Login Successful" if username == "admin" and password == "1234" else  "Invalid Credentials"
print(
    login_user("admin", "1234")
    )
print(
    login_user("user", "124")
    )


# 2. Write a function called response(message, code)
#    It should return a dictionary like:
#    {"status": code, "message": message}

def response(message, code):
    return {"message": message, "status": code}

print(
    response("unsuccessful", 400)
)

print(
    type(response("successful", 200))
)


# 3. Write a function called validate_username(name)
#    Return True if the username has at least 4 characters,
#    else return False.

def validate_username(name):
    # if len(name) >= 4:
    #     return True
    # else: 
    #     return False
    return True if len(name) >= 4 else False

print(
    validate_username(input("Enter your username: "))
)

# 4. Write a function called is_valid_email(email)
#    Return True if email contains "@" and "."
#    Else return False.

def is_valid_email(email):
    # if ("@" in email) and ("." in email) :
    #     return True
    # else:
    #     return False

    return True if ("@" in email) and ("." in email) else False

print(
    is_valid_email(input("Enter your email: "))
)


# 5. Given a list of dictionaries called users,
#    write a function get_user_by_id(users, id)
#    that returns the user with the matching id.

def get_user_by_id(users, id):
    for user in users:
        if  user ["id"] == id:
            return user
users = [
    {"name": "andi", "id": 1},
    {"name": "michael", "id": 2},
    {"name": "Vicky", "id": 3},
    {"name": "William", "id": 4},
    {"name": "Miracle", "id": 5}
]

print(get_user_by_id(users, 5))
print(type(users))

# 6. Write a function called calculate_order_total(order)
#    order is a list like:
#    [{"item": "rice", "price": 2000}, {"item": "beans", "price": 3000}]
#    Return the total cost.

def calculate_order_total(order):

    total_cost = 0

    for item in order:
        total_cost = total_cost + item["price"]
    return total_cost
order = [
    {"item": "rice", "price": 2000},
    {"item": "beans", "price": 3000}
      ]

print(calculate_order_total(order))

# 7. Write a function called add_product(products, name, price)
#    It should add a new dictionary into the products list:
#    {"name": name, "price": price}

def add_product(products, name, price):

    item = {"name": name, "price": price,}
    products.append(item)
    return products

products = [
    {"name": "bmw", "price": 1200000000}
]

print(add_product(products, "benz", 90000000))

# 8. Write a function called check_permission(role)
#    - If role is "admin" return "Full Access"
#    - If role is "user" return "Limited Access"
#    - Else return "No Access"

def check_permission(role):
   if role == "admin":
       return "Full Access"
   elif role == "user":
        return "Limited Access"
   else:
       return "No Access"
#   return "Full Access" if role == "admin" else "Limited acesss" if role == "user" else "No access"

print(check_permission(""))

# 9. Write a function called update_profile(user_dict, **changes)
#    It should update the dictionary with the new values
#    and return the updated dictionary.

def update_profile(user_dict, **changes):
    user_dict.update(changes)
    return user_dict
    # return {**user_dict, **changes}

print(update_profile({"username": "Victor"}, age =29, gender = "male"))


# 10. Given a list of users with active status,
#     write a function called count_active_users(users)
#     Return how many users are active (True).

def count_active_users(users):
    count = 0
    for user in users:
        if "active" in user and user["active"]:
            count = count + 1
    return count

users = [
    {"username": "Victor", "active": True},
    {"username": "Alice", "active": True},
    {"username": "Bob", "active": False}
]

print(count_active_users(users))