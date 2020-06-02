from BigInt import BigInt

firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

llNumber = BigInt()
llNumber2 = BigInt()

llNumber.insertNumber(firstNumber)
llNumber2.insertNumber(secondNumber)
sum = llNumber2 + llNumber
print(sum.listprint())
#$print(llNumber2.listprint())