action = ""  
carts =[]   #Appends all items the user adds in this list variable
prices = []   #Appends prices of the items in this list variable
total_items = ""

print("Welcome to the Shopping Cart Program")
print()

while action != "5":   # This loops until the user enter option 5 to quit
    print()
    print("Please select one of the following: ") #Asks the user to select an option from the menu
    print("1. Add item")    #menu option 1
    print("2. View Cart")    #menu option 2
    print("3. Remove item")   #menu option 3
    print("4. Compute total")    #menu option 4
    print("5. Quit")     #menu option 5
    print()

    action = input("Please enter an action: ")  #Asks the user to select an action he would like to take
    if action == "1":
        add_item = input("What item would you like to add? ").capitalize()
        price = float(input(f"What is the price of the {add_item}? "))  #converts entry to a float. Prices could be float instead of an interger
        carts.append(add_item)
        prices.append(price)     #This adds the item the user entered to the cart list
        print()
        print(f"'{add_item}' has been added to your cart")  #Notifies the user that the item has been added to the cart
        
    
    elif action == "2":
        if(len(carts)>0):
            print("The contents of your shopping list are:")  
        for i in range(0,len(carts)):
            print("{0}. {1} - ${2}".format(i+1, carts[i], (prices[i])))
        
        
  #for example, if the has 2 items in the cart and wants to remove a 4th item,
  #the program informs the user that the number is invalid
  #because 4 - 1 > 2, 3 is greater than 2 (items) in the cart, and that is not possible
    elif action == "3":
         remove_item = int(input("What item would you like to remove? "))
         if (remove_item - 1)> len(carts):  
             print("Sorry, that item number was not valid.")
         else:
             del carts[remove_item - 1]  #deletes the number from the cart.
             #If the user enter 5, python reads it as 6, so the "-1" balances the calculation
             #With this, if the user wants to delete number 4, and enter 4, but to actually get the 4,
             #python reads it as 5, and then we have 5 - 1 to give 4.
             del prices[remove_item - 1]
             print("The item was removed")
        
    elif action == "4":
         total = sum(prices)  # vairable to sum up the prices of items in the cart
         total_items = len(carts)   #variable for the total number of items in the cart #Showed creativity
         print(f"You have {total_items} item(s) in your cart.")
         print(f"The total price of items in the shopping cart is ${total :.2f}.") #Prints the total prices of items in the cart
                                                                                  #rounds it up to 2 decimal places             
else:              #If the user has nothing else to add, remove, view, then this terminates the loop.
    print("Thank you. Goodbye.")
        