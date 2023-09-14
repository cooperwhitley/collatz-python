from timeit import default_timer as timer


num = 1
total_time = 0
def collatz_machine():
    global num, total_time
    seed = num
    # start execution timer
    time_start = timer()
    # convert prompt to integer
    # keep original seed for printing at end
    start = seed
    # initialize step counter
    steps = 0
    max = 0

    while True:
        # on each loop add a step
        steps += 1
        # if even, divide by two
        if seed % 2 == 0:
            seed /= 2
            if seed > max:
                max = seed
        # if odd, multiply by three then add one
        if seed % 2 != 0:
            seed *= 3
            seed += 1
            if seed > max:
                max = seed
        # python doesn't like to check for 1, bug to be fixed. so instead at the second integer of the terminal loop:
        if seed == 2.0:
            # add one more step
            steps += 1
            # print this step (divide by two as 2 is even)
            break
    # store finish time
    time_end = timer()
    # program execution timer
    print(f'{start}: {steps} steps in {round(((time_end - time_start) * 1000), 3)} ms max: {max}')
    total_time += (time_end - time_start) * 1000
    # restart fn
    if num < 996:
        num += 1
        collatz_machine()
    else:
        print(f'collatz seeds 1-996 calculated in {round(total_time, 3)}ms')

collatz_machine()