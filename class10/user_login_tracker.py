login_counts = {"admin": 5, "dev_user": 12, "guest_1": 1}
def record_login(user_dict,username):
    user_dict.setdefault(username,0)
    user_dict[username] +=1
    
record_login(login_counts, "admin")
record_login(login_counts, "new_user")
record_login(login_counts, "guest_1")

print("After record_login calls:", login_counts)

new_logins = {"guest_2": 1, "dev_user": 1, "super_admin": 1}
for user,count in new_logins.items():
    login_counts[user] = login_counts.get(user,0) + count
print("After batch update:", login_counts)

