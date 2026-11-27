#!/usr/bin/python3
"""Sends POST request with email using requests."""

import requests
import sys

if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data=data)
    print(response.text)
