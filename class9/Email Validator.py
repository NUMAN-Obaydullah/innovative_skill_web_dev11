def process_email(email):
    email = email.strip().lower().split('@')
    return (email[0], email[1])

procesed_mail= (process_email("obaydullah@example.com"))
print(type(procesed_mail), procesed_mail)