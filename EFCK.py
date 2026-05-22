import tkinter as tk
from tkinter import messagebox

import math


def calculate_Q(age, sex):
    """
    Calculate Q factor based on age and sex
    age: in years
    sex: "male" or "female"
    """
    if age <= 25:
        if sex.lower() == "female":
            lnQ = (3.080
                   + 0.177 * age
                   - 0.223 * math.log(age)
                   - 0.00596 * age ** 2
                   + 0.0000686 * age ** 3)
        elif sex.lower() == "male":
            lnQ = (3.200
                   + 0.259 * age
                   - 0.543 * math.log(age)
                   - 0.00763 * age ** 2
                   + 0.0000790 * age ** 3)
        else:
            raise ValueError("Sex must be 'male' or 'female'")

        return math.exp(lnQ)

    else:
        if sex.lower() == "female":
            return 62.0
        elif sex.lower() == "male":
            return 80.0
        else:
            raise ValueError("Sex must be 'male' or 'female'")


def calculate_eGFR_EKFC(scr_umol, age, sex):


    Q = calculate_Q(age, sex)
    ratio = scr_umol / Q

    if age <= 40:
        if ratio < 1.0000:
            egfr = 107.3 * (ratio ** -0.322)
        else:
            egfr = 107.3 * (ratio ** -1.132)
    else:
        if ratio < 1.0000:
            egfr = 107.3 * (ratio ** -0.322) * (0.990 ** (age - 40))
        else:
            egfr = 107.3 * (ratio ** -1.132) * (0.990 ** (age - 40))

    return egfr


# GUI
root = tk.Tk()
root.title("EKFC GFR Calculator")

tk.Label(root, text="Age (years):").grid(row=0, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=0, column=1)

tk.Label(root, text="Creatinine:").grid(row=1, column=0)
entry_creatinine = tk.Entry(root)
entry_creatinine.grid(row=1, column=1)

unit_var = tk.StringVar(value="µmol/L")
tk.OptionMenu(root, unit_var, "µmol/L", "mg/dL").grid(row=1, column=2)

tk.Label(root, text="Gender:").grid(row=2, column=0)
gender_var = tk.StringVar(value="Male")
tk.OptionMenu(root, gender_var, "Male", "Female").grid(row=2, column=1)

def calculate_gfr():
    try:
        age = float(entry_age.get())
        creatinine = float(entry_creatinine.get())
        sex = gender_var.get()
        unit = unit_var.get()

        if unit == "mg/dL":
            creatinine = creatinine * 88.42  # convert to µmol/L

        egfr = calculate_eGFR_EKFC(creatinine, age, sex)
        result_label.config(text=f"eGFR: {egfr:.2f} mL/min/1.73m²")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Button(root, text="Calculate", command=calculate_gfr).grid(row=3, column=0, columnspan=3)

result_label = tk.Label(root, text="eGFR: ")
result_label.grid(row=4, column=0, columnspan=3)

root.mainloop()

