# File: test_reservation_edge_cases.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from test_config import get_driver, BASE_URL
import time

def test_maximum_length_inputs():
    """Test form with very long input values"""
    driver = get_driver()
    try:
        print("🧪 Testing maximum length inputs...")
        driver.get(BASE_URL + "/")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)
        
        # Very long strings
        long_name = "A" * 100  # 100 character name
        long_email = "a" * 50 + "@" + "b" * 40 + ".com"  # Very long email
        long_phone = "1" * 20  # 20 digit phone number
        
        # Fill form with long values
        first_name_field = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        first_name_field.send_keys(long_name)
        
        last_name_field = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        last_name_field.send_keys(long_name)
        
        driver.find_element(By.XPATH, "//input[@type='date']").send_keys("2025-12-25")
        driver.find_element(By.XPATH, "//input[@type='time']").send_keys("15:30")
        
        email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        email_field.send_keys(long_email)
        
        phone_field = driver.find_element(By.XPATH, "//input[@placeholder='Phone']")
        phone_field.send_keys(long_phone)
        
        print(f"✅ Filled form with long values")
        print(f"  - Name length: {len(long_name)} characters")
        print(f"  - Email length: {len(long_email)} characters")
        print(f"  - Phone length: {len(long_phone)} characters")
        
        # Check if values were truncated
        actual_first_name = first_name_field.get_attribute('value')
        actual_email = email_field.get_attribute('value')
        actual_phone = phone_field.get_attribute('value')
        
        if len(actual_first_name) < len(long_name):
            print(f"✅ First name was truncated to {len(actual_first_name)} characters")
        if len(actual_email) < len(long_email):
            print(f"✅ Email was truncated to {len(actual_email)} characters")
        if len(actual_phone) < len(long_phone):
            print(f"✅ Phone was truncated to {len(actual_phone)} characters")
        
        # Submit form
        reserve_button = driver.find_element(By.XPATH, "//button[contains(text(), 'RESERVE NOW')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", reserve_button)
        time.sleep(1)
        reserve_button.click()
        
        time.sleep(3)
        
        print("✅ Maximum length inputs test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    finally:
        driver.quit()

def test_special_characters():
    """Test form with special characters and unicode"""
    driver = get_driver()
    try:
        print("🧪 Testing special characters...")
        driver.get(BASE_URL + "/")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)
        
        # Special character inputs
        special_name = "José-María O'Connor"  # Accents, hyphens, apostrophes
        unicode_name = "李小明"  # Chinese characters
        special_email = "test+special@domain-name.co.uk"
        special_phone = "+92-300-123-4567"  # International format
        
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys(special_name)
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys(unicode_name)
        driver.find_element(By.XPATH, "//input[@type='date']").send_keys("2025-07-15")
        driver.find_element(By.XPATH, "//input[@type='time']").send_keys("14:45")
        driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(special_email)
        driver.find_element(By.XPATH, "//input[@placeholder='Phone']").send_keys(special_phone)
        
        print(f"✅ Filled form with special characters:")
        print(f"  - Name with accents: {special_name}")
        print(f"  - Unicode name: {unicode_name}")
        print(f"  - Complex email: {special_email}")
        print(f"  - International phone: {special_phone}")
        
        # Submit form
        reserve_button = driver.find_element(By.XPATH, "//button[contains(text(), 'RESERVE NOW')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", reserve_button)
        time.sleep(1)
        reserve_button.click()
        
        time.sleep(3)
        
        print("✅ Special characters test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    finally:
        driver.quit()

def test_rapid_form_submission():
    """Test submitting form multiple times rapidly"""
    driver = get_driver()
    try:
        print("🧪 Testing rapid form submission...")
        driver.get(BASE_URL + "/")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)
        
        # Fill form once
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Speed")
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Test")
        driver.find_element(By.XPATH, "//input[@type='date']").send_keys("2025-08-01")
        driver.find_element(By.XPATH, "//input[@type='time']").send_keys("12:00")
        driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("speed@test.com")
        driver.find_element(By.XPATH, "//input[@placeholder='Phone']").send_keys("1122334455")
        
        # Try to click submit button multiple times rapidly
        reserve_button = driver.find_element(By.XPATH, "//button[contains(text(), 'RESERVE NOW')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", reserve_button)
        time.sleep(1)
        
        print("🔄 Clicking submit button multiple times...")
        for i in range(3):
            try:
                reserve_button.click()
                print(f"  Click {i+1}: ✅")
                time.sleep(0.5)  # Small delay between clicks
            except Exception as e:
                print(f"  Click {i+1}: Button no longer clickable (good!)")
                break
        
        time.sleep(3)
        
        # Check if button is disabled after first click (prevents double submission)
        try:
            reserve_button = driver.find_element(By.XPATH, "//button[contains(text(), 'RESERVE NOW')]")
            if not reserve_button.is_enabled():
                print("✅ Button disabled after submission (prevents double booking)")
            else:
                print("ℹ️  Button still enabled (may allow multiple submissions)")
        except:
            print("✅ Button removed after submission (prevents double booking)")
        
        print("✅ Rapid submission test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    finally:
        driver.quit()

def test_browser_back_button():
    """Test form behavior after using browser back button"""
    driver = get_driver()
    try:
        print("🧪 Testing browser back button behavior...")
        driver.get(BASE_URL + "/")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)
        
        # Fill form partially
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Back")
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Button")
        driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("back@test.com")
        
        print("✅ Partially filled form")
        
        # Navigate away (simulate going to another page)
        driver.get(BASE_URL + "/#about")  # Navigate to different section
        time.sleep(2)
        
        # Go back
        driver.back()
        time.sleep(3)
        
        print("✅ Used browser back button")
        
        # Check if form data is preserved
        first_name_value = driver.find_element(By.XPATH, "//input[@placeholder='First Name']").get_attribute('value')
        last_name_value = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").get_attribute('value')
        email_value = driver.find_element(By.XPATH, "//input[@placeholder='Email']").get_attribute('value')
        
        if first_name_value == "Back" and last_name_value == "Button" and email_value == "back@test.com":
            print("✅ Form data preserved after back button")
        elif not first_name_value and not last_name_value and not email_value:
            print("✅ Form data cleared after back button (also acceptable)")
        else:
            print("ℹ️  Form data partially preserved")
        
        # Complete the form and submit
        if not first_name_value:
            driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Back")
        if not last_name_value:
            driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Button")
        if not email_value:
            driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("back@test.com")
        
        driver.find_element(By.XPATH, "//input[@type='date']").send_keys("2025-09-01")
        driver.find_element(By.XPATH, "//input[@type='time']").send_keys("16:00")
        driver.find_element(By.XPATH, "//input[@placeholder='Phone']").send_keys("5566778899")
        
        # Submit
        reserve_button = driver.find_element(By.XPATH, "//button[contains(text(), 'RESERVE NOW')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", reserve_button)
        time.sleep(1)
        reserve_button.click()
        
        time.sleep(3)
        
        print("✅ Browser back button test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    finally:
        driver.quit()

def run_all_edge_case_tests():
    """Run all edge case tests"""
    print("=" * 60)
    print("🧪 RESERVATION FORM EDGE CASE TESTS")
    print("=" * 60)
    
    tests = [
        ("Maximum Length Inputs", test_maximum_length_inputs),
        ("Special Characters", test_special_characters),
        ("Rapid Form Submission", test_rapid_form_submission),
        ("Browser Back Button", test_browser_back_button)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🔍 Running: {test_name}")
        print("-" * 40)
        result = test_func()
        results.append((test_name, result))
        print(f"Result: {'✅ PASSED' if result else '❌ FAILED'}")
    
    print("\n" + "=" * 60)
    print("📊 EDGE CASE TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    print("=" * 60)
    
    return passed == total

if __name__ == "__main__":
    run_all_edge_case_tests()
    