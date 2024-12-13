import json
import random

def random_integer():
    options = [1,2,3]
    return random.choice(options)

def lambda_handler(event, context):
    option = random_integer()
    if option == 1:
        value = "Yes"
    elif option == 2:
        value = "No"
    else:
        value = "Maybe"
    message = f"{value}"
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
