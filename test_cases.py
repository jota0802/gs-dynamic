"""
Arquivo de Testes Adicionais e Exemplos de Uso
Global Solution 2025 - Dynamic Programming

Este arquivo demonstra como usar cada uma das funções individualmente
e inclui testes unitários básicos.
"""

from portfolio_optimization import (
    greedy_portfolio,
    recursive_portfolio,
    memoized_portfolio,
    dp_bottom_up_portfolio
)


def test_exemplo_basico():
    """
    Testa com o exemplo básico do enunciado.
    """
    print("=" * 70)
    print("TESTE 1: Exemplo Básico do Enunciado")
    print("=" * 70)
    
    projetos = [
        ("Projeto A", 12, 4),
        ("Projeto B", 10, 3),
        ("Projeto C", 7, 2),
        ("Projeto D", 4, 3)
    ]
    capacidade = 10
    
    print(f"\nCapacidade: {capacidade}")
    print("Projetos:", projetos)
    
    # Testa todas as 4 abordagens
    resultado_greedy = greedy_portfolio(projetos, capacidade)
    resultado_recursivo = recursive_portfolio(projetos, capacidade)
    resultado_memo = memoized_portfolio(projetos, capacidade)
    resultado_dp = dp_bottom_up_portfolio(projetos, capacidade)
    
    print(f"\nGreedy: {resultado_greedy}")
    print(f"Recursivo: {resultado_recursivo}")
    print(f"Memoização: {resultado_memo}")
    print(f"DP Bottom-Up: {resultado_dp}")
    
    # Verifica se as soluções ótimas são iguais
    assert resultado_recursivo == resultado_memo == resultado_dp[0], \
        "Soluções ótimas diferentes!"
    
    print("\n✅ Teste 1 passou!")


def test_greedy_falha():
    """
    Demonstra um caso onde Greedy falha.
    """
    print("\n" + "=" * 70)
    print("TESTE 2: Caso onde Greedy Falha")
    print("=" * 70)
    
    # Este é um caso clássico onde greedy falha
    projetos = [
        ("X", 60, 10),   # V/E = 6.0
        ("Y", 100, 20),  # V/E = 5.0
        ("Z", 120, 30)   # V/E = 4.0
    ]
    capacidade = 50
    
    print(f"\nCapacidade: {capacidade}")
    print("Projetos:", projetos)
    print("\nRelações V/E:")
    for nome, valor, custo in projetos:
        print(f"  {nome}: {valor}/{custo} = {valor/custo:.2f}")
    
    valor_greedy, proj_greedy, _ = greedy_portfolio(projetos, capacidade)
    valor_otimo, proj_otimo = dp_bottom_up_portfolio(projetos, capacidade)
    
    print(f"\nGreedy escolhe: {proj_greedy} = {valor_greedy}")
    print(f"Ótimo é: {proj_otimo} = {valor_otimo}")
    print(f"\nDiferença: {valor_otimo - valor_greedy}")
    
    assert valor_greedy < valor_otimo, "Greedy deveria falhar aqui!"
    print("\n✅ Teste 2 passou! Greedy falhou como esperado.")


def test_caso_vazio():
    """
    Testa com lista vazia de projetos.
    """
    print("\n" + "=" * 70)
    print("TESTE 3: Caso Vazio")
    print("=" * 70)
    
    projetos = []
    capacidade = 10
    
    print(f"\nCapacidade: {capacidade}")
    print("Projetos:", projetos)
    
    resultado_recursivo = recursive_portfolio(projetos, capacidade)
    resultado_memo = memoized_portfolio(projetos, capacidade)
    resultado_dp = dp_bottom_up_portfolio(projetos, capacidade)
    
    print(f"\nRecursivo: {resultado_recursivo}")
    print(f"Memoização: {resultado_memo}")
    print(f"DP Bottom-Up: {resultado_dp}")
    
    assert resultado_recursivo == resultado_memo == resultado_dp[0] == 0, \
        "Lista vazia deveria retornar 0!"
    
    print("\n✅ Teste 3 passou!")


