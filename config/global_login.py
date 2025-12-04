from locust import events
import requests

GLOBAL_TOKEN = None
API_KEY = "7ca7c0a9-4d15-4697-81ae-e0b9ded2502d"

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    global GLOBAL_TOKEN
    print("\n🔐 Performing ONE-TIME login...")

    login_payload = {
        "email": "habib.qtec@gmail.com",
        "password": "asdfgh"
    }

    resp = requests.post(
        environment.host + "/api/auth/login/",
        json=login_payload
    )

    if resp.status_code == 200:
        GLOBAL_TOKEN = resp.json().get("access")
        print("✅ Global Bearer token saved.")
    else:
        print("❌ Login failed:", resp.text)
