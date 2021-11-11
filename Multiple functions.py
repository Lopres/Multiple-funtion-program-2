def Apples_want_to_buy():
    apples = int(input("Apples: "))
    oranges = int(input("Oranges: "))
    return apples, oranges 

def compute_amount(apples, oranges, price_of_apple, price_of_orange):
    apple_amount = apples * price_of_apple
    orange_amount = oranges * price_of_orange
    total_amount = apple_amount + orange_amount
    return apple_amount, orange_amount, total_amount

def display_output(total_amount):
    print (f"The total amount is {total_amount}")






#Create a program that will ask how many apples and oranges you want to buy.
print ("How many you want to buy? ")
apples, oranges, = Apples_want_to_buy()
#Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
price_of_apple = 20
price_of_orange = 25
#Display the output in the following format.
apple_amount, orange_amount, total_amount = compute_amount(apples, oranges, price_of_apple, price_of_orange)
#The total amount is ______.
display_output(total_amount)