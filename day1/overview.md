

  Web applications needs to scale continuously in response to the number of users on the platform and to be available in a highly available manner.
  
  In being highly available, an application needs to be able to operate in multiple data centers and continue to function as components, servers, or even data centers fail
  
  In these project, we are going to deploy a wordpress applicaiton in such a way that the application server, database, and file server can scale independently of one another.
  
  We will also deploy the application's components into two availability zones to distribute it and guard against failure of any one availability zone. The wordpress application will be deployed in a stateless fashion so that we can add or remove web application servers in response to the requests flowing into the system.
  
  Now, let's look at the aws services that we are going to use for this project.👇
  
  First, we will create a virtual network spread across multiple availability zones in our region of choice.
  
  we will then deploy a highly available relational database across those availability zones using Amazon RDS. with your database deployed the next step will be to create a database caching layer using Amazon Elasticache.  This will provide us with a cache around your database for frequently run queries, improving HTTP response time performance and reducing strain on your RDBMS.
  
  with the **datatier** created we will then begin to create the **application tier** 
  
  We will provision a shared storage layer powered by NFS. using Amazon EFS. We will create an NFS cluster across multiple availability zones. Then we will create a loadbalanced group of web servers that will automatically scale in response to load  to complete your application tier.
  
  TO finish this project successfully please follow below steps in order after going through **prerequisites.md**
  
  1. Configuring the network
  
  **Build the HA Data Tier**
  
  2. set up RDS database
  3. set up Elasticache for memcached
  4. Create the shared file system

**Build the application tier**

  5. create the load balancer
  6. create a launch template
  7. create the app-server
  8. Adding caching
  
  **Summary :**
  
