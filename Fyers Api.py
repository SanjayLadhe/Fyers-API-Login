from fyers_api import accessToken
from fyers_api import fyersModel
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fyers credentials
client_id = os.getenv('FYERS_CLIENT_ID')
secret_key = os.getenv('FYERS_SECRET_KEY')
redirect_uri = os.getenv('FYERS_REDIRECT_URI')

# Create a session
session = accessToken.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type='code',
    grant_type='authorization_code'
)

# Generate the auth code
response = session.generate_authcode()
print("Login URL:", response)

# Get the auth code from the redirected URL
auth_code = input("Enter the auth code from the redirected URL: ")

# Generate access token
session.set_token(auth_code)
response = session.generate_token()
access_token = response["access_token"]

print("Access Token:", access_token)

# Create FyersModel instance
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="")

# Test the connection
profile = fyers.get_profile()
print("Profile:", profile)

# You can now use the 'fyers' object to make API calls
