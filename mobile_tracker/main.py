import phonenumbers
from number import number

from phonenumbers import geocoder

location = phonenumbers.parse(number,"ch")
print(geocoder.description_for_number(location,"en"))



from phonenumbers import carrier

service = phonenumbers.parse(number,"rn")
print(carrier.name_for_number(service,"en"))