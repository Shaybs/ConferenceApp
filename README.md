# Book Review Web Application

### Application Setup

To set up this application two virtual machines should be instantiated. After which the ansible playbook, 'playbook-inistialisation.yaml' should be run, ensure that the relevant IP addresses have been amended in the inventory file. Another playbook is utilised to add environment variables which has not been uploaded to GitHub, this is used to set up the environment variables in the VMs. The '.bashrc' file has to be manually sourced in both VMs. The ssh keys need to be generated manually on the VM/instance used to run ansible. The permissions need to be manually added for jenkins by utilising the 'sudo visudo' command as well. The initial password for Jenkins needs to be retrieved as well. After that the relevant global security settings in Jenkins need to made to allow for traffic. A webhook from the GitHub repository needs to set for effective integration as well. After these steps have been taken. The application can be run.

### Agile Methodology

Elements of Agile and Scrum will be utilised in this project. Since this is an individual project, the Agile role, events and artefacts will be defined as follows:
There will be a Project Owner who will be responsible for planning, creating, managing and deploying the entire software project. The duties of the Scrum Master will not be conducted. The Product Owner’s responsibility of creating and defining the Product Backlog will be conducted by the Project Owner. The Development of the software and the Sprint Backlog will be undertaken by the Product Owner. The Product Owner is also responsible for changing the Sprint Backlog as the Sprint progresses.
The Agile Events will consist of a single Sprint, in which the entire project will be completed. This project will have a Sprint Planning phase, which may involve a simulation with QA as the client. In this meeting the client requirements will be gathered and the user stories will be mutually reviewed and assessed. Artefacts such as the Product Backlog and Sprint Backlog will be created from the client requirements and user stories based on MoSCoW principles. After which the Sprint will be conducted. After the completion and demonstration of the project, a Project Retrospective will be conducted with or without client interaction. This Project Retrospective will detail what could have done better, room for improvements in the software and how the process could be improved. Daily Scrums will not be conducted and there will be no team meetings.

### Program Overview

In the sixth week new languages such as Powershell and Linux Bash were introduced. Different programming techniques such as if statements and for loops were shown. The techniques used to connect, create and delete instances were demonstrated. Further, the the requests and request libraries and how these libraries are used to send and receive json objects was shown.
In the seventh week docker and the concept of containers, how docker identifies containers and the purpose and benefits of containerisation was presented. The notions of dockerfiles, registries, volumes, nginx and docker compose were exhibited.
In the eighth week, docker swarm and how it can be used to have multiple containers across multiple nodes and the master node was showcased. Later Ansible was taught to enable quick set up of environments for testing and deployment.

### Project Overview

The requirements have been listed below:

| Project requirements |
|  ------ |
| Program Overview |
| Agile Methodology |
| Risk Assessment | 
| Test Driven Development |
| Asana Board |
| ERD |
| User Stories | 
| Product Backlog |
| Sprint Backlog  |
| Processes |
| Use Case Scenarios |
| CI Pipeline |
| Tests Log |
| Ansible |
| Demonstration |
| Further Improvements |


The MoSCoW has been listed below:

|  | MoSCoW |
| ------ | ------ |
| MUST | Have Unit tests for all web pages |
| MUST | Use Test Driven Development methodology |
| MUST | Have automated deployment with a Jenkins CI Server |
| MUST | Have Version Control System (VCS) and a GitHub repository |
| MUST | Be developed on a feature/development branch |
| MUST | Use python |
| MUST | Use Flask |
| MUST | Use a could hosted database and GCP Compute Engine |
| MUST | Have a Trello board(s) with User Stories, User Requirements, Sprint Backlog |
| SHOULD | CSS template |
| SHOULD | Have unique book identifies like ISBN |	
| SHOULD | Basic instance protections |
| SHOULD | Have Login features with hashed/encrypted passwords |
| COULD | Search |
| COULD | Have images |
| WOULD | Defend against security attacks |

### Introduction

The project aims to create a banking application that allows users to generate an account number, cvc, card number and IBAN. The project aims to utilise a microservices architecture, containers and replicas for rolling updates.

### Personal Project Goals

The Keep it Simple Stupid (KISS) method was adhered to. Hence, the entire project was designed to keep the GUI and user experience as simple as possible. It primarily aims to demonstrate that an account can be generated using a service architecture; and the application can be updated utilising the required DevOps tools.

### Project

First a risk assessment was conducted. After which potential tests were assessed. Tests were then written. After which the initiative, theme and epics were developed. Based on the epics, user stories were developed. The user stories were used to create the Product Backlog. Asana was used then used to list the User Stories, Sprint Backlog Items and the Backlog items were moved from To Do, Doing to Done as the project progressed. Later, the Account Epic was combined into a single user story.

![Risk Assessment](/Documents/RiskAssessment.png)

