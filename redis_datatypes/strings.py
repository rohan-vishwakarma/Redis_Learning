from connection import redis_conn


setName = redis_conn.set("name", "John")
setAge  = redis_conn.set("age", 25)
redis_conn.incr("age", 1)


getName = redis_conn.get("name")
getAge  = redis_conn.get("age")

print(getName, getAge) 