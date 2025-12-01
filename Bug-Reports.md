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


# QA Bug Report – Security Issue: PIN Code Not Masked During Login

**Type:** Security Vulnerability  
**Platform:** Web  
**Device:** Dell Laptop, Inspiron 5537, DESKTOP-0OJ9KTC  
**Operating System:** Windows 10 Home, Version 10.0.19045 Build 19045  
**Browser:** Google Chrome, Version 140.0.7339.128 (64-bit)  
**Environment:** Production / Development / Beta  
**Reproducibility:** 100%  

---

## **Preconditions**
- User is not logged in.  
- User has a valid email registered in the system.  
- User has access to their email inbox to receive the PIN code.  

---

## **Steps to Reproduce**
1. Navigate to [example-login.com](https://example-login.com) (placeholder for NDA).  
2. Click **"Login"** or **"Sign In"**.  
3. Enter a valid email address in the email field.  
4. Click **"Continue"** or **"Send PIN"**.  
5. Wait for the PIN code to arrive via email.  
6. Check the email and note the PIN code.  
7. Return to the login page and locate the PIN verification input field.  
8. Begin typing the PIN code.  
9. Observe the input as each digit is typed.  

---

## **Actual Result**
- The PIN code appears in plain text (e.g., `123456`) in the verification input field.  
- All digits are fully visible as they are typed.  
- The sensitive credential is exposed on screen, allowing anyone nearby to see and memorize it.  

---

## **Expected Result**
- The PIN code should be masked immediately upon entry (displayed as dots `••••••` or asterisks).  
- Each typed character should be replaced by a masking symbol.  
- The PIN code must never appear in plain text at any point.  
- This ensures protection against shoulder surfing, screen recording, or accidental screenshots.  

---

## **Impact**
- Exposing PIN codes creates a **security vulnerability**, as unauthorized users could access accounts by observing the screen.  
- Masking sensitive authentication input is a **standard security requirement** for login flows.  

---

## **Attachments**
- None (screenshots omitted for NDA compliance).


  # QA Bug Report – File Upload Without Network Connection

**Type:** Functional / UX Issue  
**Platform:** Web  
**Device:** Dell Laptop, Inspiron 5537, DESKTOP-0OJ9KTC  
**Operating System:** Windows 10 Home, Version 10.0.19045 Build 19045  
**Browser:** Google Chrome, Version 140.0.7339.128 (64-bit)  
**Environment:** Production / Development / Beta  
**Reproducibility:** 100% (Occurs every time network is interrupted during upload)

---

## **Preconditions**
- User is logged in.  
- User has a file ready to upload.  
- WiFi/network connection is turned OFF before attempting upload.  

---

## **Steps to Reproduce**
1. Turn OFF WiFi / disable network connection.  
2. Open [example-chat-app.com](https://example-chat-app.com) (placeholder for NDA).  
3. Navigate to the chat section.  
4. Attempt to upload a file (image, document, etc.).  
5. Observe any error messages or upload behavior.  
6. Turn WiFi back ON / restore network connection.  
7. Observe if the upload starts automatically.  

---

## **Actual Result**
- The system allows the upload attempt without showing an immediate error.  
- No indication that the network is disconnected.  
- Upload does not queue or resume automatically when connection is restored.  
- Upload appears stuck, with no way for the user to proceed.  

---

## **Expected Result**
- An immediate error message should display:  
  `"No network connection. Please check your internet and try again."`  
  **OR**  
- The upload should queue and start automatically when the network is restored.  
- Users should receive clear feedback about network status.  
- No credits or resources should be deducted for failed upload attempts.  

---

## **Impact**
- Users may think the file is uploaded successfully, leading to confusion or potential data loss.  
- Poor UX and lack of feedback reduces trust in the platform.  

---

## **Attachments**
- None (NDA-compliant).

