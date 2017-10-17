from replicon import Replicon

test_rep = Replicon(test_company, test_userName, test_password)
        

def test_GetUser():
    resp = test_rep.getUsers()
    assert resp.status_code == 200
    assert resp.json()['d'][0]['loginName'] == test_userName


def test_getUserByLogin():
    resp = test_rep.getUserByLogin(test_userName)
    assert resp.status_code == 200
    assert resp.json()['d'][0]['slug'] = ''


def test_getbulkUser():
    userURIs = ['','','']
    resp = test_rep.getBulkUsers(userURIs) 

    assert resp.status_code == 200
    for user in userURIs:
        assert user in resp.json()['d'][0].values()
    

def test_getTimeOff():
    startDate = (1,1,2017)
    endDate = (1,30,2017)

    resp = test_rep.getTimeOff(startDate, endDate)

    assert resp.status_code == 200


def test_getAllHolidays():
    holidays = ["Holiday","Family Day", "Good Friday", "Easter Monday",
                "Victoria Day", "Canada Day", "BC Day", "Labor Day",
                "Thanksgiving Day", "Remembrance Day",
                "Christmas Day", "Boxing Day", "Stat"]
    resp = test_rep.getAllHolidays()

    assert resp.status_code == 200
    for holiday in holidays:
        assert holliday in resp.json()['d'][0].values()


def test_getHolidays():
    startDate = (20,12,2017)
    endDate = (31,12,2017)
    expected_holidays = ['Christmas Day', 'Boxing Day']
    resp = test_rep.getHolidays(startDate, endDate)

    assert resp.status_code == 200
    for holiday in expected_holidays:
        assert holiday in resp.json()['d'][0].values()