# Django Unchained
## Run Project

```bash
pip install -r requirements.txt
python manage.py runserver
```

## Django

```bash
pip install django
```

```bash
PS C:\Users\At0m\Documents\Coding\Django Unchained> python -m django --version
5.2.8
```
Create new project:

```bash
PS C:\Users\At0m\Documents\Coding\Django Unchained> django-admin startproject Django_Unchained
```

`manage.py` - Command-line utility for Django project administration
`asgi.py` - Configuration for ASGI web servers to serve your project
`settings.py` - Contains all project settings and configuration
`urls.py` - URL declarations - maps URLs to views
`wsgi.py` - Configuration for Web Server Gateway Interface (WSGI) web servers to serve your project
`init.py` - Empty file that indicates this directory should be treated as a Python package

Run server:

```bash
python manage.py runserver
```

Create blog section:

```bash
python manage.py startapp blog
```

```bash
PS C:\Users\At0m\Documents\Coding\Django Unchained\Django_Unchained\blog> tree /F .
Folder PATH listing
Volume serial number is 0000009D FEB9:D921
C:\USERS\AT0M\DOCUMENTS\CODING\DJANGO UNCHAINED\DJANGO_UNCHAINED\BLOG
│   admin.py
│   apps.py
│   models.py
│   tests.py
│   views.py
│   __init__.py
│
└───migrations
        __init__.py
```

`admin.py` - Register models to manage them in Django's admin interface
`apps.py` - Configuration settings for this specific Django application
`models.py` - Define database models (tables) using Python classes
`tests.py` - Write test cases for your application's functionality
`views.py` - Handle web requests and return responses (controller logic)
`init.py` - Marks this directory as a Python package
`migrations/init.py` - Enables database migration tracking for model changes
## Django Routing Flow

URLs → urls.py → views.py → Template/Response

1. Project urls.py - Main URL router that includes app URLs
2. App urls.py - Defines URL patterns for specific app views
3. URL Pattern - `path('blog/', views.blog_view)` maps URL to view function
4. View Function - Processes request and returns HTTP response
5. Template - Renders HTML (optional) or returns JSON/data

```python
# urls.py
path('articles/', views.article_list),  # URL → View

# views.py  
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/articles.html', {'articles': articles})
```

`domain.com/articles/` → `urls.py` → `article_list()` → `articles.html`
## Django Templates Flow

Views → Templates → Rendered HTML

1. Template Configuration - Defined in `settings.py` `templates` DIRS
2. View Renders Template - 1render(request, 'template.html', context)`
3. Template Structure - HTML with Django Template Language (DTL)
4. Context Variables - Data passed from view to template `{{ variable }}`
5. Template Inheritance - Base template with `{% block content %}`

```python
# views.py
def article_list(request):
    return render(request, 'blog/articles.html', {'articles': articles})

# templates/blog/articles.html
{% extends 'base.html' %}
{% block content %}
  {% for article in articles %}
    <h2>{{ article.title }}</h2>
  {% endfor %}
{% endblock %}
```
## Create SuperUser 

First you need to create a database.

```bash
PS C:\Users\At0m\Documents\Coding\Django Unchained\Django_Unchained> python manage.py makemigrations
No changes detected
PS C:\Users\At0m\Documents\Coding\Django Unchained\Django_Unchained> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length.
```

Now auth table should exist.

```bash
PS C:\Users\At0m\Documents\Coding\Django Unchained\Django_Unchained> python manage.py createsuperuser
Username (leave blank to use 'at0m'): at0m
Email address: at0m@gmail.com
Password: at0m123
Password (again): at0m123
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```
Now you can access to `/admin`.
## Migrations and ORM

Django ORM is a powerful feature that allows you to interact with your database using Python objects instead of writing SQL queries directly.

Models are Python classes representing database tables.

```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
```

Basic ORM operations:

```python
# Create
user = User.objects.create(name="John", email="john@example.com", age=25)

# Or
user = User(name="Alice", email="alice@example.com", age=30)
user.save()

# Read
all_users = User.objects.all()
john = User.objects.get(name="John")  # Get single object
young_users = User.objects.filter(age__lt=30)  # Filter
ordered_users = User.objects.all().order_by('-created_at')

# Update
user = User.objects.get(name="John")
user.age = 26
user.save()

# Or bulk update
User.objects.filter(age__lt=25).update(age=25)

# Delete
user = User.objects.get(name="John")
user.delete()

# Or bulk delete
User.objects.filter(age__gt=100).delete()
```

Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

Create initial migration:

```bash
python manage.py makemigrations your_app_name
python manage.py migrate
```
When you modify models:

```python
# Add a new field to User model
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)  # New field
    is_active = models.BooleanField(default=True)  # New field
```

```bash
# Generate migration file
python manage.py makemigrations

# Apply migration
python manage.py migrate

