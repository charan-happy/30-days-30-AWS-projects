# Deploy a three tier web application in the cloud
scalability, High availability, Fault tolerant, security, Improved performance services using are : VPC, Amazon EC2, RDS, AWS Load balancer 
-----------------------------------------------------------------
# Lab 4 - Introduction to Amazon Relational Database Service (Amazon RDS)

Lab overview
Traditionally, creating a database can be a complex process that requires either a database administrator or a systems administrator. In the cloud, you can simplify this process by using Amazon Relational Database Service (Amazon RDS).

Objectives
After completing this lab, you should be able to:

Launch a database using Amazon RDS
Configure a web application to connect to the database instance
At the end of this lab, your architecture will look like the following example:


![image](https://user-images.githubusercontent.com/89054489/232302566-53314859-ccb0-40fc-a3e5-15975f486ee8.png)

Architecture

Duration
This lab requires approximately 30 minutes to complete.

Accessing the AWS Management Console

Arrange the AWS Management Console tab .

## Task 1: Creating an Amazon RDS database
In this task, you create a MySQL database in your virtual private cloud (VPC). MySQL is a popular open-source relational database management system (RDBMS), so there are no software licensing fees.

 Windows Users: Use Chrome or Firefox as your web browser for this lab. The lab instructions are not compatible with Internet Explorer because of a difference in the Amazon RDS console.

On the Services  menu, choose RDS.

Choose Create database

Under Engine options, select  MySQL.

The options include several use cases, ranging from enterprise-class databases to Dev/Test systems. In the options, you might notice Amazon Aurora. Aurora is a MySQL-compatible system that was re-architected for the cloud. If your company uses large-scale MySQL or PostgreSQL databases, Aurora can provide enhanced performance.

In the Templates section, select  Dev/Test.

You can now select a database configuration, including software version, instance class, storage, and login settings. The Multi-AZ deployment option automatically creates a replica of the database in a second Availability Zone for high availability. 

In Availability and durability section, choose  Single DB instance.

In the Settings section, configure the following options:

DB instance identifier: inventory-db
Master username: admin
Master password: lab-password
Confirm password: lab-password
In the DB instance class section, configure the following options:

Select  Burstable classes (includes t classes).
Select db.t3.micro.
In the Storage section, configure the following options:

Storage type: Select General Purpose SSD (gp2).
Allocated storage: Enter 20 GiB.
In the Connectivity section, configure the following option: 

Virtual private cloud (VPC): Lab VPC
In the Connectivity section, for Existing VPC security groups, choose the X on default to remove this security group. Then choose the dropdown list, and select DB-SG to add it.

Scroll to the Monitoring section, and clear (deselect) the Enable Enhanced monitoring option.

Scroll to the Additional configuration section, and choose  to expand it. 

For Initial database name, enter inventory

 

	This is the logical name of the database that the application will use.

	 You can review the many other options displayed on the page, but leave them set to their default values. Options include automatic backups, the ability to export log files, and automatic version upgrades. 
The ability to activate these features with check boxes demonstrates the power of using a fully managed database solution instead of installing, backing up, and maintaining the database yourself.

At the bottom of the page, choose Create database
	You should receive this message: Creating database inventory-db.

	 If you receive an error message that mentions rds-monitoring-role, 	confirm that you   have cleared the Enable Enhanced monitoring option in the previous step, and then try again.

	Before you continue to the next task, the database instance status must be Available. This process could take several minutes.

![image](https://user-images.githubusercontent.com/89054489/232353681-a70aea7d-c5b5-4410-980c-66ca8d1d5fb8.png)
![image](https://user-images.githubusercontent.com/89054489/232353751-e6271b72-49c8-4b1c-b882-2ca0e61e87ea.png)
![image](https://user-images.githubusercontent.com/89054489/232353814-01c69e38-88ee-4d7b-b185-8ffb36178c87.png)
![image](https://user-images.githubusercontent.com/89054489/232353847-bc6eef15-0973-47b6-8f3c-0b8c5fbf6227.png)
![image](https://user-images.githubusercontent.com/89054489/232353895-20728873-a935-45ba-8c0b-88eab146dffc.png)
![image](https://user-images.githubusercontent.com/89054489/232354026-28da3aee-8aef-4944-b74b-2c57c4423786.png)
![image](https://user-images.githubusercontent.com/89054489/232354116-8307a3b4-4623-47a4-a406-e547faf91bc0.png)
![image](https://user-images.githubusercontent.com/89054489/232354200-267e1656-42ad-45d1-a3f6-0be4b8b0dbc7.png)
![image](https://user-images.githubusercontent.com/89054489/232354394-2136a1c5-ced4-4f35-9f28-0125bf6d7ef9.png)
![image](https://user-images.githubusercontent.com/89054489/232354504-74480e52-d72b-4918-a117-ec7786edc9a2.png)
![image](https://user-images.githubusercontent.com/89054489/232354533-b88ce82a-0aae-451f-9756-bedacbb9ce2c.png)
![image](https://user-images.githubusercontent.com/89054489/232354556-7da86f3c-e808-4d49-8d26-a218dfb65670.png)
![image](https://user-images.githubusercontent.com/89054489/232354829-d0683382-c147-4e46-8c02-eb3a6774ce67.png)
![image](https://user-images.githubusercontent.com/89054489/232355297-42a2756f-d239-4c8a-8d48-9e08969875b3.png)



## Task 2: Configuring web application communication with a database instance

This lab automatically deployed an Amazon Elastic Compute Cloud (Amazon EC2) instance with a running web application. You must use the IP address of the instance to connect to the application.

On the Services  menu, choose EC2.
In the left navigation pane, choose Instances.
In the center pane, there should be a running instance that is named App Server.

Select the check box for the App Server instance.
In the Details tab, copy the Public IPv4 address to your clipboard.
Tip: If you hover over the IP address, a copy  icon appears. To copy the displayed value, choose the icon.

Open a new web browser tab, paste the IP address into the address bar, and then press Enter.
The web application should appear. It does not display much information because the application is not yet connected to the database.

Choose  Settings.
You can now configure the application to use the Amazon RDS database instance that you created earlier. You first retrieve the database endpoint so that the application knows how to connect to a database.

Return to the AWS Management Console, but do not close the application tab. (You will return to it soon.)
On the Services  menu, choose RDS.
In the left navigation pane, choose Databases.
Choose inventory-db.
Scroll to the Connectivity & security section, and copy the Endpoint to your clipboard.
It should look similar to this example: inventory-db.crwxbgqad61a.rds.amazonaws.com

Return to the browser tab with the inventory application, and enter the following values:

For Endpoint, paste the endpoint you copied earlier.
For Database, enter inventory
For Username, enter admin
For Password, enter lab-password
Choose Save.
		The application will now connect to the database, load some initial data, and display information.

You can use the web application to   Add inventory,  edit, and  delete inventory information.
 The inventory information is stored in the Amazon RDS MySQL database that you created earlier in the lab. This means that in the event of any failure in the application server, you will not lose any data. It also means that multiple application servers can access the  same data.

Insert new records into the table. Ensure that the table has 5 or more inventory records before submitting your work.
 You have now successfully launched the application and connected it to the database.

Optional: To access the saved parameters, go to the AWS Management console. On the Services  menu, choose Systems Manager. In the left navigation menu, choose Parameter Store. 

![image](https://user-images.githubusercontent.com/89054489/232355327-00118c39-051c-4f12-8798-28d0134ab47c.png)
![image](https://user-images.githubusercontent.com/89054489/232355390-6933bdb6-8523-4053-b249-d8e3829bec1f.png)
![image](https://user-images.githubusercontent.com/89054489/232355431-c6c5f315-e0d4-4416-bf0a-fda7a9045dc4.png)
![image](https://user-images.githubusercontent.com/89054489/232355594-47a2c348-b5fa-439a-96d1-0a47fc32782e.png)
![image](https://user-images.githubusercontent.com/89054489/232355189-d4316604-dee8-4e1a-9901-2f72acca2bef.png)
![image](https://user-images.githubusercontent.com/89054489/232355685-1f2a9dbb-07c0-45dd-9912-a7578a542a24.png)
![image](https://user-images.githubusercontent.com/89054489/232355758-bed4df89-d178-41ad-939b-2db8f02341b8.png)
![image](https://user-images.githubusercontent.com/89054489/232355817-058bed46-de61-4b40-b9b7-8505ec6c67c3.png)

![image](https://user-images.githubusercontent.com/89054489/232355898-b367108d-151a-422c-923f-62d6c6f51b41.png)
![image](https://user-images.githubusercontent.com/89054489/232357268-18e57394-496f-43d6-830a-84b84f943e85.png)


Lab complete 
 Congratulations! You have completed the lab. 

 

