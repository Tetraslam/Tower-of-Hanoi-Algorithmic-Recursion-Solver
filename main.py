import time

def tower_of_hanoi(x, source, auxiliary, target, elapsed_time):
    if x == 1:
        print("Move disk 1 from source", source, "to target", target)
        return elapsed_time
    elapsed_time = tower_of_hanoi(x - 1, source, target, auxiliary, elapsed_time)
    print("Move disk", x, "from source", source, "to target", target)
    elapsed_time = tower_of_hanoi(x - 1, auxiliary, source, target, elapsed_time)
    return elapsed_time

def measure_time(x):
    start_time = time.time()
    elapsed_time = tower_of_hanoi(x, 'A', 'B', 'C', 0)
    elapsed_time += time.time() - start_time
    print("Total time elapsed: ", elapsed_time, " seconds")

x = int(input("Enter the number of disks: "))
measure_time(x)
