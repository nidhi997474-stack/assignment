def format_follower_count(n):
    if n >= 1000000:
        return str(round(n / 1000000, 1)) + "M"
    elif n >= 1000:
        return str(round(n / 1000, 1)) + "K"
    else:
        return str(n)