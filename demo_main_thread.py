import os
import threading


def main() -> None:
    print(f"Python process running with process id: {os.getpid()}")

    total_threads: int = threading.active_count()
    thread_name: str = threading.current_thread().name

    print(f"Python is currently running {total_threads} thread\\threads")
    print(f"The current thread is {thread_name}")


if __name__ == "__main__":
    main()
