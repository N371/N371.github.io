from django.db import models

class Cartoes(models.Model):
    quantidade  = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    numero_serial  = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    fila = models.BooleanField(default=True)
    estagio_atual = models.CharField(max_length=10)
    codigo_barras = models.CharField(max_length=10)
    itinerario =models.JSONField('Resultado', null=True, blank=True)
    id_produto = models.PositiveIntegerField()
    estrutura_produto = models.JSONField('Resultado', null=True, blank=True)
    id_versao_supermercado = models.PositiveIntegerField()
    id_destinacao = models.PositiveIntegerField()
    quantidade_regeitada = models.PositiveIntegerField()
    quantidade_aceita = models.PositiveIntegerField()
    id_ordem_de_venda = models.PositiveIntegerField()
    od_ordem_producao  = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    id_disparo = models.PositiveIntegerField()

class Produtos(models.Model):
    codigo = models.PositiveIntegerField()
    ativado = models.BooleanField(default=True)
    cod_barras = models.CharField(max_length=10)
    custo_unitario = models.PositiveIntegerField()
    descricao = models.CharField(max_length=255)
    familia = models.CharField(max_length=255)
    final = models.BooleanField(default=True)
    medida = models.CharField(max_length=255)
    arquivo_image = models.CharField(max_length=255)
    conteudo = models.CharField(max_length=255)
    tamanho_imagem = models.PositiveIntegerField()
    modificacao_imag = models.DateTimeField(auto_now=True)
    lote_minimo = models.PositiveIntegerField()
    opcional = models.CharField(max_length=255)
    opcional2 = models.CharField(max_length=255)
    opcional3 = models.CharField(max_length=255)
    opcional4 = models.CharField(max_length=255)
    opcional5 = models.CharField(max_length=255)
    lote_multiplo = models.PositiveIntegerField()
    vendivel = models.BooleanField(default=True)
    id_destinacao = models.PositiveIntegerField()
    id_origem = models.PositiveIntegerField()
    numero_serial = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

