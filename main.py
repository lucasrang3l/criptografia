# NUMEROS PRIMOS DEFINIDOS POR NOS
p = 17
q = 41

# FUNCOES DE CIFRAR E DECIFRAR A MENSAGEM
def monta_menu(caractere=" "):
       
        print(caractere*12,    "▒▒▒▒▒", caractere*30 , "╔═════════════════════════════════════════════════════════════════╗" ,caractere*37,"▒▒▒▒▒")

        print (caractere*10, "▒▒▒▒▒▒▒▒▒", caractere*28 , "║", caractere*21 , "CRIPTOGRAFIA RSA" , caractere*24 ,  "║",caractere*35,"▒▒▒▒▒▒▒▒▒")
        
        print (caractere*10, "▒▒     ▒▒", caractere*28 , "║", caractere*63, "║",caractere*35,"▒▒     ▒▒")
        
        print(caractere*10,  "▒▒     ▒▒", caractere*28 ,"║", caractere*7, " Digite 'criptografar' para cifrar uma mensagem", caractere*7 ,"║",caractere*35,"▒▒     ▒▒")
        
        print(caractere*8,"█████████████", caractere*26 , "║", caractere*4, " Digite 'descriptografar' para descifrar uma mensagem", caractere*4 ,"║",caractere*26,"█████████████")

        print(caractere*8,"█████████████", caractere*26 , "║", caractere*11, " Digite 'sair' para finalizar o programa", caractere*10 ,"║",caractere*26,"█████████████")
        
        print(caractere*8,"██████  █████", caractere*26 ,"║", caractere*63, "║",caractere*26,"██████  █████")
       
        print(caractere*8,"██████ ██████", caractere*26 ,"║", caractere*63, "║",caractere*26,"██████ ██████")
       
        print(caractere*8,"██████ ██████", caractere*26 ,"║", caractere*63, "║",caractere*26,"██████ ██████")
        
        print(caractere*8,"█████████████", caractere*26 ,"╚═════════════════════════════════════════════════════════════════╝",caractere*26,"█████████████")

    
# FUNCOES DE CALCULOS PARA GERAR AS CHAVES   
def gerar_chaves():
    n = p * q
    phi = (p-1)*(q-1)  # Função Phi
    
    print(str(coprimos(phi)) + "\n") # Print para escolha da chave
    e = int(input("Escolha nas opções acima a sua chave pública : \t"))

    d = inverso_modular(e,phi) # calculo da chave privada d*e = 1 mod(φ(n))
    return print("\nChaves públicas (e=" + str(e) + ", n=" + str(n) + ")" + "\nChaves privadas (d=" + str(d) + ", n=" + str(n) + ")\n")

def mdc(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def coprimos(a):
    l = []
    for x in range(2, a): 
        if mdc(a, x) == 1 and inverso_modular(x,a) != None: #  MDC(φ(n), e) = 1
            l.append(x)   
    for x in l:
        if x == inverso_modular(x,a):
            l.remove(x)
    return l

def inverso_modular(a, m): # m = c ^ d mod n
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    print('Não ha inverso modular para o bloco.\n')
    return None

def criptografia(m, e, n):
    c = (m**e) % n
    return c

def descriptografia(c, d, n):
    m = c**d % n
    return m

def encripta_mensagem():
    s = input("Digite a mensagem: \t")
    print("="*5 + " Digite as chaves públicas: " + "="*5)
    e = int(input("Chave e: \t"))
    n = int(input("Chave n: \t")) 
    encriptar = "".join(chr(criptografia(ord(x), e, n)) for x in s)
    print("Texto Cifrado: ", encriptar, "\n")
    return encriptar
        
        
def decripta_mensagem(s):
    s = s
    print('='*5 + ' Digite as chaves privadas: ' + '='*5)
    d = int(input("Chave d: \t"))
    n = int(input("Chave n: \t")) 
    descriptar = "".join(chr(descriptografia(ord(x), d, n)) for x in s)
    return print('Texto Decifrado: ', descriptar, '\n')

condicao=1
while(condicao==1):
    monta_menu()
    op_menu = input("                                                                   Digite a opção desejada: ")
    if op_menu == "criptografar":
        numero_p = p
        print('\n P :',str(numero_p))

        numero_q = q
        print('\n Q : ',str(numero_q),'\n')

        chaves = numero_p, numero_q
        gerar_chaves()

        encripta = encripta_mensagem()
    elif op_menu == "descriptografar":
        decripta_mensagem(encripta)

    elif op_menu == "sair":

        break
    else:
        print("dados invalidos")
