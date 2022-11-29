# JUSTIFICATION FOR DESIGN DECISIONS
Due to the nature of the "https://www.aerlingus.com/" site i decided to opt for a REST api approach. Initially i had planned to use selenium to automate the scraping process, however i encoutered a lot of issues with captcha mechanisms. Hence, this prompted me to check for the presence of an api. Once i was able to find the api i decided to make requests to specific endpoints which would enable me retrieve the information which was required. I opted to make use of the Flask framework as it is quite light weight and would enable me set up the endpoints i needed quickly

# FURTHER PLANS IF MORE TIME IS TO BE SPENT
If i am to spend more time on this i would definitely look for more measures to handle the captcha issues. Furhtermore i would also try to prevent the 403 error which often occurs when requests are made to the api which provides airport codes. Perhaps i would try switching useragents on each request. Another feature i would try to implement is to have a list of available destinations for each airport available to the user. This would enable the user to have an idea for which origin and destination airports can be used when making a request. 
 
# HOW TO RUN THIS CODE
To run this code simply change directoy into this folder in your prefered terminal of choice(CMD or BASH) and simply install the requirements using the command "pip install -r requirements.txt". This installs "flask" as well as other dependencies that come with the framework.

# STARTING THE SERVER
To start the server simply run the command "python main.py"(on WINDOWS) or "python3 main.py"(on MAC) on your terminal. The server should start providing you with the given URL "http://127.0.0.1:5000/" to start making requests.

# MAKING REQUESTS
To make requests please refer to the api documentation: https://documenter.getpostman.com/view/11891675/2s8YszN9pU

# RUNNING TESTS
To run tests make sure the server is running and run "python main_tests.py". If using MAC, please use "python3".

# DOCKERHUB REPO
* efemp/flight_api