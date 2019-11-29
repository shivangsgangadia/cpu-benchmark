#import libraries
from multiprocessing import Pool
import time
import threading

def calculate_sum_upto(n):
    sum = 0
    for i in range(n):
        sum += i
    # print("Sum : " + str(sum))

def test_all(limit):
    print("\nFor sum of series upto : " + str(limit))
    # Define input case, that is an array of numbers
    array_of_numbers = [limit for i in range(8)]

    # Adding time for performace calculation
    start_time_1 = time.time()

    # First, let's try using raw approach
    # print("\nStarting Raw approach...\n")
    for num in array_of_numbers:
        calculate_sum_upto(num)
    # print("result obtained using raw approach : " + str(super_sum_raw))
    # print("\nRaw approach finished.")

    end_time_1 = time.time()

    start_time_2 = time.time()

    # Now trying using parallel processing
    # print("\n\nStarting multiprocessing approach...\n")
    pool = Pool()
    super_sum_optimized_values = pool.map(calculate_sum_upto, array_of_numbers)
    pool.close()
    pool.join()
    # print("result obtained using parallel processing approach : " + str(super_sum_optimized))
    # print("\nParallel Processing approach finished.")

    end_time_2 = time.time()

    start_time_3 = time.time()
    # Trying using general threading approach
    # print("\n\nStarting Threading approach...\n")
    thread_array = [threading.Thread(target=calculate_sum_upto, args=(num,)) for num in array_of_numbers]
    for thread in thread_array:
        thread.start()
    
    for thread in thread_array:
        thread.join()
    # print("\nThreading approach finished.\n\n")
    end_time_3 = time.time()
    
    # Printing results
    print("\nRaw approach : {:10.5f}".format(end_time_1 - start_time_1))
    print("Multithreading approach : {:10.5f}".format(end_time_3 - start_time_3))
    print("Multiprocessing approach : {:10.5f}".format(end_time_2 - start_time_2))

if __name__ == "__main__":
    # print("This test bench records time for calculating sum of series upto n terms for 4 numbers using 3 approaches : \n1 : Linear calculation for each number one after the other.\n2 : Calculating sum of series for 4 numbers on 4 different threads.\n3 : Calculating sum of series for 4 numbers on 4 different processes.")
    # print("For simplicity, all 4 numbers have the same value, i.e. sum of series upto n terms for m, 4 times.")
    n = 10000
    # for i in range(5):
    #     test_all(n)
    #     n *= 10
    test_all(10000000)
    
    print("\n\nEnd of test.")