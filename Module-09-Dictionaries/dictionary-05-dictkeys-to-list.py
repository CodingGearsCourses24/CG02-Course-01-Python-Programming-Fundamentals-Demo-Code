# Dictionary
# Converting dictionary keys to list

# Dictionary -------------------------------------------
print(" Dictionary with string keys ".center(44, "-"))
dict_airport_code_to_city = {"AAL": "Aalborg, Denmark",
                             "AES": "Aalesund, Norway",
                             "AAR": "Aarhus, Denmark",
                             "YXX": "Abbotsford, BC, Canada",
                             "YXX": "Abbotsford, BC, Canada",
                             "ABZ": "Aberdeen, Scotland",
                             "ABR": "Aberdeen, SD, USA",
                             "ABJ": "Abidjan, Ivory Coast",
                             "ABI": "Abilene, TX, USA",
                             "AUH": "Abu Dhabi, United Arab Emirates",
                             "ABV": "Abuja, Nigeria",
                             "ACA": "Acapulco, Mexico",
                             "ACC": "Accra, Ghana",
                             "ADA": "Adana, Turkey",
                             "ADD": "Addis Ababa, Ethiopia",
                             "ADL": "Adelaide, S.A., Australia",
                             "ADE": "Aden, Yemen",
                             "ADF": "Adiyaman, Turkey",
                             "AGA": "Agadir, Morocco",
                             "GUM": "Agana, Guam",
                             "BQN": "Aguadilla, Puerto Rico",
                             "AGU": "Aguascalientes, Mexico",
                             "AHE": "Ahe, French Polynesia",
                             "AMD": "Ahmedabad, India",
                             "AJA": "Ajaccio, Corsica, France",
                             "AXT": "Akita, Japan",
                             "CAK": "Akron, OH, USA",
                             "ALS": "Alamosa, CO, USA",
                             "ABY": "Albany, GA, USA",
                             "ALB": "Albany, NY, USA",
                             "ALL": "Albenga, Italy",
                             "ABQ": "Albuquerque, NM, USA",
                             "ABX": "Albury, N.S.W., Australia",
                             "ALY": "Alexandria, Egypt",
                             "HBE": "Alexandria, Egypt",
                             "AEX": "Alexandria, LA, USA",
                             "AXD": "Alexandroupolis, Greece",
                             "AHO": "Alghero, Sardinia, Italy",
                             "ALG": "Algiers, Algeria",
                             "ALC": "Alicante, Spain",
                             "ASP": "Alice Springs, N.T., Australia",
                             "NSB": "Alice Town, North Bimini Island, Bahamas",
                             "ABE": "Allentown, PA, USA",
                             "AIA": "Alliance, NE, USA",
                             "ALA": "Almaty, Kazakhstan",
                             "LEI": "Almeria, Spain",
                             "AOR": "Alor Setar, Malaysia",
                             "APN": "Alpena, MI, USA",
                             "ALF": "Alta, Norway",
                             "ACH": "Altenrhein, Switzerland"}

print(dict_airport_code_to_city)

# Converting dictionary keys to list & sorting them
print(" Converting dictionary keys to list & sorting them ".center(44, "-"))
airport_codes = list(dict_airport_code_to_city.keys())
print(type(airport_codes))
print(airport_codes)
airport_codes.sort()
print(airport_codes)

# Displaying info
print(" Displaying info based on a key ".center(44, "-"))
code = "ALB"
for airport_code in airport_codes:
    if airport_code == code:
        print(airport_code, " : ", dict_airport_code_to_city[airport_code])

# Using if
if code in dict_airport_code_to_city:
    airport_info = dict_airport_code_to_city[code]
    print(code, " : ", airport_info)