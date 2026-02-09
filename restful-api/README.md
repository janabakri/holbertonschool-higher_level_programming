RESTful API – Exercises (Holberton School)
This directory contains a set of small exercises to practice REST concepts, API consumption, and building simple APIs in Python.

Contents
Task 00: Basics of HTTP/HTTPS (concepts)
Task 01: Consume data from an API using command line tools (curl)
Task 02: Consume and process data from an API using Python (requests + CSV)
Task 03: Develop a simple API using Python http.server
Task 04: Develop a simple API using Flask
Task 05: API Security and Authentication (Basic Auth + JWT + RBAC)
0) Basics of HTTP/HTTPS (Concepts)
HTTP vs HTTPS
HTTP: Not encrypted. Data can be intercepted or modified by attackers.
HTTPS: HTTP over TLS/SSL providing:
Encryption (confidentiality)
Integrity (tamper detection)
Server authentication (certificate-based)
HTTP Request / Response Structure
Request

Request line: METHOD /path HTTP/1.1
Headers (e.g., Host, Accept, Content-Type, Authorization)
Optional Body (usually with POST/PUT/PATCH)
Response

Status line: HTTP/1.1 200 OK
Headers (e.g., Content-Type, Content-Length)
Optional Body (HTML/JSON/etc.)
Common Methods
GET: Retrieve data
POST: Create resource / submit data
PUT: Replace full resource
DELETE: Delete resource
Common Status Codes
200 OK: Request succeeded
201 Created: Resource created
400 Bad Request: Invalid request data
401 Unauthorized: Missing/invalid authentication
404 Not Found: Resource does not exist
1) Consume API using curl (JSONPlaceholder)
Verify curl:

curl --version
Author
jana bakri
