#!/usr/bin/env python3
"""
Simple test script to verify backend endpoints are working.
Run this after starting the Flask application.
"""

import requests
import json

BASE_URL = "http://localhost:5000/api"

def test_basic_endpoint():
    """Test the basic API endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✅ Basic API endpoint: {response.status_code}")
        print(f"   Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Basic API endpoint failed: {e}")
        return False

def test_protected_endpoint_without_auth():
    """Test that protected endpoints require authentication"""
    try:
        response = requests.get(f"{BASE_URL}/users/profile")
        print(f"✅ Protected endpoint without auth: {response.status_code}")
        print(f"   Response: {response.json()}")
        return response.status_code == 401
    except Exception as e:
        print(f"❌ Protected endpoint test failed: {e}")
        return False

def main():
    print("🧪 Testing Kinri Backend Endpoints")
    print("=" * 40)

    results = []

    print("\n1. Testing basic API endpoint...")
    results.append(test_basic_endpoint())

    print("\n2. Testing protected endpoint without authentication...")
    results.append(test_protected_endpoint_without_auth())

    print("\n" + "=" * 40)
    print(f"✅ Tests passed: {sum(results)}/{len(results)}")

    if all(results):
        print("🎉 All basic tests passed! Backend appears to be running correctly.")
    else:
        print("⚠️  Some tests failed. Check the backend server logs.")

if __name__ == "__main__":
    main()