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
    sudo docker container rm <container id>
    sudo docker build -t flaskapi:latest .
    sudo docker run --rm -it -v $(pwd)/api_flask:/api_flask -p 5000:5000 flaskapi
    sudo docker run --rm -it -v $(pwd)/api_flask:/api_flask -p 5000:5000 flaskapi sh
    sudo docker run --rm -it -v $(pwd)/api_flask:/api_flask -p 5000:5000 --network=host flaskapi
```
## Licensing

This example is open-sourced software licensed under the
[MIT license](https://opensource.org/licenses/MIT).
