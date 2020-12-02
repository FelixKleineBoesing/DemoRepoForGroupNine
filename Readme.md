# Demo Repo for multi-language Analysis

### Description

##### Python

- all analysis, data cleaning, modelling in python belongs in dir "python"
- code files (python files and jupyter notebooks) should be create in python/src
- data files (json, csv, excel) are stored in python/data
- keep in mind that your web dev guy needs to have all the packages that you use for your analysis and modelling. 
    Therefore keep track of every package in the requirements.txt. I already added the flask requirement
    
You are able to install all libraries in the requirements.txt with this command (in Terminal/CMD): 

```
pip3 install -r python/requirements.txt
```

##### Web 
 
 - the frontend (webdev) project should be created in the web directory
 
 
 
 
#### Test

You can test this project by following these steps:

- install python 3

INstall packages: 
```
pip3 install -r python/requirements.txt
```

RUn API (via Terminal/CMD or simply click run in an IDE like Pycharm):

```
python3 python/src/app.py
```

Open the file index.html in dir "web" in firefox/chrome/safari. 
You are also able to call the python api directly with http://127.0.0.1:5000. 
The API than returns the text "This is the root page".