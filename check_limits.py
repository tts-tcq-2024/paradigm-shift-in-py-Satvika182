def check_temperature(temperature):
    limits = (0, 45)
    tolerance = (limits[1] - limits[0]) * 0.05
    
    if temperature < limits[0] or temperature > limits[1]:
        return 'Temperature is out of range!'
    elif temperature <= limits[0] + tolerance:
        return 'Warning: Temperature approaching low limit'
    elif temperature >= limits[1] - tolerance:
        return 'Warning: Temperature approaching high limit'
    return None

def check_soc(soc):
    limits = (20, 80)
    tolerance = (limits[1] - limits[0]) * 0.05
    
    if soc < limits[0] or soc > limits[1]:
        return 'State of Charge is out of range!'
    elif soc <= limits[0] + tolerance:
        return 'Warning: Approaching discharge'
    elif soc >= limits[1] - tolerance:
        return 'Warning: Approaching charge-peak'
    return None

def check_charge_rate(charge_rate):
    limit = 0.8
    tolerance = limit * 0.05
    
    if charge_rate > limit:
        return 'Charge rate is out of range!'
    elif charge_rate >= limit - tolerance:
        return 'Warning: Charge rate approaching limit'
    return None

def battery_is_ok(temperature, soc, charge_rate):
    # Check each parameter and collect warnings
    temp_warning = check_temperature(temperature)
    soc_warning = check_soc(soc)
    charge_rate_warning = check_charge_rate(charge_rate)
    
    # Print the appropriate messages
    if temp_warning:
        print(temp_warning)
        if 'out of range' in temp_warning:
            return False
    if soc_warning:
        print(soc_warning)
        if 'out of range' in soc_warning:
            return False
    if charge_rate_warning:
        print(charge_rate_warning)
        if 'out of range' in charge_rate_warning:
            return False
    
    return True

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
