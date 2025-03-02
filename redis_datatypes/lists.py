import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connection import redis_conn

studentsData = ["Alice", "Bob", "Charlie", "David", "Eve"]

class RedisList:
    def __init__(self, userId):
        self.userId = userId
        redis_conn.expire(f"students:{userId}", 60)

    def addStudents(self, students):
        return redis_conn.rpush(f"students:{self.userId}", *students)

    def addstudentAtHead(self, student):
        return redis_conn.lpush(f"students:{self.userId}", student)

    def addstudentAtTail(self, student):
        return redis_conn.rpush(f"students:{self.userId}", student)
    
    def getStudents(self):
        return redis_conn.lrange(f"students:{self.userId}", 0, -1)

    def getStudentCount(self):
        return len(redis_conn.lrange(f"students:{self.userId}", 0, -1))

    def deleteStudent(self, student):
        return redis_conn.lrem(f"students:{self.userId}", 0, student)
    
    def getTtl(self):
        return redis_conn.ttl(f"students:{self.userId}")
        

userId = 1
listObj = RedisList(userId)
getStudentList = listObj.getStudents()
print(f"Students: {getStudentList}")
