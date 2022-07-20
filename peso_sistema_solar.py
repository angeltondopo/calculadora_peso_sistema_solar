# Lista de la gravedad de los astros
g_tierra = 9.8
g_sol = 274
g_luna = 1.62
g_mercurio = 1.7
g_venus = 8.87
g_marte = 3.711
g_fobos = 0.0057
g_deimos = 0.003
g_ceres = 0.27
g_jupiter = 24.79
g_ganimedes = 1.428
g_calisto = 1.236
g_saturno = 10.44
g_titan = 1.352
g_io = 1.796
g_europa = 1.315
g_urano = 8.87
g_neptuno = 11.15
g_pluton = 0.62
g_betelgeuse = 0.003162

def peso_planeta(nombre_astro, gravedad_astro):
    peso_usuario = float(input('¿Cuál es tu peso en kilos? '))
    peso_final = (peso_usuario * gravedad_astro) / 9.8
    peso_final = round(peso_final, 4)
    print('Tu peso en \U0001f52d ' + nombre_astro + ' es ' + str(peso_final) + ' kilos \U0001faa8')


def run():
    eleccion_astro = input('''Tu peso en el sistema solar \u2604\uFE0F
En la tierra \U0001f30e pesas distinto que en Marte o Júpiter \U0001f30c

Futuro \U0001f468\u200D\U0001f680astronauta \U0001f469\u200D\U0001f680averígüelo.

   1-  Sol
   2-  Luna
   3-  Mercurio
   4-  Venus
   5-  Marte
   6-  Fobos
   7-  Deimos
   8-  Ceres
   9-  Jupiter
   10- Ganimedes
   11- Calisto
   12- Saturno
   13- Titan
   14- Ío
   15- Europa
   16- Urano
   17- Neptuno
   18- Pluton
   19- Betelgeuse

Elige un astro \U0001fa90: ''')

    while eleccion_astro == (0, 19):
        continue
    if eleccion_astro == '1':
        peso_planeta('el Sol',  g_sol)
    elif eleccion_astro == '2':
        peso_planeta('la Luna',  g_luna)
    elif eleccion_astro == '3':
        peso_planeta('Mercurio',  g_mercurio)
    elif eleccion_astro == '4':
        peso_planeta('Venus',  g_venus)
    elif eleccion_astro == '5':
        peso_planeta('Marte',  g_marte)
    elif eleccion_astro == '6':
        peso_planeta('Fobos',  g_fobos)
    elif eleccion_astro == '7':
        peso_planeta('Deimos',  g_deimos)
    elif eleccion_astro == '8':
        peso_planeta('Ceres',  g_ceres)
    elif eleccion_astro == '9':
        peso_planeta('Jupiter',  g_jupiter)
    elif eleccion_astro == '10':
        peso_planeta('Ganimedes',  g_ganimedes)
    elif eleccion_astro == '11':
        peso_planeta('Calisto',  g_calisto)
    elif eleccion_astro == '12':
        peso_planeta('Saturno',  g_saturno)
    elif eleccion_astro == '13':
        peso_planeta('Titan',  g_titan)
    elif eleccion_astro == '14':
        peso_planeta('Ío',  g_io)
    elif eleccion_astro == '15':
        peso_planeta('Europa',  g_europa)
    elif eleccion_astro == '16':
        peso_planeta('Urano',  g_urano)
    elif eleccion_astro == '17':
        peso_planeta('Neptuno',  g_neptuno)
    elif eleccion_astro == '18':
        peso_planeta('Pluton',  g_pluton)
    elif eleccion_astro == '19':
        peso_planeta('Betelgeuse',  g_betelgeuse)
    else:
        print('Introduce una opción válida \U0001f4e1')
        return run()


if __name__ == '__main__':
    run()