class Ordens(models.Model):
    id_supermercado = models.PositiveIntegerField()
    id_produto = models.PositiveIntegerField()
    ltplanejado = models.PositiveIntegerField()
    ltrealizado = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    qtd_em_aberto = models.PositiveIntegerField()
    qtd_entregue = models.PositiveIntegerField()
    qtd_pendente = models.PositiveIntegerField()
    qtd_cancelado = models.PositiveIntegerField()
    numero_de_ordem = models.CharField(max_length=10)
    valor  = models.PositiveIntegerField()
    dias_atrazados = models.PositiveIntegerField()
    descricao = models.CharField(max_length=255)
    ordem_venda  = models.PositiveIntegerField()
    tipo_ordem = models.CharField(max_length=255)
    consider = models.BooleanField(default=True)
    id_origem  = models.PositiveIntegerField()
    documento_linha = models.PositiveIntegerField()
    id_disparo = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now=True)
    data_esperada  = models.DateTimeField(auto_now=True)
    data_terminado  = models.DateTimeField(auto_now=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

class Calendario(models.Model):
    feriado = models.DateTimeField(auto_now=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

class Grupo_do_disparo(models.Model):
    user_id = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)


class Disparos(models.Model):
    tipo = models.CharField(max_length=255)
    user_id = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    id_grupo_do_disparo = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

class Logs_Cartoes(models.Model):
    id_cartao = models.PositiveIntegerField()
    id_produto = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    historico = models.JSONField('Resultado', null=True, blank=True)
    
class Metrica_Cartoes(models.Model):
    id_cartao = models.PositiveIntegerField()
    id_produto = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    estagio_atual = models.CharField(max_length=10)
    fila = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

class Demanda_calculada(models.Model):
    id_demanda = models.PositiveIntegerField()
    id_produto = models.PositiveIntegerField()
    media = models.PositiveIntegerField()
    st_dev = models.PositiveIntegerField()
    frequencia_on = models.PositiveIntegerField()
    media_quando_freq  = models.PositiveIntegerField()
    st_dev_quando_freq = models.PositiveIntegerField()
    volume_total = models.PositiveIntegerField()
    volume_relativo = models.PositiveIntegerField()
    volume_cumulativo = models.PositiveIntegerField()
    valor_total = models.PositiveIntegerField()
    valor_relativo = models.PositiveIntegerField()
    valor_cumulativo = models.PositiveIntegerField()
    contagem_valores = models.PositiveIntegerField()
    abc_valor = models.CharField(max_length=255)
    abc_volume = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

class Demanda_produtos(models.Model):
    id_demanda = models.PositiveIntegerField()
    id_produto = models.PositiveIntegerField()
    data  = models.DateTimeField(auto_now_add=True)
    valor  = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

class Demanda(models.Model):
    nome = models.CharField(max_length=255)
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(auto_now=True)
    volume_total = models.PositiveIntegerField()
    valor_total  = models.PositiveIntegerField()
    contagem_valores = models.PositiveIntegerField()
    base = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

class Estrutura_Produto(models.Model):
    id_produto = models.PositiveIntegerField()
    id_pai = models.PositiveIntegerField()
    qtd = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

class Integracao(models.Model):
    data_movimentacao = models.DateTimeField(auto_now=True)
    id_demanda = models.PositiveIntegerField()
    id_produto = models.PositiveIntegerField()
    movimentacao_id = models.PositiveIntegerField()
    descricao_movimentacao = models.CharField(max_length=255)
    qtd = models.PositiveIntegerField()

class Ordens_Integradas(models.Model):
    data_criacao = models.DateTimeField(auto_now=True)
    id_supermercado = models.PositiveIntegerField()
    id_ordem = models.PositiveIntegerField()
    id_produto = models.PositiveIntegerField()
    qtd_original = models.PositiveIntegerField()
    qtd_entregue = models.PositiveIntegerField()
    qtd_cancelado = models.PositiveIntegerField()

class Estoque(models.Model):
    id_supermercado = models.PositiveIntegerField()
    id_produto = models.PositiveIntegerField()
    qtd = models.PositiveIntegerField()

class Fases(models.Model):  
    nome = models.CharField(max_length=255) 
    code = models.CharField(max_length=10) 
    deposito = models.PositiveIntegerField()
    codigo_barras = models.CharField(max_length=10)  
    tercerizado = models.BooleanField(default=True)
    comprado = models.BooleanField(default=True)
    tem_fila = models.BooleanField(default=True)
    apelido = models.CharField(max_length=255) 

class Procedimentos(models.Model):
    nome = models.CharField(max_length=255)

class Processo_em_acao(models.Model):
    processo = models.CharField(max_length=255) 
    data_inicio  = models.DateTimeField(auto_now=True)
    percentual = models.PositiveIntegerField()
    status  = models.PositiveIntegerField()
    entidade  = models.CharField(max_length=255)  
    notas  = models.CharField(max_length=255) 
    arquivo_url = models.CharField(max_length=255) 
    id_disparo  = models.PositiveIntegerField()
    nome = models.CharField(max_length=255) 
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    data_final = models.DateTimeField(auto_now=True)

class Estoque_produtos(models.Model):
    id_supermercado = models.PositiveIntegerField()
    id_produto = models.PositiveIntegerField()
    qtd = models.PositiveIntegerField()
    data_operacao = models.DateTimeField(auto_now=True)
    hora_operacao = models.DateTimeField(auto_now=True)
    cod_operacao = models.PositiveIntegerField() 
    fonte = models.CharField(max_length=255)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    data_final = models.DateTimeField(auto_now=True)

class Estrutura_Produtos_local(models.Model):
    id_pai = models.PositiveIntegerField()
    id_produto = models.PositiveIntegerField()
    qtd = models.PositiveIntegerField()
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    data_final = models.DateTimeField(auto_now=True)

class Deposito_produtos(models.Model):   
    id_deposito = models.PositiveIntegerField() 
    id_produto = models.PositiveIntegerField()
    balanco = models.PositiveIntegerField()
    comitted = models.PositiveIntegerField()
    qtd_ordered = models.PositiveIntegerField()
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    data_final = models.DateTimeField(auto_now=True)

class Itineracio_producao(models.Model): 
    sequencia = models.PositiveIntegerField() 
    fase_id = models.PositiveIntegerField() 
    id_produto = models.PositiveIntegerField() 

class Ordem_venda(models.Model):
    numero_de_ordem = models.CharField(max_length=10)
    codigo_cliente = models.CharField(max_length=10)
    nome_cliente = models.CharField(max_length=255) 
    due_date = models.DateTimeField(auto_now=True) 
    status = models.PositiveIntegerField()  
    id_produto  = models.PositiveIntegerField() 
    qtd = models.PositiveIntegerField() 
    quantidade_entregue = models.PositiveIntegerField() 
    quantidade_cancelada = models.PositiveIntegerField() 
    wip_quantidade = models.PositiveIntegerField() 
    quantidade_pendente  = models.PositiveIntegerField() 
    unidade_venda_valor = models.CharField(max_length=10)
    id_origem = models.PositiveIntegerField() 
    documento_linha = models.PositiveIntegerField() 
    interno = models.BooleanField(default=True)
    terminado  = models.DateTimeField(auto_now=True) 
    criado = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

class Numeros_seriais(models.Model):
    numero_serial = models.PositiveIntegerField()
    numero_de_ordem = models.CharField(max_length=10)
    codigo_produto = models.CharField(max_length=10)
    issue_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

class Estagio_dos_Cartoes(models.Model):
    id_disparo  = models.PositiveIntegerField()
    id_produto  = models.PositiveIntegerField() 
    id_ordem_de_venda = models.PositiveIntegerField() 
    id_versao_supermercado = models.PositiveIntegerField() 
    qtd = models.PositiveIntegerField() 
    qtd_strutura = models.PositiveIntegerField() 
    cartao_valido = models.BooleanField(default=True)
    itinerafio = models.JSONField('Resultado', null=True, blank=True)
    destinacao_estagio_id = models.PositiveIntegerField() 
    incluido_pelo_pai = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

class Estagio_das_Ordens(models.Model):
    id_disparo  = models.PositiveIntegerField()
    id_produto  = models.PositiveIntegerField() 
    id_versao_supermercado = models.PositiveIntegerField() 
    id_estagio_cartao = models.PositiveIntegerField() 
    id_cartao = models.PositiveIntegerField()
    qtd = models.PositiveIntegerField() 
    tipo_ordem =  models.PositiveIntegerField() 
    lt = models.PositiveIntegerField()
    data_esperada = models.DateTimeField(auto_now=True)
    criado = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

class Estagio_Produtos_Depositos(models.Model):
    id_produto  = models.PositiveIntegerField()
    id_deposito  = models.PositiveIntegerField()
    qtd  = models.PositiveIntegerField() 
    qtd_comit =  models.PositiveIntegerField() 
    qtd_ordered =  models.PositiveIntegerField() 
    id_disparo  = models.PositiveIntegerField()
    criado = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

class Dias_estoque(models.Model):
    Metrica_data = models.DateTimeField(auto_now=True) 
    nome_supermercado = models.CharField(max_length=255) 
    familia_de_produtos = models.CharField(max_length=255) 
    valor_demanda = models.PositiveIntegerField()
    valor_estoque = models.PositiveIntegerField() 
    controle = models.CharField(max_length=255)
    criado = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

class Qualidade_estoque(models.Model):
    Metrica_data = models.DateTimeField(auto_now=True) 
    nome_supermercado = models.CharField(max_length=255) 
    familia_de_produtos = models.CharField(max_length=255) 
    vermelho = models.PositiveIntegerField()
    verde = models.PositiveIntegerField()
    amarelo = models.PositiveIntegerField()
    contagem_estoque_out = models.PositiveIntegerField()

class Valor_de_estoque(models.Model):
    Metrica_data = models.DateTimeField(auto_now=True) 
    nome_supermercado = models.CharField(max_length=255) 
    familia_de_produtos = models.CharField(max_length=255) 
    valor = models.PositiveIntegerField()
    controle = models.CharField(max_length=25)
    criado = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True) 

