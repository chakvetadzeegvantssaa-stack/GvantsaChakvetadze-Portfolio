{
	"info": {
		"_postman_id": "a0980609-3340-44e7-ac19-8e6c49f3646b",
		"name": "1st assignment",
		"description": "### Welcome to Postman! This is your first collection. \n\nCollections are your starting point for building and testing APIs. You can use this one to:\n\n• Group related requests\n• Test your API in real-world scenarios\n• Document and share your requests\n\nUpdate the name and overview whenever you’re ready to make it yours.\n\n[Learn more about Postman Collections.](https://learning.postman.com/docs/collections/collections-overview/)",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "49236971",
		"_collection_link": "https://chakvetadzeegvantssaa-3075898.postman.co/workspace/Gvantssaa-Chakvetadzee's-Worksp~d89bb14e-ebd4-45b3-8159-11bd6b828df4/collection/49236971-a0980609-3340-44e7-ac19-8e6c49f3646b?action=share&source=collection_link&creator=49236971"
	},
	"item": [
		{
			"name": "New Request",
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "x-api-key",
						"value": "reqres-free-v1",
						"type": "text"
					}
				],
				"url": {
					"raw": "https://reqres.in/api/users",
					"protocol": "https",
					"host": [
						"reqres",
						"in"
					],
					"path": [
						"api",
						"users"
					]
				}
			},
			"response": []
		},
		{
			"name": "New Request",
			"event": [
				{
					"listen": "test",
					"script": {
						"exec": [
							"// Negative test: Expect failure when required fields are missing\r",
							"pm.test(\"Should return error for missing required fields\", function () {\r",
							"    pm.expect(pm.response.code).to.be.oneOf([400, 422]);\r",
							"    // Optionally, check for error message in the response\r",
							"    const responseBody = pm.response.text();\r",
							"    pm.expect(responseBody).to.include(\"error\");\r",
							"});"
						],
						"type": "text/javascript",
						"packages": {},
						"requests": {}
					}
				}
			],
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "x-api-key",
						"value": "reqres-free-v1",
						"type": "text"
					}
				],
				"url": {
					"raw": "https://reqres.in/api/users",
					"protocol": "https",
					"host": [
						"reqres",
						"in"
					],
					"path": [
						"api",
						"users"
					]
				}
			},
			"response": []
		},
		{
			"name": "New Request",
			"request": {
				"method": "PUT",
				"header": [
					{
						"key": "x-api-key",
						"value": "reqres-free-v1",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"firstName\": \"Gvantsa\",\r\n  \"lastName\": \"Updated\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://reqres.in/api/user/112",
					"protocol": "https",
					"host": [
						"reqres",
						"in"
					],
					"path": [
						"api",
						"user",
						"112"
					]
				}
			},
			"response": []
		},
		{
			"name": "New Request",
			"request": {
				"method": "DELETE",
				"header": [
					{
						"key": "x-api-key",
						"value": "reqres-free-v1",
						"type": "text"
					}
				],
				"url": {
					"raw": "https://reqres.in/api/users/112",
					"protocol": "https",
					"host": [
						"reqres",
						"in"
					],
					"path": [
						"api",
						"users",
						"112"
					]
				}
			},
			"response": []
		},
		{
			"name": "https://reqres.in/api/users",
			"request": {
				"method": "PUT",
				"header": [
					{
						"key": "x-api-key",
						"value": "reqres-free-v1",
						"type": "text"
					},
					{
						"key": "",
						"value": "",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"id\": 101,\r\n  \"firstName\": \"Gvantsa\",\r\n  \"lastName\": \"Tester\",\r\n  \"email\": \"gvantsa.tester@example.com\",\r\n  \"password\": \"Password123!\",\r\n  \"role\": \"admin\"\r\n}\r\n\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://reqres.in/api/users",
					"protocol": "https",
					"host": [
						"reqres",
						"in"
					],
					"path": [
						"api",
						"users"
					]
				}
			},
			"response": []
		}
	]
}






{
	"info": {
		"_postman_id": "e80a4c71-0f79-4f69-9bfe-e250f22d32ce",
		"name": "2nd assignment",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "49236971",
		"_collection_link": "https://chakvetadzeegvantssaa-3075898.postman.co/workspace/Gvantssaa-Chakvetadzee's-Worksp~d89bb14e-ebd4-45b3-8159-11bd6b828df4/collection/49236971-e80a4c71-0f79-4f69-9bfe-e250f22d32ce?action=share&source=collection_link&creator=49236971"
	},
	"item": [
		{
			"name": "login",
			"event": [
				{
					"listen": "test",
					"script": {
						"exec": [
							"pm.test(\"Status code is 200\", function () {\r",
							"pm.test(\"Successful POST request\", function () {\r",
							"    pm.expect(pm.response.code).to.be.oneOf([201,202]);\r",
							"});\r",
							"pm.test(\"Response time is less than 200ms\", function () {\r",
							"    pm.expect(pm.response.responseTime).to.be.below(200);\r",
							"});\r",
							"    pm.response.to.have.status(200);\r",
							"});"
						],
						"type": "text/javascript",
						"packages": {},
						"requests": {}
					}
				}
			],
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "x-api-key",
						"value": "reqres-free-v1",
						"type": "text"
					},
					{
						"key": "",
						"value": "",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"username\": \"string\",\r\n  \"email\": \"string\",\r\n  \"password\": \"string\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://reqres.in/api/login/users2",
					"protocol": "https",
					"host": [
						"reqres",
						"in"
					],
					"path": [
						"api",
						"login",
						"users2"
					]
				}
			},
			"response": []
		},
		{
			"name": "register",
			"event": [
				{
					"listen": "test",
					"script": {
						"exec": [
							"pm.test(\"Status code is 200\", function () {\r",
							"    pm.response.to.have.status(200);\r",
							"});\r",
							"pm.test(\"Response time is less than 200ms\", function () {\r",
							"    pm.expect(pm.response.responseTime).to.be.below(200);\r",
							"});\r",
							"pm.test(\"Successful POST request\", function () {\r",
							"    pm.expect(pm.response.code).to.be.oneOf([201, 202]);\r",
							"});"
						],
						"type": "text/javascript",
						"packages": {},
						"requests": {}
					}
				}
			],
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "x-api-key",
						"value": "reqres-free-v1",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"username\": \"string\",\r\n  \"email\": \"string\",\r\n  \"password\": \"string\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://reqres.in/api/register/users2",
					"protocol": "https",
					"host": [
						"reqres",
						"in"
					],
					"path": [
						"api",
						"register",
						"users2"
					]
				}
			},
			"response": []
		},
		{
			"name": "logout",
			"event": [
				{
					"listen": "test",
					"script": {
						"exec": [
							"pm.test(\"Status code is 200\", function () {\r",
							"    pm.response.to.have.status(200);\r",
							"});\r",
							"pm.test(\"Response time is less than 200ms\", function () {\r",
							"    pm.expect(pm.response.responseTime).to.be.below(200);\r",
							"});\r",
							"pm.test(\"Successful POST request\", function () {\r",
							"    pm.expect(pm.response.code).to.be.oneOf([201, 202]);\r",
							"});\r",
							""
						],
						"type": "text/javascript",
						"packages": {},
						"requests": {}
					}
				}
			],
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "x-api-key",
						"value": "reqres-free-v1",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "''",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "https://reqres.in/api/logout/users2",
					"protocol": "https",
					"host": [
						"reqres",
						"in"
					],
					"path": [
						"api",
						"logout",
						"users2"
					]
				}
			},
			"response": []
		}
	]
}