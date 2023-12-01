def get_solution(day):
    if not isinstance(day, int) or day < 1 or day > 31:
        return f"Error: \"day\" must be integer between 1 and 31"

    if day == 1:
        return "TODO day 1"
    
    return f"Day {day} solution not available"