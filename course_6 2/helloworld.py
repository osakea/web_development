# -*- coding: utf-8 -*-
""" The program uses flask and runs a web server. 
When requesting this server, it returns the text "Hello World!""""
from flask import Flask

def index():
    """ The function returns the text of a document """
    return 'Hello World!' 

# Creating a web application object:
app = Flask(__name__)   # parameter is the name of the module for a web app
                        # value __name__ contains the correct module name for the current file 
                        # it will contain the "__main__" value if the module is started directly,
                        # and another name if the module is connected

app.add_url_rule('/', 'index', index)   # creates a URL rule: 
                                        # when receiving a GET request to the '/' address on this site,
                                        # the index function will be run (specified as the third parameter)
                                        # and its value will be the response to the request.
                                        # The second parameter is endpoint -
                                        # it is a string that contains the name of this rule. 
                                        # Usually it is recommended to make endpoint identical to the function name, 
                                        # but in complex applications there may be several functions with the same name in different modules, 
                                        # and to distinguish between them within the entire website, you can specify different endpoint.

if __name__ == "__main__":
    # Starting the web server:
    app.run() 
