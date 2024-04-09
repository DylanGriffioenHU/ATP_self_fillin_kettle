import functools

def log_arguments(function):
    """
    Logs the arguments for the given function

    Logs the decorated function arguments  which are stored in the .__logged_info member list

        Parameters:
                        Function: the function you want to get logged

                Returns:
                        wrapper: returns the wrapper function
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        def log_to_string(index, args_list, args_string):
            if index == len(args_list):
                return args_string
            args_string += (str(args_list[index]))
            return log_to_string(index+1, args_list, args_string)

        arguments = log_to_string(0, args,'')

        log_entry = f"Called function {function.__name__} with arguments: {arguments}"
        log_arguments.__logged_info__.append(log_entry)
        return function(*args, **kwargs)
    return wrapper

log_arguments.__logged_info__ = []

def show_log():
    def print_log(log_list):
        if not log_list:
            return
        print(log_list[0])
        if log_list[1:]:
            print_log(log_list[1:])

    print_log(log_arguments.__logged_info__)
     
    log_arguments.__logged_info__ = []