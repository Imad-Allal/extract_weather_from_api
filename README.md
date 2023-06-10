# Weather Extract From Different APIs

## About The Project
The main idea of this project is to extract weather information for different cities in Algeria every hour. The project utilizes an ETL (Extract, Transform, Load) process to gather weather data from reliable sources. The ETL process is implemented in a Python script named etl.py. The script imports additional modules such as extract.py, transform.py, and display_map.py to perform specific tasks.

## Built With
[requests](https://requests.readthedocs.io/en/latest/)
[folium](https://python-visualization.github.io/folium/)
[glob](https://docs.python.org/3/library/glob.html)

## Getting Started
To run the project, you can either run manually the project, or use [Docker](https://www.docker.com/)

### 1) Manual Installation
1) Install the 3 different libraries: **requests**, **folium** and **glob**
```Bash
!pip install requests
```

```Bash
!pip install folium
```

```Bash
!pip install glob3
```

2) Run the etl.py file
```bash
python3 etl.py
```

### 2) Using Docker
If you want to run your program every 1 hour automatically, use Docker instead, to do that, you can follow the steps below:

1) Building the project
```bash
docker build -t my-app .
```

2) Running the project
```bash
docker run my-app
```

*Note: Building the Docker might take some time to install all the dependencies*


## Contact
[LinkedIn](https://www.linkedin.com/in/imad-allal-106653204/)

[pro.imadallal@outlook.com](mailto:pro.imadallal.com)

## Project Link
https://github.com/Imad-Allal/web_scraping
