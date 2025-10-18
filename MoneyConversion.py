# Simple USD to VND converter

# Current exchange rate (you can update this value)
usd_to_vnd_rate = 25000  # Example: 1 USD = 25,000 VND

# Get amount in USD from user
usd = float(input("Enter amount in USD: "))

# Convert to VND
vnd = usd * usd_to_vnd_rate

# Display result
print(f"{usd} USD = {vnd:,.0f} VND")
