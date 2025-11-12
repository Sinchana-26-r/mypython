def simple_interest(principal,rate,time):
    interest = (principal*rate*time)/100
    return interest
result = simple_interest(100,6,4)
print("simple interest:",result)
