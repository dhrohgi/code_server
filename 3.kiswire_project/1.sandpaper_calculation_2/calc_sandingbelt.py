
# Sandpaper 의 sandingbelt 사용 정도에 따른 속도제어 계산

def get_sandingbelt_info(frequency, speed, forward, length):
    coil = {
        'length' : 10747,
        'usage' : 12
    }

    phase_ratio = [0.00, 1.00, 1.05, 1.10, 1.15]

    phase_interval = [0, 30000, 50000, 90000, coil.get('length') * coil.get('usage')]
            

    # current_length 는 loop 종료를 위해 문자열로 받았으므로 int 로 변환시켜줘야 함.
    length = int(length)

    for x in [0, 1, 2, 3, 4]:
        if length > phase_interval[4]:
            sandingbelt_data = {
                    "phase_ratio": phase_ratio,
                    "phase_interval": phase_interval,
                    "frequency": 0,
                    "speed": 0,
                    "forward": 0,
                    "x+1": x+1
                }        
        else:
            if length >= phase_interval[x] and length < phase_interval[x+1]:
                frequency = frequency * phase_ratio[x+1]
                speed = speed * phase_ratio[x+1]
                forward = forward * phase_ratio[x+1]

                sandingbelt_data = {
                    "phase_ratio": phase_ratio,
                    "phase_interval": phase_interval,
                    "frequency": frequency,
                    "speed": speed,
                    "forward": forward,
                    "x+1": x+1
                }
                
    return sandingbelt_data