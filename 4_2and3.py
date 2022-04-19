def currency_rates(cur):
    """ Возвращает курс(float) валюты относительно рубля и дату(date) , не смотрит на регистр букв если нет валюты возвращает None


    :param cur:
    :return:
    """
    import requests
    import datetime
    some_rec = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    tex = some_rec.json()
    try:
        value = tex['Valute'][cur.upper()]['Value']
    except KeyError:
        value = None
    if value == None:
        print(value)
    else:
        text = tex['Date']
        text = str(text[:10])
        print(
            f" 1 {cur.upper()}  =  {tex['Valute'][cur.upper()]['Value']} руб {datetime.datetime.strptime(text, '%Y-%m-%d')}")


currency_rates("uSd")
currency_rates("eur")