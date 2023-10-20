
from calc_sandpaper import get_sandpaper_info
from calc_sandingbelt import get_sandingbelt_info

calculating = True

while calculating:
    wire_speed = float(input("Wire Speed(m/s):"))
    follow_ratio_spindle = float(input("Follow Ratio for Spindle:"))
    follow_ratio_sandingbelt = float(input("Follow Ratio for Sandingbelt:"))
    current_length = input("현재 코일사용길이(m) ['ex' to exit]:")

    if current_length == "ex":
        calculating = False
    else:
        sandpaper_data = get_sandpaper_info(wire_speed, follow_ratio_spindle, follow_ratio_sandingbelt)
        sandingbelt_data = get_sandingbelt_info(sandpaper_data["sbf"], sandpaper_data["sbs"], sandpaper_data["sbft3"], current_length)

        print("📌")
        print("Spindle 기본주파수:", sandpaper_data["spf"], "Hz")
        print("Spindle 기본회전속도:", round(sandpaper_data["sps"], 2), "rpm")
        print("Spindle 기본회전수:", round(sandpaper_data["sprt3"], 2), "rev/300mm")
        print("Sandingbelt 기본주파수:", sandpaper_data["sbf"], "Hz")
        print("Sandingbelt 기본전진속도:", round(sandpaper_data["sbs"], 2), "m/s")
        print("Sandingbelt 기본전진거리:", round(sandpaper_data["sbft3"], 2), "m/300mm")
        print("------------------------")
        if sandingbelt_data["frequency"] != 0:
            print(f"현재 {sandingbelt_data['x+1']}번째 설정구간(<{format(sandingbelt_data['phase_interval'][sandingbelt_data['x+1']], ',d')}m)에서 가동 중")
            print("Sandingbelt 주파수:", round(sandingbelt_data["frequency"], 2), 'Hz')
            print("Sandingbelt 전진속도:", round(sandingbelt_data["speed"], 2), 'm/s')
            print("Sandingbelt 전진거리:", round(sandingbelt_data["forward"], 2), 'm/300mm') 
            print("------------------------")
        else:
            print("샌딩벨트를 설정 이상으로 오래 사용 중입니다. 교체해주세요!")