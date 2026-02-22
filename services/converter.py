def calculate_cross_rate(source, target, base, rates):
    source = source.upper()
    target = target.upper()
    base = base.upper()

    if source == base:
        return rates.get(target)
    if source == target:
        return 1.0
    if base == target:
        return 1 / rates.get(source)

    return rates.get(target)/rates.get(source)

def buy(amount,rate):
    return amount * rate

def sell(amount, rate):
    return amount / rate

def process_transaction(action, amount, rate):
    if action == 'buy':
        return buy(amount, rate)
    elif action == 'sell':
        return sell(amount, rate)
    else:
        raise ValueError('Invalid action')