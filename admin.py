import requests
import json

from qr_info_class import qr_info_class
from user_class import UserInfo

# Define the base URL
# base_url = "http://18.162.149.95/sph_portal/user/"
base_url = "http://1.14.135.210:8569/sph_portal/user/"


def getContact():
    contactResponse = requests.post(
        f"{base_url}getContact",
    )
    json_data = json.loads(contactResponse.text)
    body = json_data["body"]
    resultCode = body["resultCode"]
    if resultCode == "1000":
        resultData = body["data"]
        img = resultData["img"]
        content = resultData["content"]
        print(img)
        print(content)
        contact = qr_info_class(img, content)
        return contact
    else:
        return None


def register(account, pwd, tel):
    register_response = requests.post(
        f"{base_url}register",
        data={
            'account': account,
            'pwd': pwd,
            'tel': tel
        }
    )
    json_data = json.loads(register_response.text)
    body = json_data["body"]
    resultCode = body["resultCode"]
    if resultCode == "1000":
        return True
    else:
        return False


def login_admin(account, pwd):
    login_response = requests.post(
        f"{base_url}login",
        data={
            'account': account,
            'pwd': pwd
        }
    )
    print(login_response.text)
    json_data = json.loads(login_response.text)
    body = json_data["body"]
    resultCode = body["resultCode"]
    if resultCode == "1000":
        resultData = body["data"]
        userId = resultData["userId"]
        userCode = resultData["userCode"]
        account = resultData["account"]
        point = resultData["point"]
        token = resultData["token"]
        return UserInfo(userId, userCode, account, point, token)
    else:
        return None


def get_point(userId, token):
    get_point_response = requests.post(
        f"{base_url}getPoint",
        data={
            'userId': userId,
            'token': token
        }
    )
    json_data = json.loads(get_point_response.text)
    body = json_data["body"]
    resultCode = body["resultCode"]
    if resultCode == "1000":
        resultData = body["data"]
        point = resultData["point"]
        return point
    else:
        return None


def use_point(userId, token, point):
    use_point_response = requests.post(
        f"{base_url}usePoint",
        data={
            'userId': userId,
            'token': token,
            'point': point
        }
    )
    json_data = json.loads(use_point_response.text)
    body = json_data["body"]
    resultCode = body["resultCode"]
    if resultCode == "1000":
        return True
    else:
        return False
