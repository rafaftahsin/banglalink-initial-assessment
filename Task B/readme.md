- How to spin up the server
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
- http://127.0.0.1:5000/ will show the output.
- Sample input 
```
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
```
- Sample Output
```
['25200', '88200']
```
