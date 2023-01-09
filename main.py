import time

def tower_of_hanoi(n, source, auxiliary, target, elapsed_time):
    if n == 1:
        print("Move disk 1 from source", source, "to target", target)
        return elapsed_time
    elapsed_time = tower_of_hanoi(n - 1, source, target, auxiliary, elapsed_time)
    print("Move disk", n, "from source", source, "to target", target)
    elapsed_time = tower_of_hanoi(n - 1, auxiliary, source, target, elapsed_time)
    return elapsed_time

def measure_time(n):
    start_time = time.time()
    elapsed_time = tower_of_hanoi(n, 'A', 'B', 'C', 0)
    elapsed_time += time.time() - start_time
    print("Total time elapsed: ", elapsed_time, " seconds")

n = int(input("Enter the number of disks: "))
measure_time(n)
