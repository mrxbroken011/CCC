# bot/card_checker.py

import stripe
import os


from .config import SK


stripe.api_key = SK


def check_stripe_key(card_details):
    try:
        token = stripe.Token.create(
            card={
                "number": card_details["number"],
                "exp_month": card_details["exp_month"],
                "exp_year": card_details["exp_year"],
                "cvc": card_details["cvc"],
            },
        )
        return f"Card is valid: {token.id}"
    except stripe.error.CardError as e:
        return f"Card validation failed: {e.user_message}"
    except stripe.error.StripeError as e:
        return f"Stripe API error: {str(e)}"
    except Exception as e:
        return f"An error occurred: {e}"

# Function to check card details from message
def check_card_from_message(card_details):
    card_details = card_details.split(',')
    if len(card_details) != 4:
        return 'Please provide card details in the correct format: number, exp_month, exp_year, cvc'

    card_details = {
        "number": card_details[0].strip(),
        "exp_month": int(card_details[1].strip()),
        "exp_year": int(card_details[2].strip()),
        "cvc": card_details[3].strip(),
    }

    return check_stripe_key(card_details)

# Function to check card details from file
def check_card_from_file(file_path):
    if not os.path.exists(file_path):
        return 'File not found.'

    results = []
    with open(file_path, 'r') as file:
        for line in file:
            card_details = line.strip().split(',')
            if len(card_details) != 4:
                results.append('Invalid card details format')
                continue
            
            card_details = {
                "number": card_details[0].strip(),
                "exp_month": int(card_details[1].strip()),
                "exp_year": int(card_details[2].strip()),
                "cvc": card_details[3].strip(),
            }

            results.append(check_stripe_key(card_details))

    return '\n'.join(results)
