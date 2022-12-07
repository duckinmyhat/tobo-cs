import ipapi

# Prompt the user for an IP address
ip_address = input("Enter an IP address: ")

# Look up the location of the IP address
location = ipapi.location(ip_address)

# Print the location
print(f"City: {location['city']}")
print(f"Region: {location['region']}")
print(f"Country: {location['country_name']}")