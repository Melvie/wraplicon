import requests
from requests import Session
from requests.auth import AuthBase
import json
import sys

class Replicon():

    def __init__(self, companyName, userName, password):
        self.company = companyName
        self.session = Session()
        self.session.auth = (self.company+'\\'+userName, password)
        self.session.headers = {'Content-Type': 'application/json'}

        resp = self.session.post(self._getRepliconnectUrl(), data=json.dumps({'Action':'BeginSession'}))
        # assert(resp)


    def _getBaseServiceUrl(self):
        return f"https://na3.replicon.com/{self.company}/services"

    def _getRepliconnectUrl(self):

        # url = self.session.post(f'http://services.replicon.com/FetchRemoteApiUrl.ashx?CompanyKey={self.company}&Version=8.29.66')

        return f"https://na3.replicon.com/{self.company}/RemoteAPI/RemoteAPI.ashx/8.29.66/"

    def getUsers(self):
        url = self._getBaseServiceUrl()  + '/UserService1.svc/GetAllUsers'

        response = self.session.post(url)

        return response

    def getBulkUsers(self, userURIs):
        url = self._getBaseServiceUrl()  + '/UserService1.svc/BulkGetUsers'

        query = {
                 "userUris": [userURIs]
                 }
        return self.session.post(url, data=json.dumps(query))


    def getTimeOff(userURI, startDate, endDate):
        url = self._getBaseServiceUrl()  + '/TimeOffService1.svc/GetTimeOffDetailsForUserAndDateRange'
        s_year, s_month, s_day = startDate.timetuple()
        e_year, e_month, e_day = endDate.timetupe()
        query={"userUri": userURI,
               "dateRange": {"startDate": {"year": s_year,
                                           "month": s_month,
                                           "day": s_day},
                             "endDate": {"year": e_year,
                                         "month": e_month,
                                         "day": e_day},
                             "relativeDateRangeUri": None,
                             "relativeDateRangeAsOfDate": None}
            }

        response = self.session.post(url, data=json.dumps(query))

        return response


    def getUserByEmail(self, email):
        """TODO: FIX"""
        url = self._getBaseServiceUrl()  + '/UserService1.svc/GetUser2'
        url = self._getRepliconnectUrl()
        query={}
        query['data'] = {"Action": "Query", "DomainType":"Replicon.Domain.User",
                         "QueryType":"UserByLoginName", "Args": [email], "SortBy":["LastName","FirstName"],
                         }

        response = self.session.post(url, data=json.dumps(query))

        return response


    def getUserByLogin(self, login):
        url = self._getBaseServiceUrl()  + '/UserService1.svc/GetUser2'

        query={"user": {"uri": None,
                        "loginName": login,
                        "parameterCorrelationId": None}}

        response = self.session.post(url, data=json.dumps(query))
        assert(response)
        return response


    def getAllHolidays(self,year):
        """TODO: chanve from year to actual range"""
        url = self._getBaseServiceUrl() +'/HolidayCalendarService1.svc/GetHolidaysInDateRange'

        query = {"holidayCalendarUri": "urn:replicon-tenant:dynamic-structures-new:holiday-calendar:3",
                 "dateRange": {"startDate": {"year": year,
                                             "month": 1,
                                             "day": 1},
                               "endDate": {"year": year,
                                           "month": 12,
                                           "day": 31 },
                               "relativeDateRangeUri": None,
                               "relativeDateRangeAsOfDate": None }
                }

        response = self.session.post(url, data=json.dumps(query))

        return response.json()['d']







def main():
    sesh = Replicon(companyKey, loginName, password)
    users = sesh.getAllHolidays(2017)
    # print (users[0])
    for item in users:
        print( f"Holiday:{item['name']}")
    # try:
    #     if 'application/json' in users.headers['Content-Type']:
    #         print(users.json())
    #     else:
    #         print(f'No JSON:{users.headers}')
    # except:
    #     print (users)

if __name__ == "__main__":
    main()