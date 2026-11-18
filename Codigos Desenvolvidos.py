import os

TARIFA_PADRAO = 1.00       
FATOR_EMISSAO = 0.06        
POTENCIA_CHUVEIRO = 5500    
DIAS_MES = 30
REDUCAO_MINUTOS = 3     
FRACAO_SOLAR = 0.70        
CUSTO_SOLAR = 4000.00       
LIMITE_PAYBACK_MESES = 72   

def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def mostrar_titulo():
    print("            CITIZEN ASSIST AI")
    print("   Energia e Sustentabilidade - Chuveiro Eletrico")
    print("")


def pausar():
    print("")
    input("Pressione Enter para voltar ao menu...")


def ler_inteiro_positivo(pergunta):
    texto = input(pergunta)
    while not texto.isdigit() or int(texto) <= 0:
        print("Digite um numero inteiro maior que zero.")
        texto = input(pergunta)
    return int(texto)


def ler_tarifa():
    pergunta = "Tarifa da sua conta de luz em R$/kWh (Enter para usar 1,00): "
    texto = input(pergunta).replace(",", ".")
    while texto != "" and (not texto.replace(".", "", 1).isdigit() or float(texto) <= 0):
        print("Valor invalido. Exemplo: 0,95")
        texto = input(pergunta).replace(",", ".")
    if texto == "":
        return TARIFA_PADRAO
    return float(texto)


def pedir_dados():
    pessoas = ler_inteiro_positivo("Quantas pessoas moram na sua casa? ")
    minutos = ler_inteiro_positivo("Quantos minutos dura cada banho (em media)? ")
    tarifa = ler_tarifa()
    return pessoas, minutos, tarifa


def calcular_consumo_mensal(pessoas, minutos):
    horas_por_dia = pessoas * minutos / 60
    return (POTENCIA_CHUVEIRO / 1000) * horas_por_dia * DIAS_MES


def calcular_situacao_atual(pessoas, minutos, tarifa):
    consumo = calcular_consumo_mensal(pessoas, minutos)
    return {
        "consumo": consumo,
        "custo": consumo * tarifa,
        "co2": consumo * FATOR_EMISSAO,
    }


def calcular_alternativa_a(pessoas, minutos, consumo_atual, tarifa):
    minutos_novo = minutos - REDUCAO_MINUTOS
    if minutos_novo < 1:
        minutos_novo = 1
    consumo_novo = calcular_consumo_mensal(pessoas, minutos_novo)
    kwh_economizados = consumo_atual - consumo_novo
    return {
        "minutos_novo": minutos_novo,
        "economia": kwh_economizados * tarifa,
        "co2_evitado": kwh_economizados * FATOR_EMISSAO,
    }


def calcular_alternativa_b(consumo_atual, tarifa):
    kwh_economizados = consumo_atual * FRACAO_SOLAR
    economia = kwh_economizados * tarifa
    if economia > 0:
        payback_meses = CUSTO_SOLAR / economia
    else:
        payback_meses = 0
    return {
        "economia": economia,
        "co2_evitado": kwh_economizados * FATOR_EMISSAO,
        "payback_meses": payback_meses,
    }


def calcular_tudo(pessoas, minutos, tarifa):
    atual = calcular_situacao_atual(pessoas, minutos, tarifa)
    alt_a = calcular_alternativa_a(pessoas, minutos, atual["consumo"], tarifa)
    alt_b = calcular_alternativa_b(atual["consumo"], tarifa)
    return atual, alt_a, alt_b


def mostrar_menu():
    print("")
    print("1 - Meu consumo com o chuveiro")
    print("2 - Comparar alternativas")
    print("3 - Recomendacao")
    print("4 - Referencias e limitacoes")
    print("5 - Alterar meus dados (pessoas, banho e tarifa)")
    print("0 - Sair")


