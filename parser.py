from dateutil import parser
from datetime import datetime

def convertToHoursAgo(timestamp: str):
        now = datetime.now()
        timestamp = parser.parse(timestamp)
        age = now - timestamp
        return round(age.total_seconds() / 3600.0, 2)