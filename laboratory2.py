def add_listener(obj, method_name, listener):

    # Get any existing listeners
    listener_attr = method_name + '_listeners'
    listeners = getattr(obj, listener_attr, None)

    # If this is the first listener, then set up the method wrapper
    if not listeners:

        listeners = [listener]
        setattr(obj, listener_attr, listeners)

        # Get the object's method
        method = getattr(obj, method_name)

        @wraps(method)
        def method_wrapper(*args, **kwags):
            method(*args, **kwags)
            for l in listeners:
                l(obj, *args, **kwags) # Listener also has object argument

        # Replace the original method with the wrapper
        setattr(obj, method_name, method_wrapper)

    else:
        # Event is already set up, so just add another listener
        listeners.append(listener)


def remove_listener(obj, method_name, listener):

    # Get any existing listeners
    listener_attr = method_name + '_listeners'
    listeners = getattr(obj, listener_attr, None)

    if listeners:
        # Remove the listener
        next((listeners.pop(i)
              for i, l in enumerate(listeners)
              if l == listener),
             None)

        # If this was the last listener, then remove the method wrapper
        if not listeners:
            method = getattr(obj, method_name)
            delattr(obj, listener_attr)
            setattr(obj, method_name, method.__wrapped__)
