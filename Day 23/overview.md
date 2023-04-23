# Migrating a database with the Database MIgration Service
This project involves 5 steps
## step 1
## step 2
## step 3
## step 4
## step 5

### step-1 Architecture Diagram
![image](https://user-images.githubusercontent.com/89054489/233835565-82de192c-74de-4836-9ead-a670f5667adc.png)

- login to the [AWS account](https://aws.amazon.com/)
- Make sure to select the N.virginia region just like below image 👇
![image](https://user-images.githubusercontent.com/89054489/233834727-7f31ec29-3efc-4162-834e-74cc47cab8f5.png)

- [click Here](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/aws-dms-database-migration/DMS.yaml&stackName=DMS ) To provision base lab infrastructure for our current project.

You should take note of the `parameter` values

- DBName
- DBPassword
- DBRootPassword
- DBUser

You will need all of these in later stages.
All defaults should be pre-populated, you just need to scroll to the bottom, check the capabilities box and click `Create Stack`

![image](https://user-images.githubusercontent.com/89054489/233835053-78382fc6-2858-4477-8e3c-07c4d5499fac.png)

### stage 1 final steps
- Once the stack is in the `CREATE_COMPLETE` status you will have a simulated `on-premises` environment and an AWS environment. 
once you click on the `create stack on the above step` after couple of minutes you can able to see below👇 image
![image](https://user-images.githubusercontent.com/89054489/233835619-b669a30b-6c82-4444-ae18-82ea160e0c10.png)

Now, let's verify it once.
- Move to the [EC2 console](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1)
- Click `Running Instances`
![image](https://user-images.githubusercontent.com/89054489/233836291-56b33037-6c73-4ddb-8b22-c7af53ac7b1f.png)

- Select the `CatWEB` instance
![image](https://user-images.githubusercontent.com/89054489/233835777-c86209b5-a0a1-488d-b975-3d4b84a34873.png)

- Copy down its `Public IPv4 DNS` into your clipboard and open it in a new tab.
![image](https://user-images.githubusercontent.com/89054489/233836145-b2420ed4-8134-4806-b34a-d16daa6525e8.png)

- You should see the `Animals4life Hall of Fame load...` this is running from the simulated onpremises environment using the CatDB mariaDB instance.
![image](https://user-images.githubusercontent.com/89054489/233836180-1f19d2a2-118e-4f67-8bc9-99057a5fcec6.png)


## stage 2

### stage-2 Architecture Diagram

![image](https://user-images.githubusercontent.com/89054489/233836751-9040f6ee-ac1e-455f-ae62-eed5ab08f667.png)

Move to the [VPC Console ](https://console.aws.amazon.com/vpc/home?region=us-east-1#)
![image](https://user-images.githubusercontent.com/89054489/233837036-79011f9c-771c-4db9-ad88-cfe3809aa733.png)
![image](https://user-images.githubusercontent.com/89054489/233837100-d45e1664-9b26-4b16-95d0-214c56936e1f.png)

Click on `Peering Connections` under `Virtual Private Cloud`  
![image](https://user-images.githubusercontent.com/89054489/233837149-002b83a4-aaa3-4f44-b3b4-70d8e8e690a2.png)

Click `Create Peering Connection`  
for `Peering connection name tag` choose `A4L-ON-PREMISES-TO-AWS`  
for `VPC (Requester)` choose `onpremVPC`  
for `VPC (Accepter)` choose `awsVPC`  
Scroll down and click `Create Peering Connection` 
![image](https://user-images.githubusercontent.com/89054489/233837342-528d59d2-4958-49b1-b7fe-0013a14bae80.png)

...then click `Actions` and then `Accept Request`  
Click `Accept Request`  
 ![image](https://user-images.githubusercontent.com/89054489/233837434-849f576d-e1db-4bff-8c2a-86c14b1e2b74.png)
![image](https://user-images.githubusercontent.com/89054489/233837460-fea83d00-2bec-4a5d-9199-bfc56e7bf183.png)


# STAGE 2B - Create Routes on the On-premises side
Move to the [route tabes console](https://console.aws.amazon.com/vpc/home?region=us-east-1#RouteTables:sort=routeTableId)  
Locate the `onpremPublicRT` route table and select it using the checkbox.  
![image](https://user-images.githubusercontent.com/89054489/233837711-9353c7a6-7b0f-43f4-9775-16b693bfee11.png)

Click on the `Routes` Tab.  
You're going to add a route pointing at the AWS side networking, using the VPC Peer.  
Click `Edit Routes`  
Click `Add Route`  
For Destination enter `10.16.0.0/16`  
Click the `Target` dropdown & click `Peering Connection` and select the `A4L-ON-PREMISES-TO-AWS` then click `Save Changes`  
The Onpremises network can now route to the AWS Network, but as data transfer requires bi-directional traffic flow, you need to do the same at the other side.
![image](https://user-images.githubusercontent.com/89054489/233837797-ffcba42c-83b5-4593-a337-a7001008e1f3.png)


# STAGE 2C - Create Routes on the AWS side
Move to the [route tabes console](https://console.aws.amazon.com/vpc/home?region=us-east-1#RouteTables:sort=routeTableId)
Locate the `awsPublicRT` route table and select it using the checkbox.  
Click on the `Routes` Tab.  
You're going to add a route pointing at the AWS side networking, using the VPC Peer.  
Click `Edit Routes`  
Click `Add Route`  
For Destination enter `192.168.10.0/24`  
Click the `Target` dropdown & click `Peering Connection` and select the `A4L-ON-PREMISES-TO-AWS` then click `Save Changes`  

![image](https://user-images.githubusercontent.com/89054489/233837866-71f57503-8ec3-45e0-b4bf-df120a6560db.png)
![image](https://user-images.githubusercontent.com/89054489/233837910-161f4edc-92b1-4d25-bbcd-f350997a5d08.png)

Move to the [route tabes console](https://console.aws.amazon.com/vpc/home?region=us-east-1#RouteTables:sort=routeTableId)  
Locate the `awsPrivateRT` route table and select it using the checkbox.  
Click on the `Routes` Tab.  
You're going to add a route pointing at the AWS side networking, using the VPC Peer.  
Click `Edit Routes`  
Click `Add Route`  
For Destination enter `192.168.10.0/24`  
Click the `Target` dropdown & click `Peering Connection` and select the `A4L-ON-PREMISES-TO-AWS` then click `Save Changes`  

![image](https://user-images.githubusercontent.com/89054489/233838021-5a673676-68c0-4b3a-9886-c9bbe874f282.png)
![image](https://user-images.githubusercontent.com/89054489/233838057-4a5458d5-f604-4cb5-9bd0-ca24e149b090.png)

# STAGE 2 - FINISH   

At this point you have created the peering connection between the VPCs and the gateway objects within each VPC.  
you have also configured routing from ONPremises -> AWS and vice-versa.  
In stage 3 you will use this architecture to begin a migration.  


## step 3

![image](https://user-images.githubusercontent.com/89054489/233838155-2bbd7662-6a2d-42cb-853b-8c8b1a4f7a1e.png)

### STAGE 3A - CREATE THE RDS INSTANCE
Move to the [RDS Console](https://console.aws.amazon.com/rds/home?region=us-east-1)
Click `Subnet Groups`
Click `Create DB Subnet Group`
For Name call it `A4LDBSNGROUP` enter the same for description in the VPC dropdown, choose `awsVPC`
Under availability zones, choose `us-east-1a` and `us-east-1b`
for subnets check the box next to 10.16.32.0/20 which is privateA and 10.16.96.0/20 which is privateB
Scroll down and click `Create`
Click on `Databases`
Click `create Database`
Choose `Standard Create`
Choose MariaDB Choose Free Tier for Templates

You will be using the same database names and credentials to keep things simple for this demo lesson, but note that in production this could be different.

for DB instance identifier enter `a4lwordpress`
for Master username choose ``a4lwordpress`
for Masterpassword enter the DBPassword parameter for cloudformation which you noted down in stage of this demo enter that same password in the Confirm password box
Scroll down to Connectivity
for Virtual private cloud (VPC) choose `awsVPC`
make sure Subnet Groups is set toe `a4ldbsngroup`
for public access choose No
for VPC security groups select Choose Existing and choose ***-awsSecurityGroupDB-*** (*** aren't important)
remove the Default security group by clicking the X
Scroll down and expand Additional configuration
Under Initial database name enter a4lwordpress
Scroll down and click `Create Database`

This will take some time.. and you cant continue to Stage4 until the database is in a ready state.

### STAGE 3B - CREATE THE EC2 INSTANCE
Move to the [EC2Console]( https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Home:)
Click `Instances`
Click `Launch Instances`
Enter awsCatWeb for the Name of the instance.
Clck Amazon Linux and ensure Amazon Linux 2 AMI (HVM) ...... SSD Volume Type is selected.
Ensuring the architecture is set to 64-bit (x86) below.
Choose the Free Tier eligible instance (should be t2.micro or t3.micro)
Scroll down and choose Proceed without key pair (not recommended) in the dropdown
Next to Network Settings click `Edit`
For VPC pick `awsVPC`
For Subnet pick `aws-PublicA`
Select Select an existing security group
Choose ***-awsSecurityGroupWeb-*** (*** aren't important)
Scroll down past Storage and expand Advanced Details (don't confuse this with Advanced Network Configuration in the current area)
for IAM Instance Profile pick ***-awsInstanceProfile-**** (*** aren't important)
Click `Launch Instance`
Click View All Instances

Wait for the awsCatWeb instance to be in a Running state with 2/2 checks before continuing.

### STAGE 3C - INSTALL WORDPRESS Requirements
Select the awsCatWeb instance, right click, Connect
Select Session Manager and click Connect
When connected type sudo bash to run a privileged bash shell then update the instance with a yum -y update and wait for it to complete.
Then install the apache web server with yum -y install httpd mariadb (the mariadb part is for the mysql tools) Then install php with amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2 
then make sure apache is running and set to run at startup with

systemctl enable httpd
systemctl start httpd
You now have a running apache web server with the ability to connect to the wordpress database (currently running onpremises)

STAGE 3D - MIGRATE WORDPRESS Content over
You're going to edit the SSH config on this machine to allow password authentication on a temporary basis.
You will use this to copy the wordpress data across to the awsCatWeb machine from the on-premises CatWeb Machine

run a nano /etc/ssh/sshd_config
locate PasswordAuthentication no and change to PasswordAuthentication yes , then ctrl+o to save and ctrl+x to exit.
then set a password on the ec2-user user
run a passwd ec2-user and enter the DBPassword you noted down at the start of the demo.
this is only temporary.. we're using the same password throughout the demo to make things easier and less prone to mistakes

restart SSHD to make those changes with service sshd restart or systemctl restart sshd

Return back to the EC2 console https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Instances:
with the awsCatWeb instance selected, note down its Private IPV4 Address you will need this in a moment.

Select the CatWeb instance, right click, Connect
Select Session Manager and click Connect
When connected type sudo bash to run a privileged bash shell

move to the webroot folder by typing cd /var/www/

run a scp -rp html ec2-user@privateIPofawsCatWeb:/home/ec2-user and answer yes to the authenticity warning.
this will copy the wordpress local files from CatWeb (on-premises) to awsCatWeb (aws)

now move back to the awsCatWeb server, if you dont have it open still, reconnect as per below

Select the awsCatWeb instance, right click, Connect
Select Session Manager and click Connect
When connected type sudo bash to run a privileged bash shell

move to the ec2-user home folder by doing a cd /home/ec2-user
then do an ls -la and you should see the html folder you just copied.
cd html
next copy all of these files into the webroot of awsCatWeb by doing a cp * -R /var/www/html/

STAGE 3E - Fix Up Permissions & verify awsCatWeb works
run the following commands to enforce the correct permissions on the files you've just copied across

usermod -a -G apache ec2-user   
chown -R ec2-user:apache /var/www
chmod 2775 /var/www
find /var/www -type d -exec chmod 2775 {} \;
find /var/www -type f -exec chmod 0664 {} \;
sudo systemctl restart httpd
Move to the EC2 running instances console https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Instances:
Select the awsCatWeb instance
copy down its public IPv4 DNS into your clipboard and open it in a new tab
if working, this Web Instance (aws) is now loading using the on-premises database.

### STAGE 3 - FINISH
At this point you have a functional AWS based wordpress application instance.
You have migrated content from the on-premises virtual machine (simulated) using SCP.
And you have tested that its connects to the on-premises DB. In the next stage you will migrate the on-premises DB to AWS using DMS. before you continue, make sure the a4lwordpress RDS DB is in an Available state https://console.aws.amazon.com/rds/home?region=us-east-1#databases:


