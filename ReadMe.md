Get an API key. Instructions are here: `https://developers.google.com/maps/documentation/javascript/get-api-key#restrict_key`

To build application : `docker build -t myimage .`

To run application: `docker run -d --name mycontainer -p 80:80 myimage`

You should be able to check it in your Docker container's URL, for example: http://192.168.99.100 or http://127.0.0.1

