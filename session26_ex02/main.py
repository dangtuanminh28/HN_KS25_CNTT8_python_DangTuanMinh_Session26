'''
Phân tích
1. Python không cần biết trước kiểu dữ liệu cụ thể của từng hero, nó chỉ đọc đối tượng đó có phương thức use_ultimate()
2. Khi đối tượng Assassin thực sự gọi hàm use_ultimate() khi vòng lặp chạy đến phần tử thứ hai trong giao tranh
Khiến người chơi đã tốn thời gian tải trận, chọn tướng, đang combat thì game đột ngột bị sập. Gây ức chế và làm giảm tỷ lệ giữ chân người chơi
3. Thời điểm văng lỗi: khởi tạo đối tượng Assassin(), tức là ngay dòng code team_heroes = [Mage(), Assassin()]
4. Giúp các lập trình viên, tester phát hiện lỗi ngay lập tức trong quá trình phát triển (Development) trước khi game được phát hành
'''


# Sửa lỗi
from abc import ABC, abstractmethod

class Hero(ABC):
    @abstractmethod
    def use_ultimate(self):
        pass

class Mage(Hero):
    def use_ultimate(self):
        print("🔥 Pháp Sư tung chiêu: MƯA SAO BĂNG!")

class Assassin(Hero):
    def use_ultimate(self):
        print("🗡️ Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")

print("--- LOADING TRẬN ĐẤU ---")
team_heroes = [Mage(), Assassin()] 
print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")
for hero in team_heroes:
    hero.use_ultimate()