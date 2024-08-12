def is_within_range(value, min_val, max_val):
    return (min_val is None or value >= min_val) and (max_val is None or value <= max_val)

def is_approaching_limit(value, min_val, max_val, tolerance):
    lower_approach = min_val is not None and min_val <= value <= min_val + tolerance
    upper_approach = max_val is not None and max_val - tolerance <= value <= max_val
    return lower_approach or upper_approach

def calculate_tolerance(reference_value, tolerance_percentage=5):
    return reference_value * tolerance_percentage / 100
