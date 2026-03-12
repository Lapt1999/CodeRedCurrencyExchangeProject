def calculate_cross_rate(source, target, base, rates):
    source, target, base = source.upper(), target.upper(), base.upper()

    if source == target:
        return 1.0
    if source != base and source not in rates:
        raise ValueError(f'Rate for {source} not found')
    if target != base and target not in rates:
        raise ValueError(f'Rate for {target} not found')

    source_rate = 1 if source == base else rates[source]
    target_rate = 1 if target == base else rates[target]

    return target_rate/source_rate


def buy(amount,calculated_rate):
    return amount * calculated_rate


def sell(amount, calculated_rate):
    return amount / calculated_rate


def process_transaction(action, amount, calculated_rate):
    if action == 'buy':
        return buy(amount, calculated_rate)
    else:
        return sell(amount, calculated_rate)


def safe_process_transaction(source, target, base, rates, amount, action):
    try:
        calculated_rate = calculate_cross_rate(source, target, base, rates)
        result = process_transaction(action, amount, calculated_rate)
        return True, result
    except ValueError as e:
        return False, f'Error: {e}. Please try again.'
    except Exception as e:
        return False, f'Unexpected error: {e}'