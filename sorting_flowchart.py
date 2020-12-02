def main():
    print(bubble_sort([4, 5, 2, 1, 0, 9]))


def bubble_sort(numbers):
    N = len(numbers)
    for i in range(N-1):
        for j in range(N-i-1):
            if (numbers[j] > numbers[j+1]):
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp
    return numbers
    
    
if __name__ == '__main__':
    main()