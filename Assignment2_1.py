def check_sorted(A):
    n = len(A)
    
    for i in range(1, n):
        if A[i] < A[i - 1]:
            return "Failure"
    
    return "Success"


A= [1, 2, 3, 4, 5, 6, 7, 9, 8, 10]
print(check_sorted(A)) # Success