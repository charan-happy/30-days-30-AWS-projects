
# Lab 3: Introduction to Amazon DynamoDB
Lab overview
Amazon DynamoDB is a fast and flexible NoSQL database service for all applications that need consistent, single-digit millisecond latency at any scale. It is a fully managed database that supports both document and key-value data models. Its flexible data model and reliable performance make it a great fit for mobile, web, gaming, advertising technology, Internet of Things (IoT), and many other applications.

In this lab, you create a table in DynamoDB to store information about a music library. You then query the music library and, finally, delete the DynamoDB table.

Objectives
After completing this lab, you will know how to:

Create a DynamoDB table
Enter data into a DynamoDB table
Query a DynamoDB table
Delete a DynamoDB table

Accessing the AWS Management Console

## Task 1: Creating a New Table
In this task, you create a new table in DynamoDB named Music. Each table requires a primary key that is used to partition data across DynamoDB servers. A table can also have a sort key. The combination of a primary key and a sort key uniquely identifies each item in a DynamoDB table.

In the AWS Management Console, choose Services, and then choose DynamoDB.

Choose Create table

For Table name, enter Music

For Partition key, enter Artist and leave String selected.

For Sort key - optional, enter Song and leave String selected.

Under Settings select Customize settings then configure the following:

Read capacity
Provisioned capacity units: 10
Write capacity
Provisioned capacity units: 2
 Amazon DynamoDB has two read/write capacity modes for processing reads and writes on your tables:

On-demand
Provisioned (default, free-tier eligible)
The read/write capacity mode controls how you are charged for read and write throughput and how you manage capacity. You can set the read/write capacity mode when creating a table or you can change it later.

Your table will use default settings for indexes.

Choose Create table.

