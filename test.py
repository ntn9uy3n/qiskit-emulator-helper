import qiskit_emulator_helper as qeh

# 1. Hiển thị tất cả các trình giả lập có sẵn
print("--- Listing all available emulators ---")
qeh.show_available_backends()

# 2. Đề xuất trình giả lập cho mạch 7 qubit
print("\n--- Proposing an emulator for 7 qubits ---")
qeh.propose_backends(num_qubits=7)

# 3. Lấy một trình giả lập cụ thể bằng tên
print("\n--- Getting the 'fake_manila' emulator ---")
try:
    backend = qeh.get_backend_by_name('fake_manila')
    print(f"Successfully retrieved: {backend.name}")
    print(f"Number of qubits: {backend.target.num_qubits}")
except ValueError as e:
    print(e)