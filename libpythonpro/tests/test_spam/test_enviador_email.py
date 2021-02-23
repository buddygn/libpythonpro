import pytest

from libpythonpro.spam.enviador_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['buddygn@gmail.com', 'aaaaa@aaa.com', 'bbbb@bb.com'])
def test_remetente(destinatario):
    enviador = Enviador()
    # destinatatios = ['buddygn@gmail.com', 'aaaaa@aaa.com', 'bbbb@bb.com']
    resultado = enviador.enviar(
        destinatario,
        'roger@naspsistemas.com.br',
        'Curso',
        'jacare'
    )

    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'renzo'])
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'roger@naspsistemas.com.br',
            'Curso',
            'jacare'
        )
