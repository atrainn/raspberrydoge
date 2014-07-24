import urllib2

url = 'http://blockchain.info/ticker'

class getbtc:
    def GetVal(self):
        feed = urllib2.urlopen(url)
        var1 = feed.read()
        return var1
        
#Gets current  btc values for all currencies
    
    def UsdVal(self):
        rawVal = str(getbtc().GetVal())
        removeJunk = rawVal.split('"USD" : {')
        allUSDVal = removeJunk[1].split(',  "symbol" : "$"},')
        return allUSDVal[0]

#pulls out only the usd value line

    def FifteenVal(self):
        rawVal = str(getbtc().UsdVal())
        removeJunk = rawVal.split('"15m" : ')
        fifteenminVal = removeJunk[1].split(",")
        return fifteenminVal[0]
        
#returns the 15 minute value of btc

if __name__ == "__main__":
    print str(getbtc().GetVal())
    print str(getbtc().FifteenVal())
    
    
