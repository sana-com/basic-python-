def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
            return False
    return True
def generate_primes(start, end):
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

def main():

    num = int(input("Enter a number to check if it's prime: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

    start = int(input("\nEnter start of range: "))
    end = int(input("Enter end of range: "))
    prime_list = generate_primes(start, end)
    print(f"Prime numbers between {start} and {end} are:\n{prime_list}")


main()
