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
def  persistent(name,month,deficiencies):
    if (month>0 and month<13) and(deficiencies>-1 and deficiencies<32):
        if deficiencies>5:
            answer="Warning!"
        else:
            answer="Excellent!"
        print(answer, "Hello", name, "your deficiencies is:", deficiencies)
    else:
        print("Error.")

    
