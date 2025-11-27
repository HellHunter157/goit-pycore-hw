# перше завдання

from queue import Queue
import time

requests_queue = Queue()
request_id = 1
def generate_request():
    global request_id
    request_data = f"Request #{request_id}"
    requests_queue.put(request_data)
    print(f"Created: {request_data}")
    request_id += 1
def process_request():
    if not requests_queue.empty():
        current = requests_queue.get()
        print(f"Processing: {current}")
    else:
        print("Queue is empty.")
def main():
    print("Request processing system started. Press Ctrl+C to exit.\n")
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram terminated.")
if __name__ == "__main__":
    main()


# друге завдання

from collections import deque
def is_palindrome(text: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    dq = deque(cleaned)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
def main():
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("Palindrome")
    else:
        print("Not a palindrome")
if __name__ == "__main__":
    main()
