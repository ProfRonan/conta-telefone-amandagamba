"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    conta = 200
    chamadas = int(input("Digite o número de chamadas realizadas."))
    if chamadas <= 100:
      conta += 0
    elif chamadas > 100 and chamadas <= 150:
      conta += 0.60 * (chamadas - 100)
    elif chamadas > 150 and chamadas <= 200:
      conta += 30 + 0.5 * (chamadas - 150)
    else:
      conta += 55+ 0.4 * (chamadas-200)

    print(f"O valor devido é R$ {conta:.2f}.")


if __name__ == '__main__':
    main()
