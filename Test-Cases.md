# [Admin] Pop-Up Manager → Create New Pop-Up  
**Test Case Suite:** Functional and Validation Scenarios  
**Author:** QA Manual Tester  
**Date:** 2025-11-13  
**Application:** DressUp  
**Module:** Admin Panel → Pop-Up Manager  

---

## TC001 — Open Pop-Up Manager List

**Description:**  
Verify that clicking “Pop-Up Manager” opens a list of all existing Pop-Ups showing Name, Delivery Method, Payment Method, and Status.

**Precondition:**  
Admin is logged in and Pop-Up Manager menu is accessible.

**Test Steps and Expected Results:**  
1. Navigate to Admin Panel → Pop-Up Manager  
   - **Expected Result:** Admin panel loads and the Pop-Up Manager menu is visible.  

2. Click “Pop-Up Manager”  
   - **Expected Result:** A list of existing Pop-Ups is displayed with Name, Delivery Method, Payment Method, and Status columns.  

**Postcondition:**  
Pop-Up list is displayed and ready for further actions.  

**Priority:** High  

---

## TC002 — Search Existing Pop-Ups

**Description:**  
Verify that the search box returns correct Pop-Ups when a keyword is entered.

**Precondition:**  
At least one Pop-Up exists; Admin is logged in.

**Test Steps and Expected Results:**  
1. Enter a keyword in the search box.  
   - **Expected Result:** Keyword is accepted without any error.  

2. Click the “Search” button.  
   - **Expected Result:** Only Pop-Ups matching the entered keyword are displayed.  

**Postcondition:**  
Filtered Pop-Up list is visible.  

**Priority:** Medium  

---

## TC003 — Filter Pop-Ups

**Description:**  
Verify that Pop-Ups can be filtered by Status, Delivery Method, or Payment Method.

**Precondition:**  
Multiple Pop-Ups exist; Admin is logged in.

**Test Steps and Expected Results:**  
1. Click the “Filter” button.  
   - **Expected Result:** Filter options are displayed.  

2. Select filter criteria (Status, Delivery Method, or Payment Method).  
   - **Expected Result:** Selected criteria are highlighted and accepted.  

3. Click “Apply Filter.”  
   - **Expected Result:** Pop-Up list updates and shows only records matching the selected filter.  

**Postcondition:**  
Filtered Pop-Up list is displayed.  

**Priority:** Medium  

---

## TC004 — Edit Existing Pop-Up

**Description:**  
Verify that the admin can edit an existing Pop-Up and the changes are saved successfully.

**Precondition:**  
At least one Pop-Up exists; Admin is logged in.

**Test Steps and Expected Results:**  
1. Click the “Edit” icon next to an existing Pop-Up.  
   - **Expected Result:** Edit form opens pre-filled with the current Pop-Up data.  

2. Modify Name, Description, or Trigger fields.  
   - **Expected Result:** Changes are accepted without validation errors.  

3. Click “Save.”  
   - **Expected Result:** Pop-Up is updated successfully and changes are visible in the list.  

**Postcondition:**  
Pop-Up data is updated in the database.  

**Priority:** High  

---

## TC005 — Create New Pop-Up (Georgian Language)

**Description:**  
Verify that the admin can create a new Pop-Up in Georgian language with all required fields, triggers, and Status set to ON.

**Precondition:**  
Admin is logged in and the Pop-Up Manager section is accessible.

**Test Steps and Expected Results:**  
1. Click “Create New Pop-Up.”  
   - **Expected Result:** A blank form opens with all required fields visible.  

2. Enter a Name (maximum 100 characters).  
   - **Expected Result:** Field accepts valid input without validation errors.  

3. Enter a Description (maximum 1000 characters).  
   - **Expected Result:** Input is accepted; unsafe HTML or scripts are sanitized.  

4. Select at least one Delivery Method.  
   - **Expected Result:** Selected method is highlighted and accepted.  

5. Select at least one Payment Method.  
   - **Expected Result:** Selected method is highlighted and accepted.  

6. Ensure Status is set to ON.  
   - **Expected Result:** Pop-Up will be active after saving.  

7. Click “Save.”  
   - **Expected Result:** Pop-Up is saved successfully and appears in the Pop-Up list with correct details.  

**Postcondition:**  
New Pop-Up is saved in the database, visible in the list, and active.  

**Priority:** High  
