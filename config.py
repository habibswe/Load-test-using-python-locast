"""
Configuration file for Amal Education API Load Testing
"""

# API Configuration
API_BASE_URL = "https://backend.amal.education"
API_TOKEN = "7ca7c0a9-4d15-4697-81ae-e0b9ded2502d"

# Test User Credentials
TEST_USERS = [
    {
        "email": "mirazhs@proton.me",
        "password": "testing321"
    },
    # Add more test users as needed
]

# Load Test Configuration
DEFAULT_USERS = 10
DEFAULT_SPAWN_RATE = 2
DEFAULT_RUN_TIME = "60s"

# Task Weights
TASK_WEIGHTS = {
    "dashboard": 3,
    "ai_assistant": 2,
    "library": 2,
    "help_center": 1,
    "authentication": 1
}

# Wait Time Configuration (seconds)
MIN_WAIT_TIME = 1
MAX_WAIT_TIME = 3

# Endpoints
ENDPOINTS = {
    "sign_up": "/api/accounts/sign-up/",
    "sign_in": "/api/accounts/sign-in/",
    "token_refresh": "/api/accounts/token/refresh/",
    "dashboard": "/api/dashboard/",
    "search": "/api/dashboard/v2/search/",
    "tools_template": "/api/ai-assistant/tools-and-template/",
    "mystery_box": "/api/ai-assistant/random-mystery-box/",
    "thread": "/api/ai-assistant/chat/thread/",
    "my_collection": "/api/ai-assistant/my-collection/",
    "library": "/api/ai-assistant/library/",
    "create_collection": "/api/ai-assistant/create-collection/",
    "help_articles": "/api/help-center/help-articles/",
    "contact_us": "/api/help-center/contact-us/"
}

# Response Time Thresholds (milliseconds)
RESPONSE_TIME_THRESHOLDS = {
    "excellent": 200,
    "good": 500,
    "acceptable": 1000,
    "slow": 2000
}

# Privacy Choices
PRIVACY_PRIVATE = 1
PRIVACY_SHAREABLE = 2

# User Roles
ROLE_VIEWER = 1
ROLE_EDITOR = 2

# School Types
SCHOOL_TYPE_PRIMARY = 1
SCHOOL_TYPE_HIGH = 2
SCHOOL_TYPE_SECONDARY = 3
SCHOOL_TYPE_SECONDARY_II = 4
SCHOOL_TYPE_OTHER = 5

# Message Roles
MESSAGE_ROLE_USER = 1
MESSAGE_ROLE_AI = 2
