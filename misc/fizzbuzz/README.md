# Fizzbuzz

The FizzBuzz challenge is a counting challenge that does not follow the traditional selection process (if/elseif/else)

*Write a program that prints the numbers from 1 to 100. But for multiples of three print 'Fizz' instead of the number and for the multiples of five print 'Buzz'. For numbers which are multiples of both three and five print 'FizzBuzz'.*

My favourite approach is to generate a string and append 'fizz' and 'buzz' where applicable. This means that when we have to decide whether to print this string or the number itself, we simply need to check whether this output string has been extended or not.
