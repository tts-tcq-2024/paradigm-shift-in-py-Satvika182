def check_temperature_within_range(temperature):
    limits = (0, 45)
    return limits[0] <= temperature <= limits[1]

def check_temperature_warning(temperature):
    limits = (0, 45)
    tolerance = (limits[1] - limits[0]) * 0.05
    if temperature <= limits[0] + tolerance:
        return 'Warning: Temperature approaching low limit'
    elif temperature >= limits[1] - tolerance:
        return 'Warning: Temperature approaching high limit'
    return None

def check_soc_within_range(soc):
    limits = (20, 80)
    return limits[0] <= soc <= limits[1]

def check_soc_warning(soc):
    limits = (20, 80)
    tolerance = (limits[1] - limits[0]) * 0.05
    if soc <= limits[0] + tolerance:
        return 'Warning: Approaching discharge'
    elif soc >= limits[1] - tolerance:
        return 'Warning: Approaching charge-peak'
    return None

def check_charge_rate_within_range(charge_rate):
    limit = 0.8
    return charge_rate <= limit

def check_charge_rate_warning(charge_rate):
    limit = 0.8
    tolerance = limit * 0.05
    if charge_rate >= limit - tolerance:
        return 'Warning: Charge rate approaching limit'
    return None
