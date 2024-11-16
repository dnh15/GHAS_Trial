import paramiko

# Hardcoded dummy SSH private key (PEM format)
dummy_private_key = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA7R4JcQWjJ1KlMJmyT7P7J6Cb7jQmf62yU+mLHYJvYVydHCFL
yHn5FO+Gkl4ZKybBL8wzJa77+Y9QboXtLdqF+WZoP9adA8DfmyL2q8GNHMo9GhXq
rzqlUykE0Qj5Ede2U4pBCdU/PUwmFPCFAdbgk+QZb6X1IuTlcqSKMFvIY9k6Mu7G
NzFeBfXEjC9BOZ6z9Z6HATQhpZC/nU0Ej/sdW9/0VJjXrYyIFGjP8D9kRqIuIlPh
r+SkX8AQjlgcvLft1by3D1qAUXNKZmb3bJhfgPOWnBPIrni3KKjclJLsHd/OF+Rw
wFSki50McnSlZod5j0gZbbFbPuPyL8bXgRQpLQIDAQABAoIBAGMeMvulIWs38LLZ
KJRYN9Alc0P1ZVfLTYX5UlOvL+jhNU4CaO57Cd03XNC0OWZ1AjoBlNS6E7cl+FBN
djNtdAhGBm+oR8hV+HBK6cTWkxNdOmRUcbKvBrGv2IlxypsJ2PvdWOVtDf+jMD4q
1JKnOi+vR/RRbN3OJbGVYzgq2HQ8Xre9r4sFuvhIXYVIApVutHjVysckJx9N8Qsn
GkM8EQENM+JByjGYJ5Xf2CNsz6dlA02GYYTn8XcOi/ZJ6q0EyyWx6uAgsIE7WB+W
6i1hmMokjYlvmzZAXIn+Fd/G/qSzJ0IOop8e8MjLBmjtn+XcO7o1zRxLo+lBypuI
07V1UEECgYEA/Vl12hnDqLMOBnk4tAd8Rh7/hyGQhRgTzNTxx12GcF57h0Ib62C/
9pIgzk/Op64EVNaZkGTKRfyCKt/Otu6Tb8SYRgM0QmoFzQlUNUqBx50Fx9dwnCSP
H6pmAY9q3czGGOp/ZW+hmGH0Fc/6cRrp30Xuy/SYxsRt9L64pZc4/4kCgYEA7E+R
fo5G7FjqSKbApkNz3K+U8zPIBJIO3FByZTDbnnCZNhRmJ2D+L3jGnpw8w/+XLQwh
f59oa6c6SO+XIpz/V94cltDio5XRGI1Df+GrnA6OYJlCXD/m8dHCMzwpeGRQhX/D
xx++xtR5LPfl5v/W+Kn4XlB8FRRvQyyZb8phf3ECgYEAjWW/e5UuKXl0N/KNuRkM
AMVGahAhFwvExUosZ1khzWhuX1tfKmnChwChfCQtXhtCIV0pAT4mQJ+GeOrVc//6
+e+DWUgEjXsfthAcMrgHuWp+DZsBD7+5arV2PLIRL65ENUPUrV++53AoLhAnDB04
UBhhdxxD+LU2JHMV0W6wv+ECgYBhsPIQO2osmfIXRfBMzuy+NEvGR0uPsfKrCFPb
uRD4AFLXKPSJ6LqxXrGEY/goy+hV8cNgYmXNF55M9IsJ8I5fKgxKSKb4+CQ4N2UO
IaglaCWR2h8+g2XZELEN9+8A/NR7OQUdSRsrlRSFkRE0HLb+EBchPKk+aRrl86RU
Lg0ywQKBgQC5P3xN7lyOxGcfYlW8m0rhvEF2U51mH66OlZcXIljechmKnNkDKdpS
sb7vt5F5Xb/8UOrniYNmfo/gKkZ13T9c8zmgD1rfPKSz+XNwphHUkMrkLYgZnYTA
DdPcycY9D9Sy5cV+e9ZjQovC/KKOE9RgxyytVSIRjtZBM2HGAElNxw==
-----END RSA PRIVATE KEY-----
"""

# SSH connection details
hostname = "example.com"
username = "user"

try:
    # Initialize the SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Load the private key
    private_key = paramiko.RSAKey.from_private_key_file(dummy_private_key)

    # Connect to the SSH server
    ssh_client.connect(hostname=hostname, username=username, pkey=private_key)
    print("SSH connection established!")

    # Execute a command
    stdin, stdout, stderr = ssh_client.exec_command("whoami")
    print("Command output:", stdout.read().decode())

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    ssh_client.close()
    print("SSH connection closed.")

