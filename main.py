class ItemToPurchase:
    def __init__(self,item_name ="none",item_price =0,item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    def print_item_cost(self):
        total_price = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ {self.item_price} = $ {total_price:.2f}")

def get_valid_item_name():
    while True:
        item_name = input("Enter the item name:\n")
        if item_name.strip():
            return item_name
        print("Invalid input. Please enter a valid item name.")

#Validate the float input - item_price
def get_float_input(prompt):
    while  True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input.Please enter valid number")

#Validate the int input - item_price
def get_int_input(prompt):
    while  True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid Input.Please enter valid integer")

def main():
    #prompt the user for the first item
    print("Item 1")
    item_name1 = get_valid_item_name()
    item_price1 = get_float_input("Enter the item price:\n")
    item_quantity1 = get_int_input("Enter the item quantity:\n")
    # Create the first ItemToPurchase object
    item1 = ItemToPurchase(item_name1,item_price1,item_quantity1)

    #prompt the user for the first item
    print("Item 2")
    item_name2 = get_valid_item_name()
    item_price2 = get_float_input("Enter the item price:\n")
    item_quantity2 = get_int_input("Enter the item quantity:\n")
    # Create the first ItemToPurchase object
    item2 = ItemToPurchase(item_name2,item_price2,item_quantity2)

    # Print item costs
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    # Calculate and print total cost
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"\nTotal: ${total_cost:.2f}")


# Run the main function
if __name__ == "__main__":
    main()



    