# Introduction to Amazon S3

In these project, we are going to know how to :

Create a bucket in Amazon S3
Add an object to a bucket
Manage access permissions on an object and a bucket
Create a bucket policy
Use bucket versioning

**Task 1: Creating a bucket**
You are new to Amazon S3 and want to test the features and security of Amazon S3 as you configure the environment to hold the Amazon Elastic Compute Cloud (Amazon EC2) report data. You know that every object in Amazon S3 is stored in a bucket, so creating a new bucket to hold the reports is the first thing on your task list. 

In this task, you create a bucket to hold your Amazon EC2 report data and then examine the different bucket configuration options.

At the upper left of the AWS Management Console, on the Services menu, choose S3.
Choose Create bucket
 Bucket names must be 3–63 characters long and consist of only lowercase letters, numbers, or hyphens. The bucket name must be globally unique across all of Amazon S3 regardless of account or Region, and you cannot change a bucket name after creating the bucket. As you enter a bucket name, a help box displays showing any violations of the naming rules. Refer to the Amazon S3 bucket naming rules in the Additional resources section at the end of the lab for more information.

In the General configuration section, enter the following as the Bucket name: reportbucket(NUMBER)
In the bucket name, replace (NUMBER) with a random number so that your bucket has a unique name.

Example bucket name: reportbucket987987
Leave Region at its default value. 

By selecting a particular Region, you can optimize latency, minimize costs, or address regulatory requirements. Objects stored in a Region never leave that Region unless you explicitly transfer them to another Region.

Choose Create bucket

