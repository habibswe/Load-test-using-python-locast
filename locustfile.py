"""
Locust Load Testing for Amal Education API
Main file that imports all API test classes
"""

# Import all API test classes
from apis.authentication_api import AuthenticationAPI
from apis.dashboard_api import DashboardAPI
from apis.ai_assistant_api import AIAssistantAPI
from apis.library_api import LibraryAPI
from apis.help_api import HelpAPI

# All imported classes will be automatically discovered by Locust
# You can run specific classes using: locust -f locustfile.py ClassName

# Example:
# locust -f locustfile.py DashboardAPI
# locust -f locustfile.py HelpAPI
# locust -f locustfile.py --host=https://backend.amal.education
