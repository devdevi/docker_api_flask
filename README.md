# ApiRest D-BCH

This is an API Flask 

## Running Locally

Run the following commands to get started running this app locally:
```RUN: 
    . env/bin/activate
    flask run
```

Then visit `http://localhost:5000` to play with the app.

## Running Docker 

```
    sudo docker build -t flask-bch:latest .
    sudo docker run -d -p 5000:5000 flask-bch
    sudo docker container rm <container id>
    sudo docker build -t flaskbch:latest .
    sudo docker run --rm -it -v $(pwd)/api_flask:/api_flask -p 5000:5000 flaskbch  
    sudo docker run --rm -it -v $(pwd)/api_flask:/api_flask -p 5000:5000 flaskbch sh
    sudo docker run --rm -it -v $(pwd)/api_flask:/api_flask -p 5000:5000 --network=host flaskbch
```
## Licensing

This example is open-sourced software licensed under the
[MIT license](https://opensource.org/licenses/MIT).
