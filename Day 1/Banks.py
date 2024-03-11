balance = int(input('balance = '))
while balance > -1:
    if balance >= 0:
        What = input("What do you want me to do? expenses/revenue/exit -> ")
        if What == "expenses":
            expenses = int(input("How much? -> "))
            if expenses > balance:
                print('Operation not permitted: insufficient funds')
            else:
                balance = balance - expenses
                print('balance is', balance)
        elif What == "revenue":
            revenue = int(input("How much? -> "))
            balance = balance + revenue
            print('balance is', balance)
        elif What == 'exit':
            break
        else:
            print("Sorry I don't recognize this command")
        
    
    
 
        
