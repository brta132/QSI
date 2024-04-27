# Ferramenta QSI TP3

## Índice

- [Introdução](#item-introdução)

- [Manual de Utilização](#item-manual)

- [Cuidados Extra](#item-cuidados)

- [Dependências](#item-dependencias)

- [Erros e debugging](#item-debug)

## Introdução <a id="item-introdução"></a>

Este programa foi criado com o objetivo de facilitar a testagem da qualidade da rede internet em diferentes localizações e como estas afetam a qualidade da experiência da utilização de plataformas de distribuição de vídeos como o Youtube, utilizando ferramentas como o speedtest-CLI (speedtest.exe) para efetuar as medições.

De maneira a controlar a maioria possível das variáveis decidímos que apenas seria testado um [vídeo do Youtube em específico](https://www.youtube.com/watch?v=gYFQcOFUnqU) a uma certa hora, de modo a tentar sincronizar as medições.

Uma vez que queríamos tirar o número razoável de medições enquanto o vídeo era transmitido, escolhemos um com uma duração de aproximadamente 3:25h. Uma vez que para as medições não sofrerem devido a programas que estejam a decorrer em paralelo, foi decidido que aquando da inicialização deste programa, apenas os processos por ele chamados devem estar ativos. Isto, obviamente, iria prejudicar os elementos do grupo, que precisam do computador para as suas atividades diárias, pelo que foi acordada uma hora em que ninguém estaria a utilizar o computador (1 da manhã) para o programa se iniciar automaticamente.

## Manual de Utilização <a id="item-manual"></a>

O programa pode ser corrido iniciando o *script* quick_speedtest.py, utilizando o seguinte comando:

    python3 quick_speedtest.py

Para evitar erros, recomenda-se que primeiro verifique se a pasta que contém o *script* também inclui um ficheiro **speedtest.exe** e uma pasta **speedtest-data**, sendo que esta, por sua vez, deve conter 2 ficheiros: **error.txt** e **speedtest_data.csv**.

Todas estes ficheiros, assim como a estrutura descrita são vitais para o normal funcionamento do programa.

## Cuidados Extra <a id="item-cuidados"></a>

- **Manter o Computador Ligado à corrente**: antes de iniciar o programa recomenda-se que se ligue o computador à corrente, de modo a evitar que o programa seja interrompido por falta de bateria;

- **Suspensão do Ecrã**: Alterar as definições do computador de modo a que este não entre em modo de suspensão pelo período de 4 horas desde o ínicio do programa, uma vez que isto levaria a que o vídeo fosse automaticamente pausado;

- **Desligar todos os outros processos**: para que estes processos não afetem as medições, todos os processos (com exceção dos iniciados pelo *script*) devem ser desligados antes de se iniciar o programa.

**NOTA**: Atualmente o programa está a utilizar muitos recursos, em específico a RAM e o CPU, o que está a levar a que estes componentes atinjam temperaturas estupidamente altas (entre os 92ºC e os 99ºC), pelo que não podemos recomendar que o programa seja corrido sem supervisão.

## Dependências<a id="item-dependencias"></a>

Este *script* foi desenvolvido para correr um ficheiro .exe em ambiente Linux, pelo que tem algumas dependências obrigatórias para o seu funcionamento. Sendo estas:

- **wine**: para correr o ficheiro .exe;

- **python3**: para correr o *script*;

- **pip**: para instalar o módulo *schedule*, usado para o programa correr tarefas segundo determinados intervalos de tempo (pode ou não já vir instalado dependendo da versão do *python*);

- **schedule**: se não estiver incluído tem de ser instalado utilizando o comando **pip install schedule**;

- **firefox**: de modo a evitar que houvessem diferenças entre as medições causadas pelo tipo de *browser* utilizado, ficou decidido utilizar o *firefox* por já vir pré-instalado com várias distribuições Linux (como o Ubuntu, por exemplo).

Foi disponibilizado um ficheiro *bash* para instalar as dependências referidas, mas como este ainda não foi testado recomenda-se que este seja utilizado com cautela, já que não podemos garantir que este seja seguro e que esteja a funcionar devidamente.

## Erros e debugging <a id="item-debug"></a>

Caso esteja a haver problemas não relacionados com as dependências ou com a estrutura dos ficheiros, recomenda-se que se edite o código do *script* de modo a "descomentar" as linhas comentadas marcadas com [FOR TESTING]. Não esquecer de comentar a linha imediatamente acima desta marca.

Isto permite que o programa corra todas as tarefas pendentes mais rapidamente (demorando 3 minutos em vez de 30 para efetuar 3 medições). Isto também permite a testagem imediata a partir do momento em que o programa é iniciado (a primeira medição demora 1 minuto após a inicialização do *browser* para ser feita), retirando o requesito de ter de esperar pela 1 da manhã para iniciar as medições.

Exemplo:

    #schedule speedtest to run every 10 minutes
    schedule.every(10).minutes.do(speed_test_loop)
    #schedule.every(1).minutes.do(speed_test_loop) [FOR TESTING]

Passaria a ficar:

    #schedule speedtest to run every 10 minutes
    #schedule.every(10).minutes.do(speed_test_loop)
    schedule.every(1).minutes.do(speed_test_loop) #[FOR TESTING]

**Nota:** não é recomendável retirar o marcador **[FOR TESTING]** para ser facilmente identificável que linha é que é utilizada exclusivamente para propósitos de testagem. Para este caso, comentá-lo é a melhor solução.


