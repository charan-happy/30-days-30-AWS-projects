Introduction to Amazon EC2
In this self-paced lab, you will practice using Amazon EC2. This lab provides you with a basic overview of launching, resizing, managing, and monitoring an Amazon EC2 instance. This lab requires approximately 60 minutes to complete.

By the end of this lab, you will be able to:

Launch a web server with termination protection enabled
Monitor your EC2 instance
Modify the security group that your web server is using to allow HTTP access
Resize your Amazon EC2 instance to scale
Explore EC2 limits
Test termination protection
Terminate your EC2 instance


***************
Solution
****************
Task 1: Launching your EC2 instance
In this task, you launch an EC2 instance with termination protection. Termination protection prevents you from accidentally terminating an EC2 instance. You also deploy your instance with a user data script in order to deploy a simple web server.

 

In the AWS Management Console on the Services menu, choose EC2.
In the left navigation pane, choose EC2 Dashboard to ensure that you are on the dashboard page.
Choose Launch instance, and then select Launch instance.

![image](https://user-images.githubusercontent.com/89054489/232049688-348fe01e-3db2-4b06-ac89-b06e4426b98c.png)


Step 1: Name your EC2 instance
Using tags, you can categorize your AWS resources in different ways (for example, by purpose, owner, or environment). This categorization is useful when you have many resources of the same type. You can quickly identify a specific resource based on the tags that you have assigned to it. Each tag consists of a key and a value, both of which you define.

When you name your instance, AWS creates a key-value pair. The key for this pair is Name, and the value is the name you enter for your EC2 instance.

 

In the Name and tags section, for Name, enter Web-Server
Choose the Add additional tags link.
From the Resource types dropdown list, ensure that both Instances and Volumes are selected.
   
![image](https://user-images.githubusercontent.com/89054489/232050577-c19c8fb8-415e-4bac-8ace-7caabd5fa7c3.png)

Step 2: Choose an Amazon Machine Image (AMI)
An Amazon Machine Image (AMI) provides the information required to launch an instance, which is a virtual server in the cloud. An AMI includes the following:

A template for the root volume for the instance (for example, an operating system or an application server with applications)
Launch permissions that control which AWS accounts can use the AMI to launch instances
A block device mapping that specifies the volumes to attach to the instance when it is launched
The Quick Start list contains the most commonly used AMIs. You can also create your own AMI or select an AMI from the AWS Marketplace, an online store where you can sell or buy software that runs on AWS.

 

Locate the Application and OS Images (Amazon Machine Image) section. It is just below the Name and tags section.
In the AMI Machine Image (AMI) box, notice that Amazon Linux 2 AMI is selected by default. Keep this setting.
 ![image](https://user-images.githubusercontent.com/89054489/232051021-32a3ac55-2c1b-4af4-ae82-a32992efc781.png)


Step 3: Choose an instance type
Amazon EC2 provides a wide selection of instance types that are optimized to fit different use cases. Instance types comprise varying combinations of CPU, memory, storage, and networking capacity and give you the flexibility to choose the appropriate mix of resources for your applications. Each instance type includes one or more instance sizes so that you can scale your resources to the requirements of your target workload.

In this step, you choose a t2.micro instance. This instance type has 1 virtual CPU and 1 GiB of memory.

Keep the default instance type, t2.micro.
   

Step 4: Configure a key pair
Amazon EC2 uses public key cryptography to encrypt and decrypt login information. To log in to your instance, you must create a key pair, specify the name of the key pair when you launch the instance, and provide the private key when you connect to the instance.

In this lab, you do not log in to your instance, so you do not require a key pair.

 

In the Key pair (login) section, from the Key pair name - required dropdown list, choose Proceed without a key pair.
 ![image](https://user-images.githubusercontent.com/89054489/232051343-b4828929-396c-461f-a373-39fd8563e5a1.png)


Step 5: Configure the network settings
You use this pane to configure networking settings.

The virtual private cloud (VPC) indicates which VPC you want to launch the instance into. You can have multiple VPCs, including different ones for development, testing, and production.

 

In the Network settings section, choose Edit.

From the VPC - required dropdown list, choose Lab VPC.

The Lab VPC was created using an AWS CloudFormation template during the setup process of your lab. This VPC includes two public subnets in two different Availability Zones.

 

In the Network settings section, for Security group name - required, enter Web Server security group

A security group acts as a virtual firewall that controls the traffic for one or more instances. When you launch an instance, you associate one or more security groups with the instance. You add rules to each security group that allow traffic to or from its associated instances. You can modify the rules for a security group at any time; the new rules are automatically applied to all instances that are associated with the security group.

In this lab, you do not log in to your instance using SSH. Removing SSH access improves the security of the instance.

 

To delete the existing SSH rule, next to Security group rule 1, choose Remove.

 ![image](https://user-images.githubusercontent.com/89054489/232052841-ff252ddf-59e1-4101-87f8-65663c565848.png)


Step 6: Add storage
Amazon EC2 stores data on a network-attached virtual disk called Amazon Elastic Block Store (Amazon EBS).

You launch the EC2 instance using a default 8 GiB disk volume. This is your root volume (also known as a boot volume).

 

In the Configure storage pane, keep the default storage configuration.
 ![image](https://user-images.githubusercontent.com/89054489/232053065-da948bec-357c-46c6-9f7f-dd658daa9fc8.png)


Step 7: Configure advanced details
Expand the Advanced details pane.

 

When you no longer require an EC2 instance, you can terminate it, which means that the instance stops, and Amazon EC2 releases the instance's resources. You cannot restart a terminated instance. If you want to prevent your users from accidentally terminating the instance, you can enable termination protection for the instance, which prevents users from terminating instances.

From the Termination protection dropdown list, choose  Enable.

 

When you launch an instance in Amazon EC2, you have the option of passing user data to the instance. These commands can be used to perform common automated configuration tasks and even run scripts after the instance starts. 

Copy the following commands, and paste them into theIn the User data text box.

#!/bin/bash
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
The script does the following:

Install an Apache web server (httpd)
Configure the web server to automatically start on boot
Activate the Web server
Create a simple web page
 
![image](https://user-images.githubusercontent.com/89054489/232053665-96b1eaf2-234b-45b4-a9db-62f2a1e93eda.png)

![image](https://user-images.githubusercontent.com/89054489/232053752-2b8c8f28-1e31-4aec-b9a1-d1369fee3eff.png)

Step 8: Launch an EC2 instance
Now that you have configured your EC2 instance settings, it is time to launch your instance.

 

In the Summary section, choose Launch instance.
![image](https://user-images.githubusercontent.com/89054489/232054029-e7288212-91ba-4d7f-a2e3-4bc17d9c83be.png)
![image](https://user-images.githubusercontent.com/89054489/232054153-1a5cba21-a60a-405c-b2cd-cea3190e83b2.png)

Choose View all instances

The instance appears in a Pending state, which means that it is being launched. It then changes to Running, which indicates that the instance has started booting. There will be a short time before you can access the instance.

The instance receives a public Domain Name System (DNS) name that you can use to contact the instance from the Internet.

Next to your Web-Server, select the  check box. The Details tab displays detailed information about your instance.

 To view more information in the Details tab, drag the window divider upward.

Review the information displayed in the Details, Security and Networking tabs.

 

Wait for your instance to display the following:

Note: Refresh if needed.

Instance State:  Running
Status Checks:   2/2 checks passed
 

 ![image](https://user-images.githubusercontent.com/89054489/232054694-d95291ba-05bf-4972-951c-3d753dd29f77.png)
![image](https://user-images.githubusercontent.com/89054489/232055223-3e632c60-661c-4b97-b1cd-b1c3f81a2dc7.png)
 

Task 2: Monitoring your instance
Monitoring is an important part of maintaining the reliability, availability, and performance of your EC2 instances and your AWS solutions.

Choose the Status checks tab.

With instance status monitoring, you can quickly determine whether Amazon EC2 has detected any problems that might prevent your instances from running applications. Amazon EC2 performs automated checks on every running EC2 instance to identify hardware and software issues.

Notice that both the System reachability and Instance reachability checks have passed.

![image](https://user-images.githubusercontent.com/89054489/232055607-191b4a4d-c97e-489c-a669-2c711ab04c4a.png)


Choose the Monitoring tab.

This tab displays Amazon CloudWatch metrics for your instance. Currently, there are not many metrics to display because the instance was recently launched.

You can chose a graph to see an expanded view.

 Amazon EC2 sends metrics to Amazon CloudWatch for your EC2 instances. Basic (5 minute) monitoring is enabled by default. You can enable detailed (1 minute) monitoring.

 

At the top of the page, choose the Actions  dropdown menu. Select Monitor and troubleshoot  Get system log.

The system log displays the console output of the instance, which is a valuable tool for diagnosing problems. It is especially useful for troubleshooting kernel problems and service configuration issues that could cause an instance to terminate or become unreachable before its SSH daemon can be started. If you do not see a system log, wait a few minutes and then try again.

 ![image](https://user-images.githubusercontent.com/89054489/232056705-86e06703-c1e1-4188-af52-59847883c5dd.png)

 

Scroll through the output, and note that the HTTP package was installed from the user data that you added when you created the instance. The entries in the system log should be similar to the following example:

[   26.760639] cloud-init[3280]: Installed:
[   26.770051] cloud-init[3280]: httpd.x86_64 0:2.4.52-1.amzn2
[   26.777748] cloud-init[3280]: Dependency Installed:
[   26.781750] cloud-init[3280]: apr.x86_64 0:1.7.0-9.amzn2
[   26.793739] cloud-init[3280]: apr-util.x86_64 0:1.6.1-5.amzn2.0.2
[   26.796595] cloud-init[3280]: apr-util-bdb.x86_64 0:1.6.1-5.amzn2.0.2
[   26.805964] cloud-init[3280]: generic-logos-httpd.noarch 0:18.0.0-4.amzn2
[   26.817765] cloud-init[3280]: httpd-filesystem.noarch 0:2.4.52-1.amzn2
[   26.829760] cloud-init[3280]: httpd-tools.x86_64 0:2.4.52-1.amzn2
[   26.833753] cloud-init[3280]: mailcap.noarch 0:2.1.41-2.amzn2
[   26.845761] cloud-init[3280]: mod_http2.x86_64 0:1.15.19-1.amzn2.0.1
[   26.849762] cloud-init[3280]: Complete!
 
![image](https://user-images.githubusercontent.com/89054489/232056915-92fbf2c7-08f8-4d1a-875b-1bb858bc1f65.png)
To return to the Amazon EC2 dashboard, choose Cancel.

With your Web-Server selected, choose the Actions  dropdown menu, and select Monitor and troubleshoot  Get instance screenshot.

This option shows you what your EC2 instance console would look like if a screen were attached to it. It is essentially a command line interface.

ec2-instance-screen-shot

 If you are unable to reach your instance via SSH or RDP, you can capture a screenshot of your instance and view it as an image. This option provides visibility about the status of the instance and allows for quicker troubleshooting.

 ![image](https://user-images.githubusercontent.com/89054489/232057216-d68f078d-16b6-43f1-8d82-0546e50f8dca.png)


At the bottom of the page, choose Cancel.

 

Task 3: Updating your security group and accessing the web server
When you launched the EC2 instance, you provided a script that installed a web server and created a simple web page. In this task, you access content from the web server.

Select the check box next to the Amazon EC2 Web-Server that you created, and then choose the Details tab.

Copy the Public IPv4 address of your instance to your clipboard.

In your web browser, open a new tab, paste the IP address that you just copied, and then press Enter.

Question: Are you able to access your web server? Why not?

You are not currently able to access your web server because the security group is not permitting inbound traffic on port 80, which is used for HTTP web requests. This is a demonstration of how to use a security group as a firewall to restrict the network traffic that is allowed in and out of an instance.

To correct this issue, you now update the security group to permit web traffic on port 80.

 

Keep the browser tab open, but return to the EC2 Management Console tab.

In the left navigation pane, choose Security Groups.

Next to Web Server security group, select the  check box.

Choose the Inbound rules tab.

The security group currently has no rules.

Choose Edit inbound rules, and then choose Add rule and configure the following options:

Type: Choose HTTP.
Source: Choose Anywhere-IPv4.
Note: Notice the "Rules with source of 0.0.0.0/0 allow all IP addresses to access your instance. We recommend setting security group rules to allow access from known IP addresses only." While this is true and common best practice, this lab allows access from any IP address (Anywhere) to simplify both the security group configuration and testing of the website running on your EC2 instance.

 

Choose Save rules

Return to the web server browser tab with the public IPv4 address that you previously opened, and choose  to refresh the page.

You should see the message Hello From Your Web Server!

![image](https://user-images.githubusercontent.com/89054489/232058038-743e03ec-83d0-43a3-a163-39dac9ecaeff.png)


 ![image](https://user-images.githubusercontent.com/89054489/232057931-b56b6dcd-7d80-4e4e-b5dc-5629a65fa6b7.png)

![image](https://user-images.githubusercontent.com/89054489/232058351-80398444-16f9-46a0-bdad-c5aea2397767.png)
![image](https://user-images.githubusercontent.com/89054489/232058509-51ef3ee4-9c0a-4ef8-a87a-6d4c2cdab905.png)

Task 4: Resizing your instance - instance type and EBS volume
As your needs change, you might find that your instance is over utilized (too small) or under utilized (too large). If so, you can change the instance type. For example, if a t2.micro instance is too small for its workload, you can change it to an m5.medium instance. Similarly, you can change the size of a disk.

Stop your instance
Before you can resize an instance, you must stop it.

When you stop an instance, it is shut down. There is no charge for a stopped EC2 instance, but the storage charge for attached EBS volumes remains.


 

On the EC2 Management Console, in the left navigation pane, choose Instances.

The  check box next to Web Server should already be selected.

At the top of the page, select the Instance state  dropdown menu, and choose Stop instance.

In the Stop instance? pop-up window, choose Stop.

Your instance performs a normal shutdown and then stops running.

Wait for the Instance state to display Stopped.

Change the instance type
Select the check box next to your Web-Server. From the Actions  dropdown menu, select Instance settings  Change instance type, and then configure the following option:

Instance type: Select t2.nano.

 

Choose Apply.

When the instance is started again, it is a t2.nano instance. 

Note: You are restricted from using other instance types in this lab.

![image](https://user-images.githubusercontent.com/89054489/232184239-3b047a64-a3d2-4202-baaf-0ef3620d90cd.png)
![image](https://user-images.githubusercontent.com/89054489/232184259-61629dbd-e958-4528-9c7e-4984f4bc4492.png)
![image](https://user-images.githubusercontent.com/89054489/232184324-17973b2a-ebec-48ba-97e3-1a7b393d905b.png)
![image](https://user-images.githubusercontent.com/89054489/232184391-4f805399-a712-423c-872f-94bcc4f2a7e9.png)
![image](https://user-images.githubusercontent.com/89054489/232184554-45188099-3e45-4d59-9a93-e5ef4736b417.png)
![image](https://user-images.githubusercontent.com/89054489/232184576-ee6cadcd-886e-4c4e-8ae5-b4b44a801440.png)
![image](https://user-images.githubusercontent.com/89054489/232184660-b5086f7a-cab4-4914-8da2-bc7d4e39b09f.png)
 

Resize the EBS volume
In the left navigation menu, choose Volumes.

Select the check box for the one volume that is listed, which is attached to your Web-Server instance.

In the Actions  dropdown menu, select Modify Volume.

The disk volume currently has a size of 8 GiB. You now increase the size of this disk.

Change the Size (GiB) to 10

Choose Modify.

To confirm and increase the size of the volume, in the Modify pop-up window, choose Modify

 

Start the resized instance
You now start the instance again, which now has less memory but more disk space.

In left navigation pane, choose Instances. Next to your Web-Server, select the  check box.
From the Instance state  dropdown menu, choose Start instance.
Task 5: Exploring EC2 limits
Amazon EC2 provides different resources that you can use. These resources include images, instances, volumes, and snapshots. When you create an AWS account, there are default limits on these resources on a per-Region basis.

 

In the left navigation pane, choose Limits.

Note: There is a limit on the number of instances that you can launch in this Region. When launching an instance, the request must not cause your usage to exceed the current instance limit in that Region.

You can request an increase for many of these limits.
![image](https://user-images.githubusercontent.com/89054489/232184819-af553228-b891-400d-b2b5-efbbbaeccfd1.png)

 

Task 6: Testing termination protection
You can delete your instance when you no longer need it. This is referred to as terminating your instance. You cannot connect to or restart an instance after it has been terminated.

In this task, you learn how to use termination protection.

 

In left navigation pane, choose Instances. Select the  check box for your Web-Server.

At the top of the page in the Instance state  dropdown menu, choose Terminate instance. From the Terminate instance? pop-up window, choose Terminate. 

Note: At the top of the page, a message says Failed to terminate an instance: The instance 'i-xxxxxxxxxxxx' may not be terminated. Modify its 'disableApiTermination' instance attribute and try again. This message is a safeguard to prevent the accidental termination of an instance. If you really want to terminate the instance, you need to turn off the termination protection.
![image](https://user-images.githubusercontent.com/89054489/232184868-fea311e0-3351-44f0-85d0-a10cf52bdf3a.png)
![image](https://user-images.githubusercontent.com/89054489/232184919-c52e5ba6-fded-48f6-8a95-95a15aaef4dd.png)

 

Submitting your work
At the top of these instructions, choose Submit to record your progress and when prompted, choose Yes.

Tip: If you previously hid the terminal in the browser panel, select the Terminal  check box in the upper right to expose the panel again. This option ensures that the lab instructions remain visible after you choose Submit.

 

If the results don't display after a couple of minutes, return to the top of these instructions and choose Grades

 Note If the grading is erroring out and not grading properly. Make sure the EC2 instance tags are set as Web-Server or the grading will not work.

Tip: You can submit your work multiple times. After you change your work, choose Submit again. Your last submission is what will be recorded for this lab.

 
