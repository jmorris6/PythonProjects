def getValues():
    array1 = []
    array2 = []
    with open("input1.txt", "r") as file1:
        value = file1.readline()
        while(value != ""):
            array1.append(int(value))
            value = file1.readline()
    with open("input2.txt", "r") as file2:
        value = file2.readline()
        while(value != ""):
            array2.append(int(value))
            value = file2.readline()
    return array1, array2

def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]

        mergeSort(L)
        mergeSort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i+= 1
            else:
                array[k] = R[j]
                j+= 1
            k+=1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j+= 1
            k+=1
    return array
            
def outputResults(array):
    with open("output.txt", "w") as file:
        for x in range(len(array)):
            file.write(str(array[x]) + "\n")
array1, array2 = getValues()
array = array1 + array2
array = mergeSort(array)
outputResults(array)
