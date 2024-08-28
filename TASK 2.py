def addition(M, N):
    return M + N

def subtraction(M, N):
    return M - N

def multiplication(M, N):
    return M * N

def division(M, N):
    return M / N

def get_user_choice():
    print("Select operation:")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MILTIPLICATION")
    print("4. DIVISION")

    choice = input("Enter choice(1/2/3/4): ")
    return choice

def calculator():
    num1 = float(input("ENTER THE FIRST NUMBER: "))
    num2 = float(input("ENTER THE SECOND NUMBER: "))

    choice=get_user_choice()
    
        
    if choice == '1':    
        print(f"{num1} + {num2} = {addition(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtraction(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiplication(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {division(num1, num2)}")
    else:
        print("INVALID INPUT.ENTER A VALID CHOICE.")
   
calculator()        


