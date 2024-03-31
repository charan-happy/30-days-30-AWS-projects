# Setting up 3-Tier Architecture in AWs :
-------------------------------------

what is 3-tier Architecture ?

- A 3-tier architecture is a software design pattern that divides an application into three logical tiers: presentation, application, and data. The presentation tier handles the user interface and presentation logic, the application tier handles the business logic, and the data tier handles the data storage and retrieval. 

Benefits of 3-tier Architecture :

**Improved scalability:** Each tier can be scaled independently, making it easier to meet changing demands.<br>
**Increased security:** The separation of tiers reduces the risk of security breaches.<br>
**Easier maintenance:** Each tier can be maintained independently, making it easier to update and fix bugs.

Ex : Web applications
Enterprise applications
Mobile applications

**Presentation Tier:** This tier handles user interaction. It delivers the user interface (UI) and captures user input. Web servers, static content delivery networks (CDNs), and API gateways are common components.<br>
**Application Tier:** This tier handles the application logic. It processes user requests, interacts with the data tier, and generates responses. Application servers, container orchestration services, and serverless functions reside here.<br>
**Data Tier:** This tier stores and manages application data. Relational databases, NoSQL databases, and object storage solutions like Amazon S3 belong to this tier.


##  Building for cloud : why architecture matters ?

- When crafting a cloud-based application, the foundation you build upon — its architecture — is just as crucial as the application itself. Choosing the right architecture involves several key considerations :

    - **scalability :** Can your application seamlessly scale up or down based on user traffic ? How important is to avoid constant resource management and monitoring ?

    - **High-Availability** : Does your app require near- constant uptime? Can it tolerate extended periods of downtime? If a component fails, how resilient is the rest of the system?

    - **Security** : How robust are your app's security measures ? How does it handle access control for different functionalities ? if a breach occurs in one area, can the rest of the application be compromised ?


## Let's build network for our project :

**Setting up foundational layer: VPC**

- Let's imagine that we are renting an aparment in a big building (public cloud). A vpc is like a our room in that building . we can control who has access (security group) and how things are arranged (subnets). This private room of you ensures that your belongings (app data) are separate from other tenants (other cloud users). It's secure place to build your applications (3-tier architecture) without worrying about neighbours.

