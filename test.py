def sapa(nama):
    print("Halo", nama)

def greet(name):
    print("Hello", name)

nama = "Galih"
d = {
    "sapa": sapa,
    "greet": greet
}

print(d["greet"](nama))