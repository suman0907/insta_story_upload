from WebApp.MyStory.views import *
from WebApp import create_app
import os




app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=65531)



