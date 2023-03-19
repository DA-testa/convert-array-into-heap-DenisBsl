# python3
# 221RDB188 Deniss Buslajevs 8.grupa

def build_heap(data):
    swaps = []
    for i in range(len(data) // 2 - 1, -1, -1):
        node = i

        while node * 2 + 2 < len(data) and data[node] > data[node * 2 + 1]:
            child = node * 2 + 1
            if data[child + 1] < data[child]:
                child += 1
            swaps.append([node, child])
            data[child], data[node] = data[node], data[child]
            node = child
    return swaps


def main():
    
    data = input()
    if "F" in data:
        data = input()
        with open("./tests/" + data) as f:
            n = int(input())
            data = list(map(int, input().split()))
    elif "I" in data:
        n = int(input())
        data = list(map(int, input().split()))
    else:
        exit

    

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
