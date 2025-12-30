# Project: Security Log Analyzer
# Author: Akash Raval
# Purpose: Simulate log parsing and mapping IP addresses to Users

# Raw Data Logs (Simulated)
timestamps = ["10:00:01", "10:05:12", "10:15:45", "11:00:20"]
usernames = ["akash_cyber", "admin_root", "guest_user", "dev_rahul", "unknown_bot"]
ip_addresses = ["192.168.1.10", "10.0.0.5", "172.16.0.2", "192.168.1.15", "45.79.12.4"]
actions = ["Login Success", "File Download", "Unauthorized Access", "Password Change", "Login Failed"]

print('\n' + '='*60)
print(' 🛡️  SECURITY LOG MONITORING SYSTEM  🛡️ ')
print('='*60)

# 1. Parsing Logs using ZIP
# strict=True ensures all lists have the same length (Python 3.10+)
try:
    for time, user, ip, action in zip(timestamps, usernames, ip_addresses, actions, strict=True):
        print(f'🕒 [{time}] | 👤 {user:<12} | 🌐 {ip:<15} | ⚠️ {action}')
except ValueError:
    print('\n'+'='*60)
    print("\n❌ ERROR: Data mismatch! One of the security logs is missing information.")
print('-'*60)

# 2. Creating a Lookup Dictionary (User -> IP Mapping)
user_ip_map = dict(zip(usernames, ip_addresses))

# 3. Search Functionality
search_user = input("\n🔍 Enter Username to find IP: ")

# Checking if user exists in our map
if search_user in user_ip_map:
    print(f"✅ Found! User: {search_user} is using IP: {user_ip_map[search_user]}")
else:
    print(f"❌ Alert: Username '{search_user}' not found in logs.")

print('-'*60)

# 4. Extracting Data back (Unzipping)
users, ips = zip(*user_ip_map.items())
print(f"\n📂 All Active Users: {users}")
print(f"📂 All Active IPs  : {ips}")
