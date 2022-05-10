for fizzBuzz in range(1, 101):
    if fizzBuzz % 3 == 0 and fizzBuzz % 5 == 0:
        print ('FizzBuzz')
    elif fizzBuzz % 3 == 0:
        print ('Fizz')
    elif fizzBuzz % 5 == 0:
        print ('Buzz')
    else:
        print (str(fizzBuzz))
