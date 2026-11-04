[
        {"input": "abc12345\n1\n8\n", "expected": ["5"]},      # 5 chữ số từ vị trí 4 đến 8 là 1,2,3,4,5
        {"input": "a1b2c3d4e5\n2\n9\n", "expected": ["4"]},   # 1,2,3,4 trong chuỗi từ vị trí 2 đến 9
        {"input": "python3.9\n7\n9\n", "expected": ["2"]},    # 3,9 từ vị trí 7 đến 9
        {"input": "abcdef\n1\n6\n", "expected": ["0"]},       # Không có chữ số
        {"input": "a2b\n2\n2\n", "expected": ["1"]}           # Vị trí 2 là '2'
],
