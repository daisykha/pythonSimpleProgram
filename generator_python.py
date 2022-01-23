# Generator
# Positive integers up to and including N
# Divisible by M
# Calculate sum of all positive integers less than 102030 which are divisible by 3
def first_n_divisible_by(limit, m):
    num = 0
    while num <= limit:
        if num % m == 0:
            yield num
        num += 1


if __name__ == '__main__':
    # Question 1: Continued
    # Supposed to be strictly less than 102030 or less than or equal?
    by_3_to_10 = first_n_divisible_by(102030, 3)
    print(sum(by_3_to_10))
