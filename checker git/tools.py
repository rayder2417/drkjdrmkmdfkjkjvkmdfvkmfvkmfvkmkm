import requests

def data_bin(card):
    bin = list(card)
    bin = f"{bin[0]}{bin[1]}{bin[2]}{bin[3]}{bin[4]}{bin[5]}"
    data_binv = requests.get(f"https://bins.antipublic.cc/bins/{bin}").json()
    country = f"{data_binv["country_name"]}{data_binv["country_flag"]}"
    data = f"{data_binv["brand"]} - {data_binv["level"]} - {data_binv["type"]}"
    bank = data_binv["bank"]
    return [country, data, bank]
    
        