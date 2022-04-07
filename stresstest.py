from  multiprocessing import Process, Manager
import sys
import time
import os
import math

benchmark_results = []

def stress():
    while True:
        x = 100^100

def benchmark(benchmark_results, i):
    print("Benchmark Started")
    start_time = time.time()
    for i in range (1000000000):
        x = 100^100
    #print(benchmark_result)
    print("BENCHMARK DONE")
    finished_time = (time.time() - start_time)
    time.sleep(1)
    print("FINISHED WAIT")
    benchmark_results.append(finished_time)
    print("DONE")

def cpu_stress(Cores):
    for i in range(Cores):
        process_var = 'process{}'.format(i)
        locals()[process_var] = Process(target=stress)
        locals()[process_var].start()

def cpu_benchmark(Cores):
    with Manager() as manager:
        benchmark_results = manager.list()
        for i in range(Cores):
            process_var = 'process{}'.format(i)
            locals()[process_var] = Process(target=benchmark, args=(benchmark_results, i))
            locals()[process_var].start()
        final_process = 'process{}'.format(Cores-1)
        locals()[final_process].join() 
        print(benchmark_results)

def menu():
    print(os.cpu_count())
    print("1. Stress one core\n2. Stress all cores\n3. Single Core Benchmark\n4. Multicore benchmark\n5. Exit")
    answer = input("Input: ")
    print(answer)
    if int(answer) == 1:
        cpu_stress(1)
        input("press enter to stop script")
    elif int(answer) == 2:
        cpu_stress(os.cpu_count())
    elif int(answer) == 3:
        cpu_benchmark(1) 
    elif int(answer) == 4:
        cpu_benchmark(os.cpu_count())
    elif int(answer) == 5:
        sys.exit()



menu()
