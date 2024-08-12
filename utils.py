def is_within_range(value, min_val, max_val):
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True

def is_approaching_limit(value, min_val, max_val, tolerance):
    if min_val is not None:
        if min_val <= value <= min_val + tolerance:
            return True
    if max_val is not None:
        if max_val - tolerance <= value <= max_val:
            return True
    return False

def calculate_tolerance(reference_value, tolerance_percentage=5):
    return reference_value * tolerance_percentage / 100
