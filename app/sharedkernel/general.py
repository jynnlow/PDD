from pprint import pprint

class General:
    def printObject(target_object):
        for target in target_object:
            pprint(vars(target))