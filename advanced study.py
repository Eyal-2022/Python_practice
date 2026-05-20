#  תרגיל 2.2
def payment(count,age):
    activity=40
    if count>5:
        cost=(count*activity)*0.9
    else:
        cost=count*activity
    if age>=18:
        subscription="adult"
    else:
        subscription="child"
    print("The price to pay is",cost)
    print("The subscription is",subscription)
# תרגיל 2.3

    
