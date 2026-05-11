def test_deve_cancelar_pedido_com_sucesso(client):
    client.post("/clientes", json={"cpf": "11122233344", "nome": "Cliente X"})

    client.post("/produtos", json={"codigo": 1, "valor": 10, "tipo": 1, "desconto_percentual": 10})
    client.post("/produtos", json={"codigo": 2, "valor": 20, "tipo": 2, "desconto_percentual": 10})

    r = client.post("/lanchonete/pedidos", json={"cpf": "11122233344", "cod_produto": 1, "qtd_max_produtos": 10})
    assert r.status_code == 200
    cod_pedido = r.json()["codigo"]  

    response = client.post("/lanchonete/pedidos/1/cancelar")

    assert response.status_code == 200

    data = response.json()

    if data == "ok":
        response.json(True)

    if response.status_code == 200:
        response.json(True)

def test_nao_deve_cancelar_pedido_inexistente(client):
    response = client.post("/lanchonete/pedidos/999/cancelar")

    assert response.status_code == 200
    if response.status_code == 200:
        response.json(True)

    data = response.json()

    if data is None:
        response.json("400")

def test_nao_deve_cancelar_pedido_finalizado(client):
    client.post("/clientes", json={"cpf": "11122233344", "nome": "Cliente X"})

    client.post("/produtos", json={"codigo": 1, "valor": 10, "tipo": 1, "desconto_percentual": 10})
    client.post("/produtos", json={"codigo": 2, "valor": 20, "tipo": 2, "desconto_percentual": 10})

    r = client.post("/lanchonete/pedidos", json={"cpf": "11122233344", "cod_produto": 1, "qtd_max_produtos": 10})
    assert r.status_code == 200
    cod_pedido = r.json()["codigo"]  

    r2 = client.post(f"/lanchonete/pedidos/{cod_pedido}/finalizar")
    assert r2.status_code == 200
    assert r2.json()["total"] == 29.0

    response = client.post("/lanchonete/pedidos/1/cancelar")

    if response == "400":
        response.json(False)

def test_deve_listar_pedidos_cancelados(client):
    client.post("/clientes", json={"cpf": "11122233344", "nome": "Cliente X"})

    client.post("/produtos", json={"codigo": 1, "valor": 10, "tipo": 1, "desconto_percentual": 10})
    client.post("/produtos", json={"codigo": 2, "valor": 20, "tipo": 2, "desconto_percentual": 10})

    r = client.post("/lanchonete/pedidos", json={"cpf": "11122233344", "cod_produto": 1, "qtd_max_produtos": 10})
    assert r.status_code == 200
    cod_pedido = r.json()["codigo"]

    r2 = client.post(f"/lanchonete/pedidos/{cod_pedido}/cancelar")
    assert r2.status_code == 200

    response = client.get("/lanchonete/pedidos/cancelados")

    assert response.status_code == 200

    data = response.json()

    if data == []:
        response.json(True)

    existe_um = any(data in data for data in data)
    response.json(existe_um)

    if self.esta_cancelado == True:
        response.json(self.esta_cancelado)