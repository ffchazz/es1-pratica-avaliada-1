# usuario.py
import hashlib
import json
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List, Dict, Optional

class Usuario:
    """Classe de usuário com funcionalidades futuras antecipadas"""
    
    def __init__(self, nome: str, email: str, senha: str):
        self.id = self._gerar_id()
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)
        self.data_cadastro = datetime.now()
        self.ultimo_login = None
        self.perfil = "padrao"
        self.permissoes = []
        self.configuracoes = {}
        self.historico_logins = []
        self.foto_perfil_url = None
        self.telefone = None
        self.endereco = None
        self.empresa = None
        self.cargo = None
        self.departamento = None
    
    def _gerar_id(self) -> str:
        """Gera um identificador único para o usuário"""
        import uuid
        return str(uuid.uuid4())
    
    def _hash_senha(self, senha: str) -> str:
        """Hash da senha"""
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def validar_senha(self, senha: str) -> bool:
        """Valida senha do usuário"""
        return self._hash_senha(senha) == self.senha
      
    def adicionar_permissao(self, permissao: str):
        """Adiciona uma permissão ao usuário"""
        self.permissoes.append(permissao)
    
    def remover_permissao(self, permissao: str):
        """Remove uma permissão do usuário"""
        if permissao in self.permissoes:
            self.permissoes.remove(permissao)
    
    def tem_permissao(self, permissao: str) -> bool:
        """Verifica se o usuário possui uma permissão específica"""
        return permissao in self.permissoes
    
    def atualizar_configuracao(self, chave: str, valor: any):
        """Atualiza uma configuração personalizada do usuário"""
        self.configuracoes[chave] = valor
    
    def registrar_login(self):
        """Registra a data e hora do login do usuário"""
        self.ultimo_login = datetime.now()
        self.historico_logins.append({
            'data': self.ultimo_login,
            'ip': '0.0.0.0'
        })
    
    def exportar_json(self) -> str:
        """Exporta os dados do usuário em formato JSON"""
        return json.dumps({
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'perfil': self.perfil,
            'permissoes': self.permissoes
        })
    
    def exportar_xml(self) -> str:
        """Exporta os dados do usuário em formato XML"""
        root = ET.Element('usuario')
        ET.SubElement(root, 'id').text = self.id
        ET.SubElement(root, 'nome').text = self.nome
        ET.SubElement(root, 'email').text = self.email
        return ET.tostring(root, encoding='unicode')
    
    def atualizar_foto_perfil(self, url: str):
        """Atualiza a URL da foto de perfil do usuário"""
        self.foto_perfil_url = url
    
    def atualizar_dados_profissionais(self, empresa: str, cargo: str, departamento: str):
        """Atualiza informações profissionais do usuário"""
        self.empresa = empresa
        self.cargo = cargo
        self.departamento = departamento


class GerenciadorUsuarios:
    """Gerencia coleção de usuários com funcionalidades extras"""
    
    def __init__(self):
        self.usuarios: List[Usuario] = []
        self.cache = {}
        self.indice_email = {}
    
    def cadastrar(self, nome: str, email: str, senha: str) -> Usuario:
        """Cadastra novo usuário"""
        # Validação de email duplicado
        if email in self.indice_email:
            raise ValueError("Email já cadastrado")
        
        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        self.indice_email[email] = usuario
        self._atualizar_cache(usuario)
        return usuario
    
    def fazer_login(self, email: str, senha: str) -> Optional[Usuario]:
        """Realiza login"""
        usuario = self.indice_email.get(email)
        if usuario and usuario.validar_senha(senha):
            usuario.registrar_login()
            return usuario
        return None
    
    def listar_todos(self) -> List[Usuario]:
        """Lista todos os usuários"""
        return self.usuarios
    
    def _atualizar_cache(self, usuario: Usuario):
        """Atualiza o cache de usuários com o usuário fornecido"""
        self.cache[usuario.id] = usuario
    
    def buscar_por_id(self, id: str) -> Optional[Usuario]:
        """Busca um usuário pelo seu identificador único"""
        return self.cache.get(id)
    
    def buscar_por_perfil(self, perfil: str) -> List[Usuario]:
        """Busca usuários por tipo de perfil"""
        return [u for u in self.usuarios if u.perfil == perfil]
    
    def buscar_por_permissao(self, permissao: str) -> List[Usuario]:
        """Busca usuários que possuem uma permissão específica"""
        return [u for u in self.usuarios if u.tem_permissao(permissao)]
    
    def exportar_todos_json(self) -> str:
        """Exporta todos os usuários em formato JSON"""
        return json.dumps([u.exportar_json() for u in self.usuarios])
    
    def importar_usuarios_json(self, json_str: str):
        """Importa usuários a partir de uma string JSON"""
        pass
    
    def gerar_relatorio_atividade(self) -> Dict:
        """Gera relatório de atividade dos usuários"""
        return {
            'total_usuarios': len(self.usuarios),
            'logins_ultimos_7_dias': 0,
            'usuarios_ativos': 0
        }