class Metricas_Supermercado(models.Model):
    id_supermercado = models.PositiveIntegerField()
    id_versao_supermercado = models.PositiveIntegerField() 
    id_produto  = models.PositiveIntegerField()
    Metrica_data = models.DateTimeField(auto_now=True) 
    valor_estoque = models.PositiveIntegerField() 
    dimensao_verde = models.PositiveIntegerField()
    dimensao_amarelo = models.PositiveIntegerField()
    dimensao_vermelho = models.PositiveIntegerField()
    unidades_por_cartao = models.PositiveIntegerField()
    verde_quadro = models.PositiveIntegerField()
    amarelo_quadro = models.PositiveIntegerField()
    vermelho_quadro = models.PositiveIntegerField()
    status_quadro = models.PositiveIntegerField()
    estoque_azul = models.PositiveIntegerField()
    estoque_verde = models.PositiveIntegerField()
    estoque_amarelo = models.PositiveIntegerField()
    estoque_vermelho = models.PositiveIntegerField()
    status_estoque = models.PositiveIntegerField()
    custo_unitario = models.PositiveIntegerField()
    demanda_diaria = models.PositiveIntegerField()
    lote_minimo = models.PositiveIntegerField()
    lote_multiplo = models.PositiveIntegerField()
    nome_supermercado = models.CharField(max_length=255) 
    id_versao_supermercado = models.PositiveIntegerField()
    codigo_produto = models.PositiveIntegerField()
    descricao_produto = models.CharField(max_length=255)
    familia_de_produtos = models.CharField(max_length=255)
    controle = models.CharField(max_length=255)