The table is created in less than 1 minute.

 ![image](https://user-images.githubusercontent.com/89054489/232297143-c625b91d-c322-4d5a-83a9-9612d0b61afc.png)
![image](https://user-images.githubusercontent.com/89054489/232297355-19efb2d0-aee6-4311-8084-23f2889b5f17.png)
![image](https://user-images.githubusercontent.com/89054489/232298001-d3585c24-ed57-4541-acfb-318e8408a5d5.png)

![image](https://user-images.githubusercontent.com/89054489/232298229-a5e7d060-f533-4078-b3e2-c88a483e2a67.png)

![image](https://user-images.githubusercontent.com/89054489/232299231-b02bc1c2-05f8-464f-bcc4-d6f603636d93.png)

![image](https://user-images.githubusercontent.com/89054489/232299158-ccdf4f03-a52a-4c34-ae9f-c3027cedfdc9.png)


## Task 2: Adding Data
In this task, you add data to the Music table. A table is a collection of data on a particular topic.

Each table contains multiple items. An item is a group of attributes that is uniquely identifiable among all of the other items. Items in DynamoDB are similar in many ways to rows in other database systems. In DynamoDB, there is no limit to the number of items that you can store in a table.

Each item consists of one or more attributes. An attribute is a fundamental data element, something that does not need to be broken down any further. For example, an item in a Music table contains attributes such as song and artist. Attributes in DynamoDB are similar to columns in other database systems, but each item (row) can have different attributes (columns).

When you write an item to a DynamoDB table, only the primary key and sort key (if used) are required. Other than these fields, the table does not require a schema, which means that you can add attributes to one item that may be different than the attributes on other items.

Select Explore items on the left side navigation pane.

Click the radio button next to Music to select the table you created.

Click Create item.

Add in the following values.

Artist: Pink Floyd
Song: Money
These are the only required attributes, but you can now add additional attributes.

To create an additional attribute, click the Add new attribute button.

In the dropdown list, choose String.

A new attribute row is added.

For the new attribute, replace NewValue with Album and in the Value column enter The Dark Side of the Moon.

Add another new attribute by choosing the Add new attribute button.

In the dropdown list, choose Number.

For the new attribute, replace NewValue with Year and in the Value column replace 0 with 1973.

Choose Create item to store the new item with its four attributes.


The item appears in the Items returned pane in the console.

 

Next, follow the previous steps and use the following attributes to create a second item:

Attribute Name	Attribute Type	Attribute Value
Artist	String	John Lennon
Song	String	Imagine
Album	String	Imagine
Year	Number	1971
Genre	String	Soft rock
Note that this item has an additional attribute called Genre. Adding this attribute is an example of each item being capable of having different attributes without having to pre-define a table schema.

Follow the previous steps and use the following attributes to create a third item:

Attribute Name	Attribute Type	Attribute Value
Artist	String	Psy
Song	String	Gangnam Style
Album	String	Psy 6 (Six Rules), Part 1
Year	Number	2011
LengthSeconds	Number	219
Once again, this item has a new LengthSeconds attribute that identifies the length of the song. The ability to include this attribute demonstrates the flexibility of a NoSQL database.

There are also faster ways to load data into DynamoDB, such as using AWS Data Pipeline, programmatically loading data, or using one of the free tools available on the internet.

 
 ![image](https://user-images.githubusercontent.com/89054489/232299834-30ce7282-2aec-4857-8a0b-cabb5a063d98.png)
 
![image](https://user-images.githubusercontent.com/89054489/232300185-cac49f8f-dea0-4455-8bdd-caa96d7d4a45.png)

![image](https://user-images.githubusercontent.com/89054489/232300236-1264d89d-0cc0-40ad-b730-41fc948a4da4.png)

Task 3: Modifying an Existing Item
You now notice that there is an error in your data. In this task, you modify an existing item.

From the list of items, select the row where the Artist is Psy.

Choose the Actions menu, and select Edit item.

Change the Year Number from 2011 to 2012.

Choose Save changes.

The item is now updated.

 ![image](https://user-images.githubusercontent.com/89054489/232300297-5e9d8f2b-c309-4103-9877-b471cf7b91ce.png)
![image](https://user-images.githubusercontent.com/89054489/232300316-99c90f8c-bf56-4c97-8e7e-859a19fe36f8.png)


Task 4: Querying the Table
There are two ways to query a DynamoDB table: query and scan.

A query operation finds items based on the Primary Key and optionally based on the Sort Key. It is fully indexed, so it runs very fast.

Choose Explore items in the left navigation pane.

Select Music.

If Scan/Query items is not already expanded, choose the arrow  to expose the Scan and Query options.

Choose Query.

Fields for the Artist (which is the same as partition key) and Song (which is the same as sort key) are now displayed.

Enter the following details:

Artist (Partition key): Psy
Song (Sort key): Equal to Gangnam Style
Choose Run.

The song quickly appears in the list. A query is the most efficient way to retrieve data from a DynamoDB table.

Alternatively, you can scan for an item. This option involves looking through every item in a table, so this option is less efficient and can take significant time for larger tables.

Choose the Scan option.

Choose the arrow  to expand Filters.

Enter values for the scan filter:

For Enter attribute name, enter Year
Change String to Number.
Condition: Select Equal to
For Enter value, enter 1971
Choose Run.
Only the song released in 1971 is displayed.

 ![image](https://user-images.githubusercontent.com/89054489/232300832-8a1f024a-6a97-4476-b232-5032c36865c1.png)
![image](https://user-images.githubusercontent.com/89054489/232300928-e848e7c9-7d87-4216-b3ef-14e7316672f5.png)
![image](https://user-images.githubusercontent.com/89054489/232301243-3629cb7b-1f12-4bb2-bd50-a70680a99c32.png)
![image](https://user-images.githubusercontent.com/89054489/232301510-4578cfc7-4b14-48f2-9c33-1de55bf21119.png)


Task 5: Deleting an Item
In this task, you delete an item within the table.

Choose Reset then click Run. To load the full Music table.

Under Artist, select the check box for Psy to choose this item.

Choose the Actions dropdown list, and select Delete items.

On the Delete item(s) screen, choose Delete.

This item is now deleted.

 ![image](https://user-images.githubusercontent.com/89054489/232301680-f1e8dfe7-3e55-412f-9119-a2a03f02317c.png)
![image](https://user-images.githubusercontent.com/89054489/232301759-42ae0efe-5ec5-4022-9a40-d6456cee23f3.png)
![image](https://user-images.githubusercontent.com/89054489/232301992-71a484c3-2209-4237-9f47-eadaf4c3cbc1.png)
![image](https://user-images.githubusercontent.com/89054489/232302066-194e5352-636f-4eef-a00c-cbe347c79028.png)
![image](https://user-images.githubusercontent.com/89054489/232302242-dd35a5d7-0fc5-4d4c-a061-e36a9489ad00.png)


Lab complete 
 Congratulations! You have completed the lab.



 
