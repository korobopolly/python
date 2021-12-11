def solution(command):
    save_string, tmp_string ="",""
    for c in command:
        cmd = c
        if cmd =="save":
            save_string += tmp_string
            tmp_string =""
        elif cmd =="cancel":
            tmp_string =""
        else:
            tmp_string += cmd[6]
    return save_string+tmp_string

command = ["input a", "save","input b","input c", "cancel","input x"] 
ret = solution(command)
print(ret)
