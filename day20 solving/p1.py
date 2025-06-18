def mail_validator(email:str):
    if '@' in email and '.' in email:
        return True
    else:
        return False
    
email = input()  
pro_email = email[1:len(email)-1]
print(pro_email,end = "")


