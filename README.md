# pythonFlaskRestApi
implementation of REST APIs using flask in python


# Dependencies

$> pip3 install flask
$> pip3 install flask_restful

# Running your API-Service

$> python3.7 app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 419-639-766
 
 <running now>


# Testing
$> curl -X GET http://127.0.0.1:5000/user/Sachin_Tendulkar  <-- same link accessible via your browser as well
{
    "name": "Sachin_Tendulkar",
    "age": 43,
    "sport": "Cricket",
    "rank": 1
}
$> 

You can see this request pop up at your python3.7 app.py o.p:

127.0.0.1 - - [02/Oct/2019 19:48:14] "GET /user/Sachin_Tendulkar HTTP/1.1" 200 -
