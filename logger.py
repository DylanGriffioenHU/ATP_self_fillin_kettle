import functools

def log_arguments(function):
    """
    Logs the arguments for the given function and stores them in the .__logged_info member list

        Parameters:
                Function: the function you want to get logged

        Returns:
                wrapper: returns the wrapper function
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        """
        Takes the arguments from the function and the function name and turns it into a string which it puts in the .__logged_info member list

            Parameters:
                    *args, **kwargs the arguments from the function

            Returns:
                    None
        """
        def log_to_string(index, args_list, args_string):
            """
            Recursively adds all the arguments from the given list to a string which it returns

                Parameters:
                        args_list: a list with arguments that need to be turned into a string

                Returns:
                        args_string: a string containing all the arguments from the function
            """
            if index == len(args_list):
                return args_string
            args_string += ", " + (str(args_list[index]))
            return log_to_string(index+1, args_list, args_string)

        if args:
            arguments = str(args[0])
            if args[1:]:
                arguments += log_to_string(0, args[1:],'')
        # the first element of the list is added without using the recursive function to ensure the , isn't place in front of the first element

            log_entry = f"Called function {function.__name__} with arguments: {arguments}"
        else:
            log_entry = f"Called function {function.__name__} without arguments" # still log the  function name if said function has no arguments
        log_arguments.__logged_info__.append(log_entry)
        return function(*args, **kwargs)
    return wrapper

log_arguments.__logged_info__ = []

def show_log():
    """
    Prints the data from the .__logged_info member list and then clears the log list

        Parameters:
                None

        Returns:
                None
    """
    def print_log(log_list):
        """
        Recursively goes through the given log list and prints the items within it

            Parameters:
                    log_list: the list of log items you wish the function to print in this case log_arguments.__logged_info__ 

            Returns:
                    None
        """
        if not log_list: # stops the function of the list is empty
            return
        print(log_list[0]) # prints the first item from the list
        if log_list[1:]:
            print_log(log_list[1:]) # calls the function again with the remainder of the list

    print_log(log_arguments.__logged_info__)
     
    log_arguments.__logged_info__ = []
