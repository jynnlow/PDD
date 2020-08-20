from app.state.state import State
from pprint import pprint
from datetime import date, timedelta

class General:
    def printObject(target_object):
        for target in target_object:
            pprint(vars(target))

    def get7DaysByToday():
        datelist = []
        for i in range(1,7):
            datelist.append((date.today() + timedelta(days=i)).strftime("%Y%m%d"))
        return datelist