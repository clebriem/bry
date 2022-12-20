import requests

# Set the API key and phone number
API_KEY = 'YOUR_API_KEY'
PHONE_NUMBER = '+1234567890'

# Set the base URL and headers for the API request
url = 'https://lookups.twilio.com/v1/PhoneNumbers/{}'.format(PHONE_NUMBER)
headers = {'Authorization': 'Bearer {}'.format(API_KEY)}

# Make the API request
response = requests.get(url, headers=headers)

# Check the status code of the response
if response.status_code == 200:
    # The request was successful
    data = response.json()
    carrier = data['carrier']['name']
    print('The service provider for {} is {}'.format(PHONE_NUMBER, carrier))
else:
    # There was an error with the request
    print('An error occurred: {}'.format(response.status_code))
