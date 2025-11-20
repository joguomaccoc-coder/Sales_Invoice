def main():
    all_orders = []  #stores all customer orders

    while True:
        print("----------MENU----------")
        print("Bacon Burger")
        print("Hungarian Sandwich")
        print("Shawarma Burger")
        print("Black Pepper Burger")
        print("Crispy Chicken Burger")

        print("---------USER----------")

        grand_total = 0
        customer_items = []

        while True:
            item_name = input("Item_name: (type enter to break): ")
            if item_name.lower() == "enter":
                break

            while True:
                try:
                    quantity = int(input("Quantity: "))
                    if quantity <= 0:
                        print("Please enter a valid number!")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number!")

            while True:
                try:
                    price = int(input("Price: "))
                    if price <= 0:
                        print("Please enter a valid number!")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number!")

            total = quantity * price
            grand_total += total

            print(f"Total for {item_name}: {total}")
            customer_items.append({
                "item_name": item_name,
                "quantity": quantity,
                "price": price,
                "total": total
            })

        if not customer_items:
            print("No items ordered.")
            while True:
                another_order = input("You don't purchase an item do you want to add? (yes/no): ")
                if another_order.lower() == "yes":
                    break
                elif another_order.lower() == "no":
                    break
                else:
                    print("Invalid input! Please enter 'yes' or 'no'.")
            if another_order.lower() == "yes":
                continue
            else:
                break

        print("___________________")
        print("--------INVOICE--------")
        print("-----------------------")
        print("Items Purchased:")

        for item in customer_items:
            print(f"{item['item_name']}: {item['quantity']} x {item['price']} = {item['total']}")

        print("---------------------------")
        print(f"Grand Total: {grand_total}")
        print("---------------------------")

        while True:
            try:
                amount_tendered = float(input("Amount Tendered: "))
                if amount_tendered < grand_total:
                    print("Please enter a valid amount!")
                    continue
                break
            except ValueError:
                print("Please enter a valid amount!")

        change = amount_tendered - grand_total
        print(f"Change: {change}")
        print("-----------------")

        # Save order to history
        all_orders.append(customer_items)

        while True:
            another_transaction = input("Do you want another transaction? (yes/no): ")
            if another_transaction.lower() == "yes":
                break
            elif another_transaction.lower() == "no":
                break
            else:
                print("Invalid input! Please type 'yes' or 'no' ")

        if another_transaction.lower() == "yes":
            continue
        else:
            while True:
                view_orders = input("View all orders? (yes/no): ")
                if view_orders.lower() == "yes":
                    print("------- ALL ORDERS -------")
                    for order in all_orders:
                        for item in order:
                            print(f"{item['item_name']}: {item['quantity']} x {item['price']} = {item['total']}")
                        print("--------------------------")
                    break
                elif view_orders.lower() == "no":
                    break
                else:
                    print("Invalid input! Please type 'yes' or 'no' ")
            break


if _name_ == "_main_":
    main()