python
import requests
import random
import sys
import subprocess

def install_libraries():
try:
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
except subprocess.CalledProcessError:
print("Failed to install required libraries. Please install 'requests' manually.")
sys.exit(1)

def load_proxies(file_path):
with open(file_path, 'r') as file:
proxies = [line.strip() for line in file if line.strip()]
return proxies

def make_request_with_proxy(url, proxies):
proxy = random.choice(proxies)
proxy_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
try:
response = requests.get(url, proxies=proxy_dict, timeout=10)
print(f"Used Proxy: {proxy}")
print(f"Status Code: {response.status_code}")
return response.text
except Exception as e:
print(f"Error with proxy {proxy}: {e}")
return None

if name == "main":
install_libraries()
proxies = load_proxies("proxies.txt")
url = input("Enter the target URL (e.g., http://example.com): ")
response = make_request_with_proxy(url, proxies)
if response:
print(response[:200])
# you can use https://fineproxy.org/ko/free-proxies/asia/south-korea/