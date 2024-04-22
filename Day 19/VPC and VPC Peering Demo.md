![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/58724f06-dd82-4032-af64-cf32064cb445)VPC :

VPC Creation Steps :
------------------

1. VPC Creation
 
2. Internet Gateway Creation & associating it with VPC

3. Creating Public, Private, and Database Subnets in 2 AZs for HA

10.0.1.0/24 --> Flipkart-public-1a
10.0.2.0/24 --> FlipKart-public-1b

10.0.11.0/24 --> Flipkart-private-1a
10.0.12.0/24 --> FlipKart-private-1b

10.0.21.0/24 --> FlipKart-database-1a
10.0.22.0/24 --> FlipKart-database-1b


4. Create Route tables and attach them to subnets


Interview Question: Public subnet vs private subnet?
- A subnet which is connected to the internet is called a public subnet
- A subnet that is not connected to the internet is called a private subnet

5. Creating a Security Group for the instance and its rules

6. Create EC2 and a new key pair for it.


NAT Gateway :
------------
NAT Gateway is a Network Address Translation (NAT) service. You can use a NAT gateway so that instances in a private subnet can connect to services outside your VPC but external services cannot initiate a connection with those instances.


- It should have one public IP
- It should have one elastic IP(static IP)

NAT Gateway is used to enable outgoing internet connections for the servers in the private subnet.

it should have a 





![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/e9d1a57f-68d0-419d-bc01-126eb6248a60)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/4d3645f9-4d37-467a-a7f0-ca20d092cf21)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/194e3be3-f44c-4227-bd5e-77a0e8d8c257)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/1d98be63-10f0-469e-9882-e8f418c6ec19)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/2cc52843-9c9f-46a5-a7be-3072290bde36)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/ee05e6f1-34eb-44b8-a3c3-9276a1746330)


Under VPC Dashboard, we have internet gateways

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/296d3acf-5939-4e3f-8788-f48132ac8d92)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/34b9e735-9720-49f0-ae91-1434227ffc33)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/5afc6a3e-6a52-4ef2-8b63-9fb30b2f62d0)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/12caa22a-ff2c-429b-b6b9-4d51ec27827c)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/bf75cf8c-8d3d-4f12-83e7-24f8cc747b4f)

### 3. Creating Public , private and database subnets

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/76305518-f5d9-4636-8147-06e0fc3a3926)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/b4480025-5fa9-4e6b-a35e-306244eda7f4)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/41b61854-036a-4b73-87cc-57c8c7789094)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/3fdc5c5a-327d-47a0-91f0-b7fa0b932553)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/65f50024-dcf1-4d20-a622-ebba60a970d6)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/e957663f-9710-49f8-b53f-5c937360353f)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/e900cfaf-3adf-47d0-a3f7-f30f17dafc46)

### 4. Route Table Creation
![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/19884f2d-e1fc-4815-847f-0f2b84e9e47d)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/ebcea0b7-e30f-4b1d-9724-9761cb0d5ffd)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/d45982f9-3c0a-4c65-bcb6-afdc2c0b5dd1)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/8caf3d8f-2e84-4901-9538-aa8c5ea50691)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/ec776293-f5b6-4b37-ab7b-589f98a2e6e7)

Association of Route tables with respective subnets

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/84ef5799-b26f-4562-b7b2-12c5394e6fc0)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/4262f76e-c352-4a51-8124-b690b2715a01)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/0d41c2c4-d328-4ddc-ac2f-a407b3415a88)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/8394962a-8b10-4968-aa5e-9e8c4656733a)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/6653406a-73ca-40a7-925b-37f81c2c2268)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/2267eb2a-d478-4d38-bac0-42ecc85f612a)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/a81d83c9-be91-44e4-a0ab-65699fd4daaf)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/e33529be-00b1-4f3c-8003-06a8a16b97d3)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/00b89e0e-b669-4236-bec1-83264c24ae83)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/dc9d2dfd-d0fd-47d8-bb88-3dd79ebd08b6)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/11f93489-96a6-437a-a65c-85b479da34eb)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/f8da4d3f-7b8c-47d4-b191-f59f9af0e774)

# outbound

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/65cf0c44-a9b8-49da-98ad-d0cee5653054)

finally click on create security group
![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/d36cee9b-3f7d-41d9-8ace-27915b68a8b5)


## Launch EC2 instance

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/15118607-3f75-4f81-807f-7c2b3e8ad31e)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/98931de7-85c3-4ab2-91bd-c4f4212042de)


![keypair-creation](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/66ff43a3-43d2-46b6-8485-179b4a491eda)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/c0f9255b-984e-404a-a662-4b302ec5c48f)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/20521d38-660f-461c-8571-66ad6043a6ba)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/80159cf6-53f4-4f4a-b1bf-bdbbbce5c88d)


NAT Gateway 
----------

NAT Gateway is a Network Address Translation (NAT) service. You can use NAT gateway so that instances in a private subnet can connect to services outside your VPC but external services cannot initiate a connection with those instances.


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/20233e73-e1cb-40cd-a801-8dcd5d9f03f5)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/c87386e3-0075-494a-a201-634fdcb9c968)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/5f7a66da-e3e1-4a28-a59e-5d29fc995001)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/99b75b8a-f1af-468a-bb79-0c054232b980)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/39e5b8c8-1973-47b6-96d4-8e05c72bd2a1)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/5a24c929-57d7-49a9-a065-97c55569393f)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/849e5d49-19b1-4aa3-984e-2921c868f020)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/59238902-53b0-4b8a-a2f7-f70c1e560f41)

copy the flipkart.pem file that you have downloaded earlier into your public ec2-server 

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/011d77bc-4589-4aa0-8ef7-b09bfde7e4bc)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/47690b17-2586-410c-bcd4-47c2486fefe1)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/ba70c8ec-70bf-4389-bf68-31192757f7ad)


We are not able to install any packages in these server, To install any package we need NAT Gateway.

Create Elastic IP :
------------------

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/6ceb72ce-9164-40fa-9806-63bb1208912e)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/0f6dbd53-57f2-4444-b31f-9a63f233aba3)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/26fed8ec-eb75-4c84-a552-80c9c7b1fc90)



![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/a3fd19a1-4769-45af-ab20-b01635d47357)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/3391a206-682c-4ccd-bc71-a71b71c51c49)

Attach NAT Gateway to both Private and database route tables


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/4f502ed4-7c02-4869-967d-33250d10cfba)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/735ca8f1-9ca1-4ce0-8f03-731f3e83f0c8)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/4129829d-bf86-4598-bbf8-7212e17be39d)


![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/e5fcea0e-388b-4f2d-bb70-795d28376357)

![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/1ca8728b-f531-40b0-89a5-78ac301d870d)

