
# Deploying an E-Commerce three tier application on AWS EKS

- We will use a demo e-commerce project that sells Robots and AI products. This demo project is created using 12 components that includes 8 micro services, 2 Databases, 1 messaging queue and 1 In memory data store.

![Architecture](./images/image%20copy.png)

Note: All microservices should be in single programming language or multiple programming languages

![](./images/image.png)

|Monolithic Architecture|Microservices Architecture|
|---|---|
|A monolithic architecture is a singular, large computing network with one code base that couples all of the business concerns together.|A microservices architecture, also simply known as microservices, is an architectural method that relies on a series of independently deployable services. These services have their own business logic and database with a specific goal. Updating, testing, deployment, and scaling occur within each service|
|To make a change to this sort of application requires updating the entire stack by accessing the code base and building and deploying an updated version of the service-side interface.|Microservices decouple major business, domain-specific concerns into separate, independent code bases|
|This makes updates restrictive and time-consuming.|Microservices don’t reduce complexity, but they make any complexity visible and more manageable by separating tasks into smaller processes that function independently of each other and contribute to the overall whole|
|Monoliths can be convenient early on in a project's life for ease of code management, cognitive overhead, and deployment. This allows everything in the monolith to be released at once.|Adopting microservices often goes hand in hand with DevOps, since they are the basis for continuous delivery practices that allow teams to adapt quickly to user requirements|
|Advantages: <br>- Easy deployment <br>- easy Development <br>-performance <br>- simplified testing <br>- easy debugging |Advantages: <br>- Agility <br> - flexible scaling <br>- continuous deployment <br>- highly maintainable and testable <br>- Independently deployable <br>-Technology flexiblity <br>- High reliability <br>- Happier teams|
|Disadvantages: <br>- slower development speed <br>- scalability <br>- reliability <br>- Barrier to technology adoption <br>- lack of flexibility <br>- deployment|Disadvantages: <br>- Development sprawl <br>- Exponential infrastructure costs <br>- added organization overhead <br>- debugging challenge <br>- lack of standardization <br>- lack of clear ownership |
|![monolithic](./images/monolithic.png)|![Microservices](./images/Microservices.png)|


For complete project [visit here](https://github.com/charan-happy/robot-shop)

