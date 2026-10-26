# Tuần 13 — Tách module, dựng CLI và hiểu HTTP

> **Chủ đề riêng của tuần:** biến một đoạn code chạy được thành một chương trình có ranh giới rõ ràng — biết phần nào ra quyết định, phần nào nhận lệnh và phần nào giao tiếp với bên ngoài.

Tuần 13 nằm ở bước chuyển từ “viết được hàm Python” sang “biết tổ chức một chương trình nhỏ”. Ta sẽ đi theo hành trình của một bot học tập: **Core suy nghĩ → Adapter đóng gói kết quả → CLI nhận lệnh → HTTP giúp hiểu cách dữ liệu đi qua mạng**.

**Learning loop:** `Read → Import → Run → Inspect → Test → Explain`

---

## 🐸 Câu chuyện của tuần: đừng để mọi thứ nằm trong một file

Hãy tưởng tượng bot là một đội nhỏ:

- **Bot Core** là người ra quyết định: nhận trạng thái, trả về hành động.
- **Adapter** là phiên dịch: chuyển dữ liệu đầu vào thành lời gọi Core và định dạng kết quả.
- **CLI** là quầy điều khiển: nhận tham số từ terminal bằng `argparse`.
- **HTTP layer** là đường giao tiếp: tạo request, đọc status code và phân tích JSON response.

Mỗi phần có một trách nhiệm riêng. Nhờ vậy, thay đổi cách nhập lệnh không buộc ta viết lại logic quyết định; học HTTP cũng không có nghĩa là phải đưa network vào Core.

```text
Terminal arguments
       │
       ▼
      CLI ───────► Adapter ───────► Bot Core
                                      │
                                      ▼
                               action / decision

HTTP lesson: request → response status → JSON parsing
              (fixture offline, không gọi production API)
```

## 🎯 Sau tuần này, bạn có thể

- [ ] Import hàm từ module khác và giải thích vì sao cần `__init__.py`.
- [ ] Dùng `if __name__ == "__main__":` để kiểm soát điểm bắt đầu chương trình.
- [ ] Hiểu vai trò của virtual environment, `python -m pip` và `pyproject.toml`.
- [ ] Khai báo tham số CLI bằng `argparse`, bao gồm kiểu dữ liệu và tham số bắt buộc.
- [ ] Phân biệt HTTP method, status code, response body và JSON.
- [ ] Nhận biết lỗi HTTP, JSON không hợp lệ và các rủi ro như timeout.
- [ ] Giải thích được vì sao Bot Core nên độc lập với CLI và network.
- [ ] Chạy self-check và dùng kết quả làm bằng chứng rằng các hành vi chính hoạt động.

## 🧭 Lộ trình thực hành

Nên học theo thứ tự này; mỗi bước chuẩn bị kiến thức cho bước kế tiếp.

| Bước | Tệp / nội dung | Việc cần làm |
|---|---|---|
| 1 | [Notes](notes.md) | Đọc các khái niệm và sơ đồ luồng chương trình |
| 2 | [Exercise 01](exercises/README.md) | Thực hành module, import và main guard |
| 3 | [Exercise 02](exercises/README.md) | Thêm `--turn` bằng `argparse` |
| 4 | [Exercise 03](exercises/README.md) | Phân tích JSON fixture và từ chối status lỗi |
| 5 | [Hints](hints.md) | Chỉ mở khi đã tự thử và cần gợi ý |
| 6 | [Mini-project](mini-project/README.md) | Theo luồng CLI → Adapter → Core |
| 7 | Self-check | Chạy kiểm tra offline ở cuối trang |

## ▶️ Chạy thử

Các lệnh dưới đây chạy từ thư mục gốc repository.

**1. Chạy CLI chính:**

```bash
python weeks/week-13-modules-cli-api/cli.py --position 1 --goal 4
```

Với ví dụ này, vị trí `1` nhỏ hơn mục tiêu `4`, nên Core chọn hành động `right`. Kết quả được in ra theo định dạng của course adapter; đây là định dạng phục vụ học tập, không phải giao thức production.

**2. Chạy bài tập riêng lẻ** — chuyển vào thư mục tuần trước:

