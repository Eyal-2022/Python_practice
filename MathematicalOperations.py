# כתבו פונקציה המקבלת 3 נתונים על כלי שיט
# 1. כמות ליטרים של דלק בכלי  2. צריכת דלק לק"מ של הכלי   3. מהירות ממוצעת של הכלי בקמש
#   א. על הפונקציה לקלוט מהמקלדת אורך מסלול שייט ולהדפיס תשובה בוליאנית האם הכלי יכול לבצע את המסלול
#  ב. במידה והכלי יכול לבצע את המסלול שנקלט מהמקלדת , על הפונקציה להדפיס את משך זמן השייט בשעות
def f1(quantity,fuel,speed):
    length1=int(input("Enter the Length of the cruise:"))
    lengthVessel=quantity*fuel
    if lengthVessel>=length1:
        ans=True
    else:
        ans=False
    print(ans)
    if ans==True:
        time=length1/speed
        print(time)
