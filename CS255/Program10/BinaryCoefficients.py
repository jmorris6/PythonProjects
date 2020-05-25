def binaryCoefficient(n, k):
    if k == 0:
        return 1
    elif n == k:
        return 1
    elif n < k:
        return 0
    else:
        return binaryCoefficient(n-1, k-1) + binaryCoefficient(n-1, k)

n = int(input("Input the n value: "))
k = int(input("Input the k value: "))
print(str(n) + " choose " + str(k) + " = " + str(binaryCoefficient(n, k)))