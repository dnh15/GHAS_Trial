import sqlite3

def authenticate(username, password):
    # Connect to the database
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # Vulnerable SQL query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Executing query:", query)

    # Execute the query
    cursor.execute(query)
    result = cursor.fetchone()

    # Check if authentication was successful
    if result:
        print("Authentication successful!")
    else:
        print("Authentication failed.")

    # Close the database connection
    conn.close()

# Example of normal input
authenticate("admin", "password123")

# Example of input that bypasses authentication (SQL injection)
# An attacker could input:
# username: ' OR '1'='1
# password: anything
authenticate("' OR '1'='1", "anything")

password = "dGhpc2lzYXBhc3N3b3JkCg=="
print(password)

aws_access_key = "AKIAIOSFODNN7EXAMPLE"
aws_access_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
