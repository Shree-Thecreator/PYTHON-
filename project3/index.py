menu={
   
'Tandoori Chicken ':120,
'Chicken Lollipop ':133,
 'Veg Biryani ':70,
'Paneer Tikka ':80,
'chicken kosha': 150,
'fried rice': 100,
'soft drinks':70,
'cake':120,
'water':50,
}
print("Welcome to out restaurent")
print("tandoori chicken:120/nchicken lolipop:133/nveg biriyani:70/npaneer tikka:80/nchicken kosha:150/nfried rice:100/nsoft drinks:70/ncake:120/nwater:50/n")

order_total=0

while True:

  item = input("Enter the food item you want to order: ")

if item in menu:
    order_total += menu[item]
    print("Your item has been added to your order.")
else:
    print("Sorry, we don't have the item now.")

print(f"Total order amount: {order_total}")
