import math


alf="aábcdeéfghiíjklmnñoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ0123456789 ,.:-()"
msj_cifrado="ÁeóÍ ebá 5b-CeóÍósUÍCs sÍ2UeÍÚLVVpt)utÍoáÍez2ehÍÍíN1mX-ñjA1E-OmimjX-wOyimj3wPFé13iAimÚj-mj31-OXwÚjF-OwjjbmYf2áUspY7ÍíPomY íYy3KYí ÚoPbbmEYÓ YP:3mbYyÁLÁYY4v6z6(znmsnzh(v:6zW6fW6zvoz(vóp-z6(6MpWÉzxpOFpzzÍ.íÍa3ñcahuiÍa.Í3uV Ía,ua úc.uVáúua3ñca5y(Zj9aa)r7NOFyWOwóyOÁNuukYóRYOKyRYKdRkÁy(OOIiPúGTókCF5yaó95FCyCsaTó)aQAQóiZGZ("

n_simb = len(alf) #modulo
c_descifrado = [64, 5]
lineas = []

for i in range(0, 3):
    print(i)

#decodificacion con clave inicial

i = 0;
linea = ""
p = 1;
c_des = pow(c_descifrado[0], -p, n_simb)
for i in range(1, len(msj_cifrado)):
    if(linea and linea[-1] ==" " and linea[-2] ==" "):
        p = p+1
        c_des = pow(c_descifrado[0], -p, n_simb)
        lineas.append(linea)
        linea = ""
    
    n = alf.index(msj_cifrado[i])
    new_n = (c_descifrado[0]*n+c_descifrado[1])%n_simb #an + b
    linea += alf[new_n]
    
print(lineas)