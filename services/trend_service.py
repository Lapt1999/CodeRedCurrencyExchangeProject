
from services.rate_service import load_rates_from_scv

def analyze_trend(rates):

    if len(rates) < 2:
        return 'Not enough data to analyze'

    up = 0
    down = 0

    for i in range(1, len(rates)):
        if rates[i] > rates[i-1]:
            up += 1
        elif rates[i] < rates[i-1]:
            down += 1

    if up > down:
        return 'UP'
    elif up < down:
        return 'DOWN'
    else:
        return 'STABLE'


def get_recommendation(trend):
    if trend == 'UP':
        return 'Rate is increasing. Consider SELLING'
    elif trend == 'DOWN':
        return 'Rate is decreasing. Consider BUYING'
    else:
        return 'Rate is stable. No strong signal'


def analyze_and_suggest(base, source, target):
    dates, rates = load_rates_from_scv(base, source, target, filename = 'data/exchange_rates.csv')
    trend = analyze_trend(rates)
    recommendation = get_recommendation(trend)

    print(f'\nTrend: {trend}')
    print(f'Suggestion: {recommendation}')