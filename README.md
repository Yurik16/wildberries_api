# wildberries_api

"wildberries_api" is a Web API made with DRF (Django REST framework) that collects data from https://www.wildberries.ru/ <br />
Take *.xlmx file or value(number) of product and output JSON with data of this product (article, brand, title)

## Installation
Before install you must have:

<ul>
    <li> Python 3.7+
    <li> Git bash    
</ul>

Clone repository - git clone https://github.com/Yurik16/wildberries_api.git <br />
Before run parser.py move to working folder and install all packages from requirements.txt. Execute: <br />
<ul>  
    <li> virtualenv venv
    <li> source venv/bin/activate
    <li> pip install -r /path/to/requirements.txt
</ul>

## Usage
Starting development server at http://127.0.0.1:8000/ <br>
To get singe response from api use http://127.0.0.1:8000/api/`<int:pk>`/

Soon it would be able to  use that API on AWS ES2 instance or another remote web server

Using the terminal you can add arguments and change file path for saving result *.txt

## returns

Returns 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)