# See what migrations would be applied
python manage.py makemigrations --dry-run

# See SQL that will be executed
python manage.py sqlmigrate your_app 0001

# List migration status
python manage.py showmigrations

# Migrate specific app
python manage.py migrate your_app

# Migrate to specific migration
python manage.py migrate your_app 0001

# Create empty migration (for complex operations)
python manage.py makemigrations --empty your_app
```

A foreign key is a database concept that creates a relationship between two tables. It's a field in one table that references the primary key of another table.

```bash
User table (Parent)
+----+----------+           ← id is PRIMARY KEY
| id | username |
+----+----------+
| 1  | john     |
| 2  | alice    |
+----+----------+
    ↑
    │
    └─── referenced by foreign keys

Post table (Child)  
+----+---------+------------+---------+
| id | title   | author_id  | content |   ← author_id is FOREIGN KEY
+----+---------+------------+---------+       (references User.id)
| 1  | "Hello" | 1          | "..."   |
| 2  | "Test"  | 1          | "..."   |
| 3  | "Hi"    | 2          | "..."   |
+----+---------+------------+---------+
```

You can view your migrations in SQL format too:

```bash
PS C:\Users\At0m\Documents\Coding\Django Unchained\Django_Unchained> python manage.py makemigrations
Migrations for 'blog':
  blog\migrations\0001_initial.py
    + Create model Post

PS C:\Users\At0m\Documents\Coding\Django Unchained\Django_Unchained> python manage.py sqlmigrate blog 0001 
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED); 
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;
```

We now need to update it:

```bash
PS C:\Users\At0m\Documents\Coding\Django Unchained\Django_Unchained> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK
```

Django Shell is where we can interact with our Python objects:

```bash
PS C:\Users\At0m\Documents\Coding\Django Unchained\Django_Unchained> python manage.py shell
7 objects imported automatically (use -v 2 for details).

Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: at0m>]>
```

We can see our Super User through query that we made.

We can also add posts:

```bash
>>> User.objects.all()   
<QuerySet [<User: at0m>]>
>>> user = User.objects.get(id=1)
>>> user
<User: at0m>
>>> post_1 = Post(title='Blog 1', content='First Post Content!', author=user) 
>>> post_1.save()    
>>> Post.objects.all()
<QuerySet [<Post: Post object (1)>]>
```
## Random Miscs that I sometimes forget

A sitemap is a file that provides information about the pages, videos, and other files on your website, and the relationships between them. Search engines like Google read this file to more intelligently crawl your site.

Pagination - Splitting content into multiple pages instead of one long page.

In HTML, the `<legend>` element provides a caption or title for the content within its parent `<fieldset>` element. It is primarily used within forms to group related form controls and give that group a descriptive label.

Check out [here](https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_legend).

`pt-3` is a Bootstrap spacing utility class that adds padding to the top of an element.

`ml-2` margin line.

`django-crispy-forms` is used to stylize forms.

```bash
pip install crispy-bootstrap4
```

Add in `settings.py`:

```python
INSTALLED_APPS = [
    # ... other apps
    'crispy_forms',
    'crispy_bootstrap4',  # Add this
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"  # Make sure this is set
```

In template:

```html
{% load crispy_forms_tags %}
<SNIP>
                {{ form|crispy }}
```

Fixed `base.html` for logout:

If you're using Django 5 or higher you will encounter the problem with accessing the 'logout' page directly from the browser. This is because the logout endpoint can be accessed now only using a 'POST' method, and accessing it via a URL is using the 'GET' method. One of the ways you can resolve this issue is to add this short code snippet instead of the standard link element in the navbar:

```html
<!-- Other -->
<!-- Navbar Right Side -->
<div class="navbar-nav">
    {% if user.is_authenticated %}
        <form action="{% url 'logout' %}" method="post" class="form-inline">
            {% csrf_token %}
            <button type="submit" class="btn btn-outline-light">Logout</button>
        </form>
        <a class="nav-item nav-link" href="#">{{ user.username }}</a>
    {% else %}
        <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
        <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
    {% endif %}
</div>
 <!-- Other -->
```
Fixed in `users/models.py`:

```python
# before: super().save()
super().save(*args, **kwargs)  
```
## Signals

Signals in Django are a way to allow decoupled applications to get notified when certain actions occur elsewhere in the application. They implement the observer pattern - where certain "senders" notify a set of "receivers" when something happens.

`signals.py`:

```python
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# This signal receiver listens for the post_save signal from the User model
# post_save signal is sent after a model instance is saved to the database
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Automatically create a Profile when a new User is created
    
    Args:
        sender: The model class that sent the signal (User)
        instance: The actual instance being saved
        created: Boolean - True if a new record was created, False if updated
        **kwargs: Additional keyword arguments
    """
    # Only create a profile if this is a NEW user (not an update)
    if created:
        # Create a Profile instance linked to the new User
        Profile.objects.create(user=instance)


# This signal receiver also listens for post_save from User model
# It runs every time a User is saved (both created and updated)
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Automatically save the user's profile when the user is saved
    
    Args:
        sender: The model class that sent the signal (User)
        instance: The actual User instance being saved
        **kwargs: Additional keyword arguments
    """
    # Save the profile associated with this user
    # This ensures the profile is updated whenever the user is updated
    instance.profile.save()
```
## Class-Based Views (CBV) 

Uses classes instead of functions:

```python
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# LIST VIEW - Show all posts
class PostListView(ListView):
    model = Post  # Which model to use
    template_name = 'blog/home.html'  # Template to render
    context_object_name = 'posts'  # Variable name in template
    ordering = ['-date_posted']  # Newest first
    paginate_by = 5  # Show 5 posts per page

# DETAIL VIEW - Show single post
class PostDetailView(DetailView):
    model = Post  # Automatically uses post_detail.html

# CREATE VIEW - Create new post (login required)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  # Fields in form
    
    # Set author to current user before saving
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UPDATE VIEW - Edit post (login + author only)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    # Check if current user is the author
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# DELETE VIEW - Delete post (login + author only)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # Redirect home after delete
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
```

URLs:

```python
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]
```

We were using function based view at start but later changed it. You can see in `blog/views.py`.
## Mixins

Mixins are reusable classes that provide extra functionality to other classes.

```python
# Mixin class
class LoggingMixin:
    def log(self, message):
        print(f"Log: {message}")

