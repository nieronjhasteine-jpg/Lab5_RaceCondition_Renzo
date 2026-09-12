# Laboratory Activity 5 – Race Condition and Thread Synchronization

## Investigating Race Conditions Using Python Threads

## Description

This laboratory activity demonstrates how multiple Python threads access and modify shared data. It compares an unsynchronized version, where multiple threads modify a shared counter without protection, with a synchronized version using `threading.Lock`.

The purpose of the activity is to observe how thread execution timing can produce unexpected results when shared data is not protected and how synchronization can prevent this problem.

---

## Objectives

* Understand how multiple threads access the same shared data.
* Demonstrate a race condition using Python threads.
* Identify why concurrent execution can produce unexpected results.
* Use synchronization to protect shared data.
* Apply `threading.Lock`.
* Compare unsynchronized and synchronized results.

---

## Requirements

The programs use only the following Python libraries:

* `threading`
* `time`

---

# Part A and Part B – Without Lock

The unsynchronized version uses a shared counter that is modified by multiple threads without a lock.

For this experiment:

* Threads: 5
* Increments per Thread: 10,000
* Expected Counter: 50,000

The counter is intentionally accessed without synchronization.

## Part B Results

| Run | Threads | Increments per Thread | Expected Counter | Actual Counter |
| --- | ------: | --------------------: | ---------------: | -------------: |
| 1   |       5 |                10,000 |           50,000 |         10,000 |
| 2   |       5 |                10,000 |           50,000 |         10,002 |
| 3   |       5 |                10,000 |           50,000 |         10,001 |
| 4   |       5 |                10,000 |           50,000 |         10,000 |
| 5   |       5 |                10,000 |           50,000 |         10,003 |

The actual counter is different from the expected counter because multiple threads can read the same value before another thread writes its updated value. This causes some updates to be lost.

The small delay in the counter update makes the race condition easier to observe.

---

# Part C – With Lock

The synchronized version uses `threading.Lock()` to protect the section where the shared counter is read and modified.

For 5 threads with 10,000 increments per thread:

| Threads | Increments per Thread | Expected Counter | Actual Counter |
| ------: | --------------------: | ---------------: | -------------: |
|       5 |                10,000 |           50,000 |         50,000 |

The expected and actual counters are equal because the lock prevents multiple threads from modifying the shared counter at the same time.

---

# Part D – Different Number of Threads

## Without Lock

| Threads | Increments per Thread | Expected Counter | Actual Counter |
| ------: | --------------------: | ---------------: | -------------: |
|       2 |                10,000 |           20,000 |         10,000 |
|       5 |                10,000 |           50,000 |         10,000 |
|      10 |                10,000 |          100,000 |         10,000 |
|      20 |                10,000 |          200,000 |         10,005 |

## With Lock

| Threads | Increments per Thread | Expected Counter | Actual Counter |
| ------: | --------------------: | ---------------: | -------------: |
|       2 |                10,000 |           20,000 |         20,000 |
|       5 |                10,000 |           50,000 |         50,000 |
|      10 |                10,000 |          100,000 |        100,000 |
|      20 |                10,000 |          200,000 |        200,000 |

The unsynchronized results show lost updates, while the synchronized results match the expected values.

---

# Analysis Questions

## 1. What is a race condition?

A race condition occurs when multiple threads access or modify shared data and the final result depends on the timing or order of thread execution.

---

## 2. Why can the actual counter be different from the expected counter?

The actual counter can be different because the counter update involves reading the current value, adding one, and writing the new value. A thread can be interrupted between these steps, allowing another thread to read the same old value. When the threads write their results, some updates can be lost.

---

## 3. Why does running the same program multiple times potentially produce different results?

Thread scheduling and execution timing can change from one execution to another. The operating system determines when threads run, so the order of their operations may be different each time.

---

## 4. What is the purpose of `threading.Lock()`?

The purpose of `threading.Lock()` is to protect shared data by allowing only one thread at a time to enter the protected critical section.

---

## 5. How does the lock prevent multiple threads from modifying the counter at the same time?

When a thread acquires the lock, it enters the critical section. Other threads that try to acquire the same lock must wait until the first thread releases it. This prevents simultaneous modification of the shared counter.

---

## 6. What happens when the number of threads is increased?

Increasing the number of threads can increase the amount of concurrent access to the shared data. Without synchronization, this can increase the opportunity for race conditions and lost updates. With synchronization, the counter remains correct, although more threads may have to wait for the lock.

---

## 7. What is one disadvantage of using a lock?

One disadvantage is that threads may have to wait for the lock. This can reduce concurrency and may make the program slower because access to the critical section is serialized.

---

## 8. Does a lock make the program parallel? Explain.

No. A lock does not make the program parallel. Instead, it makes access to shared data safe by controlling which thread can enter the critical section. Threads may still execute concurrently, but the protected section is accessed by one thread at a time.

---

## 9. Why is synchronization important in real-world applications?

Synchronization is important because incorrect access to shared data can cause serious problems. Applications that manage shared information need to make sure that concurrent operations do not overwrite or corrupt each other's data.

---

## 10. Give two examples of real-world systems where race conditions could cause serious problems.

### Bank Transfer System

If two transactions modify the same account balance at the same time without proper synchronization, the balance may become incorrect.

### Seat Booking System

If two customers attempt to reserve the same available seat at the same time without synchronization, both customers could potentially be assigned the same seat.

---

# How to Run

Make sure Python is installed and open the terminal inside the `Laboratory_Activity_5` folder.

## Run the Race Condition Version

```text
python race_condition.py
```

This runs the experiment without a lock and displays the results for different numbers of threads.

## Run the Synchronized Version

```text
python synchronized.py
```

This runs the same thread configurations using `threading.Lock()`.

---

# Conclusion

The experiment demonstrates that multiple threads accessing the same shared counter without synchronization can produce incorrect results because of race conditions and lost updates.

The synchronized version uses `threading.Lock()` to protect the critical section. The results show that the synchronized counter matches the expected value for all tested thread configurations.

The experiment demonstrates that synchronization is important when multiple concurrent threads access and modify shared data.
