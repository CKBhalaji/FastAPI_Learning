from fastapi import status
from .utils import *
from ..routers.user import get_db, get_current_user
from ..models import User

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'qwertytest'
    assert response.json()['email'] == 'qwertytest@gmail.com'
    assert response.json()['first_name'] == 'qwertytest'
    assert response.json()['last_name'] == 'uiopastest'
    # assert response.json()['hashed_password'] == 'qwertytest'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '9789559266'
    
def test_change_paswors_sucess(test_user):
    respose = client.put("/user/changePassword", json={"password":"qwertytest", "new_password":"testqwerty"})
    assert respose.status_code == status.HTTP_204_NO_CONTENT
    
def test_change_password_invalid_current_password(test_user):
    respose = client.put("/user/changePassword", json={"password":"wrong_password", "new_password":"testqwerty"})
    assert respose.status_code == status.HTTP_401_UNAUTHORIZED    
    assert respose.json() == {"detail":"Error on the password change."}
    
def test_change_phone_number_success(test_user):
    response = client.put("/user/changephonenumber/7845123698")
    assert response.status_code == status.HTTP_204_NO_CONTENT
