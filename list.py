import math
import random
# כתבו פונקציה המקבלת רשימה ריקה, הפונקציה תקלוט 10 מספרים שלמים באופן רנדומלי בין 1 ל-6(כולל) , לאחר מכן הפונקציה תחזיר תשובה בוליאנית האם הרשימה סימטרית
def  f1(list1):
    for i in range(10):
        list1.append(random.randint(1,6))
    print(list1)
    for i in range(len(list1)//2):
        if list1[i] != list1[len(list1)-i-1]:
            return False
    return True
