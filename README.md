# Otimização de Portfólio de Projetos - Global Solution 2025

## 📚 Informações do Projeto

**Disciplina:** Dynamic Programming  
**Curso:** Engenharia de Software  
**Professor:** Marcelo Amorim  
**Tema:** O Futuro do Trabalho - Otimização de Recursos

---

## 👥 Integrantes do Grupo
## **Turma 2ESPG**
| Nome | RM |
|------|-----|
| Estevam Melo | 555124 |
| João Victor Franco | 556790 |
| Nathan Craveiro | 555508 |



---

## 📖 Descrição do Projeto

Este projeto implementa a solução para o **Problema de Otimização de Portfólio de Projetos**, uma aplicação direta do clássico **Problema da Mochila 0/1 (0/1 Knapsack Problem)**.

### Contexto

No cenário do Futuro do Trabalho, empresas de consultoria precisam otimizar a alocação de seus recursos mais valiosos: o tempo e expertise de seus colaboradores qualificados.

**Problema:** Dada uma capacidade limitada de Horas-Especialista e uma lista de projetos potenciais, determinar o conjunto ideal de projetos que maximiza o valor total (lucro/impacto) sem exceder a capacidade disponível.

---

## 🎯 Objetivo

Implementar **quatro estratégias diferentes** para resolver o problema:

1. **Fase 1:** Estratégia Gulosa (Greedy)
2. **Fase 2:** Solução Recursiva Pura
3. **Fase 3:** Programação Dinâmica Top-Down (Memoização)
4. **Fase 4:** Programação Dinâmica Bottom-Up (Iterativa)

---

## 📊 Dados de Exemplo

**Capacidade Máxima:** 10 Horas-Especialista

| Projeto | Valor (V) | Horas-Especialista (E) | Relação V/E |
|---------|-----------|------------------------|-------------|
| A | 12 | 4 | 3.00 |
| B | 10 | 3 | 3.33 |
| C | 7 | 2 | 3.50 |
| D | 4 | 3 | 1.33 |

---

## 🚀 Como Executar

### Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa necessária (apenas biblioteca padrão)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/Dream-Path-AI/gs-dynamic

# Entre no diretório
cd gs-dynamic

# Execute o programa
python portfolio_optimization.py
```

---

## 📁 Estrutura do Projeto

```
gs-dynamic/
│
├── README.md                           # Este arquivo
├── portfolio_optimization.py           # Código principal com as 4 implementações
├── test_cases.py                       # Casos de teste
├── GS-Dynamic-Progamming-Enunciado.md # Enunciado original
└── dynamic programming 2025.md         # Material de apoio da disciplina
```

---

## 🔍 Implementações

### 1. Estratégia Gulosa (Greedy)

- **Abordagem:** Prioriza projetos com maior relação Valor/Custo (V/E)
- **Complexidade:** O(n log n) - devido à ordenação
- **Limitação:** Não garante solução ótima

### 2. Solução Recursiva Pura

- **Abordagem:** Explora todas as combinações possíveis (força bruta)
- **Complexidade:** O(2^n) - exponencial
- **Limitação:** Muito lenta para grandes entradas, recalcula subproblemas

### 3. Programação Dinâmica Top-Down (Memoização)

- **Abordagem:** Recursão com cache de resultados
- **Complexidade:** O(n × C) - onde C é a capacidade
- **Vantagem:** Evita recalcular subproblemas

### 4. Programação Dinâmica Bottom-Up (Iterativa)

- **Abordagem:** Constrói tabela iterativamente
- **Complexidade:** O(n × C)
- **Vantagem:** Mais eficiente em memória, sem overhead de recursão

---

## 📈 Análise de Complexidade

| Estratégia | Tempo | Espaço | Solução Ótima? |
|------------|-------|--------|----------------|
| Greedy | O(n log n) | O(1) | ❌ Não |
| Recursiva Pura | O(2^n) | O(n) | ✅ Sim |
| Top-Down (Memo) | O(n × C) | O(n × C) | ✅ Sim |
| Bottom-Up (DP) | O(n × C) | O(n × C) | ✅ Sim |

**Conclusão:** As abordagens de Programação Dinâmica (Fase 3 e 4) são as mais eficientes, oferecendo solução ótima em tempo polinomial.

---

## 🧪 Casos de Teste

O programa inclui **4 casos de teste** diferentes para validar as implementações:

1. **Caso Base:** Exemplo do enunciado (C=10, 4 projetos)
2. **Caso Greedy Falha:** Demonstra onde a estratégia gulosa não encontra o ótimo
3. **Caso Simples:** Poucos projetos para verificação rápida
4. **Caso Complexo:** Mais projetos e capacidade maior

---

## 📝 Observações

- O código está amplamente comentado para facilitar o entendimento
- Cada função inclui documentação detalhada
- Os resultados são comparados entre as 4 abordagens
- Exemplo prático demonstra onde a abordagem Greedy falha

---

## 📚 Referências

- Material da disciplina Dynamic Programming 2025
- Problema da Mochila 0/1 (Knapsack Problem)
- Conceitos de Recursão e Memoização
- Programação Dinâmica Top-Down e Bottom-Up

---

## 📄 Licença

Este projeto é parte da Global Solution da FIAP - 2025

---

**Data de Entrega:** 21/11/2025  
