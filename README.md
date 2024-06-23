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
