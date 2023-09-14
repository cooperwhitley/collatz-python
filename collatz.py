from timeit import default_timer as timer

# opening message
print('Starting with any positive integer n, Collatz sequence is defined corresponding to n as') 
print('the numbers formed by the following operations :') 
print('If n is even, then n = n / 2. If n is odd, then n = 3n + 1')
print('The unproven conjecture is such that any starting positive integer will eventually enter a loop of 4-2-1')
print('This has been brute force tested up to 2.95 x 10^20, as of yet, however, it has not been definitively been proven')
print('So test it yourself!')

def collatz_machine():
    prompt = input('enter collatz seed, or "exit" to quit: ')
    if prompt == 'exit':
        exit()
    # start execution timer
    time_start = timer()
    print('step                                           new number')
    # convert prompt to integer
    seed = int(prompt)
    # keep original seed for printing at end
    start = seed
    # initialize step counter
    steps = 0

    while True:
        # on each loop add a step
        steps += 1
        # if even, divide by two
        if seed % 2 == 0:
            seed /= 2
            # print step
            print(f'step {steps}: x/2                                    {round(seed)}')
        # if odd, multiply by three then add one
        if seed % 2 != 0:
            seed *= 3
            seed += 1
            # print step
            print(f'step {steps}: 3x+1                                   {round(seed)}')
        # python doesn't like to check for 1, bug to be fixed. so instead at the second integer of the terminal loop:
        if seed == 2.0:
            # add one more step
            steps += 1
            # print this step (divide by two as 2 is even)
            print(f'step {steps}: x/2                                    1')
            # break the loop
            break
    # store finish time
    time_end = timer()
    # final message showing number of steps to enter loop
    print(f'the number of steps to enter the 4-2-1 loop from {start} is {steps} steps')
    # program execution timer
    print(f'calculated in {round(((time_end - time_start) * 1000), 3)} milliseconds')
    # restart fn
    collatz_machine()

collatz_machine()