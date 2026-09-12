import threading
import time


def increment_counter(counter, increments, lock):
    for _ in range(increments):
        with lock:
            current_value = counter[0]

            time.sleep(0.00001)

            counter[0] = current_value + 1


def run_experiment(num_threads, increments):
    counter = [0]
    lock = threading.Lock()
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(
            target=increment_counter,
            args=(counter, increments, lock)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return counter[0]


def main():
    experiments = [
        (2, 10000),
        (5, 10000),
        (10, 10000),
        (20, 10000)
    ]

    print("========================================")
    print("       RACE CONDITION EXPERIMENT")
    print("========================================")
    print()
    print("WITH LOCK")
    print("----------------------------------------")

    print(
        "{:<10} {:<15} {:<15} {:<15}".format(
            "Threads",
            "Increments",
            "Expected",
            "Actual"
        )
    )

    print("-" * 60)

    for num_threads, increments in experiments:
        expected = num_threads * increments

        actual = run_experiment(
            num_threads,
            increments
        )

        print(
            "{:<10} {:<15} {:<15} {:<15}".format(
                num_threads,
                increments,
                expected,
                actual
            )
        )


if __name__ == "__main__":
    main()