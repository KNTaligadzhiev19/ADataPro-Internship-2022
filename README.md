
# 💻 Technologies 💻	
- <b> GitHub: </b>  Collaboration
- <b> Visual Studio Code: </b>  As an IDE
- <b> Discord: </b>  Communication
- <b> Amazon Web Services: </b> Cloud Computing
- <b> Azure: </b>   

# 🚀 Languages 🚀
<p align="left"> 
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png" width=52px height=52px>
    <img src="https://b.thumbs.redditmedia.com/e2dMSMwIGoSHH0kHGrQk83oDxo-qy43aKJxlHKDv-ZU.png" width=52px height=52px>
</p>

# 👥 Team members 👥    
- [MVMartinov19](https://github.com/MVMartinov19)


- [KNTaligadzhiev19](https://github.com/KNTaligadzhiev19)
   
 
- [LVBozukov19](https://github.com/LVBozukov19) 
    

- [DATodorov19](https://github.com/DATodorov19) 
    
 
- [MSDikmeshefket19](https://github.com/MSDikmeshefket19)    
    

# 📚 Infrastructure 📚

- The first thing in terms of infrastructure was to create a AWS Account. After I created the account, I created a new AWS EC2 instance. For the instance I used the t2.micro instance type, which is a micro instance with a CPU of 1 core and a memory of 1GB. For storage I used the EBS volume type, which is a block storage device. The volume size was set to 30GB. The instance was then configured to have a public IP address. After that, I created a Firewall Security Group, which is a group of rules that can be used to control the incoming and outgoing traffic to the instance. The security group was then configured to allow SSH access and HTTP traffic to the instance.

- The second thing in terms of infrastructure was to configure SSH access for all team members. I created a new SSH key for each team member using the Key Pairs feature from the AWS EC2 Console and then configured the SSH key to be able to access the instance.

- When I created the instance, I made sure that the instance is running. I logged into the instance and checked the status of the instance. I also checked the status of the volume. I installed the Python 3.9.2, Sqlite3, Prometheus, and Grafana packages using the apt package manager and configured the git access from the GitHub repository. 

- For local monitoring, I created a Prometheus server and a Grafana server. I configured the Prometheus server to scrape the instance and the Grafana server to visualize the data. I also configured the Prometheus server to send the data to the Grafana server. Then made a new dashboard in Grafana to visualize the data of system resources.

# 🛠 Setting up 🛠
- Clone the repository
 ```cmd
 git clone https://github.com/KNTaligadzhiev19/ADataPro-Internship-2022.git
 ```