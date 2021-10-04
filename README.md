Welcome, here we will be comparing three python web-frameworks: Django, Flask, and FAST API.

**Common Usecases:**

For the basics, here are the traditional 'main' use cases of each framework: 

**Django:** Great for using with a nice GUI, also for database dependency, and lastly, for when a simple but intuitive admin interface is required. 

**Flask:** perfect for simpler services and when a few API Endpoints are all thats required.

**FAST API:** When performance and development speeds are of focus, this newer framework is a common choice. 

**Pros and Cons:**
We begin with the pros and cons of each framework: 

**1. Django:** 

| Pros  | Cons |
| --- | --- |
| Efficient code structure, easy to add functionality  | Previous versions needs to be compatible with new releases  |
| Has DRF for REST Framework, easing web API builds  | Simple inheritance only i.e. no mixins  |

**2. Flask:** 

| Pros  | Cons |
| ------------- | ------------- |
| Beginner friendly, quick and easy to get started.  |  Use of modules can result in security breaches |
| Flexible and customizable, most parts can be changed.  | Handles requests in turns, so for multiple immedite requests it can be slow  |

**3. FAST API:**

| Pros  | Cons |
| ------------- | ------------- |
| Always validates data types, even in deeply nested JSON requests  |  Relatively new, lack of detailed external resources|
| Built on standards, JSON, OAuth 2.0, & OpenAPI  |  Everything tied to main file, making it very crowded|


**Major Factors:**

Next up, we look at important factors when choosing a framework:

**Ease of use & education:** Django is often known for having a high learning curve, however there are many resources avaible. On the other hand, FAST API is extremly easy to learn and get started with, however, has few online resources. This brings us to Flask which is not only easy and straightforward but also has extensive resources for support and learning. 

Summary (Ease of use & learning)

| Framework  | Ease of use | Resources |
| ------------- | ------------- | ------------- |
| Django  | :star: :star:  |  :star: :star: :star: :star: :star: |
| Flask |  :star: :star: :star: :star:  |  :star: :star: :star: :star:  |
| FAST API | :star: :star: :star: :star:  |  :star: :star:  |




**Serialization:** We now look at serialization, which is the process of taking complex querysets and converting them into native Python datatypes. The Django Rest Framework (DRF) provides a serializer class for controlling output of responses. For flask and FAST API there are options available but not as integrated as Django.

Summary (Serialization)

| Framework  | Ease of use | 
| ------------- | ------------- |
| Django  | :star: :star: :star: :star: :star: |  
| Flask |  :star: :star: :star: |  
| FAST API | :star: :star: :star:| 


**ORM (Object Relational Mapping):** Django has its own ORM which is simple but very powerful, however it only works with relational databases, so in other cases, you will need a different ORM and Django will cause pain for you. Flask on the other hand, does not provide anything built in, and forces you to chose, this can result in problems as there are more moving pieces that you have to deal with. FAST API seems to have the flask use case, however it seems to have fewer mentions of problems or errors with other ORM's such as SQLAlchemy or Peewee

Summary (ORM)

| Framework  | ORM | 
| ------------- | ------------- |
| Django  | :star: :star: :star: (5 :star: if Relational DB) |  
| Flask |  :star: :star: :star: |  
| FAST API | :star: :star: :star: :star:| 





**Performance:** Django, having the most functionalities is the slowest of the three, while flask is better in performace than Django, it trails behind FAST API, which based of the name is built around speed.

Summary (Performance)

| Framework  | Performance | 
| ------------- | ------------- |
| Django  | :star: :star: |  
| Flask |  :star: :star: :star: :star: |  
| FAST API | :star: :star: :star: :star: :star:| 




**Auto documentation:** FAST API has built in automatic interactive documentation, which is a huge plus. The same thing can be done with Flask and even Django using tools like Sphinx, however, this can can be buggy at times and also requires development.

Summary (Documentation)

