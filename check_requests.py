import requests
import sys

# print current python path
# and make sure we are in .venv
print("---ENVIRONMENT CHECK ---")
print(f"Python executable path: {sys.executable}")
print("------------------------")

# try to make a simple HTTP GET request
try:
    response = requests.get('https://httpbin.org/get')
    response.raise_for_status() # 检查请求是否成功
    print(f"SUCCESS: requests library is working!")
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers['content-type']}")
    
except requests.exceptions.RequestException as e:
    print(f"ERROR: requests library failed. {e}")
