import time


def mergesort(self, a, front, last):
    if front < last:
        mid = (front + last) // 2

        self.mergesort(a, front, mid)
        self.mergesort(a, mid + 1, last)

        self.display(self.N, self.data, ['dodgerblue' for _ in range(self.N)])

        rj = mid + 1
        if a[mid] <= a[mid + 1]:
            return

        while front <= mid and rj <= last:
            self.display(self.N, self.data,
                         ['yellow' if x == front or x == rj else 'dodgerblue'
                          for x in range(self.N)])
            time.sleep(self.speed)
            if a[front] <= a[rj]:
                self.display(self.N, self.data,
                             ['lime' if x == front or x == rj else 'dodgerblue'
                              for x in range(self.N)])
                time.sleep(self.speed)
                front += 1
            else:
                self.display(self.N, self.data,
                             ['red' if x == front or x == rj else 'dodgerblue'
                              for x in range(self.N)])
                time.sleep(self.speed)
                temp = a[rj]
                i = rj
                while i != front:
                    a[i] = a[i - 1]
                    i -= 1
                a[front] = temp
                self.display(self.N, self.data,
                             ['lime' if x == front or x == rj else 'dodgerblue'
                              for x in range(self.N)])
                time.sleep(self.speed)

                front += 1
                mid += 1
                rj += 1

        self.display(self.N, self.data, ['dodgerblue' for _ in range(self.N)])
        time.sleep(self.speed)