import requests

def make_get_request(url):
    try:
        # Perform the GET request
        response = requests.get(url,allow_redirects=False)

        # Print status code and response headers
        print(f"Status Code: {response.status_code}")
        print("Response Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")

if __name__ == "__main__":
    url = "https://c006.preprod.aqfer.net/1/a/c.gif"
    make_get_request(url)
