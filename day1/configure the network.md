First let's login to the ![VPC](www.aws.com/vpc/home).

![image](https://user-images.githubusercontent.com/89054489/229305748-556ea637-37bc-4c6a-8927-a6b8299e69b8.png)

![image](https://user-images.githubusercontent.com/89054489/229305800-a538b757-06fb-492f-af50-b5db8ac2369d.png)

**Create a new virtual private cloud (VPC) **

To do this click on Your VPCs on the left hand side of the console and click Create VPC. Enter a name for your VPC and a CIDR range such as the one below. When you're fiinished click Create.

![image](https://user-images.githubusercontent.com/89054489/229306150-2e534814-3ecc-490e-ac8b-084b11b50701.png)

![image](https://user-images.githubusercontent.com/89054489/229306291-e656cc88-499b-4b3a-8343-5f4721895874.png)

![image](https://user-images.githubusercontent.com/89054489/229306403-b0d9ac77-6b03-44ce-ad63-02f910255a9d.png)

### create public and private subnets in the new VPC

- once the vpc has been created, the next step is to create the subnets that will be used to host the application across two availability zones. We are going to create six subnets in total. Three for each AZ. AS shown beloww
- 
