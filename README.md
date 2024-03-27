## Fast API to get date time and temperature for Infranet.

### Preconditions:
- Python 3

### Clone the project
```
git clone https://github.com/winston053790/fastapi-weather-provider.git
```

### How to run project

#### Install dependencies
```
pip install -r requirements.txt
```

#### Set up env
+ Copy .env.sample to .env in app directory.
+ Replace WWO_KEY with correct key
+ You can get API key from 
https://www.worldweatheronline.com/weather-api/my/

#### Run server
```
uvicorn app.main:app --reload
```

#### Run test
```
pytest test
```

#### API documentation (provided by Swagger UI)
```
http://127.0.0.1:8000/docs
```

### Author
Winston Almoguerra


