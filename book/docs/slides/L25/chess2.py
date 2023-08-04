import time
import concurrent.futures


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
    for _ in range(30):
        think()
        wait()
    print(f"Done playing against {name}")


def serial():
    print("Running serial")
    for i in range(5):
        player(f"Player {i+1}")


@take_time
def threads():
    print("\nRunning multithreading")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(5):
            executor.submit(player, f"Player {i+1}")


@take_time
def processes():
    print("\nRunning multiprocessing")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(5):
            executor.submit(player, f"Player {i+1}")


if __name__ == "__main__":
    # t0 = tim
    # think()
    # player()
    # serial()
    # threads()
    processes()
