import psutil
import pygame


 # Iniciando a janela principal
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
VERMELHO, AZUL = (255, 0, 0), (0, 0, 255)
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("TP2 -PB")
pygame.display.init()
# Cria relógio
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font(None, 32)

s1 = pygame.surface.Surface((largura_tela, altura_tela/4))
s2 = pygame.surface.Surface((largura_tela, altura_tela/4))
s3 = pygame.surface.Surface((largura_tela, altura_tela/4))

# Mostar uso de memória

def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2*20    
    pygame.draw.rect(s1, AZUL, (20, 60, larg, 70)) 
    tela.blit(s1, (0, 0))   
    larg = larg*mem.percent/100
    pygame.draw.rect(s1, VERMELHO, (20, 60, larg, 70))
    tela.blit(s1, (0, 0))    
    total = round(mem.total/(1024*1024*1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, BRANCO)
    tela.blit(text, (20, 30))

def mostra_uso_cpu():
      capacidade = psutil.cpu_percent(interval=0)
      larg = largura_tela - 2*20
      pygame.draw.rect(s2, AZUL, (20, 60, larg, 70))
      tela.blit(s2, (0, altura_tela/3))         
      larg = larg*capacidade/100
      pygame.draw.rect(s2, VERMELHO, (20, 60, larg, 70))
      tela.blit(s2, (0, altura_tela/4))      
      text = font.render("Uso de CPU:", 1, BRANCO)
      tela.blit(text, (20, 180))

def mostra_uso_disco():
      disco = psutil.disk_usage('.')
      larg = largura_tela - 2*20      
      pygame.draw.rect(s3, AZUL, (20, 60, larg, 70))
      tela.blit(s3, (0, 2*altura_tela/4))
      larg = larg*disco.percent/100
      pygame.draw.rect(s3, VERMELHO, (20, 60, larg, 70))
      tela.blit(s3, (0, 2*altura_tela/4))
      total = round(disco.total/(1024*1024*1024), 2)
      texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
      text = font.render(texto_barra, 1, BRANCO)
      tela.blit(text, (20, 330))
      
def mostra_ip():
      ip = psutil.net_if_addrs()['Wi-Fi'][1].address          
      texto_barra = "IP Address:  " + ip      
      text = font.render(texto_barra, 1, BRANCO)
      tela.blit(text, (20, 490))

# Contador de tempo
cont = 60
terminou = False
while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    # Fazer a atualização a cada segundo:
    if cont == 60:
        mostra_uso_memoria()
        mostra_uso_cpu()
        mostra_uso_disco()
        mostra_ip()
        cont = 0 
           
        # Atualiza o desenho na tela
        pygame.display.update()
        # 60 frames por segundo
        clock.tick(60)
        cont = cont + 1

    # Finaliza a janela
pygame.display.quit()

