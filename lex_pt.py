import re
from typing import List, Tuple
# Analisador léxico de lingua portuguesa... será?

# Conjunto de palavras fechadas mais frequentes em português
# (poderia vir de um arquivo ou ser bem maior)
PALAVRAS_FECHADAS = {
    # Artigos
    'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas',
    
    # Preposições + contrações
    'de', 'do', 'da', 'dos', 'das', 'em', 'no', 'na', 'nos', 'nas',
    'por', 'pelo', 'pela', 'pelos', 'pelas', 'para', 'com', 'ao', 'à', 'às',
    
    # Pronomes pessoais
    'eu', 'me', 'mim', 'comigo', 'tu', 'te', 'ti', 'contigo', 'você', 'vocês',
    'se', 'si', 'consigo', 'ele', 'ela', 'o', 'a', 'lhe', 'lhes',
    'nós', 'nos', 'conosco', 'vós', 'vos', 'convosco',
    
    # Pronomes possessivos
    'meu', 'minha', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas',
    'seu', 'sua', 'seus', 'suas', 'nosso', 'nossa', 'nossos', 'nossas',
    
    # Pronomes demonstrativos
    'este', 'esta', 'isto', 'esse', 'essa', 'isso', 'aquele', 'aquela', 'aquilo',
    
    # Conjunções coordenativas
    'e', 'mas', 'ou', 'nem', 'porém', 'todavia', 'contudo', 'entretanto',
    
    # Conjunções subordinativas mais comuns
    'que', 'porque', 'como', 'se', 'quando', 'onde', 'quanto',
}

# Verbos auxiliares e muito frequentes (formas básicas)
VERBOS_AUXILIARES_E_COMUNS = {
    'ser', 'estar', 'ter', 'haver', 'ir', 'vir', 'poder', 'querer',
    'dever', 'fazer', 'dizer', 'dar', 'ver', 'saber', 'ficar',
    'ficava', 'ficou', 'era', 'foi', 'é', 'são', 'está', 'estava',
}

def classificar_token(token: str) -> str:
    """
    Classifica o token de forma simples e heurística
    Retorna '??' quando não consegue classificar com razoabilidade
    """
    if not token or token.isspace():
        return 'ESPAÇO'

    token_lower = token.lower()

    # 1. Pontuação (sequências de pontuação são tratadas como um token único)
    if re.match(r'^[.,;:!?…—–()[\]{}“”‘’«»"\'\-]+$', token):
        return 'PONTUAÇÃO'

    # 2. Palavras conhecidas (fechadas)
    if token_lower in PALAVRAS_FECHADAS:
        if token_lower in {'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas'}:
            return 'ARTIGO'
        if token_lower in {'de', 'do', 'da', 'em', 'no', 'na', 'para', 'com', 'ao', 'à'}:
            return 'PREPOSIÇÃO'
        if token_lower in {'eu', 'me', 'mim', 'tu', 'te', 'se', 'ele', 'ela', 'nós', 'nos'}:
            return 'PRONOME'
        if token_lower in {'meu', 'minha', 'teu', 'tua', 'seu', 'sua'}:
            return 'PRONOME_POSSESSIVO'
        if token_lower in {'e', 'mas', 'ou', 'que'}:
            return 'CONJUNÇÃO'
        return 'PALAVRA_FECHADA'

    # 3. Verbos conhecidos
    if token_lower in VERBOS_AUXILIARES_E_COMUNS:
        return 'VERBO'

    # 4. Regras aproximadas para verbos (muito simplificado)
    if token_lower.endswith(('ar', 'er', 'ir', 'ava', 'ava', 'ou', 'ia', 'ei', 'emos', 'am')):
        if len(token_lower) >= 4:
            return 'VERBO'

    # 5. Nomes próprios (inicia com maiúscula e não é todo maiúsculo)
    if token[0].isupper() and not token.isupper() and len(token) > 2:
        return 'NOME_PRÓPRIO'

    # 6. Números
    if re.match(r'^-?\d+(?:\.\d+)?$', token):
        return 'NÚMERO'

    # 7. Palavras compostas com hífen (ex: chapéu-de-sol, auto-escola)
    if '-' in token and re.match(r'^[A-Za-záàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ\-]+$', token):
        return 'PALAVRA_COMPOSTA'

    # Fallback: substantivo, adjetivo ou desconhecido
    if token_lower.isalpha():
        return 'SUBSTANTIVO / ADJETIVO'

    # Caso não identificado
    return '??'


def tokenizar_portugues(texto: str) -> List[Tuple[str, str]]:
    """
    Analisador léxico simples para português literário
    Devolve lista de tuplas (token, categoria)
    """
    # Padrão para separar palavras, pontuação e manter compostos com hífen
    padrao = r"""
        (?P<palavra>   [A-Za-záàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ]+(?:-[A-Za-záàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ]+)* )
        | (?P<pontuacao>[.,;:!?…—–()[\]{}“”‘’«»"\'\-]+)
        | (?P<espaco>   \s+)
    """

    regex = re.compile(padrao, re.VERBOSE | re.UNICODE)

    tokens = []

    for match in regex.finditer(texto):
        if match.group('palavra'):
            token = match.group('palavra')
            tipo = classificar_token(token)
            tokens.append((token, tipo))
        elif match.group('pontuacao'):
            token = match.group('pontuacao')
            tipo = classificar_token(token)
            tokens.append((token, tipo))
        # ignoramos espaços

    return tokens


# Exemplo de uso
if __name__ == "__main__":
    texto = """
Uma noite destas, vindo da cidade para o Engenho Novo, encontrei no
trem da Central um rapaz aqui do bairro, que eu conheço de vista e
de chapéu. Comprimentou-me, sentou-se ao pé de mim e disse:
"Boa noite, Bentinho!"
    """

    resultado = tokenizar_portugues(texto)

    print("Token".ljust(22), "Tipo")
    print("-" * 45)
    for token, tipo in resultado:
        print(f"{token:<22} {tipo}")
