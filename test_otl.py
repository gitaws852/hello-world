import pytest
import json
import otl_cases
import os

clientId = "babab5b5-404c-4180-8e49-a24b0c924f3c"
headers = {}

# otl sandbox auth intiate call - gives success response
def test_otl_sandbox_auth_initate_200():
	response = otl_cases.otl_sandbox_auth_initate_200(headers = headers, clientId = clientId)
	assert response.status_code == 200
  
  
