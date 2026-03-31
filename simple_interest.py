# Store principal amount, rate of interest, and time in different variables
principal = 5000        # Principal amount in dollars (or any currency)
rate_of_interest = 5    # Rate of interest per annum (%)
time = 3                # Time in years

# Calculate Simple Interest using formula: SI = P x R x T / 100
simple_interest = (principal * rate_of_interest * time) / 100

# Display the results
print("Simple Interest Calculation")
print("=" * 50)
print(f"Principal Amount (P): ${principal}")
print(f"Rate of Interest (R): {rate_of_interest}% per annum")
print(f"Time Period (T): {time} years")
print("=" * 50)
print(f"Simple Interest: ${simple_interest}")
print(f"Total Amount: ${principal + simple_interest}")
