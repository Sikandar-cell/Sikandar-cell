Secure = (('a', '@'), ('b','6'),('c','<'),('d','</'),('e','*_'),('f','|`'),('g','9'),('h','|-'),('i','!'),('j','%'),('k','|<'),('l','1'),('m','#'),('n','^'),('o','0'),('p','|*'),('q','*\/'),('r','|^'),('s',',<'),('t','|~'),('u','|_|'),('v','\/'),('w','\/\/'),('x',')('),('y','1/'),('z','-/_'),('A','/->'),('N','|\|'),('R','|>_'),('S','$$'))

def password_security(password):
    for a,b in Secure:
        password = password.replace(a,b)

    return password

inputdata = input("Type your desired password: ")
decision = input("Would you like to add capital letters in your passcode ? (y/n) ")

if decision == 'y':
    print(f"Your new password is: {password_security(inputdata)}")
else:
    print(f"For lower letters the password is: {password_security(inputdata.lower())}")