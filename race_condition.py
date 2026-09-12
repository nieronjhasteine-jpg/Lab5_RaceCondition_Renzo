import threading
import time


def increment_counter(counter, increments):
    for _ in range(increments):
        current_value = counter[0]

        time.sleep(0.00001)

        counter[0] = current_value + 1


def run_experiment(num_threads, increments):
    counter = [0]
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(
            target=increment_counter,
            args=(counter, increments)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return counter[0]


def main():
    num_threads = 5
    increments = 10000
    expected = num_threads * increments

    print("========================================")
    print("       RACE CONDITION EXPERIMENT")
    print("========================================")
    print()
    print("Threads:", num_threads)
    print("Increments per Thread:", increments)
    print()
    print("PART B - WITHOUT LOCK")
    print("----------------------------------------")
    print("Expected Counter:", expected)
    print()

    for run in range(1, 6):
        actual = run_experiment(
            num_threads,
            increments
        )

        print("Run", run)
        print("Actual Counter:", actual)
        print()


if __name__ == "__main__":
    main()