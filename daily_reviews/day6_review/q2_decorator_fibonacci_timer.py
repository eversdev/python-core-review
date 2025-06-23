import time as t

def my_decorator(my_func):
    """
    Decorator to measure and print the execution time of the decorated function,
    but only for the outermost (initial) call.

    This is useful for recursive functions where multiple nested calls happen,
    preventing timing output from cluttering every recursive step.

    How it works:
    - Uses a function attribute `wrapper.running` to track if the function
      is already running.
    - When the outermost call starts, timing begins.
    - Nested recursive calls skip timing and just execute the function normally.
    - When the outermost call finishes, prints the total elapsed time.

    Args:
        my_func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function with execution timing logic.
    """
    def wrapper(*args, **kwargs):
        # Check if this is the first (outermost) call
        if not wrapper.running:
            wrapper.running = True  # mark as running
            start_time = t.time()
            result = my_func(*args, **kwargs)
            end_time = t.time()
            print(f"Execution time: {end_time - start_time:.6f} seconds")
            wrapper.running = False  # reset
            return result
        else:
            # If already running (recursive call), just call the function normally
            return my_func(*args, **kwargs)
    wrapper.running = False
    return wrapper

@my_decorator
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(35))














'''@my_decorator
def fibbonaci(n):
    prev = 0
    curr = 1
    for i in range(n):
        print(prev)
        temp = prev
        prev = curr
        curr = temp + curr
        
      
fibbonaci(10)

'''





    

