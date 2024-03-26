import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LiatrioBootcampLinkTest(unittest.TestCase):
    def setUp(self):
        # choose which webdriver to use
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def test_bootcamp_link(self):
        driver = self.driver
        driver.get("https://devops-bootcamp.liatr.io")
        # check we get expected page title
        assert "Liatrio's DevOps Bootcamp" in driver.title
        # find the link to Introduction to DevOps section at the bottom of the page
        driver.get("https://devops-bootcamp.liatr.io/#/1-introduction/1.0-overview")
        # check that we get the expected url
        assert "https://devops-bootcamp.liatr.io/#/1-introduction/1.0-overview" in driver.current_url

    def tearDown(self):
        self.driver.quit()


class LiatrioBootcampSidebarTest(unittest.TestCase):
    def setUp(self):
        # choose which webdriver to use
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def test_bootcamp_sidebar(self):
        driver = self.driver
        driver.get("https://devops-bootcamp.liatr.io")

        # check that the sidebar is shown (HINT: check html body attributes)
        body = driver.find_element(By.TAG_NAME, "body")
        assert "ready sticky" in body.get_attribute('class')

        # check that there is no CLOSE attribute on the body
        assert "close" not in body.get_attribute('class')

        # find the sidebar toggle and toggle it
        driver.find_element(By.CLASS_NAME, 'sidebar-toggle').click()

        # after toggling sidebar, check that it is closed
        assert "close" in body.get_attribute('class')


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()