email=input('enter email')
password=input('enter password')
if email=='abc@gmail.com' and password=='12345':
    print("Welcome")
elif email=='abc@gmail.com' and password!='12345':
    print('your password is incorrect')
    password=input('enter password again')
    if password=='12345':
        print('password is correct')
    else:
        print('how are you buddy?')    
else:
    print("incorect email/password")
