import csv

def collect_survey_data():
    print("Welcome to the Survey Data Collection Tool!")
    responses = []


    while True:

        #collect data for each field
        age = input("Enter age: ")
        gender = input("Enter gender (Male/Female):")

        #Ensure that satisfaction and other ratings are between 1 and 5
        satisfaction = int(input("Enter satisfaction (1-5):"))
        recommend = int(input("Enter comments:"))
        service_quality = int(input("Enter service quality (1-5):"))
        ease_of_use = int(input("Enter ease of use (1-5): "))
        price_satisfaction = int(input("Enter price satisfaction (1-5): "))


        #store the response as a dictionary
        response = {
            "Age": age,
            "Gender": gender,
            "Satisfaction": satisfaction,
            "Likely to Recommend": recommend,
            "Comments": comments,
            "Service Quality": service_quality,
            "Ease of Use": ease_of_use,
            "Price Satisfaction": price_satisfaction
            }

        # Add the response to the list of responses
        responses.append(response)
        
        # Ask if they want to enter another response
        another = input("Do you want to enter another response? (yes/no): ").lower()
        if another != 'yes':
            break

        return responses