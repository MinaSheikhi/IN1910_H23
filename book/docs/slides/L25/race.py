from threading import Thread, Lock
import time


class Database:
    def __init__(self, lock: Lock, sleep_time=0.1):
        self.value = 0
        self.sleep_time = sleep_time
        self.lock = lock

    def update_value(self, thread_index):
        self.lock.acquire()  # Get lock
        print(f"Thread {thread_index}: updating value")
        value_copy = self.value
        value_copy += 1
        # Here we sleep so that we are "sure" that we switch thread
        time.sleep(self.sleep_time)
        self.value = value_copy
        print(f"Thread {thread_index}: finished updating value")
        self.lock.release()  # Release lock


def main():
    lock = Lock()
    database = Database(sleep_time=0.1, lock=lock)
    thread1 = Thread(target=database.update_value, args=(1,))
    thread2 = Thread(target=database.update_value, args=(2,))
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print(database.value)


if __name__ == "__main__":
    main()
