import requests


def evaluate_loan(document: str, name: str):
    url = "https://loan-processor.digitalsys.com.br/api/v1/loan/"
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    data = {"document": document, "name": name}
    response = requests.post(url=url, data=data, headers=headers)
    if response.status_code != 200:
        raise Exception(f"[{response.status_code}] {response.text}")
    return response.json()


if __name__ == "__main__":
    r = evaluate_loan("88815935134", "Christian Douglas")
