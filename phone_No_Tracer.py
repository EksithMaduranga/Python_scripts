import phonenumbers
from phonenumbers import geocoder, carrier, timezone
i = 1
while i < 6 :
    number = input("Enter Your Number : ")
    phone_number = phonenumbers.parse(number)
    print(f"Location: {geocoder.description_for_number(phone_number, 'en')}")
    print(f"Carrier: {carrier.name_for_number(phone_number, 'en')}")
    print(f"Time Zone: {timezone.time_zones_for_number(phone_number)}")
i += 1


