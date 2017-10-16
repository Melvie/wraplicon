from repliwrap import Replicon

test_userName = ""
test_userName = ""
test_company = ""



def test_GetUser():
    rep = Replicon(test_userName,test_userName ,test_company)

    assert rep.getUsers().json()
