print(f"a: {20 > 10}")
print(f"b: {5 == 9}")
print(f"c: {5 == 0}")
print(f"d: {5 == 5}")

print("one is equal to 4:",int(1==4))
print("two is equal to 2:",int(2==2))

myname = "Easton"
myage = "24"

print(f"a {70}") #Numeric Literal
print(f"b {'Hola'}") #String Literal
print(f"c: {True}") #Constant Literal
print(f"d: {myname}") #String Variable
print(f"e: {myage}") #Numeric Variable

print((1-2+3),(3-2+1))
print((1*2+3),(3*2+1))

print(f"is 'joe'=='joseph'? {'joe'=='joseph'}")

my_name = "Easton"
print("assignment: ",my_name)
print("equality: ",my_name == "Easton")

print("comparison:","aa"<"b")
print("comparison:",5 < 6)

a = 5
b = 7
print(f"comparison: {a} is greater than {b}" if a > b else "")
print(f"comparison: {a} is less than {b}" if a < b else "")
print(f"comparison: {a} is greater than or equal to {b}" if a >= b else "")
print(f"comparison: {a} is less than or equal to {b}" if a <= b else "")

bank_balance = 25
if bank_balance <500:
    money = 1000
    bank_balance += money
else:
    print("balance is less than or equal to 100.")

bank_balance = 650
savings = 120
if bank_balance < 100:
    savings += 90
    bank_balance -= 90
elif bank_balance > 200:
    savings += 150
    bank_balance -= 150
else:  
    savings += 50
    bank_balance -= 25

print(bank_balance)
print(savings)

fuel = 2
print("fill tank now" if fuel <= 1 else "There's enough fuel")

fuel = 5
while fuel >2:
    #keep driving
    print("You have enough fuel")
    fuel -=1

books = ['harry potter','lord of the rings','my autobiography']
for book in books:
    print(f"book: {book}")

for i in range(6):
    print(f'i: {i}')

# examples of using 'break'
for count in range(7):
    print(f"{count} times 10 is {count * 10}")
    if count == 4:
        break

# example of using 'continue'
for count in range(8):
    if count == 3:
        continue
    print(f"{count} times 5 is {count * 5}")
    








