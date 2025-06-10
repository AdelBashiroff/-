class CurrencyConverter:
    exchange_rate = 0.85
    @staticmethod
    def convert_usd_to_eur(amount):
        return amount * CurrencyConverter.exchange_rate

if __name__ == '__main__':
    print(CurrencyConverter.convert_usd_to_eur(50))