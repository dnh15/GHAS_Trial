from cryptography.fernet import Fernet
import psycopg2

# Generate a key for encryption (store securely in production)
# Run this once and reuse the key in a secure manner
# key = Fernet.generate_key()
# print(f"Encryption Key: {key}")

# Encryption key (for demo purposes, hardcoded; avoid this in production)
encryption_key = b'YOUR_SECURE_KEY_HERE'
cipher_suite = Fernet(encryption_key)

# Example: Encrypted password
# password = "mypassword123"
# encrypted_password = cipher_suite.encrypt(password.encode())
# print(f"Encrypted Password: {encrypted_password}")

# For demonstration, we use the encrypted password directly
encrypted_password = b'gAAAAABkUVRXY4cXqJ6KSl2cvQK9Zc7oe-JNsykPvYNigGfiJQHHt6lVk53KrkCds3jzDRRhccyD2mUud7A8BmrrPa1LoDKMwA=='

# Decrypt the password
decrypted_password = cipher_suite.decrypt(encrypted_password).decode()

# Database connection details
db_username = "admin"  # Clear-text username
db_host = "localhost"
db_name = "exampledb"

# Connect to the database
try:
    connection = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_username,
        password=decrypted_password
    )
    print("Connection successful!")

    # Perform database operations here

    connection.close()
except Exception as e:
    print(f"Database connection failed: {e}")

