## Json Web Token with Django and DRF
- The tests are run with HTTPie
### Getting the Access and Refresh token
- Create a superuser
http post http://127.0.0.1:8000/api/token/ username=name password=pass
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 438
Content-Type: application/json
Date: Fri, 17 Apr 2020 09:34:43 GMT
Server: WSGIServer/0.2 CPython/3.7.4
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg3MTE2MzgzLCJqdGkiOiJiOTI1ZWRhY2JmZDQ0MGE3YTEwZDU4MGM5ZGIyZmM5NSIsInVzZXJfaWQiOjF9.zH4ySbRaNzTrjrBfNnv7M9fVI4VlgeA0XCEiBC2h6_M",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4NzIwMjQ4MywianRpIjoiYWQ5ZWEwMDMxMGFlNDVkY2I1YTVjOGVkZDI2MDJiNzciLCJ1c2VyX2lkIjoxfQ.2PQhmCwsqpvo3UV1jF7ScHsbRw9IuRboPuGCLwrX_Ko"
}


### Refreshing the token
$ http post http://127.0.0.1:8000/api/token/refresh/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4NzE5NTMzMiwianRpIjoiYTcxZWU0ZTU0MTBjNDhiYWFiZGNlYTIzMTg1YTk3NDIiLCJ1c2VyX2lkIjoxfQ.dlEtw8vhp05P2OgO9msTYG0CXPpJcnLqfSwaz_fp98o"
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 218
Content-Type: application/json
Date: Fri, 17 Apr 2020 07:41:36 GMT
Server: WSGIServer/0.2 CPython/3.7.4
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg3MTA5NTk2LCJqdGkiOiI5MGM5YjhmYThmZTI0YjMwODlkOWQ2YTRhMzQxYTg2MSIsInVzZXJfaWQiOjF9.zEmoMDiXUfgtor39MeBHUaXnJ0Hj8hNWSxd3tw97lZ8"
}

### Calling hello endpoint with the valid token
http http://127.0.0.1:8000/api/hello/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg3MTA5NTk2LCJqdGkiOiI5MGM5YjhmYThmZTI0YjMwODlkOWQ2YTRhMzQxYTg2MSIsInVzZXJfaWQiOjF9.zEmoMDiXUfgtor39MeBHUaXnJ0Hj8hNWSxd3tw97lZ8"
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Length: 27
Content-Type: application/json
Date: Fri, 17 Apr 2020 07:42:01 GMT
Server: WSGIServer/0.2 CPython/3.7.4
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "message": " Response One"
}

