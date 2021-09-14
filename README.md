# FreeCare

This project implements a web application that predict disease based on inputed symptoms. For this I am using Django, Machine Learning, Javascript, Wikipedia API, Geocoding and Seach API, Pickle and Python.

To predict the disease I am using trained model of Decision Tree Algorithm of Machine Learning.

There are 3 features available on website:

1) Disease Prediction : When user inputs the symptoms and clicks the submit button then the disease that is predicted by the trained ML model is displayed.
2) Disease Details : The disease which is predicted by the model is in fact a hyperlink which when clicked takes the user to another webpage which displays the information about the disease fetched using Wikipedia API.
3) Names and Addresses of nearby Hospitals : On the webpage where the disease is predicted there is also a button which when clicked would display to the user the names and addresses of nearby hospitals based on user's current location. This feature is implemented using Javascript and Geocoding and Search API.

Apps present in project:

1) Interface : Implements all the 3 features mentioned above. Its main files include - urls.py ( Links urls mentioned in this file to views.py's functions ) and views.py ( Implements the functions used in creating the features ) .

