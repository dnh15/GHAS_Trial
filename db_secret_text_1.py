from cryptography.fernet import Fernet
import mysql.connector

# Key used for encryption and decryption (store this securely, e.g., in an environment variable)
encryption_key = b'_YOUR_32_BYTE_KEY_HERE_'  # Replace with a securely generated key

# Encrypted password (previously encrypted and stored securely)
encrypted_password = b'gAAAAABlZEXAMPLEENCRYPTEDPASSWORD'

# Decrypt the password
cipher_suite = Fernet(encryption_key)
decrypted_password = cipher_suite.decrypt(encrypted_password).decode()

# Database credentials
db_username = "db_user"  # Plain text username
db_password = decrypted_password  # Decrypted password
db_host = "localhost"
db_name = "example_db"

try:
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host=db_host,
        user=db_username,
        password=db_password,
        database=db_name
    )
    print("Database connection successful!")
    # Perform database operations here...

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Database connection closed.")

