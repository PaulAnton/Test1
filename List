if __name__ == '__main__':
#    N = int(input())
    N = int(input())
    list1 = []
    for _ in range(N):
        s = input().split(" ")
        command = s[0]
        argument = s[1:]
        #print(s[0])
        #print(s[1:])
        if command !="print":
            command += "("+ ",".join(argument) +")"
            #print(command)
            eval("list1."+command)
        else:
            print (list1)
