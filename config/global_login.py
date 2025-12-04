from locust import events
import requests

GLOBAL_TOKEN = None
API_KEY = "7ca7c0a9-4d15-4697-81ae-e0b9ded2502d"

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    global GLOBAL_TOKEN
    print("\n🔐 Performing ONE-TIME login...")

    login_payload = {
        "username": "habib.qtec@gmail.com",
        "password": "asdfgh"
    }

    # Use X-API-Token header as required by backend
    headers = {
        "X-API-Token": API_KEY,
        "Content-Type": "application/json"
    }

    resp = requests.post(
        environment.host + "/api/accounts/sign-in/",
        json=login_payload,
        headers=headers
    )

    print(f"📊 Login response status: {resp.status_code}")
    if resp.status_code == 200:
        GLOBAL_TOKEN = resp.json().get("access")
        print(f"✅ Global Bearer token saved: {GLOBAL_TOKEN[:20]}..." if GLOBAL_TOKEN else "❌ Token is None!")
    else:
        print(f"❌ Login failed with status {resp.status_code}")
        print(f"Response: {resp.text}")
