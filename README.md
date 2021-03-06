### BUILDING STUDENT MANAGEMENT SYSTEM USING DJANGO 3.0.2

    # > - https://github.com/hackstarsj/Python_Django_Blog_Project

#### 0. Initial commit

#### 1. Create django project and app

    # > - 1. Create venv & activation
    # > - 2. Install django==3.0.2
    # > - 3. Install MySQL Client Library
    # > - 4. Create root dir
    # > - 5. Create django project
    # > - 6. Create django app
    # > - 7. Register the app to settings

#### 2. Craete MySQL Db and Add Db Credentials to settings file

    # > - 1. Create database

        K:\laragon\www
        λ mysql -u root -p
        Enter password: **** (root)

        mysql> CREATE DATABASE student_management_system;
        Query OK, 1 row affected (0.41 sec)

        mysql> CREATE USER 'student_management_system'@'localhost' identified by 'student_management_password';
        Query OK, 0 rows affected (0.40 sec)

        mysql> GRANT ALL PRIVILEGES ON *.* TO 'student_management_system'@'localhost';
        Query OK, 0 rows affected (0.24 sec)

        mysql>

    # > - 2. Configure the database in settings.py

#### 3. Create models

    # > - 1. Create (14) models

        # 1. CUSTOMUSER MODEL

        # 2. ADMINHOD MODEL

        # 3. STAFFS MODEL

        # 4. COURSES MODEL

        # 5. SUBJECTS MODEL

        # 6. STAFFS MODEL

        # 7. ATTENDANCE MODEL

        # 8. ATTENDANCEREPORT MODEL

        # 9. LEAVEREPORTSTUDENT MODEL

        # 10. LEAVEREPORTSTAFF MODEL

        # 11. FEEDBACKSTUDENT MODEL

        # 12. FEEDBACKSTAFF MODEL

        # 13. NOTIFICATIONSTUDENT MODEL

        # 14. NOTIFICATIONSTAFF MODEL

    # > - 2. Run migration

#### 4. Download admin template

    # > - 1. Open the link bellow to download the template
        htts://github.com/ColorlibHQ/AdminLTE/releases/tag/v3.0.2

#### 5. Create static files

    # > - 1. Create static folder in the root dir
    # > - 2. Copy and paste all the assets from the admin template
             to static folder
 
#### 6. Create media folder in root dir

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR , 'media')

#### 7. Linking the Static and Media path in project urls.py

    from django.conf.urls.static import static
    from core import settings

    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#### 8. Creating templates folder

    # > - 1. In root, create templates folder

#### 9. Display demo page

    # > - 1. In templates create demo.html 
             and copy & paste content of the index.html from template
    # > - 2. Creating a function in app/views.py for showing a demo page
    # > - 3. Set up the app's urls in root
    # > - 4. Include the app's urls in project's urls   
     # > - 5. Run the server


    # > - modified:   README.md
    # > - new file:   app_student/__pycache__/views.cpython-37.pyc
    # > - modified:   app_student/views.py
    # > - modified:   core/__pycache__/settings.cpython-37.pyc
    # > - modified:   core/__pycache__/urls.cpython-37.pyc
    # > - modified:   core/settings.py
    # > - modified:   core/urls.py
    # > - new file:   templates/demo.html

#### 10. Add static files

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

#### 11. Modify the db models

    # > - 1. Adding session start and end year for student in Students Class, so we can keep record
             seperate for each year
    # > - 2. Overriding the default django auth user and adding one more field in this model which
             user type user type 1: Admin, 2: Staff, 3: Student by creating CustomUser Class and passing
             AbstractUser so we can extend the default User
    # > - 3. Add One To One relationship between User Model and HOD Model and do the same with Student and Staff Model
    # > - 4. STEPS CREATE NEW TABLES:
            > - drop all tables in the db
            > - drop migrations folder from the app_student
            > - AUTH_USER_MODEL="app_student.CustomUser" in settings
            > - run: (env) λ python manage.py makemigrations app_student
            > - run: (env) λ python manage.py migrate (if it did not work, run this: (env) λ python manage.py migrate app_student) instead

