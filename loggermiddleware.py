class LoggerMiddleware(object):
    def __init__(self,app):
        self.app = app
        

def getBalance():
    print('--get balance--')
    payload = {
            'token':globalToken,
            'accountNumber':globalAccountNumber
                    }
    accountOverviewData = requests.post('https://ems.qa.tradingticket.com/api/v1/balance/getAccountOverview', params=payload)
    accountOverview = accountOverviewData.json()
    print(accountOverview)
