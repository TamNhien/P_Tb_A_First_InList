def average_of_first_a_elements(lst, a):
    return sum(lst[:a]) / a if len(lst) >= a else None

def main():
    lst = [int(x) for x in input("Nhập các số nguyên trong list, cách nhau bởi dấu cách: ").split()]
    a = int(input("Nhập số nguyên dương a: "))
    result = average_of_first_a_elements(lst, a)
    print(f"Giá trị trung bình của {a} phần tử đầu tiên trong list là: {result}" if result is not None else "Số phần tử trong list ít hơn số a, không thể tính giá trị trung bình.")

if __name__ == "__main__":
    main()
