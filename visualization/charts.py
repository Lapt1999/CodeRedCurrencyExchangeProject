from collections import defaultdict

import matplotlib.pyplot as plt

from services.trend_service import analyze_trend
from services.rate_service import load_rates_from_scv

def plot_currency_rate(base, source, target, filename = 'data/exchange_rates.csv'):
    dates, rates = load_rates_from_scv(base, source, target, filename)

    plt.figure()
    plt.plot(dates, rates)
    plt.title(f'{target}/{source} exchange rate over time')
    plt.xlabel('Date')
    plt.ylabel('Rate')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_day_to_day(base, source, target, filename = 'data/exchange_rates.csv', days = 30):
    dates, rates = load_rates_from_scv(base, source, target, filename)
    dates, rates = dates[-days:], rates[-days:]

    plt.figure()
    plt.plot(dates, rates, marker = 'o', color = 'blue')
    plt.title(f'{target}/{source} Day - to - Day Rates')
    plt.xlabel('Date')
    plt.ylabel('Rate')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_month_to_month(base, source, target, filename = 'data/exchange_rates.csv'):
    dates, rates = load_rates_from_scv(base, source, target, filename)
    monthly = defaultdict(list)
    for date,rate in zip(dates,rates):
        month = date.strftime('%Y-%m')
        monthly[month].append(rate)
    months = sorted(monthly.keys())
    avg_rates = []
    for month in months:
        avg_rate = sum(monthly[month]) / len(monthly[month])
        avg_rates.append(avg_rate)

    plt.figure()
    plt.plot(months, avg_rates, marker='o', color='purple')
    plt.title(f'{target}/{source} Month - to - Month Average Rates')
    plt.xlabel('Month')
    plt.ylabel('Average Rate')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_trend(base, source, target, filename = 'data/exchange_rates.csv'):
    dates, rates = load_rates_from_scv(base, source, target, filename)

    if len(rates) < 2:
        return 'Not enough data to analyze'

    plt.figure()

    for i in range(1, len(rates)):
        if rates[i] > rates[i-1]:
            color = 'green'
        elif rates[i] < rates[i-1]:
            color = 'red'
        else:
            color = 'gray'
        plt.plot([dates[i-1], dates[i]],
                 [rates[i-1], rates[i]],
                 color = color)

    plt.scatter(dates, rates)

    trend = analyze_trend(rates)

    plt.title(f'{target}/{source} Trend: {trend}')
    plt.xlabel('Date')
    plt.ylabel('Rate')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def all_charts(base, source, target, filename = 'data/exchange_rates.csv', days = 30):
    plot_currency_rate(base, source, target)
    plot_day_to_day(base, source, target)
    plot_month_to_month(base, source, target)
    plot_trend(base, source, target)