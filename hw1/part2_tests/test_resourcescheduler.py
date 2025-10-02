import threading
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(threadName)-15s | %(message)s'
)

# Two locks for two resources
lock_resource_a = threading.Lock()
lock_resource_b = threading.Lock()

def complex_task_function(task_id):
    logging.info(f"Starting task {task_id}")
    time.sleep(0.5)
    logging.info(f"Task {task_id} completed")
    return True

# Thread A: Acquires A then B
def worker_thread_a(thread_name):
    logging.info(f"{thread_name} starting")
    logging.info(f"{thread_name} trying to acquire Resource A...")
    
    lock_resource_a.acquire()
    logging.info(f"{thread_name} acquired Resource A")
    
    time.sleep(1)  # Give Thread B time to acquire Resource B
    
    logging.info(f"{thread_name} trying to acquire Resource B...")
    lock_resource_b.acquire()  # DEADLOCK: Waits for B (held by Thread B)
    
    logging.info(f"{thread_name} acquired both locks")
    complex_task_function(1)
    
    lock_resource_b.release()
    lock_resource_a.release()
    logging.info(f"{thread_name} released both locks")

# Thread B: Acquires B then A (OPPOSITE ORDER - causes deadlock)
def worker_thread_b(thread_name):
    logging.info(f"{thread_name} starting")
    logging.info(f"{thread_name} trying to acquire Resource B...")
    
    lock_resource_b.acquire()
    logging.info(f"{thread_name} acquired Resource B")
    
    time.sleep(1)  # Give Thread A time to acquire Resource A
    
    logging.info(f"{thread_name} trying to acquire Resource A...")
    lock_resource_a.acquire()  # DEADLOCK: Waits for A (held by Thread A)
    
    logging.info(f"{thread_name} acquired both locks")
    complex_task_function(2)
    
    lock_resource_a.release()
    lock_resource_b.release()
    logging.info(f"{thread_name} released both locks")

if __name__ == "__main__":
    print("=== ResourceScheduler Deadlock Test ===\n")
    print("This program will DEADLOCK - you will need to press Ctrl+C to exit\n")
    print("Watch the log output:\n")
    
    # Create threads
    thread_a = threading.Thread(target=worker_thread_a, args=("Thread-A",), name="Thread-A")
    thread_b = threading.Thread(target=worker_thread_b, args=("Thread-B",), name="Thread-B")
    
    # Start threads
    logging.info("Starting both threads...")
    thread_a.start()
    thread_b.start()
    
    # Wait 5 seconds to demonstrate deadlock
    time.sleep(5)
    
    print("\n" + "="*70)
    print("*** DEADLOCK DETECTED ***")
    print("="*70)
    print("Thread-A holds Resource A, waiting for Resource B")
    print("Thread-B holds Resource B, waiting for Resource A")
    print("Both threads are stuck in circular wait!")
    print("\nPress Ctrl+C to terminate the program")
    print("="*70 + "\n")
    
    # Try to join (will wait forever due to deadlock)
    try:
        thread_a.join()
        thread_b.join()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user")
        print("Deadlock prevented program from completing normally")
