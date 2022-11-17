# Mr. Big Hand
****

## Functionalities


### Progress4GL code generation

- mkp_[group]_[subgroup].p
- mkp_[group]_[version]_[api_name].p
- mkp_[api_name]_funcs.i
- mkp_[api_name]_reading.i
- mkp_[api_name]_json_funcs.i

### Postman collection code generation
- TODO

### Automation Tests (Behave) code generation
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