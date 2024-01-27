import os
import secrets

# Generate a strong, random secret key
secret_key = secrets.token_hex(16)  # 16 bytes (128 bits) is a good choice

# Store the secret key as an environment variable
os.environ['FLASK_SECRET_KEY'] = secret_key

# You can also print it for reference (do not do this in production)
print(f"Generated Flask Secret Key: {secret_key}")
