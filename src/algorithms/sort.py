class SortMethods:

    def selection_sort(self, lst: list) -> list:
        N = len(lst)

        for i in range(N - 1):
            m = lst[i]  # min value
            p = i  # index min value
            for j in range(i + 1, N):  # search min
                if m > lst[j]:
                    m = lst[j]
                    p = j

            if p != i:
                t = lst[i]
                lst[i] = lst[p]
                lst[p] = t

        return lst

    def insert_sort(self, lst: list) -> list:
        N = len(lst)

        for i in range(1, N):
            for j in range(i, 0, -1):
                if lst[j] < lst[j - 1]:
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
                else:
                    break

        return lst

    def bubble_sort(self, lst: list) -> list:
        N = len(lst)

        for i in range(0, N - 1):
            for j in range(0, N - 1 - i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

        return lst


s = SortMethods()

n = [-3, 5, 0, -8, 1, 10]

print(s.bubble_sort(n))
