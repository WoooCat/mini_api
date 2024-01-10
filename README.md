## Flask API Monaco Racing


## Install dependency
```python
poetry install --no-root
```

## Create and Populate DB from command line
```python
python3 cli_command.py create_database
```

## Run main script
`main.py`
```python

if __name__ == '__main__':
    app.config.from_object(Configuration)
    app.run()
```
## Swagger page:
`http://127.0.0.1:5000/apidocs/`

# API Usage:
### Get Report
```python
curl -X GET "http://127.0.0.1:5000/api/v1/report"
```
### Get Report order by Desc in format XML:
```python
curl -X GET "http://127.0.0.1:5000/api/v1/report?order=desc&format=xml"
```
### Get Drivers
```python
curl -X GET "http://127.0.0.1:5000/api/v1/drivers/"
```
### Get Drivers order by Desc in format JSON :
```python
curl -X GET "http://127.0.0.1:5000/api/v1/drivers/?order=desc&format=json"
```
### Get Driver:
```python
curl -X GET "http://127.0.0.1:5000/api/v1/drivers/driver_id=EOF"
```
### Get Driver in format XML:
```python
curl -X GET "http://127.0.0.1:5000/api/v1/drivers/driver_id=EOF?format=xml"
```
