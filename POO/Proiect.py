import tkinter as tk
from tkinter import messagebox

# Funcția care calculează caloriile și proteinele
def calculeaza_calorii_si_proteine():
    try:
        # Preluăm valorile din câmpurile de intrare
        sex = sex_var.get()  # Preia valoarea sexului (femeie sau barbat)
        inaltime = float(inaltime_entry.get())  # Preia inaltimea (cm) și o convertește într-un număr float
        greutate = float(greutate_entry.get())  # Preia greutatea (kg) și o convertește într-un număr float
        varsta = int(varsta_entry.get())  # Preia vârsta și o convertește într-un număr întreg
        obiectiv = obiectiv_var.get()  # Preia obiectivul (slabire, ingrasare, mentinere)

        # Calculăm BMR (Bazal Metabolic Rate) în funcție de sex
        if sex == "femeie":
            # Formula pentru femei
            BMR = 655 + (9.6 * greutate) + (1.8 * inaltime) - (4.7 * varsta)
        elif sex == "barbat":
            # Formula pentru bărbați
            BMR = 66 + (13.7 * greutate) + (5 * inaltime) - (6.8 * varsta)
        else:
            messagebox.showerror("Eroare", "Sexul trebuie să fie 'femeie' sau 'barbat'.")
            return

        # Preluăm nivelul de activitate
        activitate = int(activitate_var.get())  # Preia nivelul de activitate ca un întreg

        # Calculăm TDEE (Total Daily Energy Expenditure) pe baza nivelului de activitate
        if activitate == 1:
            TDEE = BMR * 1.2  # Sedentar (fără exerciții)
        elif activitate == 2:
            TDEE = BMR * 1.375  # Ușor activ (exerciții 1-3 zile pe săptămână)
        elif activitate == 3:
            TDEE = BMR * 1.55  # Moderat activ (exerciții 3-5 zile pe săptămână)
        elif activitate == 4:
            TDEE = BMR * 1.725  # Foarte activ (exerciții 6-7 zile pe săptămână)
        elif activitate == 5:
            TDEE = BMR * 1.9  # Extrem de activ (exerciții intense sau muncă fizică grea)
        else:
            messagebox.showerror("Eroare", "Nivelul de activitate nu este valid.")
            return

        # Ajustăm TDEE în funcție de obiectiv
        if obiectiv == "slabire":
            TDEE -= 500  # Scădem 500 de calorii pentru a ajuta la slăbire
            proteine = greutate * 2  # Proteinele rămân la 2g per kg de greutate pentru slăbire
        elif obiectiv == "ingrasare":
            TDEE += 500  # Adăugăm 500 de calorii pentru a ajuta la îngrășare
            proteine = greutate * 2.5  # Creștem aportul de proteine la 2.5g per kg de greutate pentru îngrășare
        elif obiectiv == "mentinere":
            pass  # Nu se adaugă sau se scad calorii, menținem TDEE pentru menținerea greutății
            proteine = greutate * 2  # Proteinele rămân la 2g per kg de greutate pentru menținere

        # Afișăm rezultatele în interfața grafică
        rezultat_label.config(text=f"Calorii: {TDEE:.2f} kcal\nProteine: {proteine:.2f} g")
    
    except ValueError:
        messagebox.showerror("Eroare", "Vă rugăm să introduceți valori valide.")

# Crearea ferestrei principale
root = tk.Tk()
root.title("Calculator Calorii și Proteine")

# Setăm dimensiunea ferestrei și o centrăm pe ecran
window_width = 400
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Creăm un container pentru a alinia toate widget-urile în centru
container = tk.Frame(root, bg="#f0f0f0")
container.pack(expand=True)

# Adăugăm un titlu pentru aplicație
titlu_label = tk.Label(container, text="Calculator Calorii și Proteine", font=("Arial", 16, "bold"), bg="#f0f0f0", anchor="center")
titlu_label.grid(row=0, column=0, columnspan=3, pady=10)

