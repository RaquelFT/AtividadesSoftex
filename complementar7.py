import enum


class CandidatosEleicao(enum.Enum):
    x = 889
    y = 847
    z = 515
    branco = 0


def eleicao():
    candidatos = CandidatosEleicao
    votos_candidato_x = 0
    votos_candidato_y = 0
    votos_candidato_z = 0
    votos_brancos_nulos = 0
    voto = input("Digite o seu voto ")
    fim_eleicao = False
    while not fim_eleicao:
        if voto.isdigit():
            if int(voto) == candidatos.x.value:
                votos_candidato_x += 1
            elif int(voto) == candidatos.y.value:
                votos_candidato_y += 1
            elif int(voto) == candidatos.z.value:
                votos_candidato_z += 1
            else:
                votos_brancos_nulos += 1
            if input("deseja finalizar votação (s/n) ") == "s":
                fim_eleicao = True
            else:
                voto = input("Digite o seu voto ")
        else:
            voto = input("Voto inválido, vote de novo! ")

    if votos_candidato_y < votos_candidato_x > votos_candidato_z:
        print("O vencedor foi o candidato X" )
    elif votos_candidato_x < votos_candidato_y > votos_candidato_z:
        print("O vencedor foi o candidato Y" )
    elif votos_candidato_x < votos_candidato_z > votos_candidato_y:
        print("O vencedor foi o candidato Z")
    print(f"número de votos candidato x: {votos_candidato_x}")
    print(f"número de votos candidato y: {votos_candidato_y}")
    print(f"número de votos candidato z: {votos_candidato_z}")
    print(f"número de votos nulos: {votos_brancos_nulos}")

eleicao()