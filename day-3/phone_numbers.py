import phonenumbers
from phonenumbers import geocoder

phone_number = "+251914719859"
parsed_number = phonenumbers.parse(phone_number, None)


print("Country Code:", parsed_number.country_code)
print("National Number:", parsed_number.national_number)

if phonenumbers.is_valid_number(parsed_number):
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    print("Formatted Number:", formatted_number)
    location = phonenumbers.geocoder.description_for_number(parsed_number, "en")
    print("Location:", location)
else:
    print("Invalid phone number.")
