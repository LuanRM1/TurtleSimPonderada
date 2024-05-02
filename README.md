# TurtleSimPonderada

Video de demonstração: [Link do video](https://drive.google.com/file/d/15ieUrrYV3qjIRRR0IJHgpkzn6E0YIZf8/view?usp=drivesdk) 

Este projeto implementa um nó ROS2 para fazer um desenho com o `turtlesim`.

## Funcionalidades

- **Movimento Circular**: Comanda a tartaruga para se mover em círculos continuamente.
- **Serviços de Spawn e Kill**: Adiciona ou remove tartarugas na simulação. A interação para parar a tartaruga é feita através da tecla "q" no terminal.
- **Configuração do Lápis**: Permite ajustar o traço deixado pela tartaruga no ambiente de simulação.

## Pré-requisitos

Antes de instalar e executar o projeto, certifique-se de que os seguintes pré-requisitos estão atendidos:

- ROS 2, versão Humble
- Python 3.8 ou superior
- Pacote turtlesim

Caso nao tenha essas pré-requisitos recomendo seguir esse tutorial

[Tutorial](https://rmnicola.github.io/m6-ec-encontros/E01/ros)

## Instalação

Siga estas etapas para instalar o TurtleSimPonderada no seu ambiente ROS 2:

1. Clone o repositório para o seu workspace ROS 2:
   ```bash
   git clone https://github.com/LuanRM1/TurtleSimPonderada.git
   cd TurtleSimPonderada
   ```

2. Compile o projeto usando `colcon`:
   ```bash
   colcon build
   source install/setup.bash
   ```

## Execução

Para executar o projeto, siga estes passos:

1. Navegue até o diretório de lançamento:
   ```bash
   cd launch
   ```

2. Execute o arquivo de launch para iniciar a simulação:
   ```bash
   ros2 launch teste_launch.py
   ```

Agora a tartaruga deve estar ativa e você pode interagir com ela conforme descrito nas funcionalidades.
