from threading import Thread
from multiprocessing import Process
import time


def think():
    return sum((-1.0) ** n / (2.0 * n + 1.0) for n in range(30_000_000)) * 4


def task(task_nr):
    print(f"Executing task {task_nr}")
    think()
    print(f"Done executing task {task_nr}")


def serial():
    t0 = time.perf_counter()
    task(1)
    task(2)
    print(f"Elapsed time: {time.perf_counter() - t0}")


def threads():
    t0 = time.perf_counter()
    thread1 = Thread(target=task, args=(1,))
    thread2 = Thread(target=task, args=(2,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(f"Elapsed time: {time.perf_counter() - t0}")


def processes():
    t0 = time.perf_counter()
    process1 = Process(target=task, args=(1,))
    process2 = Process(target=task, args=(2,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print(f"Elapsed time: {time.perf_counter() - t0}")


if __name__ == "__main__":
    print("Serial")
    serial()
    print("Threads")
    threads()
    print("Processes")
    processes()
