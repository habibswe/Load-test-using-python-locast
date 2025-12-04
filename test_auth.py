#!/usr/bin/env python3
"""
Quick diagnostic script to test login and API endpoints
Run this to see why your load tests are failing
"""
import requests

# Configuration
HOST = "https://backend.amal.education"
API_KEY = "7ca7c0a9-4d15-4697-81ae-e0b9ded2502d"
EMAIL = "habib.qtec@gmail.com"
PASSWORD = "asdfgh"

print("=" * 60)
print("🔍 DIAGNOSTIC TEST - Checking API Authentication")
print("=" * 60)

# Test 1: Login
print("\n1️⃣ Testing Login Endpoint...")
print(f"   URL: {HOST}/api/accounts/sign-in/")
login_payload = {"username": EMAIL, "password": PASSWORD}
headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

try:
    resp = requests.post(f"{HOST}/api/accounts/sign-in/", json=login_payload, headers=headers, timeout=10)
    print(f"   Status Code: {resp.status_code}")
    print(f"   Response: {resp.text[:200]}")
    
    if resp.status_code == 200:
        token = resp.json().get("access")
        print(f"   ✅ Login successful!")
        print(f"   Token (first 20 chars): {token[:20] if token else 'None'}...")
    else:
        print(f"   ❌ Login failed!")
        token = None
except Exception as e:
    print(f"   ❌ Error: {e}")
    token = None

# Test 2: Try an API endpoint with the token
if token:
    print("\n2️⃣ Testing Dashboard Endpoint with Token...")
    headers = {
        "Authorization": f"Bearer {token}",
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    try:
        resp = requests.get(f"{HOST}/api/dashboard/", headers=headers, timeout=10)
        print(f"   URL: {HOST}/api/dashboard/")
        print(f"   Status Code: {resp.status_code}")
        print(f"   Response: {resp.text[:200]}")
        
        if resp.status_code == 200:
            print(f"   ✅ Dashboard endpoint works!")
        else:
            print(f"   ❌ Dashboard endpoint failed!")
    except Exception as e:
        print(f"   ❌ Error: {e}")
else:
    print("\n2️⃣ Skipping endpoint test (no token)")

# Test 3: Check if server is reachable
print("\n3️⃣ Testing Server Connectivity...")
try:
    resp = requests.get(HOST, timeout=5)
    print(f"   Server is reachable (Status: {resp.status_code})")
except Exception as e:
    print(f"   ❌ Server unreachable: {e}")

print("\n" + "=" * 60)
print("DIAGNOSIS COMPLETE")
print("=" * 60)
