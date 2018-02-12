#Your optional code here
#You can import some modules or create additional functions
# my solution
def checkio(number):
    answer = []
    # (number % 3)
    if (number % 3 == 0):
        answer.append('Fizz')

    if (number % 5 == 0):
        answer.append('Buzz')

    if not answer:
        return str(number)
    else:
        return (' '.join(answer))
# creative solution
# result = "Fizz Buzz" if (number%15 == 0) else ( "Fizz" if number%3==0 else ("Buzz" if number%5 == 0 else str(number)))


#Some hints:
#Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# print(checkio(15))
# checkio(6)
# checkio(5)
# checkio(7)