Consumindo a API do Star Wars - SWAPI
=====================================

Instalando e Rodando
--------------------
* [Requisitos Mínimos](#requisitos-minimos)
* [Instalação no Linux](#instalação-no-linux)
  - [Usando ambiente virtual](#usando-ambiente-virtual)
 
Requisitos Mínimos
-----
* Python 3.6
* [pip](https://pip.pypa.io/en/stable/)

Instalação no Linux
===================

Usando ambiente virtual
----
- Para apenas rodar localmente o projeto, você precisa do [virtualenv](https://virtualenv.pypa.io/en/stable/)
instalado na sua máquina. Para verificar se ele está instalado, execute o
seguinte comando e observe a saída:

```console
$ virtualenv --version
```
- Se a saída for uma numeração, como `16.1.0`, isso significa que o virtualenv já
está instalado. Caso contrario, para instalar o virtualenv basta fazer:

```console
$ pip install virtualenv
```
- O mesmo procedimento pode ser feito para o git. Verifique se já está instalado,
com o comando:
```console
$ git --version
```

- Se a saída for algo como `git version 2.17.1`, significa que o git já está
instalado. Caso contrário, para instalar o git basta fazer:
``` console
$ sudo apt install git  # para ubuntu
```

> **Observação**: Esse comando funciona apenas em sistemas operacionais que utilizam o
`apt` gerenciador de pacotes. Caso não seja o seu caso, [verifique como instalar](https://git-scm.com/download/linux) o git no seu sistema.

- Assumindo que seu git e virtualenv já estão configurados, faça o clone do repositório

```console
$ git clone https://github.com/lis-r-barreto/Consumindo-a-API-do-Star-Wars.git
```
- Após conclusão do clone, acesse o diretório recém-criado

```console
$ cd Consumindo-a-API-do-Star-Wars
```
- Rode o comando para criação de ambiente virtual e instalação das dependências

```console
$ virtualenv .venv 	# cria ambiente virtual
$ source .venv/bin/activate	# ativa o ambiente
$ pip install -r requirements.txt	# instala as dependências

```

- Rode o projeto

```console
$ python main.py
```

- Para desativar o ambiente virtual

```console
$ deactivate
```
