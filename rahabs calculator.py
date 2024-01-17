firstnumber = input("enter your firstnumber : ")
operator = input("enter your operator: (+ , -, *, /, %)")
secondnumber = input("enter your secondnumber : ")

firstnumber = int(firstnumber)
secondnumber = int(secondnumber)

if operator == "+":
    print(int(firstnumber + secondnumber))
    
elif operator == "-":
    print(int(firstnumber-secondnumber))

elif operator =="*":
    print(firstnumber  * secondnumber)

elif operator =="/":
    print(firstnumber / secondnumber)

elif operator == "%":
    print(firstnumber  % secondnumber)
 

 





