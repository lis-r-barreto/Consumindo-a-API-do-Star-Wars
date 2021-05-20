Consumindo a API do Star Wars - SWAPI
=====================================

Instalando e Rodando
--------------------
* [Requisitos Mínimos](#requisitos-minimos)
* [Instalação no Linux](#instalação-no-linux)
 
Requisitos Mínimos
------------------
* Python 3.6
* [pip](https://pip.pypa.io/en/stable/)

Instalação no Linux
===================

- Verifique se o git já está instalado, com o comando:
```console
git --version
```

- Se a saída for algo como `git version 2.25.1`, significa que o git já está
instalado. Caso contrário, para instalar o git basta fazer:
``` console
sudo apt install git  # para ubuntu
```

> **Observação**: Esse comando funciona apenas em sistemas operacionais que utilizam o
`apt` gerenciador de pacotes. Caso não seja o seu caso, [verifique como instalar](https://git-scm.com/download/linux) o git no seu sistema.

- Assumindo que seu git já está configurado, faça o clone do repositório

```console
git clone https://github.com/lis-r-barreto/Consumindo-a-API-do-Star-Wars.git
```
- Após conclusão do clone, acesse o diretório recém-criado

```console
cd Consumindo-a-API-do-Star-Wars
```
- Rode o comando para instalação das dependências

```console
pip install -r requirements.txx
```

- Rode o projeto

```console
python main.py
```
