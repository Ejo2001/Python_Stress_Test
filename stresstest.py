import multiprocessing

def Stress():
    x = 1
    while True:
        x = 100^100

for i in range(multiprocessing.cpu_count()):
    var_name = 'var{}'.format(i)
    locals()[var_name] = multiprocessing.Process(target=Stress)
    locals()[var_name].start()
