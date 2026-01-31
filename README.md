# Ratio-of-prime-numbers
This code designed to approach the ratio of prime numbers till n, where n approaches infinity. This is the well-known Prime Number Theorem.   
First I created an is_prime() function to decide wether an intiger is prime or not. This too slow to decide, so I tried to make it faster by ruling out even numbers, and defining 2 as a prime.
Then I created a list for the primes, and I used the length of the list to determine the ratio of prime numbers.
Finally I plotted the 1/ln(x) function to see how close it is to the ratio of prime numbers. 
At the beginning the mistake is too big so I made two different charts. The first one is just until 100, and it fluctuates so much. But as n approaches infity the function getting smoother, and 1/(ln(x)) is a good under boundary as we know from the prime number theorem. 
