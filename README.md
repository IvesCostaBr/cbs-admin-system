# cbs-admin-system

-Sistema para Gerênciamento de Funcionarios em HomeOffice

-Bio:
O sistema em questão foi desenvolvido com o intuito de realizar a gestão dos funcionarios em homeoffice da empresa Grupo Banho de Cheiro AC(OBoticário Acre)
servindo como plataforma de gerenciamento de tarefas individuais(Direto para o Funcionario) ou por Setor.
O sistema encontra-se em fase de alpha, o qual quando tenho tempo estou fazendo as refatorações e corrigindo os bugs na aplicação.Em breve estarei migrando
o fron-end da aplicação para o Angular para abaixar ainda mais o acoplamento da aplicação.


Features :

-Sistema de Cadastro de funcioanrios Através de um code da empresa que é gerado qual a empresa é criado na plataforma.
-Criação, Removação, Atualização de tarefas utilizando Ajax com upload de arquivos de media.
-Gerenciamento de Horas de determiando funcionario(Em desenvolvimento).
-Monitoramento de Usuario logados da plataforma + calculo de horas logadas.
-Aplicação consumindo staticfiles per CDN Amazon s3Bucket.
-Api Rest de Leitura com authentication Token.

[Atenção]

No projeto utilizei a biblioteca python-decouple que faz a leitura de varaiveis de ambiente através de um arquivo .env na raiz projeto 
criar o arquivo .env e colocar as configurações da sua app nele, seugue as variaveis abaixo:


SECRET_KEY=''
DEBUG=0
EMAIL_HOST=''
EMAIL_PORT=''
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''
DEFAULT_FROM_EMAIL=''

AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
DISABLE_COLLECTSTATIC=1
