from appium import webdriver
import time

def test_android_calculator():

    from appium.options.android import UiAutomator2Options
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "10"
    options.device_name = "Android Emulator"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.android.calculator2"
    options.app_activity = "com.android.calculator2.Calculator"
    driver = webdriver.Remote('http://android:4723/wd/hub', options=options)


    time.sleep(2)
    assert driver.is_app_installed("com.android.calculator2")
    driver.quit()