def mostrar_consumo(pessoas, minutos, tarifa, atual):
    print("Citizen Assist AI: com", pessoas, "pessoa(s) e banhos de", minutos, "min,")
    print("o chuveiro consome cerca de", round(atual["consumo"], 1), "kWh por mes.")
    print("Isso custa em torno de R$", round(atual["custo"], 2), "por mes (tarifa R$", tarifa, "/kWh).")
    print("Emissao estimada de CO2:", round(atual["co2"], 1), "kg por mes.")


def mostrar_comparacao(alt_a, alt_b):
    print("--- Alternativa A: banhos ate", REDUCAO_MINUTOS, "min mais curtos (custo zero) ---")
    print("Novo tempo de banho:", alt_a["minutos_novo"], "min")
    print("Economia estimada: R$", round(alt_a["economia"], 2), "por mes")
    print("CO2 evitado:", round(alt_a["co2_evitado"], 1), "kg por mes")
    print("")
    print("--- Alternativa B: aquecedor solar (fonte renovavel) ---")
    print("Economia estimada: R$", round(alt_b["economia"], 2), "por mes")
    print("CO2 evitado:", round(alt_b["co2_evitado"], 1), "kg por mes")
    print("Investimento estimado: R$", CUSTO_SOLAR)
    if alt_b["payback_meses"] > 0:
        print("Retorno do investimento (payback):", round(alt_b["payback_meses"] / 12, 1), "anos")


def mostrar_recomendacao(alt_a, alt_b):
    payback = alt_b["payback_meses"]
    print("Citizen Assist AI - minha recomendacao:")
    if alt_a["economia"] > 0:
        print("1) Comece pela Alternativa A: nao custa nada e reduz o gasto estimado.")
    else:
        print("1) Com o tempo informado, a Alternativa A nao gera economia adicional.")
    if payback > 0 and payback <= LIMITE_PAYBACK_MESES:
        print("2) O retorno estimado do aquecedor solar e de cerca de", round(payback / 12, 1), "anos.")
        print("   Vale pesquisar orcamentos se voce tem telhado com sol.")
    else:
        print("2) O aquecedor solar demora para se pagar nesse caso. Avalie com cuidado.")
    print("Lembrete: sao estimativas, nao resultados garantidos.")


def mostrar_referencias():
    print("Fontes: Lorenzetti, ANEEL, MCTI, Inmetro e MME. Veja referencias.md.")
    print("Valores e premissas da simulacao: veja dados_premissas.md.")
    print("Limitacoes: os valores variam com a distribuidora, o clima, o modelo do chuveiro,")
    print("o preco real da instalacao e o espaco no telhado. Dados ESTIMADOS.")


def main():
    limpar_tela()
    mostrar_titulo()
    print(" Irei ajuda-lo a entender o gasto de energia do seu chuveiro.")
    print("")

    pessoas, minutos, tarifa = pedir_dados()
    atual, alt_a, alt_b = calcular_tudo(pessoas, minutos, tarifa)

    opcao = ""
    while opcao != "0":
        limpar_tela()
        mostrar_titulo()
        mostrar_menu()
        opcao = input("Escolha uma opcao: ")
        limpar_tela()
        mostrar_titulo()

        if opcao == "1":
            mostrar_consumo(pessoas, minutos, tarifa, atual)
            pausar()
        elif opcao == "2":
            mostrar_comparacao(alt_a, alt_b)
            pausar()
        elif opcao == "3":
            mostrar_recomendacao(alt_a, alt_b)
            pausar()
        elif opcao == "4":
            mostrar_referencias()
            pausar()
        elif opcao == "5":
            pessoas, minutos, tarifa = pedir_dados()
            atual, alt_a, alt_b = calcular_tudo(pessoas, minutos, tarifa)
            print("")
            print("Dados atualizados! Escolha uma opcao para ver os novos resultados.")
            pausar()
        elif opcao != "0":
            print("Opcao invalida. Escolha de 0 a 5.")
            pausar()

    print("Ate logo!")


main()