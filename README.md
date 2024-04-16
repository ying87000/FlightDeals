# FlightDeals
Find the best deal of flight

Step 1: Create a Google sheet contains two tabs, Prices and Users
    In Prices tab, please list all the cities you wish to visit, and the acceptable price.
    In Users tab, list all the user and email that should be notified when flight ticket price is lower than acceptable price.
    Example Google Sheet: https://docs.google.com/spreadsheets/d/1aE-RY9Zmod2-fF1FET6VhDbYRGQK-aq_jPQSHLliwxA/edit?usp=sharing

Step 2: Get Sheety API for Google sheet
    Go to https://sheety.co/, and sign up a free account
    Follow the instruction on https://sheety.co/docs/spreadsheet.html, get API for Prices tab and Users tab
    Fill in both API in data_manager.py

Step 3: Get Tequila API key for flight search
    Go to https://tequila.kiwi.com/ , and sign up a free account
    Get Tequila API key and fill in flight_search.py

Step 4: Get Twilio API key and Auth SID, for sending SMS messages
    Go to https://www.twilio.com/ , and sign up a free account
    Get Account SID, Auth token, and My Twilio phone number, fill these info in notification_manager.py
    

    
