class MargeSort:
    def __init__(self, data):
        self.data = data

    def merge(self, left, mid, right):
        L = self.data[left:mid]
        R = self.data[mid:right]
        l = r = 0
        for d in range(left, right):
            if r == len(R) or l < len(L) and L[l] <= R[r]:
                self.data[d] = L[l]
                l += 1
            else:
                self.data[d] = R[r]
                r += 1


    def sort(self, left, right):
        mid = (left + right) // 2
        print(f"left: {left}, right: {right}, mid: {mid}")
        if left + 1 < right:
            self.sort(left, mid)
            self.sort(mid, right)
            self.merge(left, mid, right)


if __name__ == '__main__':
    A = [7675, 8, 678, 9, 87, 84, 645, 3, 46456, 24, 423, 4, 3]
    MargeSort(A).sort(0, len(A))
    print(A)