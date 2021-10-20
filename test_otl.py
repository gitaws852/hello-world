import pytest
import json
import otl_cases

clientId = "9ec75914-f886-4dce-9557-9e54efa7c821"
headers = {}

# otl sandbox auth intiate call - gives success response
def test_otl_sandbox_auth_initate_200():
	response = otl_cases.otl_sandbox_auth_initate_200(headers = headers, clientId = clientId)
	assert response.status_code == 200
  
  