| Framework  | Documentation | 
| ------------- | ------------- |
| Django  | :star: :star: |  
| Flask |  :star: :star: |  
| FAST API | :star: :star: :star: :star: :star:| 




**Database migrations:** Django is repeatedly mentioned as having an easy to use built in database migration tool, while this is something that flask and FAST API lack.

Summary (DB Migrations)

| Framework  | DB Migrations | 
| ------------- | ------------- |
| Django  | :star: :star: :star: :star:  |  
| Flask |  :star: :star: |  
| FAST API | :star: :star: | 


**Code structur and  flexibility:** Django provides more features, however is less flexible, while Flask and FAST API are very flixible

Summary (DB Migrations)

| Framework  | DB Migrations | 
| ------------- | ------------- |
| Django  | :star: :star:  |  
| Flask |  :star: :star: :star: :star: :star: |  
| FAST API | :star: :star: :star: :star:  | 


**Questions from previous huddle:** 

FAST API main file crowded: 

So yes this is true becuase everything needs to be tied inside of your the main file. 

For instance: 

```
app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
app.include_router(shops.router)
app.include_router(other.router)

@app.exception_handler(SomeException)
async def http_exception_handler(request: Request, exc: SomeException) -> PlainTextResponse:
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@app.exception_handler(SomeOtherException)
async def http_exception_handler(request: Request, exc: SomeOtherException) -> PlainTextResponse:
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
```

Now say we have 20 routers and 50 exceptions, we will have a very large file. 

But, with more research it turns out we can do something like this: 

```
app = FastAPI()

include_routers(app);
add_exception_handlers(app);
```

And have seperate files for include_routers and add_exception_handlers


What exactly is meant by Performance:

Does depend on server that is used, but generally when looking at responses per second and 20 queries per request, here are the results: 

| Framework  | # of responses | 
| ------------- | ------------- |
| Django  | 1643  |  
| Flask |  6542 |  
| FAST API | 12774  | 

Results were very similar accross sources, with a generall consensus favouring FAST API for when performance of requests is preferred, but it will vary across servers.


FAST API demo:

Create a more advanced app with FAST API to see size of main file, and testing/debugging. demo now


Django Migrations: 

As stated before, migrations are built in to Django and a major Pro for using it. 
Django has the following built-in functions: 

migrate, which is responsible for applying and unapplying migrations.
makemigrations, which is responsible for creating new migrations based on the changes you have made to your models.
sqlmigrate, which displays the SQL statements for a migration.
showmigrations, which lists a project’s migrations and their status.

PostgreSQL, MySQL, and SQLite are the most compatible DB's with Django migrations. Django can still work with many other supported ones.

Code structure and flexibility:

Flask and FAST API are very flixible, while Django sacrifices flexibility at the expense of having many built-in features (admin, migrations, etc)
The increased flexibility can result in more to maintain, and more setup time depending on the complexibity of the application. However, Django can seem more complicated at a 'hello world' level compared to flask and FAST API



**Running Apps:**

So, with everything in mind, you are now ready to make a decision, or would like to actually try using each of these frameworks, you can clone this repo which includes a HelloWorld app of each of the web-frameworks.

Here is how to run each of the web frameworks: 

**1. Django:** 

First go to the direcotry

```
$ cd django
```

Next, we will run the server

```
$ python manage.py runserver
```

Thats it! You can now visit http://127.0.0.1:8000/ to see the welcome page. 

**2. Flask:** 

First go to the direcotry

```
$ cd flask
```

Next, we will export the flask file

```
$ export FLASK_APP=helloWorld
```

Finally, we now run the app

```
$ flask run
```
Thats it! You can now visit http://127.0.0.1:5000/ to see the welcome page. 

**3. FAST API:** 

First go to the direcotry

```
$ cd fastAPI
```

Next, we will run the server

```
$ uvicorn main:app --reload
```
Thats it! You can now visit http://127.0.0.1:8000 to see the welcome page. 

