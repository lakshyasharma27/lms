
<h3>Create Virtual Environment</h3>
<ol>
    <li>python3 -m pip install --user virtualenv (if not installed)</li>
    <li>python3 -m venv venv</li>
    <li>source venv/bin/activate (to activate)</li>
    <li>deactivate (to deactivate)</li>
</ol>
<hr>

<h3>Clone the project</h3>
<ol>
    <li>git clone git@github.com:lakshyasharma27/lms.git</li>
</ol>
<hr>

<h3>Installed Python libraries</h3>
<ol>
    <li>
    pip freeze > requirements.txt (To add libraries) 
    </li>
    <li>
    pip install -r requirements/development.txt (install packages for development purpose)
    </li>
    <li>
    pip install -r requirements/development.txt (install packages for production purpose)
    </li>    
</ol>
<hr>

<h3>Migrations steps</h3>
<ol>
    <li>
    python manage.py makemigrations
    </li>
    <li>
    python manage.py migrate
    </li>    
</ol>
<hr>

<h3>Locally run server with development settings</h3>
<ol>
    <li>
    python manage.py runserver --settings=mysite.settings.development
    </li>
</ol>
<hr>



