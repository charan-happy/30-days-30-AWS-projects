![image](https://github.com/charan-happy/30-days-30-AWS-projects/assets/89054489/e0a182fc-b0c4-4822-a348-88b14fe513ce)

Scenario :

In some companies, there is no need to run their EC2 instances 24/7; they require instances to operate during specific time periods, such as company working hours, from 8:00 AM in the morning to 5:00 PM in the evening. To address this scenario, I will implement two Lambda functions responsible for starting and stopping instances. These Lambda functions will be triggered by two CloudWatch Events in the morning and evening. This solution is fully serverless.
