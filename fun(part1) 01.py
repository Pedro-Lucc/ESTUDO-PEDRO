# DEFININDO A FUNÇÃO PARA CALCULAR A ÁREA DE UM TERRENO
def área(largura, comprimento):
    area_terreno = largura * comprimento
    print(f'a largura da área é {largura}m, o comprimento é {comprimento}m\ne a área total deste terreno é {area_terreno}m^2')


largura = int(input("LARGURA DO TERRENO: "))
comprimento = int(input("COMPRIMENTO DO TERRENO: "))
área(largura, comprimento)
