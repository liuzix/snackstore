# Snackstore
This is Project 1 for COMS 4111.
## Deployment
- You need to install docker and docker-compose on your machine.
- Run "docker-compose up"
- Access the web app at http://localhost/

## Development environment

    pip3 install gunicorn                                                                                                                 
    pip3 install flask                                                                                                                    
    pip3 install sqlalchemy                                                                                                               
    pip3 install simplejson                                                                                                               
    pip3 install psycopg2
    cd backend
    python3 main.py
    # in another terminal session
    cd frontend
    npm install
    npm run dev

You can then access the web app at http://localhost:8080/
