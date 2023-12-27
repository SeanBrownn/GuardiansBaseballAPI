# GuardiansBaseballAPI

The functions are split up into 3 classes: teams, mlb, and players. The functions are organized by the scope of data
we are searching, not by what is returned. For example, functions in the "teams" class all require that we specify a
team. Similarly, functions in the "players" class all require that we specify a player in some way. The rest of the
functions, which search across all of MLB for data, are in the "mlb" class.

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