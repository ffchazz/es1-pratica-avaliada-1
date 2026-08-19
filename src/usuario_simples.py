"""
Módulo de gerenciamento simples de usuários aplicando o princípio YAGNI (XP).
Requisitos: Cadastrar, Fazer Login (com hash e validação de e-mail) e Listar.
"""

import hashlib
from typing import List, Optional


class Usuario:
    """Representa um usuário básico do sistema."""

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)

    def _hash_senha(self, senha: str) -> str:
        """Gera o hash SHA-256 da senha para armazenamento seguro."""
        return hashlib.sha256(senha.encode()).hexdigest()

    def validar_senha(self, senha: str) -> bool:
        """Valida se a senha informada corresponde ao hash armazenado."""
        return self._hash_senha(senha) == self.senha


class GerenciadorUsuarios:
    """Gerencia a coleção de usuários, autenticação e listagem."""

    def __init__(self):
        self.usuarios: List[Usuario] = []

    def cadastrar(self, nome: str, email: str, senha: str) -> Usuario:
        """
        Cadastra um novo usuário no sistema.
        Lança ValueError caso o e-mail já esteja cadastrado.
        """
        if any(u.email == email for u in self.usuarios):
            raise ValueError("Email já cadastrado")

        novo_usuario = Usuario(nome, email, senha)
        self.usuarios.append(novo_usuario)
        return novo_usuario

    def fazer_login(self, email: str, senha: str) -> Optional[Usuario]:
        """
        Realiza a autenticação de login por e-mail e senha.
        Retorna o objeto do usuário se autenticado com sucesso, ou None caso contrário.
        """
        for usuario in self.usuarios:
            if usuario.email == email and usuario.validar_senha(senha):
                return usuario
        return None

    def listar_todos(self) -> List[Usuario]:
        """Retorna a lista com todos os usuários cadastrados."""
        return self.usuarios
