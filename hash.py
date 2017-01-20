if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    #k=input().split()
    #print(k)
    integer=tuple(integer_list)
    tup=hash(integer)
    #print(integer_list)
    print(tup)
