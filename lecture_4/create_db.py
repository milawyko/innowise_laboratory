import sqlite3
import os

print("=== Student Grades Database Manager ===")

# Подключаемся к базе
conn = sqlite3.connect("school.db")
cursor = conn.cursor()
try:
    with open("queries.sql", "r") as f:
        sql_script = f.read()
    
    print("✓ Reading queries.sql...")
    
    sql_commands = sql_script.split(';')
    
    for command in sql_commands:
        command = command.strip()
        if command:  # leave null strings
            try:
                cursor.execute(command)
            except sqlite3.OperationalError as e:
                if "already exists" in str(e):
                    print(f"  ⚠️  Table/index already exists, skipping...")
                else:
                    print(f"  ❌ Error: {e}")
    
    conn.commit()
    
    cursor.execute("SELECT COUNT(*) FROM students")
    students = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM grades")
    grades = cursor.fetchone()[0]
    
    print(f"\n=== Database Status ===")
    print(f"Students in database: {students}")
    print(f"Grades in database: {grades}")
    print(f"File: school.db ({os.path.getsize('school.db')} bytes)")
    print("Ready to use!")
    
except FileNotFoundError:
    print("Error: queries.sql not found in current folder!")
    print(f"Current folder: {os.getcwd()}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    conn.close()
    print("\n🔒 Connection closed")