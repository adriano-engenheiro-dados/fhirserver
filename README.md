# fhirserver
POC para criação de Servidor baseado em FHIR

Configuração de Servidor FHIR (Arquitetura)

1 - Arquitetura construida sobre um servidor Linux em ambiente windows utilizando Oracle VirtualBox,
com 8Gb de RAM, 50Gb de armazenamento e 2 CPU's, pela praticidade de ter um servidor Linux com distribuição Ubuntu LTS on premisse. 
Fazer download do VirtualBox no link https://www.virtualbox.org/wiki/Downloads e instalar;

2 - Distribuição Linux Ubuntu 20.04.3 LTS, por ser a distribuição mais difundida e comunidade ativa. Também por se demonstrar uma 
versão estável para o projeto. Optei por versão LTS (Long Term Suport). Efetuar download do ISO e disponibilizar em diretório 
para instalação na VM (Workspace/iso);

3 - Para criação de VM no Virtual Box com a imagem Linux, seguir passo-a-passo para criação de VM no VirtualBox, configurando 
diretório para instalação do SO para o diretório Workspace/iso_linux, além de configurar a VM no diretório Workspace/vm;

4 - Instalação do Docker no Ubuntu utilizando APT do Linux Ubuntu e o PIP Install do Python, incluindo
docker-compose para salvar configurações do servidor.
Códigos utilizados:
Docker:
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
sudo systemctl enable --now docker

Docker Compose:
pip install docker-compose
docker-compose --version

5 - Gerado Docker Compose baseado em imagens disponíveis no Docker HUB, utilizando HAPI FHIR para criação de servidor FHIR baseado
Nas seguintes Tecnologias:
Java, Spring Boot (RestFull), Hibernate, PostgreSQL, Tomcat (Server), JSON / XML, Swagger (Documentação)
Podemos destacar que a HAPI FHIR implementa em 100% o padrão FHIR.
Para mais informações da implementação, acessar:
https://hub.docker.com/r/hapiproject/hapi (Link da Imagem e documentação HAPI FHIR implementado com PostgreSQL)

6 - Sobre o Docker Compose gerado: O arquivo foi criado baseado nas especificações do Docker Compose .yaml, com implementação extra de segurança para
não expor dados sensíveis de acesso ao banco de dados, adotando outra abordagem, que seria configuração dessas informações
direto no ambiente de variáveis do sistema operacional. Para isso, foi criado o arquivo enviroments.env que armazena essas informações.
É necessário executar primeiro este arquivo, para depois executar o Docker Compose.

