from selenium.webdriver import Chrome


driver = Chrome('./chromedriver')

url = 'https://www.ptt.cc/bbs/index.html'

driver.get(url)