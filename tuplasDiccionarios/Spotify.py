playList = {}
# 1
def agregarArtista(playlist):
    art = input("Nombre del artista: ")
    if art in playlist:
        print(art,'ya está, seleccione la opción 5: ')
    else:
        playlist[art] = {}
        can = input("Nombre de la canción: ")
        gen = input("Género: ")
        dur = float(input("duración de la cancion: "))
        playlist[art].update({'cancion':can,'genero':gen,'duracion':dur})
        print(playlist)
# 2
def eliminarArtista(playlist):
    eliminar = input("Nombre del artista: ")
    del playlist[eliminar]
    print(playlist)
# 3
def buscarArtista (playlist):
    art = input("Nombre del artista: ")
    if art in playlist:
        print('El artista si está, datos de la PlayList: ',playlist[art])
    else:
        print("El artista no está")
# 4
def buscarCancion(playlist):
    can = input("Nombre de la canción: ")
    for y in playlist.keys():
        if can in playlist[y]["cancion"]:
            print("Si está")
        else:
            print("no está")
# 5
def agregarCancion (playlist):
    art = input("A qué artista quiere agregarle una canción: ")
    if art in playlist:
        can = input("Nombre de la canción: ")
        gen = input("Género: ")
        dur = float(input("duración de la cancion: "))
        playlist[art].update({'cancion':can,'genero':gen,'duracion':dur})
        print(playlist)
    else:
        print("El artista no está en la PlayList")
# 6
def masCanciones(playlist):
    for llaves in playlist.keys(): 
        cont = 0
        for valores in playlist.values():
            if x in playlist[llaves]["cancion"]:
                cont += 1
                if cont >= cont:
                    print(playlist[valores])

print('\nPlayList >>> ',playList)

while True:

    x = input('\nAgregar art --> 1\nEliminar art --> 2\nBuscar art --> 3\nBuscar can --> 4\nAgregar can --> 5\nBye --> 0\nY bien... ')

    if x == '1':
        agregarArtista(playList)
        #print(sorted(playList.items()))

    elif x == '2':
        eliminarArtista(playList)

    elif x == '3':
        buscarArtista(playList)

    elif x == '4':
        buscarCancion(playList)

    elif x == '5':
        agregarCancion(playList)

    elif x == '0':
        print('\n╔═════════════════════════╗\n║ Hasta la próxima...  ;)\n╚═════════════════════════╝\n')
        break