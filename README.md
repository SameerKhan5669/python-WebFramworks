this is what I remember:
Ease of use
Serialization
ORM
OpenAPI

Welcome, here we will be comparing three python web-frameworks: Django, Flask, and FAST API.

For the basics, here are the traditional 'main' use cases of each framework: 

Django: Great for using with a nice GUI, also for database dependency, and lastly, for when a simple but intuitive admin interface is required. 

Flask: perfect for simpler services and when a few API Endpoints are all thats required.

FAST API: When performance and development speeds are of focus, this newer framework is a common choice. 

We begin with the pros and cons of each framework: 

1. Django: 

| pros  | Cons |
| --- | --- |
| Efficient code structure, easy to add functionality  | Previous versions needs to be compatible with new releases  |
| Has DFR for REST Framework, easing web API builds  | Simple inheritance only i.e. no mixins  |

2. Flask: 

| pros  | Cons |
| ------------- | ------------- |
| Beginner friendly, quick and easy to get started.  |  Use of modules can result in security breaches |
| Flexible and customizable, most parts can be changed.  | Handles requests in turns, so for multiple immedite requests it can be slow  |

3. Flask: 

| pros  | Cons |
| ------------- | ------------- |
| Always validates data types, even in deeply nested JSON requests  |  Relatively new, lack of detailed external resources|
| Built on standards, JSON, OAuth 2.0, & OpenAPI  |  Everything tied to main file, making it very crowded|