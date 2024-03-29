# local-web-app-temperature-and-humidity-generator

This is the test harness for the Vantiq temperature and humidity prototype. This will produce a random number between the values given to represent the current temperature and humidity of a device. It will also create as many of these devices as the user wishes and will delete these devices after the messages have stopped sending.

## How do I get set up?

1. Download Python to your machine if you have not already done so
2. Either download or clone this repository to your local machine
3. Within the terminal navigate to the install location run the following command:
   * Run the command ```$ py  -m venv venv```
4. Then activate the virtual environment dependencies using the command:
   * If using Windows run ```$ venv\scripts\activate```
   * If using Linux run ```$ source venv/bin/activate```
5. Install the dependencies by using the command ```pip install -r requirements.txt```
6. Run the script by running the command:
   * Run the command ```$ py app.py```
7. Finally navigate to <http://127.0.0.1:8080/>
