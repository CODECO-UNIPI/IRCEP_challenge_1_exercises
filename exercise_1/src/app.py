# Υπολογισμός αθροίσματος τετραγώνων για αριθμούς 1..Ν

import sys

def sum_of_squares(n: int) -> int:
    return sum(i * i for i in range(1, n + 1))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Χρήση: python app.py <N>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Το N πρέπει να είναι ακέραιος αριθμός.")
        sys.exit(1)

    result = sum_of_squares(n)
    print(f"Άθροισμα τετραγώνων από 1 έως {n}: {result}")
