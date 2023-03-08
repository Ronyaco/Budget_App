from datetime import date, timedelta
from tabnanny import check

def calculate_interval_between_dates(start_date, end_date,days_or_months):
    if days_or_months == 'days':
        delta = end_date - start_date
        return delta.days
    elif days_or_months == 'months':
        delta = end_date.year - start_date.year
        if end_date.month < start_date.month:
            delta -= 1
        return delta
    else:
        raise Exception('days_or_months must be days or months')

def add_interval_to_date(date, days_or_months, value):
    if days_or_months == 'days':
        return date + timedelta(days=value)
    elif days_or_months == 'months':
        y, m = divmod(date.month + value, 12)
        return date.replace(year=date.year + y, month=m)
    else:
        raise Exception('days_or_months must be days or months')


def calculate_repetitive_total(obj, last_balance, today):
    total = 0
    repetition_time = obj.repetition_time
    if obj.repetition_interval == 2: #days
        days_or_months = 'days'
    elif obj.repetition_interval == 3: #weeks
        repetition_time *= 7
        days_or_months = 'days'
    elif obj.repetition_interval == 4: #months
        days_or_months = 'months'
    elif obj.repetition_interval == 5: #years
        repetition_time *= 12   
        days_or_months = 'months'
    else:
        raise Exception('repetition_time_interval must be 2, 3, 4 or 5')
    
    balance_to_obj_time = calculate_interval_between_dates(last_balance.date, obj.date, days_or_months)
    if balance_to_obj_time <= 0:
        check_date = obj.date
    else:
        no_of_intervals_before = int(balance_to_obj_time / repetition_time)
        check_date = add_interval_to_date(last_balance.date, days_or_months, no_of_intervals_before * repetition_time)
    
    while last_balance.date > check_date:
        check_date = add_interval_to_date(check_date, days_or_months, repetition_time)
    while check_date <= today:
        total += obj.value
        check_date = add_interval_to_date(check_date, days_or_months, repetition_time)

    return total



