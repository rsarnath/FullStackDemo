import redis

# Connect to Redis
redis_host = 'localhost'
redis_port = 6379

try:
    # Create a connection to the Redis server
    redis_conn = redis.Redis(host=redis_host, port=redis_port)
    # If the connection is successful, print a success message
    print("Connected to Redis successfully!")

    # Now you can perform operations on the Redis database

    # Set a key-value pair
    redis_conn.set('favorite_color', 'blue')

    # Get the value for a key
    value = redis_conn.get('favorite_color')
    print("Favorite color:", value.decode('utf-8'))

    # Increment a value
    redis_conn.incr('counter')
    print("Incremented counter:", redis_conn.get('counter').decode('utf-8'))

    # Decrement a value
    redis_conn.decr('counter')
    print("Decremented counter:", redis_conn.get('counter').decode('utf-8'))

    # Delete a key
    redis_conn.delete('favorite_color')

    # Check if a key exists
    print("Does 'favorite_color' exist?", redis_conn.exists('favorite_color'))

except redis.ConnectionError as e:
    # If connection fails, print an error message
    print(f"Error connecting to Redis: {e}")