class Procedimento_Supermercado(models.Model):
    id_supermercado = models.PositiveIntegerField()
    id_procedimento = models.PositiveIntegerField()

class Supermercado_Produto(models.Model):
    id_supermercado = models.PositiveIntegerField()
    id_produto  = models.PositiveIntegerField()
    tamanho_container  = models.PositiveIntegerField()
    cartao_verde = models.PositiveIntegerField()
    cartao_amarelo = models.PositiveIntegerField()
    cartao_vermelho = models.PositiveIntegerField()
    rf = models.PositiveIntegerField()
    rlt = models.PositiveIntegerField()
    slt = models.PositiveIntegerField()
    controle = models.CharField(max_length=255)
    opcional = models.CharField(max_length=255)
    opcional2 = models.CharField(max_length=255)
    opcional3 = models.CharField(max_length=255)
    opcional4 = models.CharField(max_length=255)
    opcional5 = models.CharField(max_length=255)
    demanda_diaria = models.PositiveIntegerField()
    frequencia_on  = models.PositiveIntegerField()
    std_deviation_rf = models.PositiveIntegerField()
    std_deviation_flt = models.PositiveIntegerField()
    unidades_por_cartao = models.PositiveIntegerField()
    turnover = models.PositiveIntegerField()
    ajuste_cartoes = models.PositiveIntegerField()
    abc_valor = models.PositiveIntegerField()
    abc_volume = models.PositiveIntegerField()
    id_versao_supermercado = models.PositiveIntegerField()
    lote_minimo = models.PositiveIntegerField()
    codigo_barras = models.PositiveIntegerField()
    lote_multiplo = models.PositiveIntegerField()
    volume_relativo = models.PositiveIntegerField()
    valor_cumulativo = models.PositiveIntegerField()
    rf_valor = models.PositiveIntegerField()
    valor_total = models.PositiveIntegerField()
    rf_real = models.PositiveIntegerField()
    rlt_real = models.PositiveIntegerField()
    slt_real = models.PositiveIntegerField()
    custo_unitario = models.PositiveIntegerField()
    media_estoque = models.PositiveIntegerField()
    ciclo = models.PositiveIntegerField()
    ativado = models.BooleanField(default=True)
    numero_desvio_verde = models.PositiveIntegerField()
    numero_desvio_amarelo = models.PositiveIntegerField()
    id_destinacao = models.PositiveIntegerField()
    transporte_fase_id = models.PositiveIntegerField()
    deposito_suplimento_id = models.PositiveIntegerField()

class Supermercado_Versao(models.Model):
    descricao = models.CharField(max_length=255)
    data_inicio = models.DateTimeField(auto_now=True)
    data_fim = models.DateTimeField(auto_now=True)
    id_supermercado = models.PositiveIntegerField()
    numero_versao = models.PositiveIntegerField()
    id_versao_anterior = models.PositiveIntegerField()
    id_demanda = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

class Supermercado_Deposito(models.Model):
    id_supermercado = models.PositiveIntegerField()  
    id_deposito = models.PositiveIntegerField()
    visivel = models.BooleanField(default=True)
    considerar = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True) 

class Supermercado(models.Model):
    id_supermercado = models.PositiveIntegerField()
    nome = models.CharField(max_length=255)
    controle = models.CharField(max_length=255)
    opcional = models.CharField(max_length=255)
    opcional2 = models.CharField(max_length=255)
    opcional3 = models.CharField(max_length=255)
    opcional4 = models.CharField(max_length=255)
    opcional5 = models.CharField(max_length=255)
    rfs = models.CharField(max_length=10)
    codigo_barras = models.CharField(max_length=10)
    cartoes_genericos = models.BooleanField(default=True)
    pendentes_aprovacao = models.BooleanField(default=True)

class Fornecedores(models.Model):
    code = models.PositiveIntegerField()
    nome = models.CharField(max_length=255)
    fase_id = models.PositiveIntegerField()
    deposito_padrao = models.PositiveIntegerField()

class Reposicao_temporaria(models.Model):
    id_supermercado = models.PositiveIntegerField()
    id_produto  = models.PositiveIntegerField()
    qtd  = models.PositiveIntegerField()
    criado = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True) 

class Depositos(models.Model):
    code = models.PositiveIntegerField()
    descricao = models.CharField(max_length=255)
    tercerizado = models.BooleanField(default=True)
    pecas_regeitadas = models.BooleanField(default=True)















 
















    





   


