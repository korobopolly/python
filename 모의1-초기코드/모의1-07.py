def solution(s):
    s_lst=list(s)
    n=len(s)
    for i in range(n):
        if s_lst[i]=='a':
            s_lst[i]='z'
        elif s_lst[i]=='z':
            s_lst[i]='a'
    return "".join(s_lst)

s="abz"
answer=solution(s)
print("solition(s)의 리턴값: {}".format(answer))
