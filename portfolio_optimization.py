"""
Global Solution 2025 - Dynamic Programming
Otimização de Portfólio de Projetos (Problema da Mochila 0/1)

Disciplina: Dynamic Programming
Curso: Engenharia de Software
Professor: Marcelo Amorim

Este módulo implementa 4 abordagens diferentes para resolver o problema:
1. Estratégia Gulosa (Greedy)
2. Solução Recursiva Pura
3. Programação Dinâmica Top-Down (Memoização)
4. Programação Dinâmica Bottom-Up (Iterativa)
"""


# ==============================================================================
# FASE 1: ESTRATÉGIA GULOSA (GREEDY)
# ==============================================================================

def greedy_portfolio(projetos, capacidade):
    """
    Implementa uma estratégia gulosa para seleção de projetos.
    
    ABORDAGEM:
    - Calcula a relação Valor/Custo (V/E) para cada projeto
    - Ordena os projetos pela relação V/E em ordem decrescente
    - Seleciona projetos sequencialmente até esgotar a capacidade
    
    LIMITAÇÃO:
    Esta estratégia NÃO GARANTE a solução ótima! É uma heurística que pode
    falhar em casos específicos onde a combinação ideal não segue a ordem gulosa.
    
    COMPLEXIDADE DE TEMPO: O(n log n)
    - Ordenação dos projetos: O(n log n)
    - Iteração pelos projetos: O(n)
    - Total: O(n log n)
    
    COMPLEXIDADE DE ESPAÇO: O(n)
    - Lista ordenada: O(n)
    
    Args:
        projetos: Lista de tuplas (nome, valor, custo)
        capacidade: Capacidade máxima de Horas-Especialista
        
    Returns:
        Tupla contendo (valor_total, projetos_selecionados, horas_utilizadas)
    """
    # Calcula a relação V/E e cria lista ordenada
    # Cada elemento: (relação V/E, nome, valor, custo)
    projetos_com_razao = []
    for nome, valor, custo in projetos:
        razao = valor / custo  # Relação Valor/Custo
        projetos_com_razao.append((razao, nome, valor, custo))
    
    # Ordena em ordem DECRESCENTE pela relação V/E
    projetos_ordenados = sorted(projetos_com_razao, reverse=True)
    
    # Seleciona projetos gulosa
    valor_total = 0
    horas_utilizadas = 0
    projetos_selecionados = []
    
    for razao, nome, valor, custo in projetos_ordenados:
        # Verifica se ainda há capacidade para este projeto
        if horas_utilizadas + custo <= capacidade:
            # Aceita o projeto
            projetos_selecionados.append(nome)
            valor_total += valor
            horas_utilizadas += custo
    
    return (valor_total, projetos_selecionados, horas_utilizadas)


# ==============================================================================
# FASE 2: SOLUÇÃO RECURSIVA PURA
# ==============================================================================

def recursive_portfolio(projetos, capacidade, index=0):
    """
    Solução recursiva pura para o problema da mochila 0/1.
    
    ABORDAGEM:
    - Explora TODAS as combinações possíveis de projetos
    - Para cada projeto, testa duas opções:
      1. Incluir o projeto (se couber)
      2. Não incluir o projeto
    - Retorna o máximo entre as duas opções
    
    FÓRMULA DE RECORRÊNCIA:
    MaximoValor(i, c) = max(
        MaximoValor(i-1, c),                              # Não incluir projeto i
        Valor_i + MaximoValor(i-1, c - Custo_i)           # Incluir projeto i
    )
    
    CASO BASE:
    - Se não há mais projetos (index >= len(projetos)): retorna 0
    - Se não há capacidade (capacidade <= 0): retorna 0
    
    LIMITAÇÃO:
    Esta solução RECALCULA os mesmos subproblemas múltiplas vezes!
    Isso leva a uma complexidade exponencial, tornando-a impraticável
    para entradas grandes.
    
    COMPLEXIDADE DE TEMPO: O(2^n)
    - Árvore de recursão com 2 ramificações por nível
    - Profundidade máxima: n (número de projetos)
    - Total de chamadas: 2^n
    
    COMPLEXIDADE DE ESPAÇO: O(n)
    - Pilha de recursão: O(n) no pior caso
    
    Args:
        projetos: Lista de tuplas (nome, valor, custo)
        capacidade: Capacidade restante de Horas-Especialista
        index: Índice do projeto atual sendo considerado
        
    Returns:
        Valor máximo que pode ser obtido
    """
    # CASO BASE 1: Não há mais projetos para considerar
    if index >= len(projetos):
        return 0
    
    # CASO BASE 2: Não há capacidade restante
    if capacidade <= 0:
        return 0
    
    # Extrai informações do projeto atual
    nome, valor, custo = projetos[index]
    
    # OPÇÃO 1: NÃO incluir o projeto atual
    # Avança para o próximo projeto mantendo a mesma capacidade
    valor_sem_incluir = recursive_portfolio(projetos, capacidade, index + 1)
    
    # OPÇÃO 2: INCLUIR o projeto atual (se couber)
    valor_com_incluir = 0
    if custo <= capacidade:
        # Soma o valor deste projeto + valor ótimo do restante
        # com capacidade reduzida
        valor_com_incluir = valor + recursive_portfolio(
            projetos, 
            capacidade - custo, 
            index + 1
        )
    
    # Retorna o MÁXIMO entre incluir e não incluir
    return max(valor_sem_incluir, valor_com_incluir)


# ==============================================================================
# FASE 3: PROGRAMAÇÃO DINÂMICA TOP-DOWN (MEMOIZAÇÃO)
# ==============================================================================

def memoized_portfolio(projetos, capacidade):
    """
    Solução com Programação Dinâmica Top-Down usando Memoização.
    
    ABORDAGEM:
    - Usa a MESMA lógica recursiva da Fase 2
    - Adiciona um CACHE (dicionário) para armazenar resultados
    - Antes de calcular, verifica se o resultado já foi computado
    - Se sim, retorna o valor do cache
    - Se não, calcula e armazena no cache antes de retornar
    
    VANTAGEM:
    Elimina a redundância de cálculos! Cada subproblema único é
    resolvido apenas UMA VEZ. Isso reduz drasticamente o tempo de execução.
    
    COMPLEXIDADE DE TEMPO: O(n × C)
    - n = número de projetos
    - C = capacidade máxima
    - Cada combinação (index, capacidade) é calculada apenas uma vez
    - Total de subproblemas: n × C
    
    COMPLEXIDADE DE ESPAÇO: O(n × C)
    - Cache (memo): O(n × C) para armazenar todos os subproblemas
    - Pilha de recursão: O(n)
    - Total: O(n × C)
    
    Args:
        projetos: Lista de tuplas (nome, valor, custo)
        capacidade: Capacidade máxima de Horas-Especialista
        
    Returns:
        Valor máximo que pode ser obtido
    """
    # Dicionário para armazenar resultados
    # Chave: (index, capacidade_restante)
    # Valor: valor_maximo para esse estado
    memo = {}
    
    def helper(index, cap_restante):
        """
        Função auxiliar recursiva com memoização.
        
        Args:
            index: Índice do projeto atual
            cap_restante: Capacidade restante
            
        Returns:
            Valor máximo para o estado (index, cap_restante)
        """
        # IMPORTANTE: Verifica se o resultado já foi calculado
        if (index, cap_restante) in memo:
            return memo[(index, cap_restante)]
        
        # CASO BASE 1: Não há mais projetos
        if index >= len(projetos):
            return 0
        
        # CASO BASE 2: Não há capacidade
        if cap_restante <= 0:
            return 0
        
        nome, valor, custo = projetos[index]
        
        # OPÇÃO 1: Não incluir o projeto atual
        valor_sem = helper(index + 1, cap_restante)
        
        # OPÇÃO 2: Incluir o projeto atual (se couber)
        valor_com = 0
        if custo <= cap_restante:
            valor_com = valor + helper(index + 1, cap_restante - custo)
        
        # Calcula o máximo
        resultado = max(valor_sem, valor_com)
        
        # ARMAZENA no cache antes de retornar
        memo[(index, cap_restante)] = resultado
        
        return resultado
    
    # Chama a função auxiliar começando do índice 0
    return helper(0, capacidade)


# ==============================================================================
# FASE 4: PROGRAMAÇÃO DINÂMICA BOTTOM-UP (ITERATIVA)
# ==============================================================================

def dp_bottom_up_portfolio(projetos, capacidade):
    """
    Solução com Programação Dinâmica Bottom-Up (Iterativa).
    
    ABORDAGEM:
    - Constrói uma TABELA (matriz) de forma iterativa
    - Tabela T[i][c] representa:
      "Valor máximo com os primeiros i projetos e capacidade c"
    - Preenche a tabela linha por linha (projeto por projeto)
    - Cada célula é calculada usando a fórmula de recorrência
    - Resultado final está em T[n][capacidade]
    
    FÓRMULA DE RECORRÊNCIA:
    T[i][c] = max(
        T[i-1][c],                    # Não incluir projeto i
        Valor_i + T[i-1][c-Custo_i]   # Incluir projeto i (se couber)
    )
    
    INICIALIZAÇÃO:
    - Primeira linha (sem projetos): T[0][c] = 0 para todo c
    - Primeira coluna (sem capacidade): T[i][0] = 0 para todo i
    
    VANTAGENS:
    - Não usa recursão (sem overhead de chamadas de função)
    - Uso eficiente de memória em Python
    - Mais intuitivo para debug (pode visualizar a tabela)
    
    COMPLEXIDADE DE TEMPO: O(n × C)
    - n = número de projetos
    - C = capacidade máxima
    - Dois loops aninhados: O(n × C)
    
    COMPLEXIDADE DE ESPAÇO: O(n × C)
    - Tabela T: (n+1) × (C+1) = O(n × C)
    - Nota: Pode ser otimizada para O(C) usando apenas duas linhas
    
    Args:
        projetos: Lista de tuplas (nome, valor, custo)
        capacidade: Capacidade máxima de Horas-Especialista
        
    Returns:
        Tupla contendo (valor_maximo, projetos_selecionados)
    """
    n = len(projetos)
    
    # Cria a tabela T com (n+1) linhas e (capacidade+1) colunas
    # T[i][c] = valor máximo com primeiros i projetos e capacidade c
    # Inicializa tudo com 0
    T = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    
    # PREENCHE A TABELA (Bottom-Up)
    # i representa: quantos projetos estamos considerando (0 até n)
    for i in range(1, n + 1):
        # Índice real do projeto na lista (projetos começa em 0)
        projeto_idx = i - 1
        nome, valor, custo = projetos[projeto_idx]
        
        # c representa: capacidade disponível (0 até capacidade)
        for c in range(capacidade + 1):
            # OPÇÃO 1: NÃO incluir o projeto i
            # O valor máximo é o mesmo de considerar apenas os i-1 primeiros
            valor_sem_incluir = T[i-1][c]
            
            # OPÇÃO 2: INCLUIR o projeto i (se couber)
            valor_com_incluir = 0
            if custo <= c:
                # Soma: valor deste projeto + valor ótimo com capacidade reduzida
                valor_com_incluir = valor + T[i-1][c - custo]
            
            # Armazena o MÁXIMO das duas opções
            T[i][c] = max(valor_sem_incluir, valor_com_incluir)
    
    # O resultado final está na última célula da tabela
    valor_maximo = T[n][capacidade]
    
    # RECONSTRUÇÃO DA SOLUÇÃO (Backtracking)
    # Descobre quais projetos foram selecionados
    projetos_selecionados = []
    i = n
    c = capacidade
    
    while i > 0 and c > 0:
        # Se o valor mudou em relação à linha anterior,
        # significa que incluímos este projeto
        if T[i][c] != T[i-1][c]:
            projeto_idx = i - 1
            nome, valor, custo = projetos[projeto_idx]
            projetos_selecionados.append(nome)
            # Reduz a capacidade
            c -= custo
        # Move para o projeto anterior
        i -= 1
    
    # Inverte a lista (ela foi construída de trás para frente)
    projetos_selecionados.reverse()
    
    return (valor_maximo, projetos_selecionados)


# ==============================================================================
# FUNÇÃO PRINCIPAL E TESTES
# ==============================================================================

