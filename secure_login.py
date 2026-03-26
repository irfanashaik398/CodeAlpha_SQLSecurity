print("Secure Login System")

username = input("Enter username: ")
password = input("Enter password: ")
# Simple SQL Injection detection patterns
sql_injection_patterns = ["'", "--", ";", "OR", "AND", "=", "DROP", "SELECT"]
def is_safe(input_text):
    for pattern in sql_injection_patterns:
        if pattern.lower() in input_text.lower():
            return False
        return True
    if not is_safe(username) or not is_safe(password):
        print("⚠️ SQL Injection Detected! Access Denied.")
    else:
        print("✅ Login Successful (Safe Input)")