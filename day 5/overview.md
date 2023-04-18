
## Lab 5: Creating a Virtual Private Cloud
Lab overview
Traditional networking is difficult. It involves equipment, cabling, complex configurations, and specialist skills. Amazon Virtual Private Cloud (Amazon VPC) hides the complexity and simplifies the deployment of secure private networks.

This lab shows you how to build your own virtual private cloud (VPC), deploy resources, and create private peering connections between VPCs.

Objectives
After completing this lab, you should be able to:

Deploy a VPC

Create an internet gateway and attach it to the VPC

Create a public subnet

Create a private subnet

Create an application server to test the VPC

At the end of this lab, your architecture will look like the following example:

![image](https://user-images.githubusercontent.com/89054489/232357827-5b682018-5764-4deb-8fd1-b9e0c55e3c97.png)

Architecture

Duration
This lab requires approximately 45 minutes to complete.


Accessing the AWS Management Console

## Task 1: Creating a VPC
You begin by using Amazon VPC to create a new VPC.

A VPC is a virtual network that is dedicated to your Amazon Web Services (AWS) account. It is logically isolated from other virtual networks in the AWS Cloud. You can launch AWS resources, such as Amazon Elastic Compute Cloud (Amazon EC2) instances, into the VPC. You can configure the VPC by modifying its IP address range and can create subnets. You can also configure route tables, network gateways, and security settings.

In the AWS Management Console, on the Services  menu, choose VPC.

The VPC console provides a wizard that can automatically create several VPC architectures. However, in this lab, you create the VPC components manually.

In the left navigation pane, choose Your VPCs.

A default VPC is provided so that you can launch resources as soon as you start using AWS. There is also a shared VPC that you use later in the lab. However, you now create your own Lab VPC.

The VPC will have a Classless Inter-Domain Routing (CIDR) range of 10.0.0.0/16, which includes all IP address that start with 10.0.x.x. It contains more than 65,000 addresses. You later divide the addresses into separate subnets.

Choose Create VPC.

Under Resources to create, choose VPC only.

Configure the following settings:

For Name tag enter Lab VPC

For IPv4 CIDR block, enter 10.0.0.0/16

For Tenancy, select Default.

For Tags, ensure that:
Key: Name
Value: Lab VPC

 

Choose Create VPC.

From the VPC Details page, choose the Tags tab.

Tags are useful for identifying resources. For example, you can use a tag to identify cost centers or different environments (such as development, test, or production).

Choose Actions  and select Edit VPC settings.

In the DNS settings section, select  Enable DNS hostnames.

This option assigns a friendly Domain Name System (DNS) name to EC2 instances in the VPC, such as the following:

ec2-52-42-133-255.us-west-2.compute.amazonaws.com

Choose Save.

Any EC2 instances that are launched into the VPC now automatically receive a DNS hostname. You can also add a more-meaningful DNS name (such as app.example.com) later by using Amazon Route 53.

![image](https://user-images.githubusercontent.com/89054489/232374427-404f31cd-a6a6-4539-9c04-e9b941a31335.png)
![image](https://user-images.githubusercontent.com/89054489/232375047-06d48d2f-5437-4b99-866e-0fb04a9d6068.png)
![image](https://user-images.githubusercontent.com/89054489/232375255-eae5ed2c-82ce-43ff-913c-fd94a4925f79.png)
![image](https://user-images.githubusercontent.com/89054489/232375410-d04e8f13-9c8c-462a-ae18-6a00a2e75436.png)
![image](https://user-images.githubusercontent.com/89054489/232375544-7686adc1-98f5-42d5-b9f8-0ccea94fb481.png)

## Task 2: Creating subnets
A subnet is a subrange of IP addresses in the VPC. AWS resources can be launched into a specified subnet. Use a public subnet for resources that must be connected to the internet, and use a private subnet for resources that must remain isolated from the internet.

In this task, you create a public subnet and a private subnet:

Subnets
![image](https://user-images.githubusercontent.com/89054489/232357859-cb473d52-489b-4dab-9ad4-80d0a829a52b.png)

Create a public subnet
You use the public subnet for internet-facing resources.

In the left navigation pane, choose Subnets.

Choose Create subnet and configure the following settings:

For VPC ID, choose Lab VPC.

For Subnet name, enter Public Subnet

For Availability zone, select the first Availability Zone in the list. Do not choose No Preference.

For IPv4 CIDR block, enter 10.0.0.0/24

Choose Create subnet

 The VPC has a CIDR block of 10.0.0.0/16, which includes all 10.0.x.x IP addresses. The subnet you just created has a CIDR block of 10.0.0.0/24, which includes all 10.0.0.x IP addresses. They might look similar, but the subnet is smaller than the VPC because of the /24 in the CIDR range.

You now configure the subnet to automatically assign a public IP address for all instances that are launched in it.

Select the check box for  Public Subnet.

Choose Actions  and select Edit subnet settings. Then configure the following option:

Under Auto-assign IP settings, select  Enable auto-assign public IPv4 address.

Choose Save

 Though this subnet is named Public Subnet, it is not yet public. A public subnet must have an internet gateway, which you attach in the next task.

Create a private subnet
You use the private subnet for resources that must remain isolated from the internet.

Use what you learned in the previous steps to create another subnet with the following settings:

For VPC ID, choose Lab VPC.

For Subnet name, enter Private Subnet

For Availability Zone, select the first Availability Zone in the list. Do not choose No Preference.

For IPv4 CIDR block, enter 10.0.2.0/23

Choose Create subnet

The CIDR block of 10.0.2.0/23 includes all IP addresses that start with 10.0.2.x and 10.0.3.x. This is twice as large as the public subnet because most resources should be kept private unless they specifically must be accessible from the internet.

Your VPC now has two subnets. However, the public subnet is totally isolated and cannot communicate with resources outside the VPC. Next, you configure the public subnet to connect to the internet via an internet gateway.

 ![image](https://user-images.githubusercontent.com/89054489/232375676-ff8b58be-85cb-411c-90c7-9e2ff0bcc742.png)
![image](https://user-images.githubusercontent.com/89054489/232375892-e0c89829-ff52-4e07-a722-4713a46bcbfd.png)
![image](https://user-images.githubusercontent.com/89054489/232375986-619d892a-fa99-47cd-8cd6-87ed9b8cc755.png)
![image](https://user-images.githubusercontent.com/89054489/232376091-f4a246c6-a5d7-400b-bfc5-93408255b3f6.png)
![image](https://user-images.githubusercontent.com/89054489/232376326-9473cb49-3fc3-4a89-8505-3f2cc8e877f4.png)


## Task 3: Creating an internet gateway
An internet gateway is a horizontally scaled, redundant, and highly available VPC component. It allows communication between the instances in a VPC and the internet. It imposes no availability risks or bandwidth constraints on network traffic.

An internet gateway serves two purposes:

To provide a target in route tables that connects to the internet

To perform network address translation (NAT) for instances that were assigned public IPv4 addresses

In this task, you create an internet gateway so that internet traffic can access the public subnet.

In the left navigation pane, choose Internet Gateways.

Choose Create internet gateway and configure the following settings:

For Name tag, enter Lab IGW

Choose Create internet gateway

You can now attach the internet gateway to your Lab VPC.

Choose Actions  and then Attach to VPC, and configure the following settings:

For  Available VPCs, select Lab VPC.

Choose Attach internet gateway

This action attaches the internet gateway to your Lab VPC. Although you created an internet gateway and attached it to your VPC, you must also configure the public subnet route table so that it uses the internet gateway.

![image](https://user-images.githubusercontent.com/89054489/232376429-03176fbc-a959-4ff5-b379-e312916a0a97.png)
![image](https://user-images.githubusercontent.com/89054489/232376470-7df08d65-82e3-4d51-91df-1dac14883343.png)
![image](https://user-images.githubusercontent.com/89054489/232376557-ed63a481-8664-4654-8764-4aaeff3fbf8a.png)
![image](https://user-images.githubusercontent.com/89054489/232376648-0eafce9b-eee2-43f6-962a-f6076eb5eb96.png)

## Task 4: Configuring route tables
A route table contains a set of rules, called routes, that are used to determine where network traffic is directed. Each subnet in a VPC must be associated with a route table because the table controls the routing for the subnet. A subnet can be associated with only one route table at a time, but you can associate multiple subnets with the same route table.

To use an internet gateway, a subnet's route table must contain a route that directs internet-bound traffic to the internet gateway. If a subnet is associated with a route table that has a route to an internet gateway, it is known as a public subnet.

In this task, you:

Create a public route table for internet-bound traffic

Add a route to the route table to direct internet-bound traffic to the internet gateway

Associate the public subnet with the new route table

In the left navigation pane, choose Route Tables.

Several route tables are displayed, but there is only one route table associated with Lab VPC. This route table routes traffic locally, so it is a private route table.

In the VPC column, find the route table that shows Lab VPC, and select the check box for this route table. (You can expand the column to see the names.)

In the Name column, choose  and then enter the name  Private Route Table and choose Save

In the lower half of the page, choose the Routes tab.

   There is only one route. It shows that all traffic that is destined for 10.0.0.0/16 (which is the range of the Lab VPC) will be routed locally. This route allows all subnets in a VPC to communicate with each other.

   You now create a new public route table to send public traffic to the internet gateway.

Choose Create route table and configure the following settings:

For Name, enter Public Route Table

For VPC, choose Lab VPC.

Choose Create route table

In the Routes tab, choose Edit routes

You now add a route to direct internet-bound traffic (0.0.0.0/0) to the internet gateway.

Choose Add route and then configure the following settings:

For Destination, enter 0.0.0.0/0

For Target, select Internet Gateway, and then from the dropdown list select Lab IGW.

Choose Save changes

The last step associates this new route table with the public subnet.

Choose the Subnet associations tab.

In the Subnets without explicit associations section, choose Edit subnet associations

Select the row with Public Subnet.

Choose Save associations

 The public subnet is now public because it has a route table entry that sends traffic to the internet via the internet gateway.

 To summarize, you can create a public subnet by following these steps:

Create an internet gateway.

Create a route table.

Add a route to the route table that directs 0.0.0.0/0 traffic to the internet gateway.

Associate the route table with a subnet, which then becomes a public subnet.

 ![image](https://user-images.githubusercontent.com/89054489/232376842-2bfb0358-7b0c-48c3-9d09-73c9fa67e694.png)
![image](https://user-images.githubusercontent.com/89054489/232376916-93f72a36-7228-4f53-b225-d6b1d942ce8b.png)
![image](https://user-images.githubusercontent.com/89054489/232377043-51ec21f3-1703-418e-a300-7a3c1a5b5e32.png)
![image](https://user-images.githubusercontent.com/89054489/232377210-8c4ddbbf-33d2-4e52-8c31-2be7d861fc6e.png)
![image](https://user-images.githubusercontent.com/89054489/232377295-e8c02dfe-61fb-4ced-86c4-d390d4210ed1.png)


## Task 5: Creating a security group for the application server
A security group acts as a virtual firewall for instances to control inbound and outbound traffic. Security groups operate at the level of the elastic network interface for the instance. Security groups do not operate at the subnet level. Thus, each instance can have its own firewall that controls traffic. If you do not specify a particular security group at launch time, the instance is automatically assigned to the default security group for the VPC.

In this task, you create a security group that allows users to access your application server via HTTP.

In the left navigation pane, choose Security Groups.

Choose Create security group and configure the following settings:

For Security group name, enter App-SG

For Description, enter Allow HTTP traffic

For VPC, choose Lab VPC.

Choose Create security group

Choose the Inbound Rules tab.

The settings for Inbound Rules determine what traffic is permitted to reach the instance. You configure it to permit HTTP (port 80) traffic that comes from anywhere on the internet (0.0.0.0/0).

Choose Edit inbound rules

Choose Add rule and then configure the following settings:

For Type, choose HTTP.

From the Source type dropdown list, choose Anywhere IPv4.

For Description, enter Allow web access

Choose Save rules

You use this App-SG in the next task.

![image](https://user-images.githubusercontent.com/89054489/232377519-ab35afd8-ca33-4b6d-831b-ef321e91149e.png)
![image](https://user-images.githubusercontent.com/89054489/232377674-f537fa1c-3836-4ccb-94f0-8710eff89de3.png)
![image](https://user-images.githubusercontent.com/89054489/232377891-8ddb2ed2-673f-4d09-9472-976411a8211c.png)

## Task 6: Launching an application server in the public subnet
To test that your VPC is correctly configured, you now launch an EC2 instance into the public subnet. You also confirm that you can access the EC2 instance from the internet.

On the Services  menu, choose EC2.

Choose Launch instance and then select Launch instance from the dropdown list. Configure the following options:

In the Name and tags pane, in the Name text box, enter App Server

In the Application and OS Images (Amazon Machine Image) section, keep default selection, Amazon Linux 2.

In the Instance type section, keep the default instance type, t2.micro. 

In the Key pair (login) section, from the Key pair name - required dropdown list, choose Proceed without a key pair (not recommended).

In the Network settings section, choose Edit

From the VPC - required dropdown list, choose Lab VPC.

From the Subnet dropdown list, choose Public Subnet.

Ensure that Auto-assign public IP is Enable.

In the Firewall (security groups)  section, choose Select existing security group

From the Common security groups dropdown list, choose App-SG.

In the Configure storage section, keep the default storage configuration.

Expand the Advanced details section.

For IAM instance profile, choose the role Inventory-App-Role.

Scroll down to User data section, copy and paste the below code in the block.

#!/bin/bash
# Install Apache Web Server and PHP
yum install -y httpd mysql
amazon-linux-extras install -y php7.2
# Download Lab files
wget https://aws-tc-largeobjects.s3-us-west-2.amazonaws.com/ILT-TF-200-ACACAD-20-EN/mod6-guided/scripts/inventory-app.zip
unzip inventory-app.zip -d /var/www/html/
# Download and install the AWS SDK for PHP
wget https://github.com/aws/aws-sdk-php/releases/download/3.62.3/aws.zip
unzip aws -d /var/www/html
# Turn on web server
chkconfig httpd on
service httpd start
From the Summary section, choose Launch instance

Choose View all instances

Wait for the application server to fully launch. It should display the following status:

Instance State:  Running

       You can choose refresh   occasionally to update the display.

Select  App Server.

From the Details tab, copy the Public IPv4 address address.

Open a new browser tab, paste the IP address you just copied, and press Enter.

   If you configured the VPC correctly, the Inventory application and this message should appear: Please configure Settings to connect to database. You have not configured any database settings yet, but the appearance of the Inventory application demonstrates that the public subnet was correctly configured.

     If the Inventory application does not appear, wait for 60 seconds and refresh  the page to try again. It can take a couple of minutes for the EC2 instance to boot and run the script that installs the software.

![image](https://user-images.githubusercontent.com/89054489/232378000-0f920906-250c-4806-83cb-33b39b719bc8.png)
![image](https://user-images.githubusercontent.com/89054489/232381786-f6f38543-6968-4c0b-bb1e-9bfd09a743e0.png)
![image](https://user-images.githubusercontent.com/89054489/232381818-545b800a-9f6b-4910-9148-4b98aaae365e.png)
![image](https://user-images.githubusercontent.com/89054489/232381868-68542bfd-bae6-4276-b039-70af4111b41d.png)
![image](https://user-images.githubusercontent.com/89054489/232381970-eaea6c73-d795-4441-aaa9-72557722c2c2.png)
![image](https://user-images.githubusercontent.com/89054489/232382044-c6a7d974-b858-4a47-ac9b-550673f09a28.png)
![image](https://user-images.githubusercontent.com/89054489/232382122-ce7ec88a-c3a8-4fbf-b410-0b50bdecb797.png)


![image](https://user-images.githubusercontent.com/89054489/232378662-67ba405f-9126-4704-9ef1-825d9bf4589e.png)

 ![Uploading image.png…]()


Lab complete 
 Congratulations! You have completed the lab.
