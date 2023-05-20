import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://wwww.python.org")
        
    # def test_example():
    #     print("Test")
    #     assert False
        
    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()