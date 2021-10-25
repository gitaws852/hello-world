import pytest
import json
import otl_cases
import os

clientId = os.environ['Client_Id']
headers = {}

# otl sandbox auth intiate call - gives success response
def test_otl_sandbox_auth_initate_200():
	response = otl_cases.otl_sandbox_auth_initate_200(headers = headers, clientId = clientId)
	assert response.status_code == 200
  
  
