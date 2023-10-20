
import math

def get_sandpaper_info(wire_speed, follow_ratio_spindle, follow_ratio_sandingbelt):

    # Sandpaper Spindle 및 sanding belt 기본조건계산
    
    spindle_frequency = wire_speed * follow_ratio_spindle * 10
    spindle_speed = 120 / 6 * spindle_frequency * 0.98 * 27 / 51
    spindle_revolution_thru_300mm = spindle_speed / 60 / wire_speed * 0.3
    
    sandingbelt_frequency = wire_speed * follow_ratio_sandingbelt * 10 
    sandingbelt_speed = 120 / 6 * sandingbelt_frequency * 0.98 * 27 / 43 * 30 /43 * 43 / 30 / 60 * math.pi * 92 / 1000    
    sandingbelt_forward_thru_300mm = 0.3 / wire_speed * sandingbelt_speed

    sandpaper_data = {
        "spf": spindle_frequency,
        "sps": spindle_speed,
        "sprt3": spindle_revolution_thru_300mm,
        "sbf": sandingbelt_frequency,
        "sbs": sandingbelt_speed,
        "sbft3": sandingbelt_forward_thru_300mm
    }
    
    return sandpaper_data