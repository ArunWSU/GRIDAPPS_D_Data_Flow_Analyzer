# GridAPPS-D Initial WSU ADMS Application: Data Flow Analyzer

After Installation of GRIDAPPS-D, this application can be built using the following command as depicted in GRIDAPPS- D sample app repository.

## Creating the application container

1.  From the command line execute the following commands to build the sample-app container

    ```console
    osboxes@osboxes> cd repository
    osboxes@osboxes> docker build --network=host -t app3 .
    ```

1.  Add the following to the gridappsd-docker/docker-compose.yml file

    ```` yaml
    app3:
      image: app3
      depends_on: 
        gridappsd    
    ````
## Program Execution

1. GRIDAPPS-D message output is available every 3 seconds. Accordingly, modify variable `constant` (Program sampling time) in runsample.py using any IDE

The following are to be executed from the Linux terminal.

2. After making changes execute to copy changed file into container 
	```
	docker cp runsample.py gridappsddocker_adms_app3_1:/usr/src/adms_app3/app3
	```
3. To check whether the file has changed in the container
	```
	docker exec -it gridappsddocker_adms_app3_1 bash
	cat runsample.py
	```
4. Next, Determine the application container name
	```
	docker ps -a
	```
5.  After starting the simulation, enter the docker container 
	```
	docker exec -it gridappsddocker_adms_app3_1(application container name) bash
	```
	
6. Extract the measurements after modifying the Line name to denote particular test system for simulation
	```
	python runsample.py 75076236 '{"power_system_config":  {"Line_name":"_E407CBB6-8C8D-9BC9-589C-AB83FBF0826D"}}'
	```

7. Copy the output json file from the container
	```
	docker cp gridappsddocker_adms_app3_1:/usr/src/adms_app3/voltage_123pv_use_loads.json /home/(output path)
	```
