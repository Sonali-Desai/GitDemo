import pytest

'''
Its mot working
@pytest.mark.usefixtures("dataload")
class testexample:
    def profile(self,dataload):
        print(dataload)
        print(dataload[1])'
        '''
#its working
def test_profile(dataload):
        print(dataload)
        print(dataload[1])

def test_browser(browsers):
    print(browsers) 
    