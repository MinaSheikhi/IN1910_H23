import time
from threading import Thread
from multiprocessing import Process


def take_time(f):
    def wrap():
        t0 = time.perf_counter()
        f()
        print(f"Elapsed time: {time.perf_counter() - t0} seconds")

    return wrap


def wait():
    time.sleep(0.05)


def think():
    sum((-1.0) ** n / (2.0 * n + 1.0) for n in range(500_000)) * 4


def player(name="Player1"):
    print(f"Start playing against {name}")
    for move in range(30):
        think()  # Tar 10 sekunder
        wait()  # Tar 50 sekunder
    print(f"Done playing against {name}")


@take_time
def serial():
    print("Running serial")
    for i in range(5):
        player(f"Player {i+1}")


@take_time
def threads():
    print("\nRunning multithreading")
    all_threads = []
    for i in range(5):
        thread = Thread(target=player, args=(f"Player {i+1}",))
        thread.start()
        all_threads.append(thread)

    # Wait for all threads to finish
    for thread in all_threads:
        thread.join()


@take_time
def processes():
    print("\nRunning multiprocessing")
    all_processes = []
    for i in range(5):
        process = Process(target=player, args=(f"Player {i+1}",))
        process.start()
        all_processes.append(process)

    # Wait for all processs to finish
    for process in all_processes:
        process.join()


if __name__ == "__main__":
    serial()
    threads()
    processes()
