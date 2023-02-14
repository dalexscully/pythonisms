from functools import wraps

def nice_day(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    original_val = func(*args, **kwargs)
    return f'Have a nice day "{original_val}"'
  return wrapper

@nice_day
def decorate(text):
    return text