# Crearea și plasarea widget-urilor pentru sex (radio buttons)
sex_var = tk.StringVar(value="femeie")
sex_label = tk.Label(container, text="Sex:", bg="#f0f0f0", anchor="center",font=("Arial", 10, "bold"))
sex_label.grid(row=1, column=0, pady=5)

sex_femeie_rb = tk.Radiobutton(container, text="Femeie", variable=sex_var, value="femeie", bg="#f0f0f0")
sex_femeie_rb.grid(row=1, column=1, pady=5)

sex_barbat_rb = tk.Radiobutton(container, text="Barbat", variable=sex_var, value="barbat", bg="#f0f0f0")
sex_barbat_rb.grid(row=1, column=2, pady=5)

# Crearea și plasarea widget-urilor pentru înălțime, greutate și vârstă
inaltime_label = tk.Label(container, text="Inaltime (cm):", bg="#f0f0f0", anchor="center")
inaltime_label.grid(row=2, column=0, pady=5)

inaltime_entry = tk.Entry(container, justify="center")
inaltime_entry.grid(row=2, column=1, pady=5)

greutate_label = tk.Label(container, text="Greutate (kg):", bg="#f0f0f0", anchor="center")
greutate_label.grid(row=3, column=0, pady=5)

greutate_entry = tk.Entry(container, justify="center")
greutate_entry.grid(row=3, column=1, pady=5)

varsta_label = tk.Label(container, text="Varsta (ani):", bg="#f0f0f0", anchor="center")
varsta_label.grid(row=4, column=0, pady=5)

varsta_entry = tk.Entry(container, justify="center")
varsta_entry.grid(row=4, column=1, pady=5)

# Crearea și plasarea widget-urilor pentru nivelul de activitate (radio buttons)
activitate_var = tk.StringVar(value="1")
activitate_label = tk.Label(container, text="Nivel activitate:", bg="#f0f0f0", anchor="center" ,font=("Arial", 10, "bold"))
activitate_label.grid(row=5, column=0, pady=5, columnspan=3)

activitate_optiuni = [
    ("Sedentar (fără exerciții)", "1"),
    ("Ușor activ (exerciții 1-3 zile pe săptămână)", "2"),
    ("Moderat activ (exerciții 3-5 zile pe săptămână)", "3"),
    ("Foarte activ (exerciții 6-7 zile pe săptămână)", "4"),
    ("Extrem de activ (exerciții intense sau muncă fizică grea)", "5")
]

# Plasăm fiecare opțiune pe un rând diferit
for idx, (text, value) in enumerate(activitate_optiuni):
    activitate_rb = tk.Radiobutton(container, text=text, variable=activitate_var, value=value, bg="#f0f0f0")
    activitate_rb.grid(row=6 + idx, column=0, columnspan=3, pady=5)  # Incrementăm rândul

# Crearea și plasarea opțiunii pentru obiectiv
obiectiv_var = tk.StringVar(value="mentinere")
obiectiv_label = tk.Label(container, text="Obiectiv:", bg="#f0f0f0", anchor="center",font=("Arial", 10, "bold"))
obiectiv_label.grid(row=11, column=1, pady=5)

obiectiv_optiuni = [
    ("Slăbire", "slabire"),
    ("Îngrășare", "ingrasare"),
    ("Menținere", "mentinere")
]

for idx, (text, value) in enumerate(obiectiv_optiuni):
    obiectiv_rb = tk.Radiobutton(container, text=text, variable=obiectiv_var, value=value, bg="#f0f0f0")
    obiectiv_rb.grid(row=12, column=idx, pady=5)

# Crearea și plasarea butonului de calcul
calcul_button = tk.Button(container, text="Calculeaza", command=calculeaza_calorii_si_proteine, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), anchor="center")
calcul_button.grid(row=13, column=0, columnspan=3, pady=10)

# Crearea și plasarea etichetei pentru afișarea rezultatelor
rezultat_label = tk.Label(container, text="Rezultate vor apărea aici.", justify="center", bg="#f0f0f0", font=("Arial", 12), anchor="center")
rezultat_label.grid(row=14, column=0, columnspan=3, pady=10)

# Rularea aplicației
root.mainloop()
