import requests
from concurrent.futures import ThreadPoolExecutor

def stress_test(url, num_requests):
    def send_request():
        try:
            response = requests.get(url)
            print(response.status_code)
        except Exception as e:
            print(f"Request failed: {e}")

    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(send_request) for _ in range(num_requests)]
        for future in futures:
            future.result()

if __name__ == "__main__":
    url = "http://127.0.0.1:5000"
    num_requests = 1000  # Número de requisições para enviar
    stress_test(url, num_requests)
