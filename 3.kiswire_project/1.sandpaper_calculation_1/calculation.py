
import math

def get_sandpaper_info(wire_speed, follow_ratio_spindle, follow_ratio_sandingbelt, current_length):

    # Sandpaper Spindle 및 sanding belt 기본조건계산
    
    spindle_frequency = wire_speed * follow_ratio_spindle * 10
    spindle_speed = 120 / 6 * spindle_frequency * 0.98 * 27 / 51
    spindle_revolution_thru_300mm = spindle_speed / 60 / wire_speed * 0.3
    
    sandingbelt_frequency = wire_speed * follow_ratio_sandingbelt * 10 
    sandingbelt_speed = 120 / 6 * sandingbelt_frequency * 0.98 * 27 / 43 * 30 /43 * 43 / 30 / 60 * math.pi * 92 / 1000    
    sandingbelt_forward_thru_300mm = 0.3 / wire_speed * sandingbelt_speed

    print("📌")
    print("Spindle 주파수:", spindle_frequency, "Hz")
    print("Spindle 회전속도:", round(spindle_speed, 2), "rpm")
    print("Spindle 회전수:", round(spindle_revolution_thru_300mm, 2), "rev/300mm")
    print("Sandingbelt 기본주파수:", sandingbelt_frequency, "Hz")
    print("Sandingbelt 기본전진속도:", round(sandingbelt_speed, 2), "m/s")
    print("Sandingbelt 기본전진거리:", round(sandingbelt_forward_thru_300mm, 2), "m/300mm")


    # Sandpaper 의 sandingbelt 사용 정도에 따른 속도제어 계산
    
    coil = {
        'length' : 10747,
        'usage' : 12
    }

    phase_ratio = [0.00, 1.00, 1.05, 1.10, 1.15]

    phase_interval = [0, 30000, 50000, 90000, coil.get('length') * coil.get('usage')]

    def get_sandingbelt_figures(frequency, speed, forward):
        print("Sandingbelt 주파수:", round(frequency, 2), 'Hz')
        print("Sandingbelt 전진속도:", round(speed, 2), 'm/s')
        print("Sandingbelt 전진거리:", round(forward, 2), 'm/300mm')    
        
    # current_length 는 loop 종료를 위해 문자열로 받았으므로 int 로 변환시켜줘야 함.
    current_length = int(current_length)
    
    for x in [0, 1, 2, 3, 4]:
        if current_length >= phase_interval[x] and current_length < phase_interval[x+1]:
            sandingbelt_frequency = sandingbelt_frequency * phase_ratio[x+1]
            sandingbelt_speed = sandingbelt_speed * phase_ratio[x+1]
            sandingbelt_forward_thru_300mm = sandingbelt_forward_thru_300mm * phase_ratio[1]
            print("------------------------")
            print(f"현재 첫번째 설정구간(<{format(phase_interval[x+1], ',d')}m)에서 가동 중")
            get_sandingbelt_figures(sandingbelt_frequency, sandingbelt_speed, sandingbelt_forward_thru_300mm)
            print("------------------------")

    
    
    
    
    
    
    
    
    
    """
    if current_length >= phase_interval[0] and current_length < phase_interval[1]:
        sandingbelt_frequency = sandingbelt_frequency * phase_ratio[1]
        sandingbelt_speed = sandingbelt_speed * phase_ratio[1]
        sandingbelt_forward_thru_300mm = sandingbelt_forward_thru_300mm * phase_ratio[1]
        print("------------------------")
        print(f"현재 첫번째 설정구간(<{format(phase_interval[1], ',d')}m)에서 가동 중")
        get_sandingbelt_figures(sandingbelt_frequency, sandingbelt_speed, sandingbelt_forward_thru_300mm)
        print("------------------------")
        
    elif current_length >= phase_interval[1] and current_length < phase_interval[2]:
        sandingbelt_frequency = sandingbelt_frequency * phase_ratio[2]
        sandingbelt_speed = sandingbelt_speed * phase_ratio[2]
        sandingbelt_forward_thru_300mm = sandingbelt_forward_thru_300mm * phase_ratio[2]
        print("------------------------")
        print(f"현재 두번째 설정구간(<{format(phase_interval[2], ',d')}m)에서 가동 중")
        get_sandingbelt_figures(sandingbelt_frequency, sandingbelt_speed, sandingbelt_forward_thru_300mm)
        print("------------------------")
        
    elif current_length >= phase_interval[2] and current_length < phase_interval[3]:
        sandingbelt_frequency = sandingbelt_frequency * phase_ratio[3]
        sandingbelt_speed = sandingbelt_speed * phase_ratio[3]
        sandingbelt_forward_thru_300mm = sandingbelt_forward_thru_300mm * phase_ratio[3]
        print("------------------------")
        print(f"현재 세번째 설정구간(<{format(phase_interval[3], ',d')}m)에서 가동 중")
        get_sandingbelt_figures(sandingbelt_frequency, sandingbelt_speed, sandingbelt_forward_thru_300mm)
        print("------------------------")
        
    elif current_length >= phase_interval[3] and current_length < phase_interval[4]:
        sandingbelt_frequency = sandingbelt_frequency * phase_ratio[4]
        sandingbelt_speed = sandingbelt_speed * phase_ratio[4]
        sandingbelt_forward_thru_300mm = sandingbelt_forward_thru_300mm * phase_ratio[4]
        print("------------------------")
        print(f"현재 네번째 설정구간(<{format(phase_interval[4], ',d')}m)에서 가동 중")
        get_sandingbelt_figures(sandingbelt_frequency, sandingbelt_speed, sandingbelt_forward_thru_300mm)
        print("------------------------")
        
    else:
        print("------------------------")
        print(f"{format(phase_interval[4], ',d')}m 초과\n샌딩벨트를 설정 이상으로 오래 사용 중입니다. 교체해주세요!")
        print("------------------------")
    """
