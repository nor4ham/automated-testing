from appium import webdriver
import time

def test_ios_settings_app():
    from appium.options.ios import XCUITestOptions
    options = XCUITestOptions()
    options.platform_name = "iOS"
    options.platform_version = "14.4"
    options.device_name = "iPhone Simulator"
    options.automation_name = "XCUITest"
    options.bundle_id = "com.apple.Preferences"
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)

    time.sleep(2)
    assert driver.is_app_installed("com.apple.Preferences")
    driver.quit()
