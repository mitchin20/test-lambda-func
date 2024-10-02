import json
from services.random_number_service import generate_random_number

def lambda_handler(event, context):
    try:
        number = generate_random_number()
        message = f"Random number generated: {number}"
        return {
            'statusCode': 200,
            'body': json.dumps(message)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
