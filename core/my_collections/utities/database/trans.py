from datetime import datetime
# from  getmac  import get_mac_address
from collections import  Counter

class Transcode:
    def transact_code(self):
        return f'{self.timeformat()}'

    def timeformat(self):
        return datetime.now().strftime("%f-%S%M-%d%m%y")

    # def getadder(self):
    #     return get_mac_address()

if __name__ == "__main__":
    p = Transcode()
    # c = Counter()
    # for x in range(1000):
    #     c[p.transact_code()] += 1

    print(p.transact_code())



