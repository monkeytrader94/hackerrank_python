if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    lst = list(set(arr))
    lst.sort()
    
    print(lst[-2])