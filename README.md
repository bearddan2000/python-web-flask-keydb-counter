# python-web-flask-keydb-counter

## Description
A POC python flask web counter
that uses keydb as a datastore.

KeyDb is a database that persists data
however it is not a websocket that updates multiple
clients.

Testing frameworks: *testify* and *selenium*

## Tech stack
- python
  - flask
  - testify
  - selenium
- keydb

## Docker stack
- python:latest
- eqalpha/keydb
- selenium:latest

## To run
`sudo ./install.sh -u`
Available at http://localhost

## To stop (optional)
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
