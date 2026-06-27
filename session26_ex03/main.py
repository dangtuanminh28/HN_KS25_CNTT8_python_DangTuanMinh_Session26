from abc import ABC, abstractmethod

class Champion(ABC):
    def __init__(self, champion_id: str, name: str, base_hp: int, base_atk: int):
        self.champion_id = champion_id
        self.name = name
        self.base_hp = base_hp
        self.base_atk = base_atk

    @abstractmethod
    def calculate_skill_damage(self):
        pass

    def get_combat_power(self):
        return self.base_hp + (self.calculate_skill_damage() * 1.5)

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return self.get_combat_power() + other
        elif hasattr(other, 'get_combat_power'):
            return self.get_combat_power() + other.get_combat_power()  
        else:
            return NotImplemented

    def __gt__(self, other):
        if hasattr(other, 'get_combat_power'):
            return self.get_combat_power() > other.get_combat_power()
        return NotImplemented

class Warrior(Champion):
    def __init__(self, champion_id: str, name: str, base_hp: int, base_atk: int, shield_bonus: int):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus
        self.role = "Warrior"

    def calculate_skill_damage(self):
        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):
    def __init__(self, champion_id: str, name: str, base_hp: int, base_atk: int, ability_power: float):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power
        self.role = "Mage"

    def calculate_skill_damage(self):
        return self.base_atk * self.ability_power
    
champion_pool = [
        Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
        Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
        Mage("MAG01", "Rikkei Wizard", 800, 500, 2.5)
]

def show_champion(champion_pool):
    if not champion_pool:
        print("Không có tướng nào trong bể tướng hiện tại!")
        return
    else :
        print("--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")
        print(f"{'Mã':<8} | {'Tên tướng':<20} | {'Hệ':<8} | {'HP':<5} | {'ATK':<5} | {'Chỉ số riêng':<17} | {'Chiến lực'}")
        print("-----------------------------------------------------------------------------------------------------")
        for champ in champion_pool:
            if champ.role == "Warrior":
                index_champ = f"Armor: {champ.shield_bonus}"
            else:
                index_champ = f"Mana: {champ.ability_power}"

            print(f"{champ.champion_id:<8} | {champ.name:<20} | {champ.role:<8} | {champ.base_hp:<5} | {champ.base_atk:<5} | {index_champ:<17} | {int(champ.get_combat_power())}")
        
        print("-----------------------------------------------------------------------------------------------------")

def add_champion(champion_pool):
    print("--- THÊM QUÂN CỜ MỚI ---")
    
    while True:
        print("Chọn hệ tộc cho tướng mới:")
        print("1. Hệ Chiến binh (Warrior)")
        print("2. Hệ Pháp sư (Mage)")
        
        choice = input("Nhập lựa chọn của bạn (1 hoặc 2): ").strip()
        
        if choice == '1':
            print("--- TẠO TƯỚNG WARRIOR ---")
            
            while True:
                champion_id = input("Nhập mã tướng: ").strip().upper()
                if not champion_id:
                    print("Mã tướng không được để trống! Vui lòng nhập lại.")
                    continue
                is_same = False
                for champ in champion_pool:
                    if champ.champion_id == champion_id:
                        is_same = True
                        break
                
                if is_same:
                    print(f"Mã tướng '{champion_id}' đã tồn tại trong hệ thống!")
                    continue
                break
            
            while True:
                name = input("Nhập tên tướng: ").strip()
                if not name:
                    print("Tên tướng không được để trống! Vui lòng nhập lại.")
                    continue
                break
                
            while True:
                hp_in = input("Nhập HP: ").strip()
                if not hp_in:
                    print("HP không được để trống! Vui lòng nhập lại.")
                    continue
                base_hp = int(hp_in)
                if base_hp <= 0:
                    print("HP không được nhỏ hơn hoặc bằng 0!")
                    print("Hệ thống tự động đặt về 100")
                    base_hp = 100
                break
                
            while True:
                atk_in = input("Nhập ATK: ").strip()
                if not atk_in:
                    print("ATK không được để trống! Vui lòng nhập lại.")
                    continue
                base_atk = int(atk_in)
                if base_atk <= 0:
                    print("ATK không được nhỏ hơn hoặc bằng 0!")
                    print("Hệ thống tự động đặt về 100")
                    base_atk = 100
                break
                
            while True:
                armor_in = input("Nhập Armor: ").strip()
                if not armor_in:
                    print("Armor không được để trống! Vui lòng nhập lại.")
                    continue
                shield_bonus = int(armor_in)
                if shield_bonus <= 0:
                    print("Armor không được nhỏ hơn hoặc bằng 0!")
                    print("Hệ thống tự động đặt về 100")
                    shield_bonus = 100
                break
            
            new_champ = Warrior(champion_id, name, base_hp, base_atk, shield_bonus)
            champion_pool.append(new_champ)
            
            print(f"Thêm tướng Warrior thành công!")
            print(f"Mã: {new_champ.champion_id} | Tên: {new_champ.name} | Chiến lực: {int(new_champ.get_combat_power())}")
            break
        elif choice == '2':
            print("--- TẠO TƯỚNG MAGE ---")
            
            while True:
                champion_id = input("Nhập mã tướng: ").strip().upper()
                if not champion_id:
                    print("Mã tướng không được để trống! Vui lòng nhập lại.")
                    continue
                is_same = False
                for champ in champion_pool:
                    if champ.champion_id == champion_id:
                        is_same = True
                        break
                
                if is_same:
                    print(f"Mã tướng '{champion_id}' đã tồn tại trong hệ thống!")
                    continue
                break
            
            while True:
                name = input("Nhập tên tướng: ").strip()
                if not name:
                    print("Tên tướng không được để trống! Vui lòng nhập lại.")
                    continue
                break
                
            while True:
                hp_in = input("Nhập HP: ").strip()
                if not hp_in:
                    print("HP không được để trống! Vui lòng nhập lại.")
                    continue
                base_hp = int(hp_in)
                if base_hp <= 0:
                    print("HP không được nhỏ hơn hoặc bằng 0!")
                    print("Hệ thống tự động đặt về 100")
                    base_hp = 100
                break
                
            while True:
                atk_in = input("Nhập ATK: ").strip()
                if not atk_in:
                    print("ATK không được để trống! Vui lòng nhập lại.")
                    continue
                base_atk = int(atk_in)
                if base_atk <= 0:
                    print("ATK không được nhỏ hơn hoặc bằng 0!")
                    print("Hệ thống tự động đặt về 100")
                    base_atk = 100
                break
                
            while True:
                ap_in = input("Nhập hệ số phép thuật (AP): ").strip()
                if not ap_in:
                    print("Hệ số phép thuật không được để trống! Vui lòng nhập lại.")
                    continue
                ability_power = float(ap_in)
                if ability_power <= 0:
                    print("Số phép thuật không được nhỏ hơn hoặc bằng 0!")
                    print("Hệ thống tự động đặt về 100")
                    ability_power = 100
                break
            
            new_champ = Mage(champion_id, name, base_hp, base_atk, ability_power)
            champion_pool.append(new_champ)
            
            print(f"\nThêm tướng Mage thành công!")
            print(f"Mã: {new_champ.champion_id} | Tên: {new_champ.name} | Chiến lực: {int(new_champ.get_combat_power())}")
            break
            
        else:
            print("Lựa chọn không hợp lệ!(1-2)")

