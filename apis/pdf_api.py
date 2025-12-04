# from locust import task, between
# from apis.base_user import BaseUser

# class PDFAPI(BaseUser):
#     wait_time = between(2, 3)

#     @task
#     def generate_pdf(self):
#         payload = {
#             "html": "<h1>Test PDF</h1>",
#             "title": "PDF Example",
#             "landscape": True
#         }
#         self.client.post("/api/generate-pdf", json=payload, name="PDF Generate")
