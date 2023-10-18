# 0x02-redis_basic

This repository contains Python modules for basic operations with Redis and web content caching. The modules include:

1. `exercise.py`: A Redis cache module for storing data with support for tracking method calls and maintaining a call history.
2. `web.py`: A module for web page content caching using Redis, with a decorator for tracking URL access counts.

## Redis: General Information

**Redis** is an open-source, in-memory data structure store that can be used as a database, cache, and message broker. It is known for its high performance and simplicity. Redis stores data in key-value pairs and is often used for caching, real-time analytics, and queuing.

### Redis Installation on Ubuntu

To install Redis on Ubuntu, follow these steps:

1. Update the package list:
   ```
   sudo apt update
   ```

2. Install Redis server:
   ```
   sudo apt install redis-server
   ```

3. Start the Redis service and enable it to start on boot:
   ```
   sudo systemctl start redis-server
   sudo systemctl enable redis-server
   ```

4. Check the status of the Redis service to ensure it's running:
   ```
   sudo systemctl status redis-server
   ```

## Redis Commands and Examples

Here are some common Redis commands with examples:

- SET: Set a key to hold a value.
   ```
   SET mykey "Hello, Redis!"
   ```

- GET: Get the value of a key.
   ```
   GET mykey
   ```

- INCRBY: Increment the integer value of a key by a specific amount.
   ```
   INCRBY counter 5
   ```

- RPUSH: Append one or multiple values to a list.
   ```
   RPUSH mylist "item1" "item2" "item3"
   ```

- LRANGE: Get a range of elements from a list.
   ```
   LRANGE mylist 0 -1
   ```

- DEL: Delete a key.
   ```
   DEL mykey
   ```

Feel free to explore these commands and more as you use Redis for various data storage and caching needs.

## Python Modules in this Repository

### exercise.py

The `exercise.py` module includes features for basic Redis caching operations, method call counting, and maintaining a call history. It also provides a `Cache` class for storing data in Redis.

#### Usage Example:

```
from exercise import Cache

# Create a Cache instance
cache = Cache()

# Store data in Redis and retrieve it
data = "Hello, Redis!"
key = cache.store(data)
retrieved_data = cache.get(key)
print(f"Data stored with key: {key}")
print(f"Retrieved data: {retrieved_data}")
```

### web.py

The `web.py` module offers web page content caching features with a decorator for tracking URL access counts. The `get_page` function is provided for caching web responses and improving performance.

#### Usage Example:

```
from web import get_page

# Cache web page content and track access counts
url = "https://www.example.com"
page_content = get_page(url)
access_count = get_page.__wrapped__(url)
print(f"URL: {url}")
print(f"HTML Content:\n{page_content[:500]}...")
print(f"Access Count: {access_count}")
```

Explore these modules and consider integrating them into your Python applications for Redis caching and web content caching.
