


# n <= 40 and k <= 5
# Return the total number of rabbit pairs that will be present after n months.
# Start with 1 pair, 1 pair produces k rabbit pairs.

#Fn = Fn-1 + Fn-2

# Any given month will contain the rabbits that were alive the previous months,
# plus any new offspring. 
# Key observation is that the number of offspring in any month
# is equal to the number of rabbits that were alive two months prior


def sillywabbits(months, bebys):

    wabbit_pairs = 1
    maturepair = 1
    babypair = 0
    oldbabypair = 0

    if months <= 2:
        print(wabbit_pairs)

    else:
        for gen in range(2,months):

            oldbabypair = babypair
            babypair = maturepair * bebys
            maturepair = maturepair + oldbabypair

            wabbit_pairs = maturepair + babypair
           

    print(wabbit_pairs) 


def fib(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k*a + b
    print(b)















    
fib(33,3)
sillywabbits(33,3)

