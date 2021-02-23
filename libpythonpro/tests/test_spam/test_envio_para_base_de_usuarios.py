from unittest.mock import Mock
import pytest
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


# class EnviadorMock(Enviador):
#     def __init__(self):
#         super().__init__()
#         self.qtd_email_enviados = 0
#         self.parametros_de_envio = None
#
#     def enviar(self, remetente, destinatario, assunto, corpo):
#         self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
#         self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Geison', email='buddygn@gmail.com'),
            Usuario(nome='teste', email='teste@gmail.com')
        ],
        [
            Usuario(nome='Geison', email='buddygn@gmail.com'),
            Usuario(nome='teste', email='teste@gmail.com')
        ]

    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'buddygn@gmail.com',
        'Teste envio de email',
        'Corpo do email'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Amauri', email='amauri@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'teste@gmail.com',
        'Teste envio de email',
        'Corpo do email'
    )
    enviador.enviar.assert_called_once_with(
        'teste@gmail.com',
        'amauri@gmail.com',
        'Teste envio de email',
        'Corpo do email'
    )
