import requests
import json

def test_api():
    url = "http://127.0.0.1:5001/api/analyze"
    payload = {"query": "Is dumping plastic in the ocean compliant with ESG rules?"}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(f"Status Code: {response.status_code}")
        print("Response:")
        print(json.dumps(response.json(), indent=4))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api()
