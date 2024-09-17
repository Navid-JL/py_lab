import multiprocessing
import os


def main() -> None:
    hello_process = multiprocessing.Process(target=hello_from_process)

    hello_process.start()

    print(f"Hello from parent process {os.getpid()}!")

    hello_process.join()


def hello_from_process() -> None:
    print(f"Hello from child process {os.getpid()}!")


if __name__ == "__main__":
    main()
