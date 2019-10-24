
# Armillary - Seat Assingment Project

  

This project built using Python 3 with Falcon Framework for Armillary Project

Author: ([Jensen](https://github.com/weiztech/)) 

  

## Tech Stack

  - Python 3
  - Falcon Framework
     web framework
  - marshmallow
    used for api validation
  - gunicorn
     for run server
  - nose2 
     for run uni-testing code
  

### Prerequisites Installations

  

Assume you have Python 3 installed on your local, the next steps that you need todo

  
- install [pip](https://pip.pypa.io/en/stable/installing/)
- after pip installed, install all dependency modules on requirements.txt file (*make sure your on project parent folder for run this command)
```

pip install -r requirements.txt

```

### Run Server

Make sure your on parent folder
```

gunicorn main.main:app

```

### Run Test

Make sure your on parent folder
```

python -m nose2

```