def executar_testes():
    """
    Executa todos os casos de teste e compara os resultados das 4 abordagens.
    """
    print("=" * 80)
    print("GLOBAL SOLUTION 2025 - OTIMIZAÇÃO DE PORTFÓLIO DE PROJETOS")
    print("Problema da Mochila 0/1 (Knapsack Problem)")
    print("=" * 80)
    print()
    
    # ========================================================================
    # CASO DE TESTE 1: Exemplo do Enunciado
    # ========================================================================
    print("-" * 80)
    print("CASO DE TESTE 1: Exemplo do Enunciado")
    print("-" * 80)
    
    projetos1 = [
        ("Projeto A", 12, 4),
        ("Projeto B", 10, 3),
        ("Projeto C", 7, 2),
        ("Projeto D", 4, 3)
    ]
    capacidade1 = 10
    
    print(f"\nCapacidade: {capacidade1} Horas-Especialista")
    print("\nProjetos disponíveis:")
    print(f"{'Nome':<15} {'Valor':<10} {'Custo':<10} {'Relação V/E':<15}")
    print("-" * 50)
    for nome, valor, custo in projetos1:
        print(f"{nome:<15} {valor:<10} {custo:<10} {valor/custo:<15.2f}")
    
    print("\n" + "="*50)
    print("RESULTADOS:")
    print("="*50)
    
    # Fase 1: Greedy
    valor_g, proj_g, horas_g = greedy_portfolio(projetos1, capacidade1)
    print(f"\n1. GREEDY:")
    print(f"   Valor Total: {valor_g}")
    print(f"   Projetos: {', '.join(proj_g)}")
    print(f"   Horas Utilizadas: {horas_g}/{capacidade1}")
    
    # Fase 2: Recursiva
    valor_r = recursive_portfolio(projetos1, capacidade1)
    print(f"\n2. RECURSIVA PURA:")
    print(f"   Valor Máximo: {valor_r}")
    
    # Fase 3: Memoização
    valor_m = memoized_portfolio(projetos1, capacidade1)
    print(f"\n3. MEMOIZAÇÃO (Top-Down):")
    print(f"   Valor Máximo: {valor_m}")
    
    # Fase 4: DP Bottom-Up
    valor_dp, proj_dp = dp_bottom_up_portfolio(projetos1, capacidade1)
    print(f"\n4. DP ITERATIVA (Bottom-Up):")
    print(f"   Valor Máximo: {valor_dp}")
    print(f"   Projetos Selecionados: {', '.join(proj_dp)}")
    
    print("\n" + "="*50)
    print("ANÁLISE:")
    print("="*50)
    if valor_g == valor_dp:
        print("✅ Neste caso, a estratégia Greedy encontrou o ótimo!")
    else:
        print(f"⚠️  A estratégia Greedy falhou!")
        print(f"   Greedy: {valor_g} vs Ótimo: {valor_dp}")
        print(f"   Diferença: {valor_dp - valor_g}")
    
    # ========================================================================
    # CASO DE TESTE 2: Greedy Falha (Exemplo Clássico)
    # ========================================================================
    print("\n\n" + "-" * 80)
    print("CASO DE TESTE 2: Demonstração onde Greedy FALHA")
    print("-" * 80)
    
    projetos2 = [
        ("Projeto X", 60, 10),
        ("Projeto Y", 100, 20),
        ("Projeto Z", 120, 30)
    ]
    capacidade2 = 50
    
    print(f"\nCapacidade: {capacidade2} Horas-Especialista")
    print("\nProjetos disponíveis:")
    print(f"{'Nome':<15} {'Valor':<10} {'Custo':<10} {'Relação V/E':<15}")
    print("-" * 50)
    for nome, valor, custo in projetos2:
        print(f"{nome:<15} {valor:<10} {custo:<10} {valor/custo:<15.2f}")
    
    print("\n" + "="*50)
    print("RESULTADOS:")
    print("="*50)
    
    valor_g2, proj_g2, horas_g2 = greedy_portfolio(projetos2, capacidade2)
    valor_dp2, proj_dp2 = dp_bottom_up_portfolio(projetos2, capacidade2)
    
    print(f"\n1. GREEDY:")
    print(f"   Valor Total: {valor_g2}")
    print(f"   Projetos: {', '.join(proj_g2)}")
    print(f"   Horas: {horas_g2}/{capacidade2}")
    
    print(f"\n2. DP ÓTIMA:")
    print(f"   Valor Máximo: {valor_dp2}")
    print(f"   Projetos: {', '.join(proj_dp2)}")
    
    print("\n" + "="*50)
    print("ANÁLISE:")
    print("="*50)
    print(f"❌ Greedy escolheu projetos com melhor V/E, mas perdeu valor!")
    print(f"   Greedy: {valor_g2} vs Ótimo: {valor_dp2}")
    print(f"   Perda: {valor_dp2 - valor_g2} ({((valor_dp2-valor_g2)/valor_dp2*100):.1f}%)")
    
    # ========================================================================
    # CASO DE TESTE 3: Caso Simples
    # ========================================================================
    print("\n\n" + "-" * 80)
    print("CASO DE TESTE 3: Caso Simples (Verificação)")
    print("-" * 80)
    
    projetos3 = [
        ("P1", 10, 5),
        ("P2", 6, 3),
        ("P3", 12, 4)
    ]
    capacidade3 = 8
    
    print(f"\nCapacidade: {capacidade3} Horas-Especialista")
    valor_dp3, proj_dp3 = dp_bottom_up_portfolio(projetos3, capacidade3)
    print(f"\nSolução Ótima:")
    print(f"   Valor: {valor_dp3}")
    print(f"   Projetos: {', '.join(proj_dp3)}")
    
    # ========================================================================
    # CASO DE TESTE 4: Caso Maior
    # ========================================================================
    print("\n\n" + "-" * 80)
    print("CASO DE TESTE 4: Caso com Mais Projetos")
    print("-" * 80)
    
    projetos4 = [
        ("Proj A", 15, 5),
        ("Proj B", 20, 8),
        ("Proj C", 30, 12),
        ("Proj D", 10, 3),
        ("Proj E", 25, 10),
        ("Proj F", 8, 2)
    ]
    capacidade4 = 20
    
    print(f"\nCapacidade: {capacidade4} Horas-Especialista")
    print(f"Projetos disponíveis: {len(projetos4)}")
    
    valor_dp4, proj_dp4 = dp_bottom_up_portfolio(projetos4, capacidade4)
    print(f"\nSolução Ótima:")
    print(f"   Valor Máximo: {valor_dp4}")
    print(f"   Projetos: {', '.join(proj_dp4)}")
    
    # ========================================================================
    # RESUMO FINAL
    # ========================================================================
    print("\n\n" + "=" * 80)
    print("RESUMO DA ANÁLISE DE COMPLEXIDADE")
    print("=" * 80)
    print("\n| Estratégia          | Tempo      | Espaço     | Ótima? | Observações")
    print("|---------------------|------------|------------|--------|---------------------------")
    print("| Greedy              | O(n log n) | O(1)       | ❌     | Falha em alguns casos")
    print("| Recursiva Pura      | O(2^n)     | O(n)       | ✅     | Muito lenta, redundante")
    print("| Memoização (Top-D)  | O(n × C)   | O(n × C)   | ✅     | Recursiva + cache")
    print("| DP Bottom-Up        | O(n × C)   | O(n × C)   | ✅     | Mais eficiente, iterativa")
    
    print("\n" + "=" * 80)
    print("CONCLUSÃO")
    print("=" * 80)
    print("""
As abordagens de Programação Dinâmica (Fase 3 e 4) são SUPERIORES porque:

1. ✅ Garantem a solução ÓTIMA (ao contrário do Greedy)
2. ✅ Tempo POLINOMIAL O(n × C) (ao invés de exponencial O(2^n))
3. ✅ Evitam recálculos usando memoização/tabela

A escolha entre Top-Down (Memoização) e Bottom-Up (Iterativa) depende:
- Top-Down: Mais intuitiva, calcula apenas estados necessários
- Bottom-Up: Mais eficiente, sem overhead de recursão, permite otimização de espaço

Para problemas do mundo real, SEMPRE use Programação Dinâmica! 🚀
    """)
    
    print("=" * 80)
    print("FIM DOS TESTES")
    print("=" * 80)


# ==============================================================================
# EXECUÇÃO
# ==============================================================================

if __name__ == "__main__":
    executar_testes()
