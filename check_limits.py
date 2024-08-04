def battery_is_ok(temperature, soc, charge_rate):
  # Define limits and warning ranges
  temperature_limit = (0, 45)
  soc_limit = (20, 80)
  charge_rate_limit = 0.8
  
  # Calculate 5% tolerance
  temperature_warning_tolerance = (temperature_limit[1] - temperature_limit[0]) * 0.05
  soc_warning_tolerance = (soc_limit[1] - soc_limit[0]) * 0.05
  charge_rate_warning_tolerance = charge_rate_limit * 0.05
  
  # Warnings enabled for each parameter
  warning_config = {
    'temperature': True,
    'soc': True,
    'charge_rate': True
  }

  # Check temperature
  if temperature < temperature_limit[0] or temperature > temperature_limit[1]:
    print('Temperature is out of range!')
    return False
  elif warning_config['temperature']:
    if temperature_limit[0] <= temperature < temperature_limit[0] + temperature_warning_tolerance:
      print('Warning: Temperature approaching low limit')
    elif temperature_limit[1] - temperature_warning_tolerance < temperature <= temperature_limit[1]:
      print('Warning: Temperature approaching high limit')

  # Check State of Charge (SoC)
  if soc < soc_limit[0] or soc > soc_limit[1]:
    print('State of Charge is out of range!')
    return False
  elif warning_config['soc']:
    if soc_limit[0] <= soc < soc_limit[0] + soc_warning_tolerance:
      print('Warning: Approaching discharge')
    elif soc_limit[1] - soc_warning_tolerance < soc <= soc_limit[1]:
      print('Warning: Approaching charge-peak')

  # Check charge rate
  if charge_rate > charge_rate_limit:
    print('Charge rate is out of range!')
    return False
  elif warning_config['charge_rate']:
    if charge_rate_limit - charge_rate_warning_tolerance < charge_rate <= charge_rate_limit:
      print('Warning: Charge rate approaching limit')

  return True
 
 
if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
