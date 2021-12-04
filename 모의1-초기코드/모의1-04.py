def solution(scores):
    grade_counter=[0 for i in range(5)]
    for x in scores:
        if 85<=x<=100: 
            grade_counter[0]+=1
        elif x>=70 and x<=84:
            grade_counter[1]+=1
        elif x>=55 and x<=69:
            grade_counter[2]+=1
        elif x>=40 and x<=54:
            grade_counter[3]+=1
        else:
            grade_counter[4]+=1
    return grade_counter

scores=[86, 72, 98, 60, 45]
answer=solution(scores)
print("solution(scores)의 리턴값: {}".format(answer))
