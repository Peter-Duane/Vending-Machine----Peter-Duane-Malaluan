items_data = [
    {
        "itemId": 0,
        "itemName": "Green Tea",
        "itemCost": 20,
     },
    {
        "itemId": 1,
        "itemName": "Jasmine Tea",
        "itemCost": 20,
     },
    {
        "itemId": 2,
        "itemName": "Earl Gray",
        "itemCost": 25,
     },
    {
        "itemId": 3,
        "itemName": "English Breakfast",
        "itemCost": 25,
     },
    {
        "itemId": 4,
        "itemName": "Chamomile Tea",
        "itemCost": 30,
     },
]   

item = [] 

total_sum = 0  # changed variable name to total_sum to avoid confusion with built-in `sum()`
balance = 0
run = True # as long as this variable is true, the machine will run
print("----- Vending Machine -----\n\n")
print("----- Item Data -----\n\n")

for i in items_data:
    print(f"#: {i['itemId']} --- {i['itemName']} --- Cost: {i['itemCost']}")
    
def insertMoney(balance):
    while True:
        try:
            amount = int(input("Insert money: "))
            if amount > 0:
                balance += amount
                print(f"You've inserted {amount}. Total balance: {balance}")
            else:
                print("Please insert a positive amount.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    return balance
    
def vendingMachine(items_data, run, item, balance): # the main function for the vending machine
    balance = insertMoney(balance)
    
    while run:
        try:
            buyItem = int(input("\n\nEnter the item code for the item you want to buy: ")) 
            if buyItem < len(items_data): # if the user inputs a number within the length of the list 
                item_data = items_data[buyItem]
                if balance >= item_data['itemCost']:
                    item.append(item_data)
                    balance -= item_data['itemCost']
                    print(f"Added {item_data['itemName']} to your selection. Remaining balance: {balance}")
                else:
                    print("Insufficient funds, please try again.")
                    try:
                        addMoney = int(input("Please insert more funds: "))
                        if addMoney >= 0:
                            balance += addMoney
                        else:
                            print("Please enter valid amount")
                            continue
                    except ValueError:
                        print("Please enter a proper value")
            else:
                print("Please input a correct code.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        moreItems = input("Type 'more' to add more items, type 'stop' to stop: ").lower()
        if moreItems == "stop":
            run = False  # now that it's false, the machine will not run
    receiptValue = int(input("1. Print the bill. 2. Print total sum: "))
    if receiptValue == 1:
        print(createReceipt(item, balance))
    elif receiptValue == 2:
        print(f"Total sum: {sumItem(item)}")
    else:
        print("Invalid input, please try again.")

def sumItem(item):
    sumItems = 0
    for i in item:
        sumItems += i["itemCost"]
    return sumItems

def createReceipt(item, balance):
    receipt = """
    \t\tProduct -- Cost
    """
    for i in item: 
        receipt += f"""
        \t{i['itemName']} -- {i['itemCost']}
        """  
    receipt += f"""
        \tTotal Sum --- {sumItem(item)}
        """
    receipt += f"""
        \tRemaining Balance --- {balance}
        """
    return receipt
        
vendingMachine(items_data, run, item, balance)


