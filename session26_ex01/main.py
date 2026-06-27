'''
Phân tích
1. Vì lớp con Warrio hàm __init__ ghi đè lớp cha (Character) nên các thuộc tính chưa xuất hiện trong Warrio
Thiếu dòng khởi tạo super().__init__(name, hp, attack_power)
2. Gọi bằng: Character.__init__(self, name, hp, attack_power)
3. Lỗi TypeError
Vì toán tử > không có quy tắc sẵn để biết nên so sánh hp, attack_power hay bonus_armor của nhân vật
4. Magic method cần dùng: __gt__
Nhận vào 2 tham số self, other
'''

# Sửa lỗi
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

class Warrior(Character):
    def __init__(self, name, hp, attack_power, bonus_armor):
        super().__init__(name, hp, attack_power)
        self.bonus_armor = bonus_armor

    def get_total_power(self):
        return self.attack_power + self.bonus_armor

    def __gt__(self, other):
        if isinstance(other, Warrior):
            return self.get_total_power() > other.get_total_power()
        return NotImplemented

w1 = Warrior("Arthur", 1000, 150, 50)
w2 = Warrior("Lancelot", 900, 180, 10)

print(f"Chiến binh {w1.name} xuất trận!")

if w1 > w2:
    print(f"{w1.name} mạnh hơn {w2.name}!")
else:
    print(f"{w2.name} mạnh hơn hoặc hòa!")