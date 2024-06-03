def checkSort (a,n):
    isSorted = Ture
    for i in range(1,n):
        isSorted = False
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("정렬완료")
    else:
        print("정렬오류 발생")