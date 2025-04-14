import redis
import random
import string
import time

# Connect to Redis
redis_host = 'localhost'
redis_port = 6379

redis_conn = redis.Redis(host=redis_host, port=redis_port)

def generate_random_key(length=6):
    """Generate a random key"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_value(length=8):
    """Generate a random value"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_data(num_keys):
    """Generate random keys and values and store them in Redis"""
    for _ in range(num_keys):
        key = generate_random_key()
        value = generate_random_value()
        redis_conn.set(key, value)

def search_key(key):
    """Search for a specific key"""
    start_time = time.time()
    value = redis_conn.get(key)
    end_time = time.time()
    if value is not None:
        print(f"Key: {key}, Value: {value.decode('utf-8')}")
    else:
        print(f"Key '{key}' not found.")
    print(f"Time taken to search for key '{key}': {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    num_keys = 1000000 #random.randint(5, 10)  # Generate random number of keys (between 5 and 10)
    # generate_random_data(num_keys)
    print(f"Generated {num_keys} random keys and values.")

    # Get all keys
    all_keys = redis_conn.keys('*')
    print("Count of all_keys: ", len(all_keys))

    # Choose a random key
    random_key = random.choice(all_keys)

    # Decode and print the random key
    print("Random Key:", random_key.decode('utf-8'))

    # Test searching for a specific key
    search_key('ZvemDz')  # Change 'example_key' to the key you want to search for
