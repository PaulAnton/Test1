if __name__ == '__main__':
    students=[]
    for _ in range(0,int(input())):
        students.append([input(),float(input())])
    #print(students)
    second_lowest=sorted(list(set(y for x,y in students)))[1]
    #print(second_lowest)
    print("\n".join(sorted(x for x,y in students if y==second_lowest)))
