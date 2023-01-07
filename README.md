# Mr.BigHand

## Os Problemas	
	- Códigos repetitivos
	- Ctrl+C Ctrl+V que podem dar errado
	- Padronização de código
		- Não saber qual é a API correta para se basear (pois algumas estão mais atualizadas que outras)
		- Somente o code review e o confluence garantem que estamos usando os padrões corretos

## Benefícios
	
	* OBS: Estou considerando que iremos construir 700 API's, pois isso foi falado em alguma reunião.
	
	- *json_funcs.i:
		- Se em média um arquivo *json_funcs.i demora 6 horas / 1 dia para ser finalizado
			- e.g: 6h x 700API's: 4200 horas, ou 700 dias.
		- Se em média esse mesmo arquivo possui 350 linhas, serão 350 linhas a menos para todos (DEV, CODE REVIEW e MANUTENÇÃO)
			pois podemos separar a camada de regra de negócio da camada que escreve o JSON.
				
	- Temos diversos arquivos que podem ser automatizados que nem o citado acima, gerando mais benefícios que estão em:
			
			- PROGRESS
				- api.p
				- funcs.i
				- json_funcs.i
				
			- TESTES AUTOMATIZADOS BEHAVE (PYTHON)
				- api.feature
				- api.step
				- api.service
				
			- EQUELETO DA DOCUMENTAÇÃO QUE VAI PARA O CONFLUENCE
				- .txt
			
			- POSTMAN
				- collection
	
	- Onboarding
		- Esse ponto foi levantado pelo Clei e também concordei com ele, pois tendo artefatos gerados por uma ferramenta (atualizada)
			a pessoa nova vai se sentir mais segura em qual padrão seguir.
	

## Functionalities


### Progress4GL code generation

- Type: [GET]
  - Manual JSON Builder (Json.ObjectModel)
    - mkp_[group]_[subgroup].p
    - mkp_[group]_[version]_[api_name].p
    - mkp_[api_name]_funcs.i
    - mkp_[api_name]_reading.i
    - mkp_[api_name]_json_funcs.i

- Type: [POST]
  - Manual JSON Builder (Json.ObjectModel)
    - TODO

### Postman collection code generation
- TODO

### Automation Tests (Python Behave) code generation
- TODO

### Documentation generation
- TODO


## How to use
- Create your import files inside "files/import/$your_process_folder" 
- Create a json file called "api_schema.json"" inside $your_process_folder
- Execute the main program with --process=$your_process_folder.

eg: $your_process_folder = organizations_v2
```commandline
python main.py --import=organizations_v2
```