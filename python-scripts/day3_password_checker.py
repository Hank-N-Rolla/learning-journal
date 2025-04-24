import getpass

print("🔐 Password Strength Checker\n")

password = getpass.getpass("Enter your password (hidden): ")

length_ok = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(not c.isalnum() for c in password)

score = sum([length_ok, has_upper, has_lower, has_digit, has_symbol])

if score == 5:
    strength = "Strong 💪"
elif score >= 3:
    strength = "Moderate ⚖️"
else:
    strength = "Weak ⚠️"

print(f"\nYour password strength is: {strength}")

# Bonus feedback
print("\n🔍 Feedback:")
if not length_ok:
    print("- Password should be at least 8 characters long.")
if not has_upper:
    print("- Add at least one uppercase letter.")
if not has_lower:
    print("- Add at least one lowercase letter.")
if not has_digit:
    print("- Include numbers (0–9).")
if not has_symbol:
    print("- Add special characters (!, @, #, etc.) to strengthen it.")

