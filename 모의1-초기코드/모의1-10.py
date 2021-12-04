def solution(arr, k):
    answer=0
    emp=[]
    for i in arr:
        emp.extend(i)
    emp.sort()
    answer=emp[k-1]
    return answer

arr=[[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]]
k=4
answer=solution(arr, k)
print("solution(arr, k)의 리턴값: {}".format(answer))
