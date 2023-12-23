# PythonSampleAPI
## To Install Dependencies:
From Project Root Directory, Run Command:
```
pip install -r requirements.txt
```
## To Run Application on Local Web Servers:
From Project Root Directory, Run Command:
```
uvicorn main:app --reload
```

## To Run Swagger:
Add "/docs" to the end of the base url when hosting the application
```commandline
http://127.0.0.1:8000/docs
```