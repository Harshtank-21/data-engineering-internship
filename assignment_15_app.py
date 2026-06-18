import sys
from datetime import datetime

python_version = sys.version
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"Python Version: {python_version}")
print(f"Current Date and Time: {current_datetime}")
