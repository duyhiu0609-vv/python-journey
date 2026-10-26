# 🧪 Week 14 — OOP Essentials: Bài tập thực hành

> **Mục tiêu:** Luyện tập lập trình hướng đối tượng (OOP) trong Python qua class, composition và inheritance.

📁 **Thư mục:** `weeks/week-14-oop-essentials/exercises/`

---

## 🎯 Nội dung bài tập

| Bài | Chủ đề | Nội dung chính | Trạng thái |
|---|---|---|---|
| [Exercise 01 — Classes](./ex01_classes.py) | Class & Object | Khởi tạo đối tượng, thuộc tính, phương thức, `__str__()` | ✅ Đã hoàn thành |
| [Exercise 02 — Composition](./ex02_composition.py) | Composition & Strategy | Truyền hành vi vào `Bot`, đổi chiến lược mà không sửa class | ✅ Đã hoàn thành |
| [Exercise 03 — Inheritance](./ex03_inheritance.py) | Inheritance | Tạo `Dog` kế thừa `Animal`, ghi đè/mở rộng hành vi | ✅ Đã hoàn thành |

## 📚 Kiến thức cần nắm

### 1. Class và Object
- **Class** là bản thiết kế để tạo đối tượng.
- **Object** là một thực thể được tạo từ class.
- `__init__()` khởi tạo dữ liệu ban đầu cho đối tượng.
- `self` tham chiếu đến đối tượng hiện tại.
- Phương thức `__str__()` cung cấp nội dung dễ đọc khi dùng `print(object)`.

### 2. Composition và Strategy
- **Composition** giúp một đối tượng sử dụng một thành phần khác để thực hiện công việc.
- Bài tập dùng `Bot` nhận một strategy (hàm chiến lược) từ bên ngoài.
- Có thể thay đổi chiến lược như `defensive`, `balanced`, `aggressive` mà không cần sửa phần cốt lõi của `Bot`.
- Ý tưởng chính: **tách hành vi có thể thay đổi khỏi class chính**.

### 3. Inheritance
- **Inheritance (kế thừa)** biểu diễn quan hệ “is-a”.
- `Dog(Animal)` nghĩa là `Dog` là một loại `Animal`.
- `Dog` kế thừa thuộc tính `name` từ `Animal` và bổ sung phương thức `speak()`.
- Chỉ nên dùng kế thừa khi quan hệ giữa các lớp thực sự phù hợp.

---

## ▶️ Cách chạy bài

Mở terminal tại thư mục gốc repository, sau đó chạy từng file:

```bash
python weeks/week-14-oop-essentials/exercises/ex01_classes.py
python weeks/week-14-oop-essentials/exercises/ex02_composition.py
python weeks/week-14-oop-essentials/exercises/ex03_inheritance.py
```

Nếu máy dùng lệnh `python3`, thay `python` bằng `python3`.

## ✅ Kiểm tra bài làm

Chạy bộ kiểm tra của Week 14:

```bash
python weeks/week-14-oop-essentials/checks/check_week.py
```

Kết quả mong đợi khi các kiểm tra đều đạt:

```text
Week 14 solution checks: PASS
```

> Lưu ý: kết quả trên là kết quả mong đợi của bộ kiểm tra; hãy chạy lệnh trên máy của bạn để xác nhận thực tế.

---

## 🧠 Checklist tự ôn tập

- [ ] Giải thích được sự khác nhau giữa class và object.
- [ ] Nêu được vai trò của `self` và `__init__()`.
- [ ] Biết khi nào `__str__()` được gọi.
- [ ] Giải thích được vì sao có thể truyền strategy vào `Bot`.
- [ ] Phân biệt được composition và inheritance.
- [ ] Giải thích được quan hệ “is-a” qua ví dụ `Dog` và `Animal`.
- [ ] Tự chạy được cả ba bài và bộ kiểm tra.

## 🗺️ Lộ trình học

```text
Class & Object
      ↓
Composition + Strategy
      ↓
Inheritance
      ↓
Mini-project / áp dụng OOP
```

---

**Gợi ý học hiệu quả:** Đừng chỉ đọc code đã hoàn thành. Hãy thử đổi giá trị đầu vào, thêm một strategy mới hoặc tạo thêm một lớp con để hiểu vì sao chương trình hoạt động như vậy.
