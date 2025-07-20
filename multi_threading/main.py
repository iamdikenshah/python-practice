import threading
import time
import requests
from concurrent.futures import ThreadPoolExecutor
import queue

# 1. File Processing - Process multiple files simultaneously
def process_file(filename):
    print(f"Processing {filename}...")
    time.sleep(1)  # Simulate file processing
    print(f"Completed processing {filename}")
    return f"Result from {filename}"

def file_processing_example():
    files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(process_file, files))
    
    print("All files processed:", results)

# 2. API Calls - Fetch data from multiple APIs concurrently
def fetch_user_data(user_id):
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def api_calls_example():
    user_ids = [1, 2, 3, 4, 5]
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        users = list(executor.map(fetch_user_data, user_ids))
    
    for user in users:
        if "error" not in user:
            print(f"User: {user.get('name', 'Unknown')}")

# 3. Producer-Consumer Pattern - Real-time data processing
def producer(q):
    for i in range(10):
        data = f"Data item {i}"
        q.put(data)
        print(f"Produced: {data}")
        time.sleep(0.5)
    q.put(None)  # Signal completion

def consumer(q, consumer_id):
    while True:
        item = q.get()
        if item is None:
            q.put(None)  # Pass the signal to other consumers
            break
        print(f"Consumer {consumer_id} processed: {item}")
        time.sleep(1)  # Simulate processing time

def producer_consumer_example():
    data_queue = queue.Queue()
    
    # Start producer
    producer_thread = threading.Thread(target=producer, args=(data_queue,))
    producer_thread.start()
    
    # Start multiple consumers
    consumers = []
    for i in range(2):
        consumer_thread = threading.Thread(target=consumer, args=(data_queue, i))
        consumers.append(consumer_thread)
        consumer_thread.start()
    
    # Wait for completion
    producer_thread.join()
    for consumer_thread in consumers:
        consumer_thread.join()

# 4. Background Tasks - Email sending, logging, etc.
def send_email(recipient, subject):
    print(f"Sending email to {recipient}: {subject}")
    time.sleep(2)  # Simulate email sending
    print(f"Email sent to {recipient}")

def background_tasks_example():
    recipients = ["user1@example.com", "user2@example.com", "user3@example.com"]
    
    # Send emails in background threads
    threads = []
    for recipient in recipients:
        thread = threading.Thread(target=send_email, args=(recipient, "Welcome!"))
        threads.append(thread)
        thread.start()
    
    print("Main application continues...")
    
    # Wait for all emails to be sent
    for thread in threads:
        thread.join()
    print("All emails sent!")

# 5. Web Scraping - Scrape multiple URLs simultaneously
def scrape_website(url):
    try:
        response = requests.get(url, timeout=5)
        return {"url": url, "status": response.status_code, "length": len(response.text)}
    except Exception as e:
        return {"url": url, "error": str(e)}

def web_scraping_example():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/3"
    ]
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(scrape_website, urls))
    
    end_time = time.time()
    
    for result in results:
        print(f"URL: {result['url']}, Status: {result.get('status', 'Error')}")
    
    print(f"Total time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    print("=== File Processing Example ===")
    file_processing_example()
    
    print("\n=== API Calls Example ===")
    api_calls_example()
    
    print("\n=== Producer-Consumer Example ===")
    producer_consumer_example()
    
    print("\n=== Background Tasks Example ===")
    background_tasks_example()
    
    print("\n=== Web Scraping Example ===")
    web_scraping_example()

import threading
import time

def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(2) # Simulate some work
    print(f"Thread {num}: Finishing")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() # Wait for all threads to finish

print("All threads completed.")