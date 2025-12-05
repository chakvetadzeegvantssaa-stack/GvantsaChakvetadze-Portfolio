# QA Test Checklists



### TS-BR-001: Images Missing Alt Text
- [ ] Website is accessible
- [ ] Developer tools or accessibility checker is ready
- [ ] Open website and navigate pages
- [ ] Inspect all image elements
- [ ] Check that each image has descriptive alt text
- [ ] No image has empty or missing alt attribute

### TS-BR-002: Footer Email Button
- [ ] User is on footer section
- [ ] Default email client configured
- [ ] Click email button/link
- [ ] Verify email client opens
- [ ] Verify correct recipient email prefilled

### TS-BR-003: Crisp JSON Error
- [ ] Crisp chat widget active
- [ ] Developer/network tools available
- [ ] Trigger Crisp chat load
- [ ] Simulate or monitor invalid/empty JSON response
- [ ] Check no UI errors or crashes
- [ ] Console logs show error but site functions normally
- [ ] Chat widget retries or fails gracefully

---

## Pop-Up Feature

### TS-POP-001: Pop-Up Display
- [ ] User on webpage with pop-up trigger
- [ ] Click trigger button/link
- [ ] Verify pop-up appears

### TS-POP-002: Pop-Up Close
- [ ] Pop-up open
- [ ] Click close (X) button
- [ ] Click outside pop-up
- [ ] Verify pop-up closes and page returns to normal

### TS-POP-003: Data Persistence
- [ ] Enter data in pop-up form
- [ ] Close pop-up
- [ ] Reopen pop-up
- [ ] Verify entered data remains

### TS-POP-004: Data Reset
- [ ] Enter data in pop-up form
- [ ] Close pop-up
- [ ] Reopen pop-up
- [ ] Verify all fields are empty

### TS-POP-005: Mandatory Fields Validation
- [ ] Open pop-up form
- [ ] Leave mandatory fields empty
- [ ] Click Submit
- [ ] Verify error messages appear
- [ ] Verify form is not submitted