def test_capacidade_zero():
    """
    Testa com capacidade zero.
    """
    print("\n" + "=" * 70)
    print("TESTE 4: Capacidade Zero")
    print("=" * 70)
    
    projetos = [
        ("P1", 10, 5),
        ("P2", 20, 3)
    ]
    capacidade = 0
    
    print(f"\nCapacidade: {capacidade}")
    print("Projetos:", projetos)
    
    resultado_recursivo = recursive_portfolio(projetos, capacidade)
    resultado_memo = memoized_portfolio(projetos, capacidade)
    resultado_dp = dp_bottom_up_portfolio(projetos, capacidade)
    
    print(f"\nRecursivo: {resultado_recursivo}")
    print(f"Memoização: {resultado_memo}")
    print(f"DP Bottom-Up: {resultado_dp}")
    
    assert resultado_recursivo == resultado_memo == resultado_dp[0] == 0, \
        "Capacidade 0 deveria retornar 0!"
    
    print("\n✅ Teste 4 passou!")


def test_um_projeto():
    """
    Testa com apenas um projeto.
    """
    print("\n" + "=" * 70)
    print("TESTE 5: Um Único Projeto")
    print("=" * 70)
    
    # Caso 1: Projeto cabe
    projetos1 = [("P1", 15, 5)]
    capacidade1 = 10
    
    print(f"\nCaso 1 - Projeto cabe:")
    print(f"Capacidade: {capacidade1}, Projeto: {projetos1}")
    
    resultado1 = dp_bottom_up_portfolio(projetos1, capacidade1)
    print(f"Resultado: {resultado1}")
    assert resultado1[0] == 15, "Deveria incluir o projeto!"
    
    # Caso 2: Projeto não cabe
    projetos2 = [("P1", 15, 15)]
    capacidade2 = 10
    
    print(f"\nCaso 2 - Projeto NÃO cabe:")
    print(f"Capacidade: {capacidade2}, Projeto: {projetos2}")
    
    resultado2 = dp_bottom_up_portfolio(projetos2, capacidade2)
    print(f"Resultado: {resultado2}")
    assert resultado2[0] == 0, "Não deveria incluir o projeto!"
    
    print("\n✅ Teste 5 passou!")


def test_todos_projetos_mesma_razao():
    """
    Testa quando todos os projetos têm a mesma relação V/E.
    """
    print("\n" + "=" * 70)
    print("TESTE 6: Projetos com Mesma Relação V/E")
    print("=" * 70)
    
    # Todos têm V/E = 2.0
    projetos = [
        ("P1", 10, 5),
        ("P2", 6, 3),
        ("P3", 4, 2)
    ]
    capacidade = 8
    
    print(f"\nCapacidade: {capacidade}")
    print("Projetos (todos com V/E = 2.0):", projetos)
    
    valor_otimo, proj_otimo = dp_bottom_up_portfolio(projetos, capacidade)
    
    print(f"\nSolução Ótima: {proj_otimo} = {valor_otimo}")
    
    # Deve escolher os projetos que maximizam o uso da capacidade
    assert valor_otimo == 16, f"Esperado 16, obteve {valor_otimo}"
    
    print("\n✅ Teste 6 passou!")


