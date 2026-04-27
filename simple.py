# Simple DBMS-like example (in-memory)

students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 2, "name": "Bob", "marks": 78},
    {"id": 3, "name": "Charlie", "marks": 92}
]

# Query: get students with marks > 80
result = [s for s in students if s["marks"] > 80]

print("Students with marks > 80:")
for r in result:
    print(r)