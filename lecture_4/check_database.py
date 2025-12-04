import sqlite3

# connect to the base
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

print("=== DATABASE CHECK ===")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print(f"Tables: {[t[0] for t in tables]}")

cursor.execute("SELECT COUNT(*) FROM students")
print(f"Students: {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM grades")
print(f"Grades: {cursor.fetchone()[0]}")

print("\n=== SAMPLE DATA ===")
cursor.execute("SELECT * FROM students LIMIT 3")
print("First 3 students:")
for row in cursor.fetchall():
    print(f"  ID {row[0]}: {row[1]}, born {row[2]}")

print("\n=== QUERY: Alice Johnson's grades ===")
cursor.execute('''
    SELECT subject, grade FROM grades 
    WHERE student_id = (SELECT id FROM students WHERE full_name = 'Alice Johnson')
''')
for subject, grade in cursor.fetchall():
    print(f"  {subject}: {grade}")

conn.close()
print("\nDatabase is working!")