# Authentication API Testing Collection

## Overview

This collection contains automated tests for user authentication endpoints including login, registration, and logout functionality. All endpoints are tested with comprehensive validation scripts to ensure proper API behavior.

## API Information

**Base URL:** `https://reqres.in/api`

**Authentication:** API Key required in header
- Header Key: `x-api-key`
- Header Value: `reqres-free-v1`

## Collection Details

- **Collection ID:** e80a4c71-0f79-4f69-9bfe-e250f22d32ce
- **Exporter ID:** 49236971
- **Schema Version:** 2.1.0

## Endpoints

### 1. Login

Authenticates a user and initiates a session.

**Request:**
```
POST https://reqres.in/api/login/users2
```

**Headers:**
```
x-api-key: reqres-free-v1
Content-Type: application/json
```

**Body:**
```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```

**Test Scripts:**
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Successful POST request", function () {
    pm.expect(pm.response.code).to.be.oneOf([201, 202]);
});

pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});
```

**Expected Results:**
- Status code: 200, 201, or 202
- Response time: < 200ms

---

### 2. Register

Creates a new user account in the system.

**Request:**
```
POST https://reqres.in/api/register/users2
```

**Headers:**
```
x-api-key: reqres-free-v1
Content-Type: application/json
```

**Body:**
```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```

**Test Scripts:**
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});

pm.test("Successful POST request", function () {
    pm.expect(pm.response.code).to.be.oneOf([201, 202]);
});
```

**Expected Results:**
- Status code: 200, 201, or 202
- Response time: < 200ms

---

### 3. Logout

Ends the user's session and logs them out.

**Request:**
```
POST https://reqres.in/api/logout/users2
```

**Headers:**
```
x-api-key: reqres-free-v1
Content-Type: application/json
```

**Body:**
```json
''
```

**Test Scripts:**
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});

pm.test("Successful POST request", function () {
    pm.expect(pm.response.code).to.be.oneOf([201, 202]);
});
```

**Expected Results:**
- Status code: 200, 201, or 202
- Response time: < 200ms

---

## Test Coverage

All endpoints include automated tests for:

✅ **Status Code Validation** - Ensures correct HTTP status codes are returned

✅ **Response Time Performance** - Validates response time is under 200ms

✅ **Success Criteria** - Confirms POST requests return appropriate success codes (201, 202)

## Running the Tests

1. Import this collection into Postman
2. Ensure the API key is configured in headers
3. Run the entire collection or individual requests
4. View test results in the Postman Test Results tab

## Notes

- All endpoints use POST method for authentication operations
- Empty body is sent for logout endpoint
- All requests include performance testing (< 200ms response time)
- Tests validate both status codes and response times

---

**Created by:** Gvantsa Chakvetadze  
**Workspace:** Gvantsa Chakvetadze's Workspace




# API Testing Collection

## Overview

This is my first Postman collection for API testing and development. This collection demonstrates various HTTP methods and API testing scenarios using the ReqRes API.

Collections are used to:
- Group related requests
- Test APIs in real-world scenarios
- Document and share requests

## API Information

**Base URL:** `https://reqres.in/api`

**Authentication:** API Key required in header
- Header Key: `x-api-key`
- Header Value: `reqres-free-v1`

## Collection Details

- **Collection ID:** a0980609-3340-44e7-ac19-8e6c49f3646b
- **Exporter ID:** 49236971
- **Schema Version:** 2.1.0

## Endpoints

### 1. Get Users (GET)

Retrieves a list of users from the API.

**Request:**
```
GET https://reqres.in/api/users
```

**Headers:**
```
x-api-key: reqres-free-v1
```

---

### 2. Create User - Negative Test (POST)

Tests API behavior when required fields are missing (negative test case).

**Request:**
```
POST https://reqres.in/api/users
```

**Headers:**
```
x-api-key: reqres-free-v1
```

**Test Script:**
```javascript
// Negative test: Expect failure when required fields are missing
pm.test("Should return error for missing required fields", function () {
    pm.expect(pm.response.code).to.be.oneOf([400, 422]);
    // Optionally, check for error message in the response
    const responseBody = pm.response.text();
    pm.expect(responseBody).to.include("error");
});
```

**Expected Results:**
- Response code: 400 or 422
- Response body should include "error" message

---

### 3. Update User (PUT)

Updates an existing user's information.

**Request:**
```
PUT https://reqres.in/api/user/112
```

**Headers:**
```
x-api-key: reqres-free-v1
Content-Type: application/json
```

**Body:**
```json
{
  "firstName": "Gvantsa",
  "lastName": "Updated"
}
```

---

### 4. Delete User (DELETE)

Deletes a user from the system.

**Request:**
```
DELETE https://reqres.in/api/users/112
```

**Headers:**
```
x-api-key: reqres-free-v1
```

---

### 5. Create/Update Full User Profile (PUT)

Creates or updates a complete user profile with all fields.

**Request:**
```
PUT https://reqres.in/api/users
```

**Headers:**
```
x-api-key: reqres-free-v1
Content-Type: application/json
```

**Body:**
```json
{
  "id": 101,
  "firstName": "Gvantsa",
  "lastName": "Tester",
  "email": "gvantsa.tester@example.com",
  "password": "Password123!",
  "role": "admin"
}
```

---

## Resources

- [Postman Collections Documentation](https://learning.postman.com/docs/collections/collections-overview/)
- [ReqRes API Documentation](https://reqres.in/)

## Notes

- This collection uses the free ReqRes API for testing purposes
- All requests include the required API key header
- User ID 112 is used as an example in update/delete operations
- User ID 101 is used in the full profile creation request

---

**Created by:** Gvantsa Chakvetadze  
**Workspace:** Gvantsa Chakvetadze's Workspace