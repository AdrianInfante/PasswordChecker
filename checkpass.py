import requests
import hashlib
from pathlib import Path

path = Path("drag_here_pass_folder")


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}")
    return response

def get_pass_leaks_count(hashes, hash_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        # print(h,count)
        if h == hash_check:
            print("Found " + count + " times")
            return count
    return 0

def pwned_api_check(password):
    sha1pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1pass[:5], sha1pass[5:]
    response = request_api_data(first5_char)
    # print(response)
    return get_pass_leaks_count(response, tail)

def check_pass_from_file():
    for child in path.iterdir():
        with open(child) as f:
            t = f.readline()
    return pwned_api_check(t)
        
    

if __name__ == "__main__":
    check_pass_from_file()

