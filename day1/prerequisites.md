# pre-requisites

### create/use own account

1. you can use your own AWS account or ![sign-up](www.aws.com)<br>
2. Ensure you are following the remaining project steps as an IAM user with administrator access to the AWS account.<br>
3. Follow these steps :
  - Enter a user name
  - Enable programmatic and console access
  - Create a custom password
  - Uncheck the require password reset
  - click on Next: permissions

NOTE :
 You might not have to enter your account ID or alias if you've previously signed in as the IAM user with your current browser. Your browser might remember this information.


![image](https://user-images.githubusercontent.com/89054489/229304620-f8799b7e-1003-456c-a085-7e292d52a033.png)

![image](https://user-images.githubusercontent.com/89054489/229304773-69b28d3d-6059-4707-98dd-7e8d8c0d799c.png)

![image](https://user-images.githubusercontent.com/89054489/229304864-b2c51aac-baed-4a4a-ad10-8e0ea21b7699.png)

- Choose Attach existing policies directly
- Tick box next to **AdministratorAccess** for the IAM policy to be attached to the user
- click on `Next: Tags`

![image](https://user-images.githubusercontent.com/89054489/229305015-125052fc-c4cf-4548-9942-c2fa2b01333c.png)

- Leave evverything as default. Click `Next: Review`
- Review the choice taken and then click on `Create User`
- Take note of the login URL and save
- Download the credentials for the new IAM user created.

![image](https://user-images.githubusercontent.com/89054489/229305122-920297a2-b0bd-4969-90ba-258f1e6220a9.png)

![image](https://user-images.githubusercontent.com/89054489/229305158-13f1132e-81e1-4fb9-b2fd-0b74f63cb54e.png)

![image](https://user-images.githubusercontent.com/89054489/229305250-21427c5f-e764-416b-9204-e47b8bb29c3f.png)

Now we have successfully created IAM user

Pre-requisites

- The wordpress deployment will be created in an AWS Virtual private cloud (VPC) which creates a virtual software-defined network across AWS availability zones (AZs).

- An availability zone represents one or more physical data centers which are fault isolated from one another, providing you with a way to create resilient, fault-tolerant applications and architectures.

- As a first step of this project , we are going to create our own VPC in our AWS account and use the subnets and security groups we create to provision and protect your web application.

- To do it let's visit ![AWS VPC Web Console](https://console.aws.amazon.com/vpc/home) and create our first VPC.
