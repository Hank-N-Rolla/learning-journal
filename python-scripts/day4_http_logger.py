import requests

def http_logger():
    url = input("Enter the URL to test: ").strip()

    # Spoof browser user-agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)

        print("\n--- HTTP Response Info ---")
        print(f"Status Code: {response.status_code}")
        print(f"Final URL: {response.url}")
        print(f"Headers:\n{response.headers}")
        print(f"Content Length: {len(response.text)} characters")

        save = input("\nSave response body to file? (y/n): ").lower()
        if save == 'y':
            with open("response_output.html", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Response saved to response_output.html")

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")

if __name__ == "__main__":
    http_logger()
