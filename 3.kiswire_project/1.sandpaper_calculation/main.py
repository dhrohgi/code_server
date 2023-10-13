from calculation import get_sandpaper_info

calculating = True

while calculating:
    wire_speed = float(input("Wire Speed(m/s):"))
    follow_ratio_spindle = float(input("Follow Ratio for Spindle:"))
    follow_ratio_sandingbelt = float(input("Follow Ratio for Sandingbelt:"))
    current_length = input("현재 코일사용길이(m)\n['ex' to exit]:")

    if current_length == "ex":
        calculating = False
    else:
        get_sandpaper_info(wire_speed, follow_ratio_spindle, follow_ratio_sandingbelt, current_length)
