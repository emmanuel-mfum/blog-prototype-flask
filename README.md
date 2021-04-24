# blog-prototype-flask
Prototype for a personal blog written using Python and the Flask framework

This project consists of a personal blog implemented using Flask. Key to it was a good grasp and comprehension of the basics
of setting of Flask app, how routing works and templating with Jinja.

To run this program, simply run the "main.py" file which contain the Flask application and make sure to have the other files (static and templates)
in the same directory.

By running the "main.py", the app will render different HTML files depending on which route is accessed. Two routes are accessible, the home route ('/') and
the "get_post" route ('/post/<id>'). The later route requires a parameter corresponding to the id of the post to be rendered. 

In this project, we use dummy data coming from "https://api.npoint.io/5abcca6f4e39b4955965" ,which is a list of dictionaries mimicking a set of blog posts.
By reaching the home route, we launch a GET request to the above URL and get back into the app a data set of fictious blog posts. This data set is then extracted
from the response and sent to be rendered in the "index.html" file. 

Inside the HTML file "index.html", we have to use the data we got from the GET request to populate the main page of our blog. This is possible by using the Jinja 
template syntax , where we can include Python code in our HTML file by using either {{}} (double-curly braces for single line code) or {% %} for multiline code like for loops
or if-statements.

To access a post in particular, we set up a route for that purpose in the file "main.py", ('/post/<blog_id>') for the function "get_post()". The function "get_post()" requires a 
parameter "blog_id" that is coming from the route defined above the function "get_post()". 

That parameter that we are passing to the route, comes from the HTML file "index.html", where while rendering all of our posts we tapped into the id property and passed it into a URL set up to reach the route we defined earlier in our server for a post in particular. The id of the post is passed as a keyword argument with the name "blog_id", name 
we found again in our server.

When the route for a particualr post is reached, its id is also passed as part of the route ('/post/<blog_id>') and therefore we can access it in the "get_post()" function.
In that function, we again make a request to the URL that has our blog posts data and repeat the same process as in our home route in the form of extracting the data as a JSON
and sending it to be rendered along an HTML file, in this case "post.html".

In this HTML file, we are going again to use Jinja template syntax to implement the logic behind rendering this time a single post. In order to do that, we loop across all the post objects we passed and if the id of one corresponds to the id we passed along as a keyword argument, it will get rendered, by tapping into the different properties of that 
object like the title, subtitle and body.

Screenshot of the blog-prototype

Home page
![image](https://user-images.githubusercontent.com/55893421/115942114-9b16f000-a476-11eb-99c3-1f9d0e042839.png)

Single post
![image](https://user-images.githubusercontent.com/55893421/115942219-1bd5ec00-a477-11eb-9eaa-900d300a4a60.png)

