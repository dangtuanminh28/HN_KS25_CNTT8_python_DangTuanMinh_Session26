from abc import ABC, abstractmethod

class Equipment(ABC):
    @abstractmethod
    def calculate_total_damage(self):
        pass

class Weapon(Equipment):
    def __init__(self, item_id, name, base_damage, upgrade_level=0):
        if not item_id or not str(item_id).strip() or not name or not name.strip():
            raise ValueError("ID và tên không được để trống!")
        if any(item.item_id == item_id for item in inventory):
            raise ValueError("ID trang bị đã tồn tại!")
        if base_damage <= 0 or upgrade_level <= 0:
            raise ValueError("Giá trị phải lớn hơn 0!")

        self.item_id = item_id.strip()
        self.name = name.title().strip()
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        return self.base_damage + (self.upgrade_level * 10)

    def __gt__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError("Chỉ có thể so sánh giữa các trang bị!")
        return self.calculate_total_damage() > other.calculate_total_damage()

    def __add__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError("Chỉ có thể dung hợp giữa các trang bị!")

        new_id = f"F-{self.item_id}-{other.item_id}"
        new_name = f"Fusion({self.name} + {other.name})"
        new_base = self.base_damage + getattr(other, 'base_damage', 0)
        new_level = self.upgrade_level + getattr(other, 'upgrade_level', 0)

        return Weapon(new_id, new_name, new_base, new_level)

class MagicMixin:
    def __init__(self, magic_power):
        if magic_power <= 0:
            raise ValueError("Giá trị phải lớn hơn 0!")
        self.magic_power = magic_power

    def cast_glow(self):
        print(f"{self.name} đang phát sáng ma thuật!")

class MagicSword(Weapon, MagicMixin):
    def __init__(self, item_id, name, base_damage, upgrade_level, magic_power):
        Weapon.__init__(self, item_id, name, base_damage, upgrade_level)
        MagicMixin.__init__(self, magic_power)

    def calculate_total_damage(self):
        return super().calculate_total_damage() + self.magic_power


def safe_int_input(msg):
    try:
        value = int(input(msg))
        return value
    except:
        print("Vui lòng nhập số hợp lệ!")
        return None

inventory = []
def show_inventory():
    print("--- KHO VŨ KHÍ CỦA NGƯỜI CHƠI ---")
    if not inventory:
        print("Kho vũ khí hiện đang trống.")
        return

    for i, item in enumerate(inventory, 1):
        print(f"{i}. [ID: {item.item_id}] {item.name} | {type(item).__name__} | "
              f"Cấp: {item.upgrade_level} | Damage: {item.calculate_total_damage()}")


def create_weapon():
    print("--- RÈN VŨ KHÍ VẬT LÝ ---")
    item_id = input("Nhập ID: ")
    if not item_id or not item_id.strip():
        print("ID không được để trống!")
        return
    if any(item.item_id == item_id.strip() for item in inventory):
        print("ID trang bị đã tồn tại!")
        return

    name = input("Nhập tên: ")
    if not name or not name.strip():
        print("Tên không được để trống!")
        return

    base = safe_int_input("Nhập sát thương gốc: ")
    if base is None or base <= 0:
        print("Giá trị phải lớn hơn 0!")
        return

    level = safe_int_input("Nhập cấp cường hóa: ")
    if level is None or level <= 0:
        print("Giá trị phải lớn hơn 0!")
        return

    try:
        w = Weapon(item_id, name, base, level)
        inventory.append(w)
        print(">> Rèn thành công!", w.calculate_total_damage())
    except Exception as e:
        print(e)


def create_magic_sword():
    print("--- RÈN KIẾM MA THUẬT ---")
    item_id = input("Nhập ID: ")
    if not item_id or not item_id.strip():
        print("ID không được để trống!")
        return
    if any(item.item_id == item_id.strip() for item in inventory):
        print("ID trang bị đã tồn tại!")
        return

    name = input("Nhập tên: ")
    if not name or not name.strip():
        print("Tên không được để trống!")
        return
        
    base = safe_int_input("Nhập sát thương gốc: ")
    level = safe_int_input("Nhập cấp: ")
    magic = safe_int_input("Nhập sức mạnh phép: ")

    if None in (base, level, magic) or base <= 0 or level <= 0 or magic <= 0:
        print("Giá trị phải lớn hơn 0!")
        return
    try:
        ms = MagicSword(item_id, name, base, level, magic)
        inventory.append(ms)
        print(">> Thành công!", ms.calculate_total_damage())
    except Exception as e:
        print(e)


def compare_weapon():
    print("--- THẨM ĐỊNH VŨ KHÍ ---")
    if len(inventory) < 2:
        print("Cần ít nhất 2 vũ khí!")
        return

    w1, w2 = inventory[0], inventory[1]

    print(w1.name, w1.calculate_total_damage())
    print(w2.name, w2.calculate_total_damage())

    if w1 > w2:
        print(f"{w1.name} mạnh hơn {w2.name}")
    elif w2 > w1:
        print(f"{w2.name} mạnh hơn {w1.name}")
    else:
        print("Hai vũ khí ngang nhau")


def fuse_weapon():
    print("--- DUNG HỢP VŨ KHÍ ---")
    if len(inventory) < 2:
        print("Cần ít nhất 2 vũ khí!")
        return

    w1 = inventory.pop(0)
    w2 = inventory.pop(0)
    try:
        new_w = w1 + w2
        inventory.append(new_w)
        print(">> Dung hợp thành công!")
        print(new_w.name, new_w.calculate_total_damage())

    except Exception as e:
        print(e)

while True:
        print("""
===== LÒ RÈN VŨ KHÍ RIKKEI STUDIOS ===================
1. Xem kho vũ khí & Sát thương tổng
2. Rèn Vũ khí Vật lý (Tạo Weapon)
3. Rèn Kiếm Ma Thuật (Tạo MagicSword)
4. Thẩm định vũ khí (So sánh lớn hơn)
5. Dung hợp vũ khí (Cộng dồn cấp độ)
6. Thoát game
====================================================== 
""")

        choice = input("Chọn chức năng (1-6): ")
        if choice == "1":
            show_inventory()
        elif choice == "2":
            create_weapon()
        elif choice == "3":
            create_magic_sword()
        elif choice == "4":
            compare_weapon()
        elif choice == "5":
            fuse_weapon()
        elif choice == "6":
            print("Thoát game!")
            break
        else:
            print("Lựa chọn không hợp lệ!")