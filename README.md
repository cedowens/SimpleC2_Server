# SimpleC2 Server

A basic http C2 server using the python3 aiohttp framework. 

This is still a work in progress. Also note - I have not yet posted the client that connects to these C2 endpoints, so you will need to create your own client until I post one here.

Usage:
python3 simple_C2.py

Note:
to change the default port to something other than 8080, just add port=80 in the last line of the code as follows:

_web.run_app(app, port=[port])_