```bash
cd weeks/week-13-modules-cli-api
python -m exercises.ex01_modules
python -m exercises.ex02_cli --turn 3
python -m exercises.ex03_http
```

Dùng `python -m exercises.<module>` giúp Python chạy bài tập theo ngữ cảnh package. Nếu chạy trực tiếp bằng đường dẫn file, việc tìm module cùng package có thể khác.

**3. Chạy self-check offline** — quay lại thư mục gốc repository:

```bash
python weeks/week-13-modules-cli-api/checks/check_week.py
```

Kết quả mong đợi khi các kiểm tra đều qua:

```text
Week 13 solution checks: PASS
```

> Nếu một lệnh báo lỗi, hãy kiểm tra thư mục hiện tại trong terminal, phiên bản Python, tên file và cách gọi module trước khi cài thêm thư viện.

## 🔍 Ba điều cần quan sát, không chỉ nhìn output

### 1. Module và package

Một file `.py` có thể là module; package gom các module liên quan. Import giúp tái sử dụng hành vi thay vì sao chép code. Main guard giúp tách việc **import** khỏi việc **chạy chương trình**.

### 2. CLI là lớp nhận lệnh

`argparse` biến chuỗi người dùng nhập trong terminal thành giá trị có tên và kiểu dữ liệu. CLI nên chuyển input tới hàm phù hợp, không ôm luôn logic nghiệp vụ.

### 3. HTTP status tốt chưa chắc JSON tốt

Một response có status thành công vẫn có thể chứa JSON sai định dạng hoặc dữ liệu không đúng kiểu mong đợi. Vì thế cần kiểm tra status và parse body riêng. Bài học dùng fixture tĩnh để bạn kiểm tra hành vi mà không phụ thuộc Internet.

## 🧱 Ranh giới quan trọng của project

```text
Bot Core       = quyết định dựa trên dữ liệu đầu vào
Adapter        = chuyển đổi / đóng gói dữ liệu
CLI            = giao diện dòng lệnh
HTTP foundation = kiến thức request/response và JSON
```

- Core không nên đọc trực tiếp `sys.argv` hay tự gọi mạng.
- Adapter trong tuần này là adapter phục vụ khóa học.
- Ví dụ HTTP dùng dữ liệu mẫu offline.
- Endpoint, authentication, schema và runtime contract của VuaCóc production **chưa được xác minh**; không suy đoán chúng từ fixture hoặc output của bài học.

Đây là chủ ý thiết kế: hiểu ranh giới trước khi kết nối hệ thống thật.

## 🧰 Môi trường và dependency

Tuần này giới thiệu virtual environment để cô lập thư viện cho từng project. Từ thư mục tuần, có thể tạo môi trường bằng:

```bash
python -m venv .venv
```

Kích hoạt môi trường theo hệ điều hành của bạn, rồi dùng `python -m pip` để cài package vào đúng interpreter. Xem `pyproject.toml` và [notes](notes.md) để hiểu dependency/tooling của tuần; chỉ cài nhóm dev khi bạn cần chạy các công cụ phát triển được khai báo ở đó.

## 📚 Tài liệu tuần 13

- [Notes — giải thích khái niệm](notes.md)
- [Exercises — cách chạy bài tập](exercises/README.md)
- [Hints — gợi ý khi bị mắc](hints.md)
- [Bot Core package](bot_course/)
- [Mini-project — Local Bot CLI and Adapter Boundary](mini-project/README.md)

## ✅ Tự đánh giá trước khi sang tuần 14

Bạn đã thực sự hiểu bài nếu có thể tự trả lời, không nhìn code:

1. Điều gì khác nhau giữa module và package?
2. Vì sao import một file không nên tự động chạy CLI?
3. `type=int` trong `argparse` giúp ích gì?
4. Vì sao cần kiểm tra status code trước khi tin response body?
5. Vì sao Core không nên phụ thuộc vào CLI hoặc network?

**Dấu hiệu hoàn thành:** không chỉ chạy được lệnh — bạn giải thích được đường đi của dữ liệu và chỉ ra trách nhiệm của từng lớp.

---

*Python Journey · Tuần 13 — Keep the core small. Make the boundaries clear. Prove it with tests.*
