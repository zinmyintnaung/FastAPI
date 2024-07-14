## Create Virtual Environment

1. Inside the project folder, execute
   `python -m venv fastapienv`
2. Execute following code to start up the environment
   `fastapienv\Scripts\activate.bat`
3. Now we can see the packages install under this virtual enviroment
   `pip list`
4. Install the required package
   `pip install fastapi`
5. Install uvicorn webserver
   `pip install "uvicorn[standard]"`
6. To start up the webserver and reload the changes, execute
   `uvicorn filename:app --reload`
7. To stop the virtual environment, execute
   `deactivate`

### Project Three SQLite

1. In the project directory of the fastapienv, install sqlalchemy
   `pip install sqlalchemy`
2. For hashsing password, install passlib
   `pip install passlib`
3. For encryption, install bcrypt with version specify, it is important
   `pip install bcrypt==4.0.1`
4. For user input, we need to allow multipart from data
   `pip install multipart`
5. For JWT, install the jose cryptography library
   `pip install "python-jose[cryptography]"`
