# Boolean untuk status online
def check_online_status(users):
    return {user: bool(status) for user, status in users.items()}

users = {
    "Alice": True,
    "Bob": False,
    "Charlie": True
}

print("Status online pengguna:", check_online_status(users))
