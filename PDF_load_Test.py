from locust import HttpUser, task, between
import random

# -------------------------------
# Fixed Header Token
# -------------------------------
FIXED_HEADER_TOKEN = "7ca7c0a9-4d15-4697-81ae-e0b9ded2502d"

# -------------------------------
# Accounts for login
# -------------------------------
ACCOUNTS = [
    {"email": "habib.qtec@gmail.com", "password": "asdfgh"},
    # Add more accounts if needed
]

# -------------------------------
# PDF Payload
# -------------------------------
PDF_PAYLOAD = {
    "html": "<h1 dir=\"ltr\">Lesson Series Outline</h1><hr><h2 dir=\"ltr\">Basic Information</h2>"
            "<ul dir=\"ltr\" class=\"tight\" data-tight=\"true\">"
            "<li dir=\"ltr\"><p dir=\"ltr\"><strong>Date:</strong> [Please add the date]</p></li>"
            "<li dir=\"ltr\"><p dir=\"ltr\"><strong>Topic:</strong> [Please specify the overarching theme of the series]</p></li>"
            "<li dir=\"ltr\"><p dir=\"ltr\"><strong>Subject:</strong> [Please specify the subject]</p></li>"
            "<li dir=\"ltr\"><p dir=\"ltr\"><strong>Grade Level:</strong> [Please specify the grade level]</p></li>"
            "<li dir=\"ltr\"><p dir=\"ltr\"><strong>Number of Lessons:</strong> [Please specify the approximate number of lessons]</p></li>"
            "<li dir=\"ltr\"><p dir=\"ltr\"><strong>Teacher:</strong> [Please add your name or leave blank]</p></li>"
            "</ul><hr>"
            "<h2 dir=\"ltr\">Lesson Overview</h2>"
            "<table dir=\"ltr\" style=\"min-width: 900px;\">"
            "<colgroup>"
            "<col style=\"min-width: 100px;\"><col style=\"min-width: 100px;\"><col style=\"min-width: 100px;\">"
            "<col style=\"min-width: 100px;\"><col style=\"min-width: 100px;\"><col style=\"min-width: 100px;\">"
            "<col style=\"min-width: 100px;\"><col style=\"min-width: 100px;\"><col style=\"min-width: 100px;\">"
            "</colgroup>"
            "<tbody>"
            "<tr><th>Lesson</th><th>Lesson Topic</th><th>Learning Objective</th><th>Activities</th>"
            "<th>Materials</th><th>Assessment</th><th>Duration</th><th>Skills Focus</th><th>Notes</th></tr>"
            "<tr><td>1</td><td>[Topic for Lesson 1]</td><td>[Objective]</td><td>[Activities]</td>"
            "<td>[Materials]</td><td>[Assessment]</td><td>[Duration]</td><td>[Skills]</td><td>[Notes]</td></tr>"
            "<tr><td>2</td><td>[Topic for Lesson 2]</td><td>[Objective]</td><td>[Activities]</td>"
            "<td>[Materials]</td><td>[Assessment]</td><td>[Duration]</td><td>[Skills]</td><td>[Notes]</td></tr>"
            "<tr><td>3</td><td>[Topic for Lesson 3]</td><td>[Objective]</td><td>[Activities]</td>"
            "<td>[Materials]</td><td>[Assessment]</td><td>[Duration]</td><td>[Skills]</td><td>[Notes]</td></tr>"
            "<tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td>"
            "<td>...</td><td>...</td></tr>"
            "<tr><td>[N]</td><td>[Topic for Last Lesson]</td><td>[Objective]</td><td>[Activities]</td>"
            "<td>[Materials]</td><td>[Assessment]</td><td>[Duration]</td><td>[Skills]</td><td>[Notes]</td></tr>"
            "</tbody>"
            "</table><hr>"
            "<h2 dir=\"ltr\">Skills to develop</h2>"
            "<ul class=\"tight\" data-tight=\"true\">"
            "<li>[List and explain comprehensively the skills students should acquire during the lesson series.]</li>"
            "<li>[Explain how you can structure the lessons so students achieve these skills and knowledge.]</li>"
            "<li>[Add each skill as a bullet point with a brief practical explanation.]</li>"
            "</ul><hr>"
            "<h2 dir=\"ltr\">Additional Guidance</h2>"
            "<ul class=\"tight\" data-tight=\"true\">"
            "<li>Please fill in the information required above so I can generate a complete lesson plan outline tailored to your needs.</li>"
            "<li>If you have any specific wishes for content, teaching methods, materials, or additional considerations, please list them here so I can incorporate them into your lesson series outline.</li>"
            "</ul>",
    "title": "Lesson Series Outline Basic Information…",
    "landscape": True
}

class PDFUser(HttpUser):
    """
    Multi-account load test for PDF generation API
    - Logs in to get Bearer token
    - Uses fixed header token
    - Only PDF API call
    """

    wait_time = between(1, 3)

    def on_start(self):
        """Login and store Bearer token + fixed header token"""
        account = random.choice(ACCOUNTS)
        self.username = account["email"]
        self.password = account["password"]

        login_payload = {
            "email": self.username,
            "password": self.password
        }

        # Login API
        with self.client.post(
            "/api/auth/login/",
            json=login_payload,
            name="Login",
            catch_response=True
        ) as res:
            if res.status_code == 200:
                bearer_token = res.json().get("access")
                # Add both tokens in headers for all subsequent requests
                self.client.headers.update({
                    "Authorization": f"Bearer {bearer_token}",
                    "x-api-key": FIXED_HEADER_TOKEN,  # example for fixed header token
                    "Content-Type": "application/json"
                })
            else:
                res.failure(f"❌ Login failed for {self.username}: {res.text}")

    # -------------------------------
    # PDF Generation Task
    # -------------------------------
    @task
    def generate_pdf(self):
        """POST request to generate PDF"""
        with self.client.post(
            "/api/generate-pdf",
            json=PDF_PAYLOAD,
            name="Generate PDF",
            catch_response=True
        ) as res:
            if res.status_code not in [200, 201]:
                res.failure(f"⚠️ PDF generation failed ({res.status_code}): {res.text}")
