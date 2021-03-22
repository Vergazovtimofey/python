

def currency_rates(money):
    from requests import get
    link = "http://www.cbr.ru/scripts/XML_daily.asp"
    documents = get(link)
    text = documents.text

    if money == 'usd' or money == "USD" or money == 'eur' or money == "EUR":
        usd_1 = text.find("Date")
        part_1 = text[text.index("Date"):]
        date = part_1[7:16:]
        year = part_1[12:16]
        month = part_1[8:12]
        day = part_1[7:8]
        date = f'{year}{month}{day}'

    if money == 'usd' or money == "USD":

        part_1 = text[text.index("USD"):]
        value = part_1.find('<Value>')
        rub = part_1[64:71]
        rub = rub.replace(',', ".")
        rub = float(rub)
        return f'Date {date}, курс USD {rub}'

    if money == 'eur' or money == "EUR":

        part_2 = text[text.index("EUR"):]
        value_2 = part_2.find('<Value>')
        rub_1 = part_2[58:65]
        rub_1 = rub_1.replace(',', ".")
        rub_1 = float(rub_1)
        return f'Date {date}, курс EUR {rub_1}'


print(currency_rates('usd'))
# currency_rates('usd')