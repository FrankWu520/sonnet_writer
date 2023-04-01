import requests

API_URL = "https://api-inference.huggingface.co/models/wuzhenfrank/sonnet-writer"
headers = {"Authorization": "Bearer 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"}


def query(payload):
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.json()
