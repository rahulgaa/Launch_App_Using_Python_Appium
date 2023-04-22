import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.select import Select

desired_caps = {
    'platformName' : 'Android',
    'platformVersion' : '9.0',
    'deviceName' : 'Masters Interactive',
    'automationName': 'uiautomator2',
   # 'appPackage': 'com.android.chrome',
    'appPackage' : 'com.Altom.TrashCat',
   # 'appActivity': 'com.google.android.apps.chrome.Main',
    'appActivity': 'com.unity3d.player.UnityPlayerActivity',
    'udid': 'JBAAGF02L160LTJ'
    }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.start_activity("com.Altom.TrashCat", "com.unity3d.player.UnityPlayerActivity")

# to wait for 10 sec
time.sleep(10)
# To quit the app
driver.quit()
