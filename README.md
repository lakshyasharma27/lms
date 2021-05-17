
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
    pip install -r requirements/production.txt (install packages for production purpose)
    </li>    
</ol>
<hr>

<h3>Migrations steps</h3>
<p>For migrations and running the server trace to manage.py path</p>
<ol>
    <li>
    python manage.py makemigrations
    </li>
    <li>
    python manage.py migrate
    </li>    
</ol>
<hr>

<h3>To Temporarily set environment variables</h3>
<ol>
    <li>
    export $(cat ../config/.env.prod | xargs) [For prodiction variables]
    </li>
    <li>
    export $(cat ../config/.env.dev | xargs) [For development variables]
    </li>    
</ol>
<hr>



<h3>Locally run server with development or production settings</h3>
<ol>
    <li>
    python manage.py runserver --settings=mysite.settings.development
    </li>
    <li>
    python manage.py runserver --settings=mysite.settings.production (Need prod env variables)
    </li>    
</ol>
<hr>

<h3>Create Image and run the created image</h3>
<ol>
    <li>
        sudo docker-compose --env-file ./config/.env.dev build ( create the image with dev env variables)
    </li>
    <li>
    sudo docker-compose --env-file ./config/.env.dev up -d ( create the image with dev env variables)
    </li>    
</ol>
<p>
After running the container create an image and push that an image to docker hub
</p>
<hr>



