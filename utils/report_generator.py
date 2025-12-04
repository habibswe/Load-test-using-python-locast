from locust import events
import json
from datetime import datetime
import os

@events.test_stop.add_listener
def generate_reports(environment, **kwargs):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # JSON report export
    json_report_path = f"reports/json_reports/report_{timestamp}.json"
    with open(json_report_path, "w") as f:
        stats = environment.stats.serialize_stats()
        json.dump(stats, f, indent=4)
    print(f"📄 JSON Report saved: {json_report_path}")

    # HTML report export
    html_report_path = f"reports/html_reports/report_{timestamp}.html"
    html = environment.stats.dump_html()
    with open(html_report_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"📊 HTML Report saved: {html_report_path}")
