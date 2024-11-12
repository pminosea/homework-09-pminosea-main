# Homework 09 Report

1. Which Airlines have the most flights in 2015? How many flights did they have?
>Southwest Airlines Co.:       221,586
   
2. Which Airlines have the least flights in 2015? How many flights did they have?
>Hawaiian Airlines Inc.:       14,133
   
3. Data is an important aspect of our society, and it is important to understand how to work with it. What are some ways you can see data being used in your future career?
>I see data as crucial for decision-making. Websites, for example, may store large banks of data that give us information about 
our users. Let's take an e-commerce website for example: we might have data on times of purchase, products purchased, location about the user, etc.
This data will help us make decisions that will improve our website. We might analyze this data and cross-reference it with other data points 
to understand why some customers from certain regions shop less - therefore improving our customers service in that region, for example, what are the most purchased products and should they be more visible to customers, etc.
With data, we can make informed decisions about how to improve our product and our business. 

4. You should start thinking about larger applications, list some applications /  projects you would like to work on? Narrow it down to projects that you can accomplish within a couple weeks?
>I like the impact I can have by working with applications that are consumer facing and that makes people's lives easier. Programs that help count calories, or help find better prices of a product, etc. 

5. Provide output of you running `doctest` with the `-v` flag enabled (i.e. the output generated on your screen)

```
  paulaminozzo@Paulas-MacBook-Air src % python3 -m doctest -v flight_counter.py                                        
Trying:
    build_counters("../data/flights10.dat", {"AA": "American Airlines",                             "DL": "Delta Airlines", "UA": "United Airlines"})
Expecting:
    {'UA': 2, 'DL': 2}
ok
Trying:
    build_counters("../data/flights_2.dat", {"AA": "American Airlines",                             "DL": "Delta Airlines", "UA": "United Airlines"})
Expecting:
    {'AA': 1, 'DL': 1, 'UA': 1}
ok
Trying:
    load_airlines("../data/airlines.dat")                    # doctest: +NORMALIZE_WHITESPACE
Expecting:
    {'UA': 'United Air Lines Inc.',
    'AA': 'American Airlines Inc.',
    'US': 'US Airways Inc.',
    'F9': 'Frontier Airlines Inc.',
    'B6': 'JetBlue Airways',
    'OO': 'Skywest Airlines Inc.',
    'AS': 'Alaska Airlines Inc.',
    'NK': 'Spirit Air Lines',
    'WN': 'Southwest Airlines Co.',
    'DL': 'Delta Air Lines Inc.',
    'EV': 'Atlantic Southeast Airlines',
    'HA': 'Hawaiian Airlines Inc.',
    'MQ': 'American Eagle Airlines Inc.',
    'VX': 'Virgin America'}
ok
Trying:
    load_airlines("../data/airlines_2")  # doctest: +NORMALIZE_WHITESPACE
Expecting:
    {'AA': 'American Airlines',
    'DL': 'Delta Air Lines',
    'FR': 'Ryanair',
    'UA': 'United Airlines',
    'WN': 'Southwest Airlines',
    'LH': 'Lufthansa Group',
    'IAG': 'International Airlines Group',
    '6E': 'IndiGo',
    'TK': 'Turkish Airlines',
    'U2': 'easyJet',
    'AF': 'Air France',
    'EK': 'Emirates',
    'QR': 'Qatar Airways',
    'SQ': 'Singapore Airlines',
    'NH': 'All Nippon Airways',
    'BA': 'British Airways',
    'QF': 'Qantas',
    'AC': 'Air Canada',
    'KL': 'KLM Royal Dutch Airlines',
    'CZ': 'China Southern Airlines'}
ok
Trying:
    counters = {"AA": 10, "DL": 5, "UA": 3}
Expecting nothing
ok
Trying:
    airlines = {"AA": "American Airlines", "DL": "Delta Airlines", "UA": "United Airlines"}
Expecting nothing
ok
Trying:
    print_counters(counters, airlines)                   # doctest: +NORMALIZE_WHITESPACE
Expecting:
    American Airlines: 10
    Delta Airlines:     5
    United Airlines:    3
ok
2 items had no tests:
    flight_counter
    flight_counter.main
3 items passed all tests:
   2 tests in flight_counter.build_counters
   2 tests in flight_counter.load_airlines
   3 tests in flight_counter.print_counters
7 tests in 5 items.
7 passed and 0 failed.
Test passed.
paulaminozzo@Paulas-MacBook-Air src % 

   ```

6. Output of running `python3 flight_counter.py -h`, and what it means in your own words. (Note: windows is python, and file location may vary based on where you are running it. The above assume linux and running from the homework src directory)

```
>usage: flight_counter.py [-h] [-f FLIGHTS] [-a AIRLINES]
>Flight Counter
>options:
>-h, --help            show this help message and exit
>-f FLIGHTS, --flights FLIGHTS
                        The file containing the flight data.
  -a AIRLINES, --airlines AIRLINES
                        The file containing the airline data.

```
> This output gives me choices (a menu) regarding what can be within the program. 

## Deeper Thinking

When dealing with large datasets, or data in general, there needs to be a careful consideration of biases, collection, and use of that data. For example, it is very possible for real world data to be biased towards collection biases or sampling biases, and there are very real ethical issues in how that data is being used especially if a bias is not being taken into account. Take a moment to research some issues with data collection and use, and list some examples you can find. You may even find some examples that are related to data you supply on a data basis (i.e. what you give to social media)

>Our everyday data, about our location, names of friends, location and other sensitive data: we give those for free to companies – and we often do not know what they are used for.  For instance, personal data can be sold to third parties. The Cambridge Analytica scandal is an example of when data from millions of Facebook users was collected and used for political purposes before an election – targeting users. According to The Guardian, Cambdrige Analytica used personal user information to build a system that could profile individual US voters, in order to target them with personalised political advertisements. There is a discrepancy in what data we know we have provided and what actually is collected by these companies, mainly because i) it can be hard to track everyday ii) it is difficult to undertand the terms of services iii) usually our devices do not give us many choices on restricting them. Apple has made some progress in that front, but it is still gruesome to take full control. 
>
>Another topic very related to integrity of our data  is cybersecurity. Not just how we analyze data needs to be taken seriously, but also how we store data. There are many scandals involving breach of personal data, that leaves consumers exposed. Their data can be accessed by criminal organizations to later target these customers. 
