def calcular_tempo_trabalho(num_processos_5_91: int, num_processos_7_59: int, num_processos_0_85: int) -> float:
    """
    Calcula o tempo total de trabalho baseado na quantidade de processos.
    """
    tempo_5_91 = num_processos_5_91 * 5.91
    tempo_7_59 = num_processos_7_59 * 7.59
    tempo_0_85 = num_processos_0_85 * 0.85
    
    return tempo_5_91 + tempo_7_59 + tempo_0_85
