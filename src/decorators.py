from functools import wraps


def cache_results(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        if key in cache:
            print(f"[CACHE] Using cached result for {func.__name__}")
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


def validate_columns(required_columns):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            missing = [col for col in required_columns if col not in self.data.columns]

            if missing:
                raise ValueError(
                    f"Missing required columns: {missing} "
                    f"in function {func.__name__}"
                )

            return func(self, *args, **kwargs)

        return wrapper

    return decorator
