# 1. #  Write a function called greet_user() that returns:
#    "Welcome to the Backend Class!"

def greet_user():
    return "Welcome to Backend Class!"
print(
    greet_user()
)



# 2. Write a function called add_numbers(a, b) that returns the sum of two numbers.

def add_numbers(a, b):
    return a + b

print(
    add_numbers(1, 2)
)



# 3. Write a function called subtract_numbers(a, b) that returns the difference.

def subtract_numbers(a, b):
    return a - b

print(
    subtract_numbers(56, 50)
)


# 4. Write a function called format_full_name(first_name, last_name)
#    that returns: "Full Name: John Doe"

def format_full_name(first_name, last_name):
    return f"Full Name: {first_name} {last_name}"

print(
    format_full_name("Andi", "udom")
)


# 5. Write a function called check_login(is_logged_in)
#    If True return "Access Granted"
#    Else return "Access Denied"

def check_login(is_logged_in):
    if is_logged_in:
        return "Access Granted"
    else:  
        return "Access Denied"

print(
    check_login(False)
)

print(
    check_login(True)
)



# 6. Write a function called student_profile(name, age, course)
#    that returns a dictionary with the student information.

def student_profile(name, age, course):
    return {"name": name, "age": age, "course": course}

print(
    student_profile("Andi", 19, "Computer Science")
)



# 7. Write a function called is_adult(age)
#    Return "Adult" if age >= 18 else "Minor"


def is_adult(age):
#return "Adult" if age >= 18 else "Minor"
    if age >= 18:
        return "Adult"
    else: 
        return "Minor"

print(
    is_adult(13)
)



# 8. Write a function called calculate_discount(price, discount=10)
#    Apply the discount percentage and return the final price.


def calculate_discount(price, discount=10):
    price_discount = price * (discount/100)
    final_price = price - price_discount
    return final_price

print(
    calculate_discount(5000, 10)
)


# 9. Write a function called register_users(*names)
#    It should return all names inside a tuple.

def register_users(*names):
    return names

print(
    register_users("Andi", "Michael", "Vicky", "Miracle")
)


#10. Write a function called create_account(**details)
#     It should return the details as a dictionary.

def create_account(**details):

    return details

print(
    create_account(
        first_name=  "Andi",
        last_name= "Udom",
        age= "19",
        is_active=  "True"
    )
)

print(type(create_account()))



# 11. Write a function called backend_response(message, status="success")
#     Return:
#     {"status": status, "message": message}

def backend_response(message, status="success"):
    return {"status": status, "message": message}

print(
    backend_response("message", "success")
)



# 12. Write a function called find_product(products, name)
#     products will be a list of dictionaries.
#     Return the dictionary that matches the product name.

def find_product(products, name):
    for product in products:
        if product["name"] == name:
            return product

products = [
    {"name": "iphone17pm"},
    {"name": "iphone16pm"},
    {"name": "iphone15pm"},
    {"name": "iphone14pm"}
]

print(
    find_product(products, "iphone16pm")
    )


# 13. Write a function called total_cart_price(cart)
#     cart is a list of items like:
#     {"name": "rice", "price": 2000}
#     Return the total price.

def total_cart_price(cart):

    total_cart_price = 0

    for item in cart:
        total_cart_price = total_cart_price + item["price"]
    return total_cart_price

cart = [
    {"name": "rice", "price": 2000},
    {"name": "beans", "price": 3000}
]


# 14. Write a function called add_to_cart(cart, item_name, quantity, unit_price)
#     It should add a new dictionary into the cart list.


def add_to_cart(cart, item_name, quantity, unit_price):

    item = {
        "name": item_name,
        "quantity": quantity,
        "unit_price": unit_price
    }

    cart.append(item)

    return cart

cart = []


first_add = add_to_cart(cart, "Laptop", 2, 200000.00)


second_add = add_to_cart(cart, "Laptop", 3, 600000.00)


print(cart)



#15. Write a function called generate_receipt(cart)
#     Print each item and return the total cost.


def generate_receipt(cart):

    total_cost = 0

    print(f'{"==" * 24}\nSHOPPING CART: YOUR RECEIPT\n{"==" * 24}')

    for item in cart:
        print(f'Item name: {item["name"]} quantity: {item["quantity"]} unit price: {item["unit_price"]} cost: {item["quantity"] * item["unit_price"]}')
    else:
        for item in cart:
            total_cost = total_cost + item["quantity"] * item["unit_price"]
        else:
            print(f"Total Cost: {total_cost}")

    return total_cost

cart = [
    {"name": "Laptop", "quantity": 2, "unit_price": 200000.0},
    {"name": "Mouse", "quantity": 3, "unit_price": 5000.0}
]

total = generate_receipt(cart)
print("Total returned:", total)


# 16. Write a function called validate_email(email)
#     Return True if email contains "@" else False.

def validate_email(email):
     
    if "@" in email:
        return True
    else:
        return False
print(
    validate_email("andiudom274@gmail.com")
)
print(
    validate_email("andiudom274gmail.com")
)



#17. Write a function called api_response(data, code=200)
#     Return:
#     {"code": code, "data": data}

def api_response(data, code=200):
    return {"code": code, "data": data}

print(
    api_response("successful", 200)
    # api_response(data={"name": "successful"})
)



# 18. Write a function called update_user(user_dict, **kwargs)
#     Update the user dictionary with new values.

def update_user(user_dict, **kwargs):
    user_dict.update(kwargs)
    return user_dict

# def update_user(user_dict, **kwargs):
#     for key, values in kwargs.items():
#         user_dict[key] = values
#     else:
#         return user_dict

#def update_user(user_dict, **kwargs):
#    return {**user_dict, **kwargs} # destruction

print(
    update_user({"name": "Andi"}, age=19, gender="male")
)


# 19. Write a function called find_max_number(numbers)
#     numbers is a list of integers.
#     Return the largest number in the list.

def find_max_number(numbers):
    return max(numbers)

# def find_max_number(numbers):
#     max_number = 0

    # for num in numbers:
    #     if num > max_number:
    #         max_number = num
    #     else:
    #         return max_number

print(
    find_max_number([1,3,7,0,12,57])
)


# 20. Write a function called count_vowels(word)
#     Return the number of vowels (a, e, i, o, u) in the word.

def count_vowels(word):
    count = 0

    for character in word:
        if character in "aeiou":
            count = count + 1
    else:
        return count
    
print(
    count_vowels("Andikan")
)
