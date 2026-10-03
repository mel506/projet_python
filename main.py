A = [18,21,15,23,12,19,16,3]
min = A[0]
for i in A:
    if i < min :
        min = i
position = A.index(min)
print("Le plus petit element de la liste est : ",min)
print("La position du minimum de la liste est : ",position)
    