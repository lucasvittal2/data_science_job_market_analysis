import numpy as np

def generate_scaled_ticks(original_data, scaling, n_ticks, start_with_0=False):
    
    power = int(np.log10(scaling))
    
    scaled_data= original_data / scaling
    lower = scaled_data.min() if not start_with_0 else 0
    upper= scaled_data.max()
    step = (upper - lower) / n_ticks
    scaled_ticks = [ round(el, 2) for el in np.arange(lower, upper + step, step)]
    
    ticks_config = ( scaled_data,scaled_ticks, power )
    
    return  ticks_config