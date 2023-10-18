# local-temperature-and-humidity-generator

This is the test harness for the Vantiq ride management prototype. This simulates people entering a queue for particular rides and generates the length of time, in which they are willing to stay in the queue for.

## How do I get set up?

1. Download Python to your machine if you have not already done so
2. Either download or clone this repository to your local machine
3. Within the terminal navigate to the install location run the following command:
   * If using Windows run ```$ py -m venv venv```
   * If using Linux run ```$ python3 -m venv venv```
4. Then activate the virtual environment dependencies using the command:
   * If using Windows run ```$ venv\scripts\activate```
   * If using Linux run ```$ source venv/bin/activate```
5. Install the dependencies by using the command ```pip install -r requirements.txt```
6. Run the script by running the command:
   * If using Windows run ```$ py app.py```
   * If using Linux run ```$ python3 app.py```
