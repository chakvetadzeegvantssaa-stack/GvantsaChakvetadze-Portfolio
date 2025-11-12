"""
Test Suite: Invitation Creation Functionality
Author: Gvantsa Chakvetadze
Description: Automated tests for invitation management system
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class InvitationCreationTests(unittest.TestCase):
    """
    Test suite for invitation creation functionality.
    Tests both positive and negative scenarios.
    """

    @classmethod
    def setUpClass(cls):
        """Set up the WebDriver once for all tests."""
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)
        
        # Test Configuration
        cls.base_url = "https://example.com"
        cls.test_email = "testuser@example.com"
        cls.test_password = "SecurePassword123!"

    @classmethod
    def tearDownClass(cls):
        """Close the browser after all tests."""
        cls.driver.quit()

    def setUp(self):
        """Navigate to home page before each test."""
        self.driver.get(self.base_url)
        time.sleep(1)

    def login(self, email, password):
        """
        Helper method to perform login.
        
        Args:
            email (str): User email address
            password (str): User password
        """
        try:
            # Click sign in button
            sign_in_btn = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "sign in"))
            )
            sign_in_btn.click()

            # Enter email
            if email:
                email_field = self.wait.until(
                    EC.presence_of_element_located((By.ID, "email"))
                )
                email_field.clear()
                email_field.send_keys(email)

            # Enter password
            if password:
                password_field = self.driver.find_element(By.ID, "password")
                password_field.clear()
                password_field.send_keys(password)

            # Click login button
            login_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_btn.click()
            time.sleep(2)

        except TimeoutException:
            self.fail("Login elements not found within timeout period")

    def test_01_positive_create_invitation_successfully(self):
        """
        TC-001: Create invitation with valid data (Positive Test)
        
        Steps:
            1. Login with valid credentials
            2. Navigate to templates
            3. Select simple wedding template
            4. Fill in event details
            5. Submit invitation
            6. Verify success message
        
        Expected: Invitation created successfully with confirmation message
        """
        print("\n" + "="*60)
        print("TC-001: Create Invitation Successfully")
        print("="*60)

        # Step 1: Login
        print("Step 1: Logging in...")
        self.login(self.test_email, self.test_password)

        try:
            # Step 2: Navigate to templates
            print("Step 2: Navigating to templates...")
            templates_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "templates"))
            )
            templates_link.click()
            time.sleep(1)

            # Step 3: Select template
            print("Step 3: Selecting template...")
            wedding_template = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, 
                    "//div[contains(@class, 'template')]//span[text()='simple wedding']"))
            )
            wedding_template.click()
            time.sleep(1)

            # Step 4: Fill event details
            print("Step 4: Filling event details...")
            
            # Event title
            event_title = self.wait.until(
                EC.element_to_be_clickable((By.ID, "event-title"))
            )
            event_title.clear()
            event_title.send_keys("Birthday Party")
            
            # Event date
            event_date = self.driver.find_element(By.ID, "event-date")
            event_date.clear()
            event_date.send_keys("11/11/2026")
            
            # Event time
            event_time = self.driver.find_element(By.ID, "event-time")
            event_time.clear()
            event_time.send_keys("19:00")
            
            # Location
            location = self.driver.find_element(By.ID, "location")
            location.clear()
            location.send_keys("New York")
            time.sleep(1)

            # Step 5: Submit
            print("Step 5: Submitting invitation...")
            create_btn = self.driver.find_element(By.XPATH, 
                "//button[contains(text(), 'Create invitation')]")
            create_btn.click()
            time.sleep(2)

            # Step 6: Verify success
            print("Step 6: Verifying success message...")
            success_msg = self.wait.until(
                EC.presence_of_element_located((By.XPATH, 
                    "//*[contains(text(), 'Invitation created successfully')]"))
            )
            
            self.assertIsNotNone(success_msg)
            self.assertIn("Invitation created successfully", success_msg.text)
            
            print("✓ TEST PASSED: Invitation created successfully")

        except Exception as e:
            print(f"✗ TEST FAILED: {str(e)}")
            self.fail(f"Test failed: {str(e)}")

    def test_02_negative_login_validation_email_required(self):
        """
        TC-002: Email validation - Required field (Negative Test)
        
        Steps:
            1. Navigate to login page
            2. Leave email blank
            3. Enter password
            4. Click login
            5. Verify error message
        
        Expected: "Email is required" error message displayed
        """
        print("\n" + "="*60)
        print("TC-002: Email Validation Test")
        print("="*60)

        try:
            # Step 1: Click sign in
            print("Step 1: Navigating to login...")
            sign_in_btn = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "sign in"))
            )
            sign_in_btn.click()
            time.sleep(1)

            # Step 2: Leave email blank
            print("Step 2: Leaving email blank...")
            
            # Step 3: Enter password only
            print("Step 3: Entering password...")
            password_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "password"))
            )
            password_field.clear()
            password_field.send_keys("Password123!")

            # Step 4: Click login
            print("Step 4: Clicking login...")
            login_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_btn.click()
            time.sleep(2)

            # Step 5: Verify error message
            print("Step 5: Verifying error message...")
            error_msg = self.wait.until(
                EC.presence_of_element_located((By.XPATH, 
                    "//*[contains(text(), 'Email is required')]"))
            )
            
            self.assertIsNotNone(error_msg)
            self.assertIn("Email is required", error_msg.text)
            
            print("✓ TEST PASSED: Validation error displayed correctly")

        except Exception as e:
            print(f"✗ TEST FAILED: {str(e)}")
            self.fail(f"Test failed: {str(e)}")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("Starting Test Execution")
    print("="*60)
    unittest.main(verbosity=2)