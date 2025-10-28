def get_adult_users(users):
    adults = []
    for user in users:
        if user['age'] > 18:
            adults.append(user['name'])
    return adults


users = [
    {'name': 'Uttam', 'age': 20},
    {'name': 'Ravi', 'age': 16},
    {'name': 'Meera', 'age': 25}
]

print(get_adult_users(users))