![image](https://user-images.githubusercontent.com/89054489/232216379-08e032ee-74dd-4f50-b9da-92887dbfcc59.png)
![image](https://user-images.githubusercontent.com/89054489/232217093-34333ea2-1a53-402d-8647-6bd887736270.png)
![image](https://user-images.githubusercontent.com/89054489/232218545-73702a98-526d-4fe4-abf2-aeaa4b3bbb14.png)


**Task 2: Uploading an object to the bucket**
Now that you have created a bucket for your report data, you are ready to work with objects. An object can be any kind of file: a text file, a photo, a video, a .zip file, and so on. When you add an object to Amazon S3, you have the option to include metadata with the object and set permissions to control access to the object.

In this task, you test uploading objects to your reportbucket. You have a screen capture of a daily report and want to upload this image to your S3 bucket.

Right-click the following link: new-report.png. Choose Save link as, and save the file to your desktop.
In the S3 Management Console, find and select the bucket name that starts with reportbucket.
Choose Upload
This step launches an upload wizard. Use this wizard to upload files either by selecting them from a file chooser or by dragging them to the Amazon S3 window.

Choose Add files
Browse to and select the new-report.png file that you downloaded previously.
At the bottom of the page, choose Upload
Your file is successfully uploaded when the green bar indicating Upload succeeded appears.

In the Upload: status section in the upper right, choose Close

![image](https://user-images.githubusercontent.com/89054489/232222798-faaa641f-c5a8-4c95-988d-b6e84c09c94f.png)
![image](https://user-images.githubusercontent.com/89054489/232222635-c8dd6d73-d05b-4557-b265-57fc48c2c745.png)

![image](https://user-images.githubusercontent.com/89054489/232222894-6bbaa1b1-620b-4fc4-9d83-5a40869f30bf.png)
![image](https://user-images.githubusercontent.com/89054489/232222957-56baf536-d8de-4765-9fbd-06ff1c9649db.png)



**Task 3: Making an object public**
Security is a priority in Amazon S3. Before you configure your EC2 instance to connect to the reportbucket, you want to test the bucket and object settings for security.

In this task, you configure permissions on your bucket and your object to test accessibility.

First, you attempt to access the object to confirm that it is private by default.

In the reportbucket overview page, on the Objects tab, locate the new-report.png object, and choose the new-report.png file name.
The new-report.png overview page opens. The navigation in the upper left updates with a link to return to the bucket overview page.

In the Object overview section, locate and copy the Object URL link.
The link should look similar to the following: https://reportbucket987987.s3-us-west-2.amazonaws.com/new-report.png

Open a new browser tab and paste the object URL link into the address field, and then press Enter.
You receive an Access Denied error because objects in Amazon S3 are private by default.

Now that you've confirmed that the default security of Amazon S3 is private, you test how to make the object publicly accessible.

Keep the browser with the Access Denied error open, and return to the web browser tab with the S3 Management Console.
You should still be on the new-report.png Object overview tab.
In the upper right, choose the Object actions dropdown menu, you will notice that Make public via ACL is greyed out.
In the upper left of the page, choose the reportbucket name in the navigation to go back to the main reportbucket overview page.
Choose the Permissions tab.
We need to allow the use of ACLs first. Under Object Ownership choose Edit.
Choose ACLs enabled.
Choose Bucket owner preferred.
Choose the  check box next to I acknowledge that ACLs will be restored.
Choose Save Changes
Under Block public access (bucket settings), choose Edit to change the settings.
Clear the check box for the Block all public access option, and then leave all other options cleared.
 Notice that all of the individual options remain cleared. When clearing the option for all public access, you must then select the individual options that apply to your situation and security objectives. You use access control lists (ACLs) and bucket policies later in the lab, so these options remain cleared in this task. In a production environment, it is recommended to use the least permissive settings possible. Refer to the Amazon S3 block public access link in the Additional resources section at the end of the lab for more information.

Choose Save changes
A dialogue box opens asking you to confirm your changes. Enter confirm in the field, and then choose Confirm
A message that says Successfully edited Block Public Access settings for this bucket. displays at the top of the window.

Choose the Objects tab.
Choose the new-report.png file name.
At the upper right on the new-report.png overview page, choose the Object actions dropdown menu, and select Make public.
 Notice the warning: When public read access is enabled and not blocked by Block Public Access settings, anyone in the world can access the specified objects. This warning reminds you that if you make the object public, then everyone in the world will be able to read the object. 

Choose Make public and you should see the green banner Successfully edited public access at the top of the window.
In the upper right, choose Close to return to the new-report.png object overview.
Return to the browser tab that displayed Access Denied for the new-report.png object, and refresh the page.
The new-report.png object now displays properly because it is publicly accessible.

Close the web browser tab that displays your new-report.png image, and return to the tab with the Amazon S3 Management Console.
In this example, you granted read access to just one specific object. If you would like to grant access to the entire bucket, you need to use a bucket policy, which this lab covers later.

In the next task, you work with your EC2 instance to confirm connectivity to the S3 bucket.


![image](https://user-images.githubusercontent.com/89054489/232223720-5c63e347-33d4-465a-8994-0ea9e81596c0.png)
![image](https://user-images.githubusercontent.com/89054489/232223951-d6318ed0-9e34-4c6c-be70-8ccbc6f3ad06.png)
![image](https://user-images.githubusercontent.com/89054489/232224072-b81cb65b-52ce-4968-90d1-f946d1b7bdff.png)

![image](https://user-images.githubusercontent.com/89054489/232232431-7a4f1284-2a43-49d5-a786-f063495cac6b.png)

![image](https://user-images.githubusercontent.com/89054489/232232310-8b82e65f-3824-4483-94dc-b823db944d1b.png)
![image](https://user-images.githubusercontent.com/89054489/232232342-6812ccc6-911d-49a4-a4af-4eec1372f0bb.png)
![image](https://user-images.githubusercontent.com/89054489/232232703-413d64c3-7c27-4010-ace2-d2f68fbb68dc.png)
![image](https://user-images.githubusercontent.com/89054489/232232723-76bde136-9d17-4a47-a0e6-5e189567b1ee.png)
![image](https://user-images.githubusercontent.com/89054489/232232747-21f41b9d-344d-4b67-b1d6-6d4c11779e0d.png)
![image](https://user-images.githubusercontent.com/89054489/232232780-41778cbb-a915-4183-ad63-c41f0b13bdb6.png)



**Task 4: Testing connectivity from the EC2 instance**
In this task, you connect to your EC2 instance to test connectivity and security to the Amazon S3 reportbucket.

You should already be signed in to the AWS Management Console. If not, follow the steps in the Start Lab section to sign in to the AWS Management Console.

On the Services menu, choose EC2.
On the EC2 Dashboard, under the Resources section, choose Instances (running).
Select the  check box for Bastion Host and choose Connect
In the Connect to instance window, select the Session Manager tab for the connection method.
 With AWS Systems Manager Session Manager, you can connect to the bastion host instance without the need for specific ports to be open on your firewall or Amazon Virtual Private Cloud (Amazon VPC) security group. Refer to AWS Systems Manager Session Manager in the Additional resources section at the end of this lab for more information.

Choose Connect
A new browser tab or window opens with a connection to the bastion host instance.

You are now connected to the EC2 instance that holds the reporting application. Because Session Manager uses HTTPS port 443, it does not require you to open SSH port 22 to the outside world. You are satisfied with this security feature. Now you want to see how EC2 interacts with your S3 bucket.

In the bastion host session, enter the following command to change to the home directory (/home/ssm-user/):
cd ~
 The output returns you to the command prompt.

Enter the following command to verify that you are in the home directory:
pwd
The output should be as follows:

/home/ssm-user
You are now in the ssm-user's home directory where you will run all of the commands in this lab.

Enter the following command to list all of your S3 buckets. 
aws s3 ls
  The output should look similar to the following:

2020-11-11 22:34:46 reportbucket987987
You see the reportbucket you created and lab auto-generated buckets.

Note: During the creation of the lab environment, both an instance profile (which defines who you are for authentication) and a role (which defines what you can do after you authenticate) have been automatically added for the EC2 instance to allow the EC2 instance to list the S3 buckets and objects.

In the following command, change (NUMBER) at the end of the reportbucket name to the name of the bucket you created. Enter your adjusted command to list all the objects in your reportbucket. 
aws s3 ls s3://reportbucket(NUMBER)
The command looks similar to the following: aws s3 ls s3://reportbucket987987

The output should look like the following:

2020-11-11 15:46:34      86065 new-report.png
There is currently only one object in your bucket. The object is called new-report.png.

Enter the following command to change directories into the reports directory.
cd reports
The output returns you to the command prompt.

Enter the following command to list the contents of the directory.
ls
The output shows some files created in your reports directory to test the application.

dolphins.jpg files.zip report-test.txt  report-test1.txt report-test2.txt report-test3.txt  whale.jpg
In the following command, change (NUMBER) at the end of the reportbucket name to the name of the bucket you created. Enter your adjusted command to see if you can copy a file to the S3 bucket.
aws s3 cp report-test1.txt s3://reportbucket(NUMBER)
The command looks similar to this: aws s3 cp report-test1.txt s3://reportbucket987987

The output indicates an upload failed error. This error occurs because you have read-only rights to the bucket and do not have the permissions to perform the PutObject action.

Leave this window open. and go back to browser tab with the AWS console.
In the next task, you create a bucket policy to add the PutObject permission.

![image](https://user-images.githubusercontent.com/89054489/232232900-b75913e9-18cc-4388-b65c-053ed3ca079b.png)
![image](https://user-images.githubusercontent.com/89054489/232232980-b9e6bae6-6e41-43c4-91f1-8e96bf74ebcf.png)
![image](https://user-images.githubusercontent.com/89054489/232233262-d61f148e-8cc1-49b5-b8a6-b1f8d8ab986c.png)


**Task 5: Creating a bucket policy**
A bucket policy is a set of permissions associated with an S3 bucket. It is used to control access to an entire bucket or to specific directories within a bucket. 

In this task, you use the AWS Policy Generator to create a bucket policy to enable read and write access from the EC2 instance to the bucket so that your reporting application can successfully write to Amazon S3.

Right-click the following link: sample-file.txt. Choose Save link as, and save the file to your desktop.
Return to the AWS Management Console, go to the Services menu, and select S3.
In the S3 Management Console tab, select the name of your bucket.
To upload the sample-file.txt file, choose Upload and use the same upload process that you used in task 2.
On the reportbucket overview page, choose the sample-file.txt file name. The sample-file.txt overview page opens.
Under the Object overview section, locate and copy the Object URL link.
In a new browser tab, paste the link into the address field, and then press Enter.
Once again, your browser displays an Access Denied message. You need to configure a bucket policy to grant access to all objects in the bucket without having to specify permissions on each object individually.

Keep this browser tab open, but return to the tab with the S3 Management Console.
Select Services and select IAM. In the left navigation, choose Roles.
In the Search field, enter EC2InstanceProfileRole
This is the role that the EC2 instance uses to connect to Amazon S3.

Select EC2InstanceProfileRole. In the Summary section, copy the Role ARN to a text file to use in a later step.
It should look similar to the following: arn:aws:iam::596123517671:role/EC2InstanceProfileRole

Choose Services and S3, and return to the S3 Management Console.
Choose the reportbucket.
You should see the two objects you uploaded. If not, navigate back to your bucket so that you see the list of objects you have uploaded.

Choose the Permissions tab.
In the Permissions tab, scroll to the Bucket policy section, and choose Edit
A blank Bucket policy editor displays. You can create bucket policies manually, or you can create them with the assistance of the AWS Policy Generator.

 Amazon Resource Names (ARNs) uniquely identify AWS resources across all of AWS. A colon (:) separates each section of the ARN, and each section represents a specific piece of the path to the specified resource. The sections can vary slightly depending on the service being referenced but generally follow the format:

arn:partition:service:region:account-id:resource

Amazon S3 does not require Region or account-id parameters in ARNs, so those sections are left blank. However, the colon (:) to separate the sections is still used, so it looks similar to arn:aws:s3:::reportbucket987987

Refer to the Amazon Resource Names (ARNs) and AWS Service Namespaces documentation link in the Additional resources section at the end of the lab for more information.

Below the Policy examples and Policy generator buttons, find the Bucket ARN. Copy the Bucket ARN to a text file to use in a later step. 
It looks like the following:

Bucket ARN
arn:aws:s3:::reportbucket987987
Choose Policy generator
A new web browser tab opens with the AWS Policy Generator.

 AWS policies use the JSON format and are used to configure granular permissions for AWS services. You can manually write the policy in JSON, or you can use the AWS Policy Generator to create the policy with a user-friendly web interface.

In the AWS Policy Generator window, configure the following options:

For Select Type of Policy, select S3 Bucket Policy.
For Effect, select Allow.
For Principal, paste the EC2 Role ARN that you copied to a text file in a previous step.
For AWS Service, keep the default setting of Amazon S3.
For Actions, select GetObject and PutObject.
 The GetObject action grants permission for objects to be retrieved from Amazon S3. Refer to the Additional resources section at the end of the lab for links to more information about the actions available for use in Amazon S3 policies.

For Amazon Resource Name (ARN), enter *
Choose Add Statement. The details of the statement you configured are added to a table below the button. You can add multiple statements to a policy.
Choose Generate Policy.
A new window displays the generated policy in JSON format. It should look similar to the following:

{
    "Version": "2012-10-17",
    "Id": "Policy1604361694227",
    "Statement": [
        {
            "Sid": "Stmt1604361692117",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::416159072693:role/EC2InstanceProfileRole"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "*"
        }
    ]
}
 

Copy the policy that you created to your clipboard.
Close the web browser tab, and return to the S3 Management Console tab with the Bucket policy editor.
Paste the bucket policy that you created into the Bucket policy editor.
In the Bucket policy editor, update the Resource value replacing * with the Bucket ARN you saved earlier followed by /*:
The updated Resource line in the lab policy should be similar to the following example:

"Resource": "arn:aws:s3:::reportbucket987987/*"
   Confirm that /* appears after your bucket name as the Resource line in this sample shows.

Choose Save changes.
Return to the AWS Systems Manager (Systems Manager) window. If your session has timed out, reconnect to Systems Manager using the previous steps in the lab.
Enter the following command to verify that you are in the /home/ssm-user/reports directory.
pwd
The output should be as follows:

/home/ssm-user/reports
In the command below, replace (NUMBER) with the number you used to create your bucket. Enter your adjusted command to list all objects in your reportbucket. 
aws s3 ls s3://reportbucket(NUMBER)
The command should look similar to the following: aws s3 ls s3://reportbucket987987

 The output should look similar to the following:

sh-4.2$ aws s3 ls s3://reportbucket987987
2020-11-02 23:20:27      86065 new-report.png
2020-11-02 23:57:03         90 sample-file.txt
Enter the following command to list the contents of the reports directory.
ls
The output returns a list of files.

In the command below, replace (NUMBER) with the number you used to create your bucket. Enter your adjusted command to try copying the report-test1.txt file to the S3 bucket.
aws s3 cp report-test1.txt s3://reportbucket(NUMBER)
The command should look like the following: aws s3 cp report-test1.txt s3://reportbucket987987

The output returns the following:

upload: ./report-test1.txt to s3://reportbucket987987/report-test1.txt
In the command below, replace (NUMBER) with the number you used to create your bucket. Enter your adjusted command to see if the file successfully uploaded to Amazon S3.
aws s3 ls s3://reportbucket(NUMBER)
 The output should look similar to the following:

2020-11-11 18:20:23      86065 new-report.png
2020-11-11 18:32:18         31 report-test1.txt
2020-11-11 18:20:22         90 sample-file.txt
You have successfully uploaded (PutObject) a file from the EC2 instance to your S3 bucket.

In the command below, replace (NUMBER) with the number you used to create your bucket. Enter your adjusted command to retrieve (GetObject) a file from Amazon S3 to the EC2 instance.
aws s3 cp s3://reportbucket(NUMBER)/sample-file.txt sample-file.txt
 The output should look similar to the following:

download: s3://reportbucket987987/sample-file.txt to ./sample-file.txt
Enter the following command to see if the file is now in the /reports directory.
ls
 The output should look similar to the following:

dolphins.jpg  files.zip  report-test1.txt  report-test2.txt  report-test3.txt  sample-file.txt
You now see the sample-file.txt in your file list. Congratulations! You have successfully uploaded and retrieved a file from Amazon EC2 to the S3 bucket.

Return to the browser tab that displayed the Access Denied error for the sample-file.txt, and refresh  the page.
The page still displays an error message because the bucket policy gave rights to only the principal called EC2InstanceProfileRole.  

Go to the AWS Policy Generator, and add another statement to the bucket policy allowing everyone (*) read access (GetObject). Take a moment to  generate this policy. This policy allows the EC2InstanceProfileRole to have access to the bucket while giving everyone access to read the objects via the browser.
Below is an expample of the above:

        {
            "Sid": "Stmt1604428842806",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::reportbucket987987/*"
        }
To test if your policy works, go to your browser with the Access Denied error and refresh it. If you can read the text, then congratulations! Your policy was successful. 
If not, look at the following policy for help. The modified policy should look like the following policy. Notice that there are two statements: one with the EC2InstanceProfileRole and one where the principal is "*" for everyone.

If you had trouble generating the policy on your own, you can copy the policy below and paste it into the BucketPolicy Editor. Remember to replace the existing EC2InstanceProfileRole ARN in the policy below with the EC2InstanceProfileRole ARN you copied in a previous step. Ensure that you replace the reportbucket example ARN with the bucket you created and the /* appears at the end of the Bucket ARN. See the last line of the policy as an example.

{
    "Version": "2012-10-17",
    "Id": "Policy1604428844058",
    "Statement": [
        {
            "Sid": "Stmt1604428821481",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::285058481724:role/EC2InstanceProfileRole"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::reportbucket987987/*"
        },
        {
            "Sid": "Stmt1604428842806",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::reportbucket987987/*"
        }
    ]
}
Leave the tab open with the sample-file.txt displayed. You return to this tab in the next task.
In this task, you created a bucket policy to allow specific access rights to your bucket. In the next section, you explore how to keep copies of files to prevent against accidental deletion.

![image](https://user-images.githubusercontent.com/89054489/232233473-e2c36587-0fd7-40a5-a61c-05623a2fcdd1.png)
![image](https://user-images.githubusercontent.com/89054489/232233567-fb017920-b99b-4c64-af79-f511dcc1cb22.png)


**Task 6: Exploring versioning**
Versioning is a means of keeping multiple variants of an object in the same bucket. You can use versioning to preserve, retrieve, and restore every version of every object stored in your S3 bucket. With versioning, you can easily recover from both unintended user actions and application failures.

For auditing and compliance reasons, you need to enable versioning on your reportbucket. Versioning should protect the reports in the reportbucket against accidental deletion. You are curious to see if this works as advertised. In this task, you enable versioning and test the feature by uploading a modified version of the sample-file.txt file from the previous task.

You should be on the S3 bucket Permissions tab from the previous task. If you are not, choose the link to the bucket at the upper left of the screen to return to the bucket overview page.
On the reportbucket overview page, choose the Properties tab.
Under the Bucket Versioning section, click Edit select Enable then click Save changes.
 Versioning is enabled for an entire bucket and all objects within the bucket. It cannot be enabled for individual objects.

 There are also cost considerations when enabling versioning. Refer to the Additional resources section at the end of the lab for links to more information.

Right-click this link, and save the text file to your computer using the same name as the text file in the previous task: sample-file.txt
Although this file has the same name as the previous file, it contains new text.

In the Amazon S3 Management Console, on the reportbucket, choose the Objects tab.
Under the Objects section, find  Show versions.

Choose Upload and use the same upload process that you used in tasks 2 and 5 to upload the new sample-file.txt file.
Go to the browser tab that has the contents of the sample-file.txt file.
Make a note of the contents on the page, and then refresh  the page.
Notice that new lines of text appear.

If a version is not otherwise specified, Amazon S3 always returns the latest version of an object.

You can also obtain a list of available versions in the Amazon S3 Management Console.

Close the web browser tab with the contents of the text file.
In the Amazon S3 Management Console, choose the sample-file.txt file name. The sample-file.txt overview page opens.
Choose the Versions tab, and then select the check box for the bottom version, which reads null. (This is not the latest version.)
Click Open.
You should now see the original version of the file using the Amazon S3 Management Console.

However, if you try to access the older version of the sample-file.txt file using the object URL link, you will receive an access denied message. This message is expected because the bucket policy you created in the previous task allows permission to access only the latest version of the object. In order to access a previous version of the object, you need to update your bucket policy to include the s3:GetObjectVersion permission. The following bucket policy example includes the additional s3:GetObjectVersion action that allows you to access the older version using the link. You do not need to update your bucket policy with this example to complete this lab. You can try to do this on your own after you complete the task.

{
    "Id": "Policy1557511288767",
    "Version": "2012-10-17",
    "Statement": [
    {
        "Sid": "Stmt1557511286634",
        "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion"
        ],
        "Effect": "Allow",
        "Resource": "arn:aws:s3:::reportbucket987987/*",
        "Principal": "*"
    }
    ]
}
Return to the AWS Management Console tab, and choose the link for the bucket name at the upper left to return to the bucket overview tab.
Locate the  Show versions option, and toggle the button to on  to show the versions.
Now you can view the available versions of each object and identify which version is the latest. Notice that the new-report.png object has only one version. The version ID is null because the object was uploaded before versioning was enabled on this bucket.

Also notice that you can now choose the version name link to navigate directly to that version of the object in the console.

Next to Show versions, toggle the button to off  to return to the default object view.
Select the check box to the left of the sample-file.txt.
With the object selected, choose Delete
The Delete objects page appears.
At the bottom, in the Delete objects? section, enter delete and choose the Delete objects button to confirm deletion of the object.
In the upper right of the page, choose Close to return to the bucket overview.
The sample-file.txt object is no longer displayed in the bucket. However, if the object is deleted by mistake, you can use versioning to recover it.

Locate the  Show versions option, and toggle the button to on  to show the versions.
Notice that the sample-file.txt object is displayed again, but the most recent version is a Delete marker. The two previous versions are also listed. If versioning has been enabled on the bucket, objects are not immediately deleted. Instead, Amazon S3 inserts a delete marker, which becomes the current object version. The previous versions of the object are not removed. Refer to the Additional resources section at the end of the lab for links to more information about versioning.

Select the check box for the version of the sample-file.txt object with the Delete marker.
With the object selected, choose Delete
The Delete objects window appears.
At the bottom in the Permanently delete objects? section, enter permanently delete and choose the Delete objects button to confirm deletion of the object.
On the upper right of the page, choose Close to return to the bucket overview.
Next to Show versions, toggle the button to off  to return to the default object view.
Notice that the sample-file.txt object has been restored to the bucket. Removing the delete marker has effectively restored the object to its previous state. Refer to the Additional resources section at the end of the lab for links to more information about undeleting S3 objects.

Next, you delete a specific version of the object.

To delete a specific version of the object, locate the  Show versions option, and toggle the button to on  to show the versions.
You should see two versions of the sample-file.txt object.

Select the check box for the latest version of the sample-file.txt object.
With the object selected, choose Delete
The Delete objects window appears.
At the bottom in the Permanently delete objects? section, enter permanently delete and choose the Delete objects button.
On the upper right of the page, choose Close to return to the bucket overview.
Notice that there is now only one version of the sample-file.txt file. When deleting a specific version of an object, no delete marker is created. The object is permanently deleted. Refer to the Additional resources section at the end of the lab for links to more information about deleting object versions in Amazon S3.

Next to Show versions, toggle the button to off  to return to the default object view.
Choose the sample-file.txt file name. The sample-file.txt overview page opens.
Copy the Object URL link displayed at the bottom of the window.
In a new browser tab, paste the link into the address field, and then press Enter.
The browser page displays the text of the original version of the sample-file.txt object.


**Summary**
You have successfully created an S3 bucket for your company to use to store report data from your EC2 instance. You created a bucket policy so that the EC2 instance can PutObjects and GetObject from the reportbucket, and you successfully tested uploading and downloading files from the EC2 instance to test the bucket policy. You have enabled versioning on the S3 bucket to protect against accidental object deletion. You have successfully completed the configuration for your EC2 reportbucket. Congratulations!

