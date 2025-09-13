class SortAlgorithms:

    # --

    def selection_sort(self, lst: list) -> list:
        N = len(lst)

        for i in range(N - 1):
            m = lst[i]  # min value
            p = i  # index min value
            for j in range(i + 1, N):  # search min
                if lst[j] < m:
                    m = lst[j]
                    p = j

            if p != i:  # Если индекс минимального числа изменился
                lst[i], lst[p] = lst[p], lst[i]  # Меняем местами значения

        return lst

    # --

    def insert_sort(self, lst: list) -> list:
        N = len(lst)

        for i in range(1, N):
            for j in range(i, 0, -1):
                if lst[j] < lst[j - 1]:
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
                else:
                    break

        return lst

    # --

    def bubble_sort(self, lst: list) -> list:
        N = len(lst)

        for i in range(N - 1):
            for j in range(N - 1 - i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

        return lst

    # --

    def _merge_list(self, a, b) -> list:
        c = []
        A = len(a)
        B = len(b)

        i = 0
        j = 0
        while i < A and j < B:
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1

        c += a[i:] + b[j:]
        return c

    def split_and_merge_list(self, a) -> list:
        mid = len(a) // 2
        a1 = a[:mid]
        a2 = a[mid:]

        if len(a1) > 1:
            a1 = self.split_and_merge_list(a1)
        if len(a2) > 1:
            a2 = self.split_and_merge_list(a2)

        return self._merge_list(a1, a2)

    # --

    def quick_sort(self, lst: list) -> list:
        import random

        if len(lst) > 1:
            x = lst[random.randint(0, len(lst) - 1)]
            low = [n for n in lst if n < x]
            eq = [n for n in lst if n == x]
            hight = [n for n in lst if n > x]
            lst = self.quick_sort(low) + eq + self.quick_sort(hight)

        return lst


s = SortAlgorithms()

n = [-3, 5, 0, -8, 1, 10]

print(s.bubble_sort(n))
