import threading


def main() -> None:
    hello_thread = threading.Thread(target=hello_from_thread)
    hello_thread.start()

    total_threads: int = threading.active_count()
    thread_name: str = threading.current_thread().name

    print(f"Python is currently running {total_threads} thread\\threads")
    print(f"The current thread is {thread_name}")

    hello_thread.join()


def hello_from_thread() -> None:
    print(f"Hello from thread {threading.current_thread()}")


if __name__ == "__main__":
    main()
