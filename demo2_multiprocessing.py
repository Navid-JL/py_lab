import time
from multiprocessing import Process


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()

    print(f"Finished counting to {count_to} in {end - start}")
    return counter


def main() -> None:
    start_time = time.time()

    to_one_hundred_million = Process(target=count, args=(100_000_000,))
    to_two_hundred_million = Process(target=count, args=(200_000_000,))

    to_one_hundred_million.start()
    to_two_hundred_million.start()

    to_one_hundred_million.join()
    to_two_hundred_million.join()

    end_time = time.time()
    print(f"Completed in {end_time - start_time}")


if __name__ == "__main__":
    main()
