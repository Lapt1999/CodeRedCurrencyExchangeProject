
from services.rate_service import load_rates_from_scv
from ui.output_handler import suggest_order

def analyze_trend(rates):

    if len(rates) < 2:
        return 'Not enough data to analyze'

    first = rates[0]
    last = rates[-1]

    up = 0
    down = 0

    for i in range(1, len(rates)):
        if rates[i] > rates[i-1]:
            up += 1
        elif rates[i] < rates[i-1]:
            down += 1

    if last > first:
        trend = 'UP'
    elif last < first:
        trend = 'DOWN'
    else:
        trend = 'STABLE'

    return trend, up, down


def get_recommendation(trend):

    if trend == 'UP':
        return 'Rate is increasing. Consider SELLING\n'
    elif trend == 'DOWN':
        return 'Rate is decreasing. Consider BUYING\n'
    else:
        return 'Rate is stable. No strong signal\n'


def analyze_and_suggest(base, source, target):
    dates, rates = load_rates_from_scv(base, source, target, filename = 'data/exchange_rates.csv')
    trend, up, down = analyze_trend(rates)
    recommendation = get_recommendation(trend)

    print(f'\nMovements --> UP: {up}, DOWN: {down}')
    print(f'\nTrend: {trend}')
    print(f'Suggestion: {recommendation}')

    suggest_order(trend)