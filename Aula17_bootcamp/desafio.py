from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    # Criando colunas
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))


class Produto(Base):
    __tablename__ = 'produtos'

    # Criando colunas
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    # Estabelece a relação entre Produto e Fornecedor
    fornecedor = relationship('Fornecedor')

    
engine = create_engine('sqlite:///desafio.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Inserindo fornecedores 
try:
    with Session as session: # Usando a sessão corretamente com o gerenciador de contexto
        fornecedores = [
            Fornecedor(nome='Fornecedor A', telefone='12345678', email='contato1@a.com', endereco='Rua 38 qd 55'),
            Fornecedor(nome='Fornecedor B', telefone='87654321', email='contato2@b.com', endereco='Av. Central, nº 100'),
            Fornecedor(nome='Fornecedor C', telefone='99887766', email='suporte@c.com', endereco='Rua das Flores, 45'),
            Fornecedor(nome='Fornecedor D', telefone='11223344', email='vendas@d.com', endereco='Av. Brasil, 200'),
            Fornecedor(nome='Fornecedor E', telefone='33445566', email='comercial@e.com', endereco='Rua São João, 89'),
            Fornecedor(nome='Fornecedor F', telefone='44556677', email='info@f.com', endereco='Travessa dos Jacarandás, 12'),
            Fornecedor(nome='Fornecedor G', telefone='55667788', email='atendimento@g.com', endereco='Rua Aurora, 123'),
            Fornecedor(nome='Fornecedor H', telefone='66778899', email='contato@h.com', endereco='Alameda Santos, 432'),
            Fornecedor(nome='Fornecedor I', telefone='77889900', email='financeiro@i.com', endereco='Rua do Comércio, 91'),
            Fornecedor(nome='Fornecedor J', telefone='88990011', email='relacionamento@j.com', endereco='Rua das Palmeiras, 77'),
            Fornecedor(nome='Fornecedor K', telefone='99001122', email='sac@k.com', endereco='Rua Atlântica, 202'),
            Fornecedor(nome='Fornecedor L', telefone='10101010', email='pedido@l.com', endereco='Av. Paulista, 1010'),
            Fornecedor(nome='Fornecedor M', telefone='12121212', email='logistica@m.com', endereco='Rua Verde, 303'),
            Fornecedor(nome='Fornecedor N', telefone='13131313', email='compras@n.com', endereco='Rua da Paz, 44'),
            Fornecedor(nome='Fornecedor O', telefone='14141414', email='marketing@o.com', endereco='Av. Independência, 55'),
            Fornecedor(nome='Fornecedor P', telefone='15151515', email='suporte@p.com', endereco='Rua Azul, 88')
        ]
        session.add_all(fornecedores)
        session.commit()
except SQLAlchemyError as e: # Capturando exceções do SQLAlchemy
    print(f'Erro ao inserir fornecedores: {e}')


# Incluindo produtos
try:
    with Session as session:
        produtos = [
            Produto(nome='Produto1', descricao='Descrição do produto 1', preco=150, fornecedor_id=3),
            Produto(nome='Produto2', descricao='Descrição do produto 2', preco=200, fornecedor_id=7),
            Produto(nome='Produto3', descricao='Descrição do produto 3', preco=75, fornecedor_id=1),
            Produto(nome='Produto4', descricao='Descrição do produto 4', preco=180, fornecedor_id=12),
            Produto(nome='Produto5', descricao='Descrição do produto 5', preco=95, fornecedor_id=3),
            Produto(nome='Produto6', descricao='Descrição do produto 6', preco=300, fornecedor_id=9),
            Produto(nome='Produto7', descricao='Descrição do produto 7', preco=250, fornecedor_id=7),
            Produto(nome='Produto8', descricao='Descrição do produto 8', preco=120, fornecedor_id=4),
            Produto(nome='Produto9', descricao='Descrição do produto 9', preco=90, fornecedor_id=15),
            Produto(nome='Produto10', descricao='Descrição do produto 10', preco=170, fornecedor_id=6),
            Produto(nome='Produto11', descricao='Descrição do produto 11', preco=60, fornecedor_id=2),
            Produto(nome='Produto12', descricao='Descrição do produto 12', preco=220, fornecedor_id=18),
            Produto(nome='Produto13', descricao='Descrição do produto 13', preco=85, fornecedor_id=12),
            Produto(nome='Produto14', descricao='Descrição do produto 14', preco=140, fornecedor_id=23),
            Produto(nome='Produto15', descricao='Descrição do produto 15', preco=310, fornecedor_id=4),
            Produto(nome='Produto16', descricao='Descrição do produto 16', preco=45, fornecedor_id=3),
            Produto(nome='Produto17', descricao='Descrição do produto 17', preco=270, fornecedor_id=9),
            Produto(nome='Produto18', descricao='Descrição do produto 18', preco=100, fornecedor_id=21),
            Produto(nome='Produto19', descricao='Descrição do produto 19', preco=55, fornecedor_id=6),
            Produto(nome='Produto20', descricao='Descrição do produto 20', preco=190, fornecedor_id=7),
            Produto(nome='Produto21', descricao='Descrição do produto 21', preco=130, fornecedor_id=1),
            Produto(nome='Produto22', descricao='Descrição do produto 22', preco=160, fornecedor_id=19),
            Produto(nome='Produto23', descricao='Descrição do produto 23', preco=230, fornecedor_id=15)
        ]
        session.add_all(produtos)
        session.commit()
except SQLAlchemyError as e:
    print(F'Erro ao inserir produtos: {e}')