def compare_champion(champion_pool):
    print("--- SO SÁNH SỨC MẠNH 2 QUÂN CỜ ---")
    
    if len(champion_pool) < 2:
        print("Bệ tướng phải có ít nhất 2 quân để so sánh!")
        return

    while True:
        id1 = input("Nhập mã thứ nhất: ").strip()
        if not id1:
            print("Mã không được để trống!")
            continue
        break

    while True:
        id2 = input("Nhập mã thứ hai: ").strip()
        if not id2:
            print("Mã không được để trống!")
            continue
        break

    champion1 = None
    champion2 = None

    for champ in champion_pool:
        if champ.champion_id == id1:
            champion1 = champ
        if champ.champion_id == id2:
            champion2 = champ

    if champion1 is None:
        print(f"Không tìm thấy {id1} trong hệ thống!")
        return
    if champion2 is None:
        print(f"Không tìm thấy {id2} trong hệ thống!")
        return

    print("\nThong tin so sanh:")
    print(f"{champion1.champion_id} - {champion1.name} | He: {champion1.role:<7} | Chien luc: {int(champion1.get_combat_power())}")
    print(f"{champion2.champion_id} - {champion2.name} | He: {champion2.role:<7} | Chien luc: {int(champion2.get_combat_power())}")
    
    print("Kết quả:")
    if champion1 > champion2:
        print(f"{champion1.champion_id} - {champion1.name} mạnh hơn {champion2.champion_id} - {champion2.name}.")
    elif champion2 > champion1:
        print(f"{champion2.champion_id} - {champion2.name} mạnh hơn {champion1.champion_id} - {champion1.name}.")
    else:
        print(f"Cả 2 tướng {champion1.name} và {champion2.name} có chiến lực bằng nhau")

def calculate_team_combat(champion_pool):
    print("--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH RA SÂN ---")
    
    if not champion_pool:
        print("Bể tướng rỗng, không thể xây dựng đội hình!")
        return

    while True:
        raw_input = input("Nhập danh sách mã tướng, cách nhau bằng dấu phẩy: ").strip()
        if not raw_input:
            print("Danh sách không được để trống!")
            continue
        break

    input_ids = raw_input.split(",")
    team_list = []
    for raw_id in input_ids:
        clean_id = raw_id.strip()
        if clean_id:
            for champ in champion_pool:
                if champ.champion_id == clean_id:
                    team_list.append(champ)
                    break

    if not team_list:
        print("Không có tướng hợp lệ nào được tìm thấy từ danh sách bạn đã nhập!")
        return

    print("Danh sách đội hình:")
    stt = 1
    for champ in team_list:
        print(f"{stt}. {champ.champion_id} - {champ.name} | Chiến lực: {int(champ.get_combat_power())}")
        stt += 1

    total_power = 0
    for champ in team_list:
        total_power = total_power + champ

    print(f"Tổng chiến lực đội hình: {int(total_power)}")
while True :
    print("""
--- HỆ THỐNG Rikkei RPG ---
1. Hiển thị bể tướng hiện có
2. Thêm quân cờ mới
3. So sánh 2 quân cờ
4. Tính tổng chiến lực Đội Hình Ra Sân
5. Thoát chương trình           
---------------------------------
""")
    choice = input("Chọn chức năng (1-5): ").strip()
    if choice == '1' :
        show_champion(champion_pool)
    elif choice == '2' :
        add_champion(champion_pool)
    elif choice == '3' :
        compare_champion(champion_pool)
    elif choice == '4' :
        calculate_team_combat(champion_pool)
    elif choice == '5' :
        print("Cảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager!")
        break
    else :
        print("Vui lòng nhập lại!")