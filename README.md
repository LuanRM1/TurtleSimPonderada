# TurtleSimPonderada

Este projeto é um nó ROS2 que controla uma tartaruga em uma simulação do `turtlesim`, permitindo que a tartaruga se mova em um círculo e que usuários interajam via teclado.

## Funcionalidades

- **Movimento Circular**: Comanda a tartaruga para se mover em círculos.
- **Serviços de Spawn e Kill**: Permite adicionar e remover tartarugas na simulação.
- **Configuração do Lápis**: Ajusta o traço da tartaruga.

## Pré-requisitos

- ROS 2 (testado com Humble Hawksbill)
- Python 3.8+
- turtlesim

## Instalação

1. Clone o repositório no seu workspace ROS 2:
   ```bash
   cd ~/dev_ws/src
   git clone https://github.com/AntonioArtimonte/Ponderada_ROS

2.Compile o código:

bash

cd ~/dev_ws
colcon build
source install/setup.bash

3.Execute o launch:

bash

cd launch
ros2 launch launch.py
