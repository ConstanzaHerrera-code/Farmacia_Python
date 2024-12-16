def numeros_perfumeria():
    for n in range(1, 10000):
        yield f"P - {n}"

def numeros_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"

def numeros_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n}"

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador(rubro):
    print("\n" + "*" * 25 )
    print('Su número es:')
    if rubro == "P":
        print(f"🎁 {next(p)} 🎁")
    elif rubro == "F":
        print(f"🩺 {next(f)} 🩺")
    else: 
        print(f"💄 {next(c)} 💄")
    print("Aguarde y será atendido 🕰️")
    print("*" * 25 + "\n")
