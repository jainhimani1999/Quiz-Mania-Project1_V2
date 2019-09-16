# WorkFlow

Date: 16th

* Made the project named ```QuizMania``` with its first ```webapp``` names as ```QuizMania_V2```
* Made a template folder inside the ```webapp``` and copied the 3 html files inside the templates folder namely ```admin,index,result```
* Inside the ```settings``` file, added the ```templates``` dircetory path and add the ```Installed Apps``` element value to ```QuizMania_V2```
* Made a ```static/QuizMania_v2``` folder inside ```webapp``` and added the ```css js bootstrap``` folders inside it
* configured the ```urls.py``` for index page
* Given ```755``` permission to all files inside static folder
* In ```index.html``` and ```admin.html``` file , added the online ```bootstrap``` link , which are
```html
 <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script> 
```
* changes all the ```src``` paths with ```jinja``` and just added ```{% static 'QuizMania_V2/``` to all the ```source paths```

