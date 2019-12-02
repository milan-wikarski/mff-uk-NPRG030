# PID Scrapper

## Installation

This project requires certain Python packages to be function properly. To install them, run:

```console
$ pip install requests bs4 selenium flask flask-jsonpify flask-sqlalchemy flask-restful
```

## Running

To start the app, run the following command:

```console
$ python src/index.py
```

After that a REST API will be created at http://localhost:5002.

## Endpoints

### GET /connection/\<from\>/\<to\>

Returns a list containing 3 connections where **from** is the departure station and **to** is the arrival station.

Each connection has the following structure (in JSON):

```json
{
  "from": "",
  "to": "",
  "detail": "",
  "date": "",
  "time": "",
  "parts": [
    {
      "link": "",
      "departure": {
        "time": "",
        "location": ""
      },
      "arrival": {
        "time": "",
        "location": ""
      }
    },
    ...
  ]
}
```