def demonstrar_performance():
    """
    Demonstra a diferença de performance entre as abordagens.
    ATENÇÃO: Não execute com n muito grande para a recursiva pura!
    """
    print("\n" + "=" * 70)
    print("DEMONSTRAÇÃO: Diferença de Performance")
    print("=" * 70)
    
    import time
    
    # Cria um caso de teste moderado
    projetos = [
        (f"P{i}", i*10 + 5, i*2 + 1) 
        for i in range(1, 11)  # 10 projetos
    ]
    capacidade = 30
    
    print(f"\nTeste com {len(projetos)} projetos e capacidade {capacidade}")
    print("⚠️  Recursiva pura será lenta!\n")
    
    # Memoização
    start = time.time()
    resultado_memo = memoized_portfolio(projetos, capacidade)
    tempo_memo = time.time() - start
    print(f"Memoização: {resultado_memo} (tempo: {tempo_memo:.6f}s)")
    
    # DP Bottom-Up
    start = time.time()
    resultado_dp, _ = dp_bottom_up_portfolio(projetos, capacidade)
    tempo_dp = time.time() - start
    print(f"DP Bottom-Up: {resultado_dp} (tempo: {tempo_dp:.6f}s)")
    
    # Recursiva (CUIDADO!)
    print("\n⚠️  Executando recursiva pura (pode demorar)...")
    start = time.time()
    resultado_rec = recursive_portfolio(projetos, capacidade)
    tempo_rec = time.time() - start
    print(f"Recursiva Pura: {resultado_rec} (tempo: {tempo_rec:.6f}s)")
    
    print(f"\n📊 Speedup:")
    print(f"   DP é {tempo_rec/tempo_dp:.2f}x mais rápida que Recursiva")
    print(f"   Memoização é {tempo_rec/tempo_memo:.2f}x mais rápida que Recursiva")
    
    print("\n✅ Demonstração concluída!")


def exemplo_uso_individual():
    """
    Mostra como usar cada função individualmente.
    """
    print("\n" + "=" * 70)
    print("EXEMPLO: Uso Individual das Funções")
    print("=" * 70)
    
    # Define os dados
    projetos = [
        ("Website", 50, 10),
        ("App Mobile", 40, 8),
        ("Dashboard", 30, 6),
        ("API", 20, 4)
    ]
    capacidade = 20
    
    print("\n--- Dados do Problema ---")
    print(f"Capacidade: {capacidade} Horas-Especialista")
    print("\nProjetos:")
    for nome, valor, custo in projetos:
        print(f"  {nome}: Valor={valor}, Custo={custo}")
    
    print("\n--- Solução Greedy ---")
    valor, selecionados, horas = greedy_portfolio(projetos, capacidade)
    print(f"Valor Total: {valor}")
    print(f"Projetos: {', '.join(selecionados)}")
    print(f"Horas Usadas: {horas}/{capacidade}")
    
    print("\n--- Solução Recursiva ---")
    valor_rec = recursive_portfolio(projetos, capacidade)
    print(f"Valor Máximo: {valor_rec}")
    
    print("\n--- Solução com Memoização ---")
    valor_memo = memoized_portfolio(projetos, capacidade)
    print(f"Valor Máximo: {valor_memo}")
    
    print("\n--- Solução DP Bottom-Up (Completa) ---")
    valor_dp, projetos_dp = dp_bottom_up_portfolio(projetos, capacidade)
    print(f"Valor Máximo: {valor_dp}")
    print(f"Projetos Selecionados: {', '.join(projetos_dp)}")
    
    print("\n✅ Exemplo concluído!")


def executar_todos_os_testes():
    """
    Executa todos os testes em sequência.
    """
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "SUITE DE TESTES COMPLETA" + " " * 29 + "║")
    print("╚" + "=" * 68 + "╝")
    
    try:
        test_exemplo_basico()
        test_greedy_falha()
        test_caso_vazio()
        test_capacidade_zero()
        test_um_projeto()
        test_todos_projetos_mesma_razao()
        exemplo_uso_individual()
        
        print("\n" + "=" * 70)
        print("🎉 TODOS OS TESTES PASSARAM! 🎉")
        print("=" * 70)
        
        # Pergunta se quer ver a demonstração de performance
        print("\n⚠️  Deseja executar a demonstração de performance?")
        print("   (Pode demorar alguns segundos)")
        resposta = input("   [s/N]: ").lower()
        
        if resposta == 's':
            demonstrar_performance()
        
    except AssertionError as e:
        print(f"\n❌ TESTE FALHOU: {e}")
    except Exception as e:
        print(f"\n❌ ERRO: {e}")


if __name__ == "__main__":
    executar_todos_os_testes()
