# Bakery Management System

import pandas as pd
import os

# Define the CSV file name to avoid dependency on openpyxl
FILE_NAME = "bakery_inventory.csv"

def load_inventory():
    """Loads the bakery inventory from a CSV file or creates a new one."""
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    else:
        df = pd.DataFrame(columns=["Item", "Category", "Price", "Stock"])
        df.to_csv(FILE_NAME, index=False)
        return df

def save_inventory(df):
    """Saves the updated inventory to a CSV file."""
    df.to_csv(FILE_NAME, index=False)

def add_item(df):
    """Adds a new item to the bakery inventory."""
    item = input("Enter item name: ")
    category = input("Enter category (Cake, Bread, Pastry, etc.): ")
    
    try:
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
    except ValueError:
        print("Invalid input! Price should be a number and stock should be an integer.")
        return df
    
    new_data = pd.DataFrame([[item, category, price, stock]], columns=df.columns)
    df = pd.concat([df, new_data], ignore_index=True)
    save_inventory(df)
    print("Item added successfully!")
    return df

def update_item(df):
    """Updates the stock or price of an existing item."""
    print(df)
    item = input("Enter the item name to update: ")
    if item in df["Item"].values:
        field = input("What do you want to update? (price/stock): ")
        if field == "price":
            try:
                new_price = float(input("Enter new price: "))
                df.loc[df["Item"] == item, "Price"] = new_price
            except ValueError:
                print("Invalid input! Price should be a number.")
                return df
        elif field == "stock":
            try:
                new_stock = int(input("Enter new stock quantity: "))
                df.loc[df["Item"] == item, "Stock"] = new_stock
            except ValueError:
                print("Invalid input! Stock should be an integer.")
                return df
        else:
            print("Invalid option!")
            return df
        save_inventory(df)
        print("Item updated successfully!")
    else:
        print("Item not found!")
    return df

def remove_item(df):
    """Removes an item from the inventory."""
    print(df)
    item = input("Enter the item name to remove: ")
    if item in df["Item"].values:
        df = df[df["Item"] != item]
        save_inventory(df)
        print("Item removed successfully!")
    else:
        print("Item not found!")
    return df

def view_inventory(df):
    """Displays the bakery inventory."""
    print("\nCurrent Bakery Inventory:")
    print(df)

def main():
    df = load_inventory()
    while True:
        print("\n--- Bakery Management System ---")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. View Inventory")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            df = add_item(df)
        elif choice == "2":
            df = update_item(df)
        elif choice == "3":
            df = remove_item(df)
        elif choice == "4":
            view_inventory(df)
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
