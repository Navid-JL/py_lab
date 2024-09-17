import time
import threading
import requests


def read_example() -> None:
    response = requests.get("https://example.com")
    print(response.status_code)


thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

sync_start = time.time()

thread_1.start()
thread_2.start()

print("All threads running!")

thread_1.join()
thread_2.join()

sync_end = time.time()

print(f"Running with threads took {sync_end - sync_start:.4f} seconds")
