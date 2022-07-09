# How to run both the app and the test cases
## Setup work environment
Create a virtual environment and the install the required libraries.  
```pip install -r requirements```

## How to run the code
The source code contains a ```app.py``` with main method. In order to run in your project directory. Run the following command:  
```python tasks/app.py```  
You can modify the main section to add your own test data

## How to run the test cases
The are written using ```pytest``` module installed from the ```requirements.txt``` file. The application has five(5) test cases. In order to run execute the following command in your project directory:-  
```python -m pytest tests```