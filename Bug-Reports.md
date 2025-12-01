# QA Bug Reports – Portfolio

---

## 1. Images Missing Alt Text

**Browser:** Google Chrome 140.0.7339.128 (64-bit)  
**OS:** Windows 10 Home  
**Device:** Dell Laptop, Inspiron 5537  
**Page:** Add option  
**Type:** Non-Functional  
**Priority:** Medium  
**Environment:** Production / Development / Beta  
**Reproducibility:** 100%

**Steps to Reproduce:**  
1. Open [example-store.com](https://example-store.com).  
2. Use the WAVE accessibility extension.

**Actual Result:**  
- Images do not have alt text, preventing screen readers from recognizing them.

**Expected Result:**  
- All images should have descriptive alt text for accessibility.

**Attachments:**  
- [example-link.com](https://example-link.com)

---

## 2. Footer Email Button Not Functioning

**Browser:** Google Chrome 140.0.7339.128 (64-bit)  
**OS:** Windows 10 Home  
**Device:** Dell Laptop, Inspiron 5537  
**Page:** Home Page  
**Type:** Functional  
**Priority:** Medium  
**Environment:** Production / Development / Beta  
**Reproducibility:** 100%

**Steps to Reproduce:**  
1. Open [example-store.com](https://example-store.com).  
2. Scroll down to the footer section.  
3. Click the email button.

**Actual Result:**  
- Clicking the button does nothing; it is non-functional.

**Expected Result:**  
- Clicking the button should open the email form or allow copying the address.

**Recommendation:**  
- If the button is intended to be clickable, it should trigger the email form. Otherwise, allow users to copy the email address directly.

**Attachments:**  
- [example-link.com](https://example-link.com)

---

## 3. SyntaxError During Crisp Chat Integration

**Browser:** Google Chrome 140.0.7339.128 (64-bit)  
**OS:** Windows 10 Home  
**Device:** Dell Laptop, Inspiron 5537  
**Page:** Home Page  
**Type:** Functional  
**Priority:** Medium  
**Environment:** Production / Development / Beta  
**Reproducibility:** 100%

**Steps to Reproduce:**  
1. Open [example-store.com](https://example-store.com).  
2. Open DevTools → Console.  
3. Observe `[Crisp] Failed to fetch data: SyntaxError`.

**Actual Result:**  
- The code calls `response.json()` on empty/non-JSON responses → SyntaxError → Crisp chat fails.

**Expected Result:**  
- Check `response.ok` and `content-type` before `response.json()` to prevent errors.

**Attachments:**  
- [example-link.com](https://example-link.com)

PIN Code Not Masked During Login

Browser: Google Chrome 140.0.7339.128 (64-bit)
OS: Windows 10 Home
Device: Dell Laptop, Inspiron 5537
Page: Login / PIN Verification
Type: Security / Functional
Priority: High
Environment: Production / Staging
Reproducibility: 100%

Steps to Reproduce:

Navigate to https://getbot.ai
.

Click Login or Sign In.

Enter a registered email and request a PIN.

Wait for the PIN to arrive in the email inbox.

Type the PIN into the verification field.

Observe the PIN digits displayed in plain text.

Actual Result:

All typed PIN digits are visible on-screen in plain text.

Sensitive authentication credentials are exposed, allowing shoulder surfing, screenshots, or screen recordings.

Expected Result:

PIN input should be masked (dots • or asterisks *) by default.

The actual digits should never be visible while typing.

Attachments:

(Optional screenshot of the input field, redacted for NDA compliance)

Suggested Fix:

Change the input field to type="password" or a secure masked input component.

Ensure plaintext PIN is never displayed in the UI.

Add automated tests to verify masking across browsers and devices.
