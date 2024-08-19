amount = int(input("enter amount of purchase"))
if amount<=1000:
    print("the discount price is",amount/100*10)
elif 1000< amount <= 5000:
    print("the discount price is",amount/100*20)
elif 5000< amount <= 10000:
    print("the discount price is",amount/100*30)
else:
     print("the discount price is",amount/100*50)
