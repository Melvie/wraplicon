from replicon import Replicon


test_rep = Replicon(test_company, test_userName, test_password)

def test_GetUser():
    resp = test_rep.getUsers()

    assert resp.status_code == 200
    assert resp.json()['d'][0]['loginName'] == test_userName


def test_getUserByLogin():
    resp = test_rep.getUserByLogin('')

    assert resp.status_code == 200
    assert resp.json()['d']['slug'] == ''


def test_getbulkUser():
    userURIs = []

    resp = test_rep.getBulkUsers(userURIs)
    returned_users = [thing['uri'] for thing in resp.json()['d']]

    assert resp.status_code == 200
    for user in userURIs:
        assert user in returned_users


def test_getTimeOff():
    startDate = (2017, 10, 1)
    endDate = (2017, 12, 27)
    userURI = ""

    resp = test_rep.getTimeOff(userURI, startDate, endDate)

    assert resp.status_code == 200


def test_getAllHolidays():
    holidays = ["Holiday", "Family Day", "Good Friday", "Easter Monday",
                "Victoria Day", "Canada Day", "BC Day", "Labor Day",
                "Thanksgiving Day", "Remembrance Day",
                "Christmas Day", "Boxing Day", "Stat"]

    resp = test_rep.getAllHolidays()
    returned_holidays = [thing['name'] for thing in resp.json()['d']]

    assert resp.status_code == 200
    for holiday in holidays:
        assert holiday in returned_holidays


def test_getHolidays():
    startDate = (20, 12, 2017)
    endDate = (31, 12, 2017)
    expected_holidays = ['Christmas Day', 'Boxing Day']

    resp = test_rep.getHolidays(startDate, endDate)
    returned_holidays = [thing['name'] for thing in resp.json()['d']]

    assert resp.status_code == 200
    for holiday in expected_holidays:
        assert holiday in returned_holidays
