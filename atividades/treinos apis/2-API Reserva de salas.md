# API de Reserva de Salas de Estudo

Este projeto tem como objetivo o desenvolvimento de uma API REST para gerenciamento de reservas de salas de estudo.

O sistema deve seguir arquitetura em camadas e respeitar regras de negócio relacionadas a cadastro, reservas, conflitos de horário e cancelamento.

A atividade foi planejada para você desenvolver aproximadamente 50% do código.

---

## Objetivo

Construir uma API capaz de:

- cadastrar usuários
- cadastrar salas
- realizar reservas
- listar reservas
- cancelar reservas
- validar conflitos de horário
- aplicar regras de limite por usuário

---

## Contexto

Uma instituição precisa organizar o uso de salas de estudo em grupo.

Cada usuário pode reservar salas por faixa de horário, mas o sistema deve impedir conflitos e controlar limites de uso.

---

## Estrutura do Projeto

A aplicação deve seguir a seguinte organização:

```text
salas_api/
├── domain/
├── schemas/
├── repositories/
├── services/
├── api/routes/
└── main.py