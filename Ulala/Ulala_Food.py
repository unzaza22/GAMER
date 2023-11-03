def calculate_items_to_minimize_points(points, item_points):
    count = [0] * len(item_points)  # สร้างลิสต์เพื่อเก็บจำนวนของแต่ละชิ้น
    current_points = 0

    # ลูปจนกว่าแต้มที่ได้จะเกิน points ที่กำหนด
    while current_points <= points:
        for i in range(len(item_points)):
            # หากการเพิ่มชิ้นต่อไปยังไม่ทำให้แต้มเกิน หรือชิ้นนั้นคือชิ้นที่มีแต้มน้อยที่สุด
            if current_points + item_points[i] <= points or i == len(item_points) - 1:
                current_points += item_points[i]
                count[i] += 1
                break  # หยุดลูปและเริ่มนับชิ้นใหม่

    # แสดงผลลัพธ์
    print("ของที่ได้รับ:")
    for i, cnt in enumerate(count, start=1):
        if cnt > 0:
            print(f"ของชิ้นที่ {i}: {cnt} ชิ้น")
    print(f"แต้มที่ใช้ไปทั้งหมด: {current_points} (เกิน {current_points - points} แต้ม)")

# แต้มที่ต้องการ
points = 800

# แต้มของแต่ละชิ้น
item_points = [300, 150, 85, 45]

# คำนวณของ
calculate_items_to_minimize_points(points, item_points)