# Main class using the mixin
class MyView(LoggingMixin, ListView):
    def get(self, request):
        self.log("Page accessed")  # From mixin
        return super().get(request)
```
## Paginator

```bash
# Start Django shell
python manage.py shell

>>> from django.core.paginator import Paginator
>>> from blog.models import Post

# Check total posts
>>> posts = Post.objects.all()
>>> posts.count()
8

# Create paginator with 3 posts per page
>>> paginator = Paginator(posts, 3)
>>> paginator.num_pages
3
>>> paginator.page_range
range(1, 4)

# Get first page
>>> page1 = paginator.page(1)
>>> page1.number
1
>>> [post.title for post in page1]
['Post 1', 'Post 2', 'Post 3']
>>> page1.has_previous()
False
>>> page1.has_next()
True

# Get second page  
>>> page2 = paginator.page(2)
>>> page2.number
2
>>> [post.title for post in page2]
['Post 4', 'Post 5', 'Post 6']
>>> page2.has_previous()
True
>>> page2.has_next()
True

# Get third page
>>> page3 = paginator.page(3)
>>> page3.number
3
>>> [post.title for post in page3]
['Post 7', 'Post 8']
>>> page3.has_next()
False

# Safe method handles invalid pages
>>> page_safe = paginator.get_page(999)  # Non-existent page
>>> page_safe.number
3  # Returns last page instead of error

>>> page_safe = paginator.get_page('abc')  # Invalid input
>>> page_safe.number
1  # Returns first page

# Page navigation
>>> page2.next_page_number()
3
>>> page2.previous_page_number() 
1

# Page info
>>> page2.start_index()
4
>>> page2.end_index()
6
```
## Password Reset

Get App Password from [here](https://myaccount.google.com/apppasswords?rapt=AEjHL4N3aLxTD2seZMdpvSf9WN8Pvtw4iMqHIqlMzSj7_qLLWd763aE00Rv5lnUN5dG-wwiZSOaMePVz98_tCdjx4aZSWbcRSbYZOqhXUFnH6TD2SXjazA0).

For [docs](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbWNTel92S3BkZ0JyVTRZa1NsX3Brb0FfYkJhQXxBQ3Jtc0tuRDJvWkhIeDNRVjd3ckpwZEw5MXpnSGdqY1VTMzVQTVN0cjctMVluMkZTb3Rnby1uS0x4VEtqTnJjdXMzLTJMb0t1QkdjYU1reTlCUTZzU0VuV3o5MVpCNE1VYk1yWEpCUEE5UHlzQUw5Qi1oMFRYMA&q=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F2.1%2Ftopics%2Femail%2F%23configuring-email-for-development&v=-tyBEsHSv7w).

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'fatexashura@gmail.com'
EMAIL_HOST_PASSWORD = '<PASSWORD>'
```

For those that don't want to go the gmail route, go through a locally hosted dumb SMTP server.

1. Type this command into a separate shell --> `python -m smtpd -n -c DebuggingServer localhost:1025`
2. Add this line in `settings.py` --> `EMAIL_HOST = 'localhost'`
3. Add this line in `settings.py` --> `EMAIL_PORT = 1025`
4. Request password reset from within your browser

The password reset email will then populate within the shell running the SMTP server

[Video](https://www.youtube.com/watch?v=-s7e_Fy6NRU&t=45s).

---