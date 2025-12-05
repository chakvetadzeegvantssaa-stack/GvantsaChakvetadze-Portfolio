# **Test Scenarios**

## **TS-BR-001 — Images Have Descriptive Alt Text**
**Objective:**  
Ensure all images include a relevant and descriptive `alt` attribute for accessibility and SEO.

**Precondition:**  
- Website is open in a browser  
- DevTools or accessibility checker is available  

**Test Scenario:**  
Verify that all images across the website contain descriptive alt text and no image is missing an `alt` attribute.

---

## **TS-BR-002 — Footer Email Button Functionality**
**Objective:**  
Ensure the footer email button opens the default email client with the correct recipient address.

**Precondition:**  
- User is on the footer section  
- A default email client is configured  

**Test Scenario:**  
Check that clicking the email button launches the default mail client and auto-fills the correct "To" address.

---

## **TS-BR-003 — Crisp Integration Handles Invalid JSON**
**Objective:**  
Ensure the UI remains stable when the Crisp widget returns malformed or empty JSON.

**Precondition:**  
- Crisp widget is active  
- Network/DevTools are available  

**Test Scenario:**  
Verify that invalid JSON responses from Crisp do not cause UI errors, crashes, or display issues.

---

# **Pop-Up Feature — Test Scenarios**

## **TS-POP-001 — Pop-Up Appears When Triggered**
**Objective:**  
Ensure the pop-up displays correctly when activated by the user.

**Precondition:**  
- User is on the page containing the pop-up trigger  

**Test Scenario:**  
Confirm that clicking the pop-up trigger (button/link) causes the pop-up to appear.

---

## **TS-POP-002 — Pop-Up Can Be Closed Successfully**
**Objective:**  
Ensure the user can close the pop-up via the close button or by clicking outside the modal.

**Precondition:**  
- Pop-up is currently open  

**Test Scenario:**  
Verify that the pop-up closes immediately and the page returns to normal after attempting to close it.

---

## **TS-POP-003 — Data Persists After Reopening Pop-Up**
**Objective:**  
Ensure user-entered data persists if the feature is intended to save input temporarily.

**Precondition:**  
- User has entered data in the pop-up form  

**Test Scenario:**  
Check that reopening the pop-up displays the previously entered data.

---

## **TS-POP-004 — Pop-Up Resets Data if Persistence is Not Expected**
**Objective:**  
Ensure the form clears all input when the pop-up is closed and reopened (if not designed to retain data).

**Precondition:**  
- Pop-up with form fields is available  

**Test Scenario:**  
Confirm that form fields are empty each time the pop-up is reopened.

---

## **TS-POP-005 — Mandatory Field Validation**
**Objective:**  
Ensure required fields display error messages when left blank.

**Precondition:**  
- Pop-up contains mandatory form fields  

**Test Scenario:**  
Verify that leaving required fields empty triggers validation errors and prevents submission.

- Pop-up form contains mandatory input fields.  
**Steps:**  
1. Open the pop-up form.  
2. Leave one or more mandatory fields empty.  
3. Click the “Submit” button.  
**Expected Result:**  
- Appropriate validation error messages appear near each empty field.  
- The form is not submitted until all required data is entered.  


