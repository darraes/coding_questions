def find_happy_number(num):
    slow = fast = num
    while True:
        slow = next_number(slow)
        fast = next_number(next_number(fast))
        if fast == 1 or fast == slow:
            break
    return fast == 1


def next_number(n):
    result = 0
    while n > 0:
        result += (n % 10) ** 2
        n = n // 10
    return result


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
