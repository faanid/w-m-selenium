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
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
        
   
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()