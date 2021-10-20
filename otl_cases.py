import requests
import uuid


valid_mobile_number = str(779999999995)
invalid_mobile_number = str(9999999995)

crId = str(uuid.uuid4())
base_url = "https://api.sandbox.bureau.id/v2/auth/"


def otl_sandbox_auth_initate_200(headers, clientId):
	payload={}
	headers = {}
	url = base_url + "initiate?" + "correlationId=" + crId + "&" + "clientId=" + clientId + "&" + "mobile=" + valid_mobile_number
	response = requests.request("GET", url, headers=headers, data=payload)
	return response

def otl_sandbox_auth_userinfo_200(headers):
	payload={}
	headers = headers
	url = base_url + "userinfo?" + "correlationId=" + crId
	response = requests.request("GET", url, headers=headers, data=payload)
	return response.status_code

def otl_sandbox_auth_initate_existing_correlationId_400(headers, clientId):
	payload={}
	headers = headers
	clientId = clientId
	url = base_url + "initiate?" + "correlationId=" + crId + "&" + "clientId=" + clientId + "&" + "mobile=" + valid_mobile_number
	response = requests.request("GET", url, headers=headers, data=payload)
	return response.status_code



