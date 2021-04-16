import math


alf="aábcdeéfghiíjklmnñoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ0123456789 ,.:-()"
msj_cifrado="ÁeóÍ ebá 5b-CeóÍósUÍCs sÍ2UeÍÚLVVpt)utÍoáÍez2ehÍÍíN1mX-ñjA1E-OmimjX-wOyimj3wPFé13iAimÚj-mj31-OXwÚjF-OwjjbmYf2áUspY7ÍíPomY íYy3KYí ÚoPbbmEYÓ YP:3mbYyÁLÁYY4v6z6(znmsnzh(v:6zW6fW6zvoz(vóp-z6(6MpWÉzxpOFpzzÍ.íÍa3ñcahuiÍa.Í3uV Ía,ua úc.uVáúua3ñca5y(Zj9aa)r7NOFyWOwóyOÁNuukYóRYOKyRYKdRkÁy(OOIiPúGTókCF5yaó95FCyCsaTó)aQAQóiZGZ("

n_simb = len(alf) #modulo
lineas = []

#decodificacion

#a y b iniciales
ab = [64, 5]
p = 1
a = pow(ab[0], p, n_simb)
b = (ab[1]*p)

linea = ""

for i in range(0, len(msj_cifrado)):

    #Si es nueva linea
    if(linea!="" and linea[-1] ==" " and linea[-2] ==" "):
        #Recalculo la clave de cifrado
        p = p+1
        a = pow(ab[0], p, n_simb)
        b = (ab[1]*p % n_simb)

        #Lo añado a la lista de lineas y vacio la linea
        lineas.append(linea)
        linea = ""

    c = alf.index(msj_cifrado[i]) #Tomo la posicion en el alfabeto del caracter cifrado
    new_n = ((pow(a, -1, n_simb)*c)%n_simb) - ((pow(a, -1, n_simb)*b)%n_simb)%n_simb #Calculo la nueva a^-1*c - a^-1*b
    linea += alf[new_n] #Añado la letra descrifrada a la linea

lineas.append(linea) #añado la ultima linea

print(*lineas, sep = "\n")