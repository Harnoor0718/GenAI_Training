# Product = []

# while True:
#     print("1. Add Product")
#     print("2. View Product")
#     print("3. Calculate GST")
#     print("4. Calculate Discount")
#     print("5. Final Bill")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         name = input("Enter product name: ")
#         price = float(input("Enter product price: "))
#         qty = int(input("Enter product quantity: "))
#         Product.append((name, price, qty))

#         print("Product added successfully!")

#     elif choice == 2:
#         if not Product:
#             print("No products available.")
#         else:
#             print("Products available:")
#             for i in range(len(Product)):
#                 print(f"Name:{Product[i][0]}, Price: {Product[i][1]}, Quantity: {Product[i][2]}")

#     elif choice == 3:
#         if not Product:
#             print("No products available.")
#         else:
#             gst_rate = float(input("Enter GST rate (in %): "))
#             for i in range(len(Product)):
#                 gst_amount = Product[i][1] * (gst_rate / 100)
#                 total_price = Product[i][1] + gst_amount
#                 print(f"Name: {Product[i][0]}, Price: {Product[i][1]}, GST Amount: {gst_amount}, Total Price: {total_price}")

#     elif choice == 4:
#         if not Product:
#             print("No products available.")
#         else:
#             discount_rate = float(input("Enter discount rate (in %): "))
#             for i in range(len(Product)):
#                 discount_amount = Product[i][1] * (discount_rate / 100)
#                 total_price = Product[i][1] - discount_amount
#                 print(f"Name: {Product[i][0]}, Price: {Product[i][1]}, Discount Amount: {discount_amount}, Total Price: {total_price}")

#     elif choice == 5:
#         if not Product:
#             print("No products available.")
#         else:
#             total_bill = 0
#             for i in range(len(Product)):
#                 total_price = Product[i][1] * Product[i][2]
#                 total_bill += total_price
#                 print(f"Name: {Product[i][0]}, Price: {Product[i][1]}, Quantity: {Product[i][2]}, Total Price: {total_price}")
#             print(f"Final Bill Amount: {total_bill}")


#     elif choice == 6:
#         print("Exiting the program.")
#         break
    

class Test:
    def _init_(self):
        print(id(self))

t = Test()
print(id(t))
