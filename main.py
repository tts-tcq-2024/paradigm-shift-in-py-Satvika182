from check_limits import (
    check_temperature_within_range,
    check_temperature_warning,
    check_soc_within_range,
    check_soc_warning,
    check_charge_rate_within_range,
    check_charge_rate_warning
)

def battery_is_ok(temperature, soc, charge_rate):
    # Check temperature
    if not check_temperature_within_range(temperature):
        print('Temperature is out of range!')
        return False
    temp_warning = check_temperature_warning(temperature)
    if temp_warning:
        print(temp_warning)
    
    # Check State of Charge (SoC)
    if not check_soc_within_range(soc):
        print('State of Charge is out of range!')
        return False
    soc_warning = check_soc_warning(soc)
    if soc_warning:
        print(soc_warning)
    
    # Check charge rate
    if not check_charge_rate_within_range(charge_rate):
        print('Charge rate is out of range!')
        return False
    charge_rate_warning = check_charge_rate_warning(charge_rate)
    if charge_rate_warning:
        print(charge_rate_warning)
    
    return True

if __name__ == '__main__':
    # Run some test cases
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
    print("All tests passed!")
