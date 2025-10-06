temp = 50

if temp > 80:
    print("It's too hot!")
    print("stay inside")
elif temp < 60:
    print("It's too cold!")
    print("stay inside")
else:
    print("enjoy the weather!")

print("OR statement")
if temp > 80 or temp < 60:
    print("stay inside")
else:
    print("enjoy the weather!")