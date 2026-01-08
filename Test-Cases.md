
# Test Case Suite – Web Application

# TC006 – Verify Layout and Responsiveness of Chat Groups Section

## TestType ## 
Functional / UI

## Preconditions ##  
- User is logged in  
- User has access to the chat dashboard  

## Test Steps ##  
1. Navigate to the chat application (NDA placeholder)  
2. Log in with valid credentials  
3. Open the chat dashboard  
4. Verify the alignment of the Chat Groups list and the "+ Add" button  
5. Resize the browser window to different screen sizes  

## Expected Result ##  
- Chat Groups list and "+ Add" button remain properly aligned  
- Layout remains responsive across different window sizes  
- No UI elements overlap or become inaccessible  

## Priority ##  
Medium

## Severity ##  
Medium

---

# TC007 – Verify SQL Injection Protection in PIN Verification Field

## Test Type ##  
Security / Functional

## Preconditions ##  
- User is on the login page  
- User has a registered email address  
- User can receive a PIN via email  

## Test Steps ##  
1. Navigate to the login page (NDA placeholder)  
2. Enter a valid email address and request a PIN  
3. Receive the PIN via email  
4. In the PIN verification field, enter: 123' OR '1'='1  
5. Click Verify / Submit  

##Expected Result##  
- PIN verification fails  
- Input is treated as an invalid PIN  
- No system, database, or security errors are displayed  
- Application remains secure against SQL injection  

##Priority##  
High

##Severity##  
High

---

# TC008 – Verify Behavior When Network Fails During Chat Message Sending

##Test Type##  
Functional / Error Handling

##Preconditions##  
- User is logged in  
- User is composing a chat message  

##Test Steps##  
1. Start composing a chat message  
2. Simulate network failure (disconnect internet connection)  
3. Attempt to send the message  

##Expected Result##  
- User is notified about the network failure  
- Message is saved as a draft or queued for retry  
- No credits or resources are consumed  
- User receives clear feedback on connection status  

##Priority##  
High

##Severity##  
High

---

# Admin Panel – Pop-Up Manager

# TC001 – Open Pop-Up Manager List

##Description##  
Verify that clicking Pop-Up Manager displays a list of existing Pop-Ups.

##Preconditions##  
Admin is logged in and has access to the Admin Panel.

##Test Steps##  
1. Navigate to Admin Panel → Pop-Up Manager  
2. Click Pop-Up Manager  

##Expected Result##  
- List of Pop-Ups is displayed  
- Columns include Name, Delivery Method, Payment Method, and Status  

##Priority##  
High

---

# TC002 – Search Existing Pop-Ups

##Description##  
Verify search functionality returns correct Pop-Ups.

##Preconditions##  
- Admin is logged in  
- At least one Pop-Up exists  

##Test Steps##  
1. Enter a keyword in the search field  
2. Click Search  

##Expected Result##  
- Only Pop-Ups matching the keyword are displayed  

##Priority##  
Medium

---

# TC003 – Filter Pop-Ups

##Description##  
Verify Pop-Ups can be filtered by available criteria.

##Preconditions##  
Multiple Pop-Ups exist.

##Test Steps##  
1. Click Filter  
2. Select filter criteria (Status, Delivery Method, or Payment Method)  
3. Click Apply Filter  

##Expected Result##  
- Pop-Up list updates according to selected filter criteria  

##Priority##  
Medium

---

# TC004 – Edit Existing Pop-Up

##Description##  
Verify admin can edit an existing Pop-Up successfully.

##Preconditions##  
At least one Pop-Up exists.

##Test Steps##  
1. Click Edit for an existing Pop-Up  
2. Modify editable fields  
3. Click Save  

##Expected Result##  
- Changes are saved successfully  
- Updated Pop-Up data is visible in the list  

##Priority##  
High

---

# TC005 – Create New Pop-Up (Georgian Language)

##Description##  
Verify admin can create a new Pop-Up in Georgian language.

##Preconditions##  
Admin is logged in and Pop-Up Manager is accessible.

##Test Steps##  
1. Click Create New Pop-Up  
2. Enter valid Name and Description  
3. Select at least one Delivery Method  
4. Select at least one Payment Method  
5. Set Status to ON  
6. Click Save  

##Expected Result##  
- New Pop-Up is created successfully  
- Pop-Up appears in the list with correct details  
- Status is active  

##Priority##  
High
will be active after saving.  

7. Click “Save.”  
   - **Expected Result:** Pop-Up is saved successfully and appears in the Pop-Up list with correct details.  

**Postcondition:**  
New Pop-Up is saved in the database, visible in the list, and active.  

**Priority:** High  







