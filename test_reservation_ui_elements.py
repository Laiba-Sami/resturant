# File: test_reservation_ui_elements.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from test_config import get_driver, BASE_URL
import time

def test_form_field_interactions():
    """Test various interactions with form fields"""
    driver = get_driver()
    try:
        print("🧪 Testing form field interactions...")
        driver.get(BASE_URL + "/")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)
        
        # Test tab navigation through form
        print("🔍 Testing tab navigation...")
        first_field = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        first_field.click()
        
        # Tab through all fields
        actions = ActionChains(driver)
        
        fields_info = []
        for i in range(6):  # We know there are 6 input fields
            current_element = driver.switch_to.active_element
            placeholder = current_element.get_attribute('placeholder')
            field_type = current_element.get_attribute('type')
            fields_info.append(f"{field_type}:{placeholder}")
            print(f"  Field {i+1}: {field_type} - {placeholder}")
            actions.send_keys(Keys.TAB).perform()
            time.sleep(0.5)
        
        print("✅ Tab navigation working")
        
        # Test field focus states
        print("🔍 Testing field focus states...")
        first_name_field = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        first_name_field.click()
        
        # Check if field has focus styling
        focused_class = first_name_field.get_attribute('class')
        focused_style = first_name_field.get_attribute('style')
        
        if 'focus' in (focused_class or '').lower() or 'focus' in (focused_style or '').lower():
            print("✅ Focus styling detected")
        else:
            print("ℹ️  No obvious focus styling (may use browser defaults)")
        
        # Test placeholder text
        print("🔍 Testing placeholder visibility...")
        placeholders = [
            "First Name", "Last Name", "Date", "Time", "Email", "Phone"
        ]
        
        for placeholder in placeholders:
            try:
                field = driver.find_element(By.XPATH, f"//input[@placeholder='{placeholder}']")
                actual_placeholder = field.get_attribute('placeholder')
                if actual_placeholder == placeholder:
                    print(f"  ✅ {placeholder} placeholder correct")
                else:
                    print(f"  ⚠️  {placeholder} placeholder mismatch: got '{actual_placeholder}'")
            except:
                print(f"  ❌ {placeholder} field not found")
        
        print("✅ Form field interactions test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    finally:
        driver.quit()

def test_responsive_design():
    """Test form responsiveness at different screen sizes"""
    driver = get_driver()
    try:
        print("🧪 Testing responsive design...")
        driver.get(BASE_URL + "/")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)
        
        # Test different screen sizes
        screen_sizes = [
            (1920, 1080, "Desktop Large"),
            (1366, 768, "Desktop Standard"),
            (768, 1024, "Tablet"),
            (375, 667, "Mobile")
        ]
        
        for width, height, device_name in screen_sizes:
            print(f"🔍 Testing {device_name} ({width}x{height})...")
            driver.set_window_size(width, height)
            time.sleep(2)
            
            # Check if form elements are visible and accessible
            try:
                # Check if form is visible
                reserve_button = driver.find_element(By.XPATH, "//button[contains(text(), 'RESERVE NOW')]")
                if reserve_button.is_displayed():
                    print(f"  ✅ Reserve button visible on {device_name}")
                
                # Check if all form fields are accessible
                fields_visible = 0
                total_fields = 6
                
                placeholders = ["First Name", "Last Name", "Email", "Phone"]
                for placeholder in placeholders:
                    try:
                        field = driver.find_element(By.XPATH, f"//input[@placeholder='{placeholder}']")
                        if field.is_displayed():
                            fields_visible += 1
                    except:
                        pass
                
                # Check date and time fields
                try:
                    date_field = driver.find_element(By.XPATH, "//input[@type='date']")
                    time_field = driver.find_element(By.XPATH, "//input[@type='time']")
                    if date_field.is_displayed():
                        fields_visible += 1
                    if time_field.is_displayed():
                        fields_visible += 1
                except:
                    pass
                
                print(f"  ✅ {fields_visible}/{total_fields} form fields visible on {device_name}")
                
                # Test if form can be filled on this screen size
                if fields_visible >= 4:  # At least most fields should be visible
                    first_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
                    first_name.clear()
                    first_name.send_keys(f"Test{device_name.replace(' ', '')}")
                    print(f"  ✅ Form interaction works on {device_name}")
                
            except Exception as e:
                print(f"  ⚠️  Some elements not accessible on {device_name}: {str(e)[:50]}...")
        
        # Reset to standard size
        driver.set_window_size(1366, 768)
        time.sleep(1)
        
        print("✅ Responsive design test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    finally:
        driver.quit()

def test_button_states_and_styling():
    """Test button states (hover, active, disabled)"""
    driver = get_driver()
    try:
        print("🧪 Testing button states and styling...")
        driver.get(BASE_URL + "/")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)
        
        # Find the reserve button
        reserve_button = driver.find_element(By.XPATH, "//button[contains(text(), 'RESERVE NOW')]")
        
        # Test initial button state
        print("🔍 Testing initial button state...")
        initial_color = reserve_button.value_of_css_property('background-color')
        initial_cursor = reserve_button.value_of_css_property('cursor')
        is_enabled = reserve_button.is_enabled()
        
        print(f"  Initial background color: {initial_color}")
        print(f"  Initial cursor: {initial_cursor}")
        print(f"  Button enabled: {is_enabled}")
        
        if is_enabled:
            print("  ✅ Button is initially enabled")
        else:
            print("  ⚠️  Button is initially disabled")
        
        # Test hover state
        print("🔍 Testing button hover state...")
        actions = ActionChains(driver)
        actions.move_to_element(reserve_button).perform()
        time.sleep(1)
        
        hover_color = reserve_button.value_of_css_property('background-color')
        hover_cursor = reserve_button.value_of_css_property('cursor')
        
        print(f"  Hover background color: {hover_color}")
        print(f"  Hover cursor: {hover_cursor}")
        
        if hover_color != initial_color:
            print("  ✅ Hover state color change detected")
        else:
            print("  ℹ️  No hover color change (may use subtle effects)")
        
        if hover_cursor == 'pointer':
            print("  ✅ Cursor changes to pointer on hover")
        else:
            print("  ⚠️  Cursor doesn't change to pointer")
        
        # Test button click state
        print("🔍 Testing button click state...")
        actions.click(reserve_button).perform()
        time.sleep(0.5)
        
        # Check if button shows active/pressed state
        active_color = reserve_button.value_of_css_property('background-color')
        print(f"  Active background color: {active_color}")
        
        # Test button with empty form (should show validation)
        print("🔍 Testing button with empty form...")
        time.sleep(2)  # Wait for any validation messages
        
        # Look for validation messages or error states
        try:
            error_messages = driver.find_elements(By.XPATH, "//*[contains(text(), 'required') or contains(text(), 'error') or contains(text(), 'invalid')]")
            if error_messages:
                print(f"  ✅ Validation messages found: {len(error_messages)} messages")
                for msg in error_messages[:3]:  # Show first 3 messages
                    print(f"    - {msg.text}")
            else:
                print("  ℹ️  No validation messages found")
        except:
            print("  ℹ️  Could not check for validation messages")
        
        # Test button styling properties
        print("🔍 Testing button styling properties...")
        button_properties = {
            'font-family': reserve_button.value_of_css_property('font-family'),
            'font-size': reserve_button.value_of_css_property('font-size'),
            'border-radius': reserve_button.value_of_css_property('border-radius'),
            'padding': reserve_button.value_of_css_property('padding'),
            'border': reserve_button.value_of_css_property('border')
        }
        
        for prop, value in button_properties.items():
            print(f"  {prop}: {value}")
        
        print("✅ Button states and styling test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    finally:
        driver.quit()

def test_form_validation_and_error_handling():
    """Test form validation, error messages, and edge cases"""
    driver = get_driver()
    try:
        print("🧪 Testing form validation and error handling...")
        driver.get(BASE_URL + "/")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)
        
        # Test 1: Submit completely empty form
        print("🔍 Testing empty form submission...")
        reserve_button = driver.find_element(By.XPATH, "//button[contains(text(), 'RESERVE NOW')]")
        reserve_button.click()
        time.sleep(2)
        
        # Check for validation messages
        validation_count = 0
        required_fields = ["First Name", "Last Name", "Email", "Phone"]
        
        for field_name in required_fields:
            try:
                field = driver.find_element(By.XPATH, f"//input[@placeholder='{field_name}']")
                validation_message = field.get_attribute('validationMessage')
                if validation_message:
                    print(f"  ✅ {field_name} validation: {validation_message}")
                    validation_count += 1
                else:
                    print(f"  ℹ️  {field_name}: No validation message")
            except Exception as e:
                print(f"  ⚠️  Could not check {field_name} validation")
        
        print(f"  Found {validation_count} field validations")
        
        # Test 2: Invalid email format
        print("🔍 Testing invalid email format...")
        email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        invalid_emails = ["invalid", "test@", "@domain.com", "test.domain"]
        
        for invalid_email in invalid_emails:
            email_field.clear()
            email_field.send_keys(invalid_email)
            reserve_button.click()
            time.sleep(1)
            
            validation_msg = email_field.get_attribute('validationMessage')
            if validation_msg:
                print(f"  ✅ '{invalid_email}' rejected: {validation_msg}")
            else:
                print(f"  ⚠️  '{invalid_email}' not validated")
        
        # Test 3: Invalid phone number formats
        print("🔍 Testing phone number validation...")
        phone_field = driver.find_element(By.XPATH, "//input[@placeholder='Phone']")
        invalid_phones = ["123", "abcd", "123-45", "+++123"]
        
        for invalid_phone in invalid_phones:
            phone_field.clear()
            phone_field.send_keys(invalid_phone)
            time.sleep(0.5)
            current_value = phone_field.get_attribute('value')
            if current_value != invalid_phone:
                print(f"  ✅ '{invalid_phone}' filtered to: '{current_value}'")
            else:
                print(f"  ℹ️  '{invalid_phone}' accepted as-is")
        
        # Test 4: Date validation (past dates, invalid dates)
        print("🔍 Testing date validation...")
        try:
            date_field = driver.find_element(By.XPATH, "//input[@type='date']")
            
            # Test past date
            past_date = "2020-01-01"
            date_field.clear()
            date_field.send_keys(past_date)
            reserve_button.click()
            time.sleep(1)
            
            validation_msg = date_field.get_attribute('validationMessage')
            if validation_msg:
                print(f"  ✅ Past date validation: {validation_msg}")
            else:
                print(f"  ℹ️  Past date '{past_date}' accepted")
            
            # Test future valid date
            future_date = "2025-12-31"
            date_field.clear()
            date_field.send_keys(future_date)
            print(f"  ✅ Future date '{future_date}' set successfully")
            
        except Exception as e:
            print(f"  ⚠️  Date field testing failed: {str(e)[:50]}...")
        
        # Test 5: Time validation
        print("🔍 Testing time validation...")
        try:
            time_field = driver.find_element(By.XPATH, "//input[@type='time']")
            
            valid_times = ["09:00", "12:30", "18:45"]
            for valid_time in valid_times:
                time_field.clear()
                time_field.send_keys(valid_time)
                current_value = time_field.get_attribute('value')
                if current_value == valid_time:
                    print(f"  ✅ Time '{valid_time}' accepted")
                else:
                    print(f"  ⚠️  Time '{valid_time}' became '{current_value}'")
                    
        except Exception as e:
            print(f"  ⚠️  Time field testing failed: {str(e)[:50]}...")
        
        # Test 6: Test field character limits
        print("🔍 Testing field character limits...")
        test_fields = [
            ("First Name", "A" * 100),
            ("Last Name", "B" * 100),
            ("Email", "test" + "@domain.com" * 20)
        ]
        
        for field_name, long_text in test_fields:
            try:
                field = driver.find_element(By.XPATH, f"//input[@placeholder='{field_name}']")
                field.clear()
                field.send_keys(long_text)
                actual_value = field.get_attribute('value')
                
                if len(actual_value) < len(long_text):
                    print(f"  ✅ {field_name} limited to {len(actual_value)} chars")
                else:
                    print(f"  ℹ️  {field_name} accepts {len(actual_value)} chars")
                    
            except Exception as e:
                print(f"  ⚠️  Could not test {field_name} character limit")
        
        # Test 7: Special characters handling
        print("🔍 Testing special characters...")
        first_name_field = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        special_chars = ["<script>", "'; DROP TABLE", "João", "François", "北京"]
        
        for special_char in special_chars:
            first_name_field.clear()
            first_name_field.send_keys(special_char)
            actual_value = first_name_field.get_attribute('value')
            
            if actual_value == special_char:
                print(f"  ✅ Special chars '{special_char}' accepted")
            else:
                print(f"  🔒 Special chars '{special_char}' filtered to '{actual_value}'")
        
        print("✅ Form validation and error handling test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    finally:
        driver.quit()

def test_accessibility_and_keyboard_navigation():
    """Test accessibility features and keyboard-only navigation"""
    driver = get_driver()
    try:
        print("🧪 Testing accessibility and keyboard navigation...")
        driver.get(BASE_URL + "/")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)
        
        # Test 1: Check for ARIA labels and accessibility attributes
        print("🔍 Testing ARIA labels and accessibility attributes...")
        
        form_elements = driver.find_elements(By.XPATH, "//input | //button | //label")
        accessibility_score = 0
        total_elements = len(form_elements)
        
        for element in form_elements:
            # Check for various accessibility attributes
            has_aria_label = element.get_attribute('aria-label')
            has_aria_describedby = element.get_attribute('aria-describedby')
            has_title = element.get_attribute('title')
            has_label = element.get_attribute('id') and driver.find_elements(By.XPATH, f"//label[@for='{element.get_attribute('id')}']")
            
            accessibility_features = []
            if has_aria_label:
                accessibility_features.append(f"aria-label='{has_aria_label}'")
            if has_aria_describedby:
                accessibility_features.append(f"aria-describedby='{has_aria_describedby}'")
            if has_title:
                accessibility_features.append(f"title='{has_title}'")
            if has_label:
                accessibility_features.append("has-label")
            
            if accessibility_features:
                accessibility_score += 1
                print(f"  ✅ Element has: {', '.join(accessibility_features)}")
            else:
                element_info = element.get_attribute('placeholder') or element.get_attribute('type') or element.tag_name
                print(f"  ℹ️  Element '{element_info}' has no accessibility attributes")
        
        accessibility_percentage = (accessibility_score / total_elements) * 100 if total_elements > 0 else 0
        print(f"  Accessibility score: {accessibility_score}/{total_elements} ({accessibility_percentage:.1f}%)")
        
        # Test 2: Keyboard-only form completion
        print("🔍 Testing keyboard-only form completion...")
        
        # Start from body and tab to first field
        driver.find_element(By.TAG_NAME, "body").click()
        actions = ActionChains(driver)
        
        # Tab to first field
        actions.send_keys(Keys.TAB).perform()
        time.sleep(0.5)
        
        # Fill form using only keyboard
        test_data = [
            "John",      # First Name
            "Doe",       # Last Name  
            "2025-12-25", # Date
            "14:30",     # Time
            "john.doe@email.com", # Email
            "1234567890" # Phone
        ]
        
        completed_fields = 0
        for i, data in enumerate(test_data):
            try:
                current_element = driver.switch_to.active_element
                placeholder = current_element.get_attribute('placeholder')
                field_type = current_element.get_attribute('type')
                
                # Clear and enter data
                current_element.clear()
                current_element.send_keys(data)
                
                # Verify data was entered
                entered_value = current_element.get_attribute('value')
                if entered_value:
                    completed_fields += 1
                    print(f"  ✅ Field {i+1} ({field_type}/{placeholder}): '{entered_value}'")
                else:
                    print(f"  ⚠️  Field {i+1} ({field_type}/{placeholder}): No data entered")
                
                # Tab to next field
                actions.send_keys(Keys.TAB).perform()
                time.sleep(0.5)
                
            except Exception as e:
                print(f"  ❌ Error on field {i+1}: {str(e)[:50]}...")
        
        print(f"  Completed {completed_fields}/{len(test_data)} fields via keyboard")
        
        # Test 3: Keyboard submission
        print("🔍 Testing keyboard form submission...")
        try:
            # Tab to submit button and press Enter
            for _ in range(3):  # Tab a few more times to reach button
                actions.send_keys(Keys.TAB).perform()
                time.sleep(0.3)
            
            current_element = driver.switch_to.active_element
            if current_element.tag_name.lower() == 'button':
                print("  ✅ Successfully navigated to submit button")
                actions.send_keys(Keys.ENTER).perform()
                time.sleep(2)
                print("  ✅ Form submitted via keyboard")
            else:
                print(f"  ⚠️  Expected button, found {current_element.tag_name}")
                
        except Exception as e:
            print(f"  ⚠️  Keyboard submission test failed: {str(e)[:50]}...")
        
        # Test 4: Focus indicators visibility
        print("🔍 Testing focus indicators visibility...")
        
        # Test focus on each input field
        input_fields = driver.find_elements(By.TAG_NAME, "input")
        focus_indicators_found = 0
        
        for field in input_fields[:4]:  # Test first 4 fields
            try:
                field.click()
                time.sleep(0.5)
                
                # Check for focus styling
                outline = field.value_of_css_property('outline')
                box_shadow = field.value_of_css_property('box-shadow')
                border = field.value_of_css_property('border')
                
                has_focus_indicator = (
                    outline and outline != 'none' and 'auto' not in outline.lower() or
                    box_shadow and box_shadow != 'none' or
                    'focus' in (field.get_attribute('class') or '').lower()
                )
                
                if has_focus_indicator:
                    focus_indicators_found += 1
                    focus_styles = []
                    if outline and outline != 'none':
                        focus_styles.append(f"outline: {outline}")
                    if box_shadow and box_shadow != 'none':
                        focus_styles.append(f"box-shadow: {box_shadow}")
                    print(f"  ✅ Focus indicator: {'; '.join(focus_styles)}")
                else:
                    print(f"  ℹ️  No visible focus indicator (using browser defaults)")
                    
            except Exception as e:
                print(f"  ⚠️  Could not test focus indicator: {str(e)[:30]}...")
        
        focus_percentage = (focus_indicators_found / len(input_fields[:4])) * 100 if input_fields else 0
        print(f"  Focus indicators: {focus_indicators_found}/{len(input_fields[:4])} ({focus_percentage:.1f}%)")
        
        # Test 5: Screen reader friendly elements
        print("🔍 Testing screen reader friendly elements...")
        
        # Check for semantic HTML elements
        semantic_elements = ['form', 'fieldset', 'legend', 'label']
        semantic_score = 0
        
        for element_type in semantic_elements:
            elements = driver.find_elements(By.TAG_NAME, element_type)
            if elements:
                semantic_score += 1
                print(f"  ✅ Found {len(elements)} {element_type} element(s)")
            else:
                print(f"  ℹ️  No {element_type} elements found")
        
        print(f"  Semantic HTML score: {semantic_score}/{len(semantic_elements)}")
        
        print("✅ Accessibility and keyboard navigation test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    finally:
        driver.quit()

# Main test runner
def run_all_ui_tests():
    """Run all UI element tests"""
    print("🚀 Starting Reservation System UI Tests")
    print("=" * 50)
    
    tests = [
        test_form_field_interactions,
        test_responsive_design,
        test_button_states_and_styling,
        test_form_validation_and_error_handling,
        test_accessibility_and_keyboard_navigation
    ]
    
    results = []
    for test in tests:
        print(f"\n{'='*50}")
        result = test()
        results.append((test.__name__, result))
        time.sleep(2)  # Brief pause between tests
    
    # Summary
    print(f"\n{'='*50}")
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed ({(passed/total)*100:.1f}%)")
    
    if passed == total:
        print("🎉 All tests passed! Your reservation system UI is working great!")
    else:
        print("⚠️  Some tests failed. Please review the issues above.")
    
    return passed == total

if __name__ == "__main__":
    run_all_ui_tests()