After completing this Initiatives, Themes Epics were researched which resulted in the following epics and user stories:
![First Epic](/Documents/EPICI.jpg)
![Second Epic](/Documents/EPICII.jpg)

A user story, its process and use case from the Login Epic has been shown below:
![A User Story and Use Case from the Login Epic](/Documents/USI.jpg)

A user story, its process and use case from the Account Epic has been shown below:
![A User Story and Use Case from the second Epic](/Documents/EPIUSI.jpg)

The product backlog was created and is shown below:

![Product Backlog](/Documents/ProductBacklog.png)

An  Entity Relationship Diagram was created as demonstrated below:

![ERD](/Documents/ERD.jpg)

The Asana Board is shown during development below:

![Asana Board In-progress](/Documents/AsanaInProgress.png)

The image below shows the board after completing all software tasks:

![Asana Board In-progress](/Documents/Asana.png)

### Development process

The source code was uploaded to GitHub, which allowed version control and the ability to switch between different versions. It also allowed the project to be pulled to different machines; and the addition and testing of new features from different machines. The program was coded in modular form with a microservices architecture and uploaded to a development branch. This modular form enabled quick troubleshooting throughout the processes. The Keep it Simple Stupid (KISS) methodology was followed. Hence, an incredibly simple application was ideated. Over 15 tests were written prior to the initiation of software development.

First the connectivity between different applications using the requests and request libraries was understood. After that the front end development was initiated to create a simple and easy to use GUI. A SQL database in GCP was spun up and the ERD model for the banking application was created. The last solution involved spinning up two instances and configuring the instances with ansible. There was a VM used to run Jenkins (Jenkins VM) and build images and another VM to deploy the application (App VM). The permissions for jenkins on the Jenkins VM and the environment variables on both VMs had to be manually set and sourced, respectively.

Docker allowed the disuse of virtual environments, it also allowed very quick deployment of containers. After utilising docker, docker-compose was utilised to build images and push them to a registry on the Jenkins VM. The images were numbered using the built in environment variable of jenkins, called ‘BUILD_NUMBER’. This was followed by the use of docker stacks and docker stack deploy on the App VM, referencing the registry’s address for quick deployment of the images. Multiple replicas of each container are created and the service maintained allowing for rolling updates.

During the Sprint phase more more test considerations were taken into account. In total over 30 tests were written and tested for all the services. The coverage reports are available in the appendix. The Front End test is shown:

![Test Log](/Documents/FrontEndTest.png)

This resulted in the following pipeline:

![CI Pipeline](/Documents/CIPipeline.jpg)

### Services Architecture

The user connects to the website, which is run by Nginx. Nginx connects to the front end service. This service renders the website and connects to the SQL database. When an account is generated, the front end service connects to the central service. This service seeks the cvc, sort code, account, card number and iban preamble from the cvc service, sort service, account service, card service and country services, respectively. This results in the following services architecture:

![Services Architecture](/Documents/ServicesArchitecture.jpg)

The account and country services have two implementations. The central service produces the iban by combining the iban preamble and the account string. The account string is generated based on the country the user has selected. If it is Pakistan, Belarus, United Kingdom, United Arab Emirates or South Korea, a 12 character string will be added. If the user selects Italy, a 13 character string will be added. If the user selects China, India, Singapore, Denmark or Singapore, a 14 character string will be added.

### Further Improvements and Future

There are many improvements that can be made to this application. For example, there could be more stringent policies for who can open or generate an account. Other features such as the ability to make transactions can be added. More tests including tests of how the application behaves after a user has logged in could be added. Security could also be enhanced through the addition of dummy data to passwords before hashing and through the randomisation of the dummy data to ensure there are no patterns for the dummy data.


### APPENDIX I

LOGIN EPIC: USER STORY I:

![Login Epic: User Story I](/Documents/LoginEpicUSI.jpg)

LOGIN EPIC: USER STORY II:

![Login Epic: User Story II](/Documents/LoginEpicUSII.jpg)

LOGIN EPIC: USER STORY III:

![Login Epic: User Story III](/Documents/LoginEpicUSIII.jpg)

EPIC I: USER STORY I:

![Epic I: User Story I](/Documents/EPICIUSI.jpg)

SORT GENERATOR SERVICE TEST:

![SORT TEST](/Documents/SortTest.png)

CVC GENERATOR SERVICE TEST:

![CVC Test](/Documents/CVCTest.png)

IBAN PREAMBLE GENERATOR SERVICE TEST:

![PREAMBLE TEST](/Documents/CountryTest.png)

ACCOUNT GENERATOR SERVICE TEST:

![Account Test](/Documents/AccountTest.png)

CARD

![Card Test](/Documents/CardTest.png)

CENTRAL

![Central Service Test](/Documents/CentralTest.png)
