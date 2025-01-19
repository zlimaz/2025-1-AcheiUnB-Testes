# Definir a tarefa 'run' para automatizar o comando
run:
	cd API && sudo docker compose up --build

# Adicione outras tarefas, se necessário
pull:
	git pull origin main
