### BUILDING STUDENT MANAGEMENT SYSTEM USING DJANGO 3.0.2

    # > - https://github.com/hackstarsj/Python_Django_Blog_Project

#### 0. Initial commit

#### 1. Create django project and app

#### 2. Craete MySQL Db and Add Db Credentials to settings file

#### 3. Create and display demo page

    # > - 1. In settings create : MEDIA_URL, MEDIA_ROOT, STATIC_URL, and STATIC_ROOT
    # > - 2. Linking the Media and Static Path in root urls.py
    # > - 3. In root, create templates folder
    # > - 4. In templates create demo.html
    # > - 5. Set the tempates path in settings
    # > - 6. Creating a function in app/views.py for showing a demo page
    # > - 7. Set up the urls in root
    # > - 8. Run the server

    # > - modified:   README.md
    # > - new file:   app_student/__pycache__/views.cpython-37.pyc
    # > - modified:   app_student/views.py
    # > - modified:   core/__pycache__/settings.cpython-37.pyc
    # > - modified:   core/__pycache__/urls.cpython-37.pyc
    # > - modified:   core/settings.py
    # > - modified:   core/urls.py
    # > - new file:   templates/demo.html

#### 4. Add static files

    # > - 1. Download admin template
    # > - 2. Create static folder in app root
    # > - 3. Copy assets from admin template to static folder
    # > - 4. Load static assets (css, js, img) -> {% static 'path' %}

    # > - new file:   .gitignore
    # > - modified:   README.md
    # > - modified:   core/__pycache__/settings.cpython-37.pyc
    # > - modified:   core/__pycache__/urls.cpython-37.pyc
    # > - modified:   core/settings.py
    # > - modified:   core/urls.py
    # > - modified:   templates/demo.html
