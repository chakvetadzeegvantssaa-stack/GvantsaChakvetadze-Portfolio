# 🧩 Test Scenarios

## TS-BR-001: Verify that all images have descriptive alt text
**Objective:** Ensure every image on the website includes an appropriate `alt` attribute for accessibility and SEO compliance.  
**Precondition:**  
- The website is accessible in a browser.  
- Developer tools or accessibility checker is available.  
**Steps:**  
1. Open the website home page and navigate through multiple pages.  
2. Inspect image elements using DevTools or an accessibility tool.  
3. Check whether each image contains a descriptive `alt` attribute.  
**Expected Result:**  
- Every image should include a relevant, descriptive `alt` text.  
- No image should have an empty or missing `alt` attribute.  

---

## TS-BR-002: Verify the functionality of the email button in the footer
**Objective:** Validate that the email button in the footer correctly redirects to the user’s default email client with the prefilled recipient address.  
**Precondition:**  
- User is on the website’s footer section.  
- A default email client (e.g., Outlook, Gmail) is configured on the device.  
**Steps:**  
1. Scroll to the footer section.  
2. Click on the email button/link.  
3. Observe whether a new email window opens with the correct “To” address.  
**Expected Result:**  
- Clicking the email button should open the default mail client.  
- The “To” field should contain the correct recipient email address.  

---

## TS-BR-003: Verify system behavior when Crisp integration returns an invalid JSON response
**Objective:** Ensure the application handles malformed or empty JSON responses from the Crisp chat integration without breaking the UI.  
**Precondition:**  
- Crisp chat widget is integrated and active.  
- Developer or network tools are accessible.  
**Steps:**  
1. Trigger the Crisp chat widget to load.  
2. Simulate or monitor a failed API response returning empty or invalid JSON.  
3. Observe browser console logs and page behavior.  
**Expected Result:**  
- No visible UI errors or crashes occur.  
- Console logs may record the error but should not interrupt normal site functionality.  
- The chat widget either retries the request or fails gracefully.  

---

# 🧪 Pop-Up Feature Test Scenarios

## TS-POP-001: Verify that the pop-up appears when triggered
**Objective:** Confirm that the pop-up is displayed when the trigger action (e.g., button click) is performed.  
**Precondition:**  
- User is on the webpage containing the pop-up trigger.  
**Steps:**  
1. Open the webpage.  
2. Click on the designated button or link that should open the pop-up.  
**Expected Result:**  
- Pop-up window appears on the screen and overlays the page content.  

---

## TS-POP-002: Verify that the pop-up can be closed successfully
**Objective:** Ensure that the user can close the pop-up via the close button (X) or by clicking outside the pop-up area.  
**Precondition:**  
- Pop-up is currently open.  
**Steps:**  
1. Click the close (“X”) button on the pop-up.  
2. Alternatively, click outside the pop-up area.  
**Expected Result:**  
- Pop-up window closes immediately.  
- Page returns to its normal state.  

---

## TS-POP-003: Verify that previously entered data remains after reopening the pop-up
**Objective:** Confirm that user-entered data remains visible when the pop-up is closed and reopened (if expected).  
**Precondition:**  
- User has entered valid data in the pop-up form.  
**Steps:**  
1. Open the pop-up and fill in all required fields.  
2. Close the pop-up.  
3. Reopen the pop-up.  
**Expected Result:**  
- Previously entered data should remain visible in the form fields (if the system is designed to save it).  

---

## TS-POP-004: Verify that the pop-up resets data after closing if not designed to store information
**Objective:** Ensure that form data inside the pop-up is cleared after closing, if data persistence is not part of functionality.  
**Precondition:**  
- Pop-up with form fields is available.  
**Steps:**  
1. Open the pop-up and fill out the form.  
2. Close the pop-up window.  
3. Reopen the pop-up.  
**Expected Result:**  
- All fields are empty; no previous data is shown.  

---

## TS-POP-005: Verify that mandatory fields in the pop-up show validation errors when empty
**Objective:** Validate that the pop-up form correctly displays error messages when required fields are left blank.  
**Precondition:**  
- Pop-up form contains mandatory input fields.  
**Steps:**  
1. Open the pop-up form.  
2. Leave one or more mandatory fields empty.  
3. Click the “Submit” button.  
**Expected Result:**  
- Appropriate validation error messages appear near each empty field.  
- The form is not submitted until all required data is entered.  

