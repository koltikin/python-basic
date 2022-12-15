from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://www.youtube.com/watch?v=b5jt2bhSeXs&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ&index=2")
driver.get("https://pypi.org/project/webdriver-manager")
driver.quit()
