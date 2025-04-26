#--------------------------------------------------
#  Password Functions
#--------------------------------------------------

#--------------------------------------------------
# Function:
def valid_password(a):

    upper = False
    lower = False
    digit = False
    special = False

    for chr in a:
        if 'A' <= chr <= 'Z':
            upper = True
        elif 'a' <= chr <= 'z':
            lower = True
        elif '0' <= chr <= '9':
            digit = True
        elif chr in '!@#$%^&*()':
            special = True
        
    if len(a) < 8:
        return 'password should be more than 8 characters'
    elif not upper:
        return 'password should contain at least one uppercase letter'
    elif not lower:
        return 'password should contain at least one lowercase letter'
    elif not digit:
        return 'password should contain at least one digit'
    elif not special:
        return 'password should contain at least one special character'
    else:
        return 'Valid'  
#--------------------------------------------------
#Maiun Program:

password = input('enter password:')
result = valid_password(password)
if result == 'Valid':
    print('Valid password, Password successfully set!')
else:
    print('invalid password',result)
#--------------------------------------------------