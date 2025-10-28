# sample
def get_adult_users(users):
    adults = []
    for user in users:
        if user.get("age", 0) > 18:
            adults.append(user["name"])
    return adults


# Example usage:
users_list = [
    {"name": "Akash", "age": 17},
    {"name": "Riya", "age": 22},
    {"name": "Manoj", "age": 19},
]

print(get_adult_users(users_list))  
