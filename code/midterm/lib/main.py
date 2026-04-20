from room_sensor import RoomSensor   # 가져오기

def main():
    # 센서 값 자유롭게 정하기 
    sensors = [
        RoomSensor("Kitchen", 30, 50, 180),
        # 온도가 딱 30이기 때문에 Warning이 출력, 조도도 180으로 Dark
        RoomSensor("Bedroom", 22, 40, 150),
        # 온도가 20~26사이, 습도가 40~60사이 이므로 Comfortable이 출력, 조도또한 Dark로 출력
        RoomSensor("Balcony", 18, 32, 900)
        # 온도가 30이상도 아니도 20~26사이도 아니어서 Normal출력, 조도가 200이상이므로 Bright 출력
    ]

    # 추가 도전 과제
    comfort_counts = {
        "Comfortable": 0,
        "Normal": 0,
        "Warning": 0
    }


    for sensor in sensors:
        sensor.show_info()
        
        c_level = sensor.comfort_level()
        l_status = sensor.light_status()
        
        print(f"Comfort Level: {c_level}")
        print(f"Light Status: {l_status}")
        print("-" * 25) # 구분을 위한 시각적 선
        
        if c_level in comfort_counts:
            comfort_counts[c_level] += 1

    print(f"Comfortable: {comfort_counts['Comfortable']}")
    print(f"Normal: {comfort_counts['Normal']}")
    print(f"Warning: {comfort_counts['Warning']}")

if __name__ == "__main__":
    main()