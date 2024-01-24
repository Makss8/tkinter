import tkinter as tk
from tkinter import PhotoImage

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Number Properties")
        self.root.configure(bg="blue")

        self.label = tk.Label(self.root, text="Number:", font=("Arial", 24), bg="blue", fg="white")
        self.label.place(x=70, y=5)

        self.entry = tk.Entry(self.root, font=("Arial", 18), bg="blue", fg="light green")
        self.entry.place(x=200, y=10)

        calculate_image = PhotoImage(file="calculate-button-hi.png")
        self.calculate_button = tk.Button(self.root, text="", font=("Arial", 18), command=self.calculate_properties,image=calculate_image, compound=tk.LEFT, bg="blue", fg="blue")
        self.calculate_button.image = calculate_image
        self.calculate_button.place(x=400, y=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 16), bg="blue", fg="white")
        self.result_label.place(x=50, y=70, width=700)

        self.root.mainloop()

    def calculate_properties(self):
        try:
            number = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="Enter a valid integer.")
            return

        prime_check = "Number is prime." if self.is_prime(number) else "Number is not prime."
        odd_check = "Number is odd." if number % 2 != 0 else "Number is even."
        divisors_check = "Prime divisors: " + ', '.join(map(str, self.get_prime_divisors(number)))
        perfect_check = "Number is perfect." if self.is_perfect(number) else "Number is not perfect."

        result_text = "\n".join([prime_check, odd_check, divisors_check, perfect_check])
        self.result_label.config(text=result_text)

    def is_prime(self, n):
        return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

    def get_prime_divisors(self, n):
        return [i for i in range(2, n + 1) if n % i == 0 and self.is_prime(i)]

    def is_perfect(self, n):
        sum = 0
        for x in range(1, n):
            if n % x == 0:
                sum += x
        return sum == n


GUI()