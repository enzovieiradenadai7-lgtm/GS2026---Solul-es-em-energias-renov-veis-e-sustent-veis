# Citizen Assist AI – Módulo de Energia e Sustentabilidade

**Global Solution 2026 – Ciência da Computação (Turmas 1CC)**
**Disciplina:** Soluções em Energias Renováveis e Sustentáveis

> Este repositório mostra a contribuição da disciplina de Energias Renováveis e Sustentáveis ao assistente digital **Citizen Assist AI**. Tudo o que está nas pastas `codigo/`, `dados/`, `analise/` e `testes/` faz parte dessa contribuição.

---

## 1. Integrantes

| Nome completo | RM |
|---|---|
| Enzo De Nadai | 569985 |
| Eduardo Oliveira | 570374 |
| Leonardo Gabriel | 569029 |

---

## 2. Público e problema

**Público atendido:** famílias que moram em casas ou apartamentos e querem reduzir a conta de luz, com linguagem simples e sem exigir conhecimento técnico.

**Problema:** o chuveiro elétrico é um dos equipamentos que mais consomem energia em uma residência, porque tem potência alta (cerca de 5.500 W) e é usado todos os dias por todos os moradores. Muitas pessoas não sabem quanto ele consome, quanto isso custa por mês e quais alternativas existem para gastar menos.

**Como o assistente ajuda:** o usuário informa quantas pessoas moram na casa e quanto tempo dura o banho. O assistente calcula o consumo e o custo estimados, compara alternativas de economia (incluindo uma fonte renovável) e dá uma recomendação com as limitações da estimativa.

---

## 3. Funcionalidades de energia

O módulo funciona por um menu no terminal:

| Opção | Funcionalidade | O que mostra |
|---|---|---|
| 1 | Meu consumo com o chuveiro | Consumo (kWh/mês), custo (R$/mês) e emissão de CO₂ (kg/mês) |
| 2 | Comparar alternativas | Economia, CO₂ evitado, investimento e tempo de retorno de cada alternativa |
| 3 | Recomendação | Qual alternativa começar a adotar, de acordo com a análise |
| 4 | Referências e limitações | Fontes usadas e avisos sobre as estimativas |

**Alternativas comparadas (mesma necessidade, mesmo período de 30 dias):**

- **Alternativa A – Banho mais curto:** reduz 3 minutos de cada banho. Custo zero.
- **Alternativa B – Aquecedor solar de água (fonte renovável):** substitui parte da energia do chuveiro por energia solar. Exige investimento inicial.

**Fórmula base:** Energia (kWh) = Potência (kW) × Tempo (h)

> **Atenção:** todos os valores (tarifa, potência, custo do aquecedor, fator de emissão) são **estimativas**. Os resultados não são garantidos e variam conforme a distribuidora, o clima, o modelo do chuveiro e o preço real da instalação. Detalhes em `dados/dados_premissas.md`.

---

## 4. Como executar

**Requisitos:** Python 3 instalado (nenhuma biblioteca extra).

```bash
# 1. Clonar o repositório
git clone COLE_AQUI_O_LINK_DO_REPOSITORIO
cd NOME_DA_PASTA

# 2. Executar
Codigos Desenvolvidos
```

No Windows, se `python` não funcionar, use `py Codigos Desenvolvidos.py`.

---

## 5. Como testar

Execute o programa, responda às perguntas iniciais e use o menu.

**Teste de exemplo (resultado esperado):**

| Entrada | Valor |
|---|---|
| Pessoas na casa | 4 |
| Minutos por banho | 10 |

| Opção | Resultado esperado |
|---|---|
| 1 | 110 kWh/mês, R$ 110,00/mês, 6,6 kg de CO₂/mês |
| 2 | A: economia de R$ 33,00/mês. B: economia de R$ 77,00/mês, payback de 4,3 anos |
| 3 | Começar pela alternativa A e pesquisar orçamentos do aquecedor solar |

Outras situações para testar: casa com 1 pessoa, banhos de 5 minutos (alternativa A reduz para 2 min) e banhos de 3 minutos ou menos (o programa mantém o mínimo de 1 minuto).

---

## 6. Estrutura do repositório

```
├── README.md
├── referencias.md
├── codigo/
│   └── assistente_energia.py
├── dados/
│   └── dados_premissas.md
├── analise/
│   ├── calculos_comparacao.md
│   └── justificativas.md
├── testes/
│   └── testes_usuarios.md
└── video/
    └── roteiro.md
```

---

## 7. Vídeo de demonstração

Link (YouTube, não listado): COLE_AQUI_O_LINK_DO_VIDEO
