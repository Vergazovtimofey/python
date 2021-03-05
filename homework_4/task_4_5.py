from utils import currency_rates
import sys



usd = currency_rates.currency_rates(sys.argv[1])
print(usd)