#### 12. Modify the db models

        modified:   README.md                                                     
        new file:   app_student/__pycache__/__init__.cpython-38.pyc               
        new file:   app_student/__pycache__/admin.cpython-38.pyc                  
        modified:   app_student/__pycache__/models.cpython-37.pyc                 
        new file:   app_student/__pycache__/models.cpython-38.pyc                 
        new file:   app_student/__pycache__/views.cpython-38.pyc                  
        modified:   app_student/admin.py                                          
        modified:   app_student/migrations/0001_initial.py                        
        modified:   app_student/migrations/__pycache__/0001_initial.cpython-37.pyc
        new file:   app_student/migrations/__pycache__/0001_initial.cpython-38.pyc
        modified:   app_student/migrations/__pycache__/__init__.cpython-37.pyc    
        new file:   app_student/migrations/__pycache__/__init__.cpython-38.pyc    
        modified:   app_student/models.py                                         
        new file:   core/__pycache__/__init__.cpython-38.pyc                      
        modified:   core/__pycache__/settings.cpython-37.pyc                      
        new file:   core/__pycache__/settings.cpython-38.pyc                      
        new file:   core/__pycache__/urls.cpython-38.pyc                          
        new file:   core/__pycache__/wsgi.cpython-38.pyc                          
        modified:   core/settings.py                                              


#### 13. | VIDEO 4 | Templates & Add Staff

    Video 4 - Part 1 (0-11:17) : Home page, login, logout and redirect

        Git add and status 

        modified:   README.md
        new file:   app_student/HodViews.py
        new file:   app_student/__pycache__/HodViews.cpython-38.pyc
        modified:   app_student/__pycache__/views.cpython-38.pyc
        new file:   app_student/templates/hod_template/base_template.html
        new file:   app_student/templates/hod_template/content_header.html
        new file:   app_student/templates/hod_template/footer.html
        new file:   app_student/templates/hod_template/home_content.html
        new file:   app_student/templates/hod_template/notification_template.html
        new file:   app_student/templates/hod_template/sidebar_template.html
        modified:   app_student/views.py
        modified:   core/__pycache__/urls.cpython-38.pyc
        modified:   core/urls.py
        modified:   templates/login_page.html

    Video 4 - Part 2 (11:17-13:55) : Customizing Sidebar & Add All Necessary Menus

        Modified sidebar and added all necessary menus

        Git add and status 

            modified:   app_student/templates/hod_template/sidebar_template.html


    Video 4 - Part 3 (11:17-17:07) : Dynamic title and page title for Home and Add Staff pages

        Git add and status 

            modified:   README.md
            modified:   app_student/HodViews.py
            modified:   app_student/__pycache__/HodViews.cpython-38.pyc
            new file:   app_student/templates/hod_template/add_course_template.html
            new file:   app_student/templates/hod_template/add_staff_template.html
            new file:   app_student/templates/hod_template/add_student_template.html
            new file:   app_student/templates/hod_template/add_subject_template.html
            modified:   app_student/templates/hod_template/base_template.html
            renamed:    app_student/templates/hod_template/content_header.html -> app_student/templates/hod_template/content_header_TOREMOVE.html
            modified:   app_student/templates/hod_template/home_content.html
            new file:   app_student/templates/hod_template/manage_course_template.html
            new file:   app_student/templates/hod_template/manage_staff_template.html
            new file:   app_student/templates/hod_template/manage_student_template.html
            new file:   app_student/templates/hod_template/manage_subject_template.html
            modified:   app_student/templates/hod_template/sidebar_template.html
            new file:   app_student/templates/hod_template/staff_feedback_template.html
            new file:   app_student/templates/hod_template/staff_leave_template.html
            new file:   app_student/templates/hod_template/student_feedback.html
            new file:   app_student/templates/hod_template/student_leave.html
            new file:   app_student/templates/hod_template/view_attendance.html
            modified:   core/__pycache__/urls.cpython-38.pyc
            modified:   core/urls.py    

