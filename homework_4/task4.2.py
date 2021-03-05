

def currency_rates(money):
    from requests import get
    link = "http://www.cbr.ru/scripts/XML_daily.asp"
    documents = get(link)
    text = documents.text
    # print(text)
    if money == 'usd' or money == "USD":

        part_1 = text[text.index("USD"):]
        value = part_1.find('<Value>')
        rub = part_1[64:71]
        rub = rub.replace(',', ".")
        rub = float(rub)
        return rub

    if money == 'eur' or money == "EUR":

        part_2 = text[text.index("EUR"):]
        value_2 = part_2.find('<Value>')
        rub_1 = part_2[58:65]
        rub_1 = rub_1.replace(',', ".")
        rub_1 = float(rub_1)
        return rub_1
    else:
        return 'None'


print(currency_rates('.'))