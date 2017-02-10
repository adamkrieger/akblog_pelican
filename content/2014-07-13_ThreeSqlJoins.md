Title: What are the Three SQL Join Syntaxes?
Category: Databases
Tags: syntax, sql
Summary: That time I was asked in an interview about SQL syntax, and wasn't old enough to know the answer.

This may or may not be a common interview question, but I was asked it once, so you're welcome. :) When referring to ‘join syntaxes’, I do not mean the type of join (INNER, OUTER, LEFT, CROSS, SELF), but the arrangement of syntax itself. <a href="http://www.mcpressonline.com/programming/sql/practical-sql-three-ways-to-join.html">This post</a> by Joe Pluta is pretty complete, but I’ll attempt to add value above and beyond it. This post assumes you’ve read Joe’s post, but I’ll quickly recap the syntaxes. <!--more-->

### What are they?

<ol>
	<li>Table List (Which Joe refers to as Traditional)

 <pre><code class="sql">SELECT
     fieldFromTable1, fieldFromTable2
 FROM
     table1, table2
 WHERE
     table1.foreignKeyCol = table2.primaryKeyCol</code></pre>

    </li>
	<li>JOIN-ON

 <pre><code class="sql">SELECT
     fieldFromTable1, fieldFromTable2
 FROM
     table1
 JOIN
     table2
     ON table1.foreignKeyCol = table2.primaryKeyCol</code></pre>

 	</li>
	<li>USING

 <pre><code class="sql">SELECT
     fieldFromTable1, fieldFromTable2
 FROM
     table1
 JOIN
     table2
 USING
     (table2Id)</code></pre>

 	</li>
</ol>

There’s a lot of knowledge out there on how to use JOINs, but not a lot on the history of them. I’ve only been exposed to JOIN-ON in production, but why? Is there something to learn from the other two?

### Table List vs. JOIN-ON - Cohesion and Clarity

At first glance, Table List appears deprecated. It looks as if this was the primordial way to slam two tables together and traverse a model. Upon looking deeper, there’s a valuable lesson. Consider this query, which has the JOIN clause do double duty and take care of the WHERE constraint.

<pre><code class="sql">SELECT
	FirstName, LastName, SaleAmount
FROM
	SalesPeople
JOIN
	Transactions
ON
	SalesPeople.Id = Transactions.SalesPersonId
	AND SalesPeople.FirstName = 'Fred'</code></pre>

This query moves the constraint into the where, which is probably the place you’d expect it to be.

<pre><code class="sql">SELECT
	FirstName, LastName, SaleAmount
FROM
	SalesPeople
JOIN
	Transactions
ON
	SalesPeople.Id = Transactions.SalesPersonId
WHERE
	SalesPeople.FirstName = 'Fred'</code></pre>

The query optimizer builds the same execution plan for both, so they’re identically performant in this case. Your mileage may vary with more complicated joins (I haven't checked). The latter example makes it easier to understand which pieces enforce the model, and which provide business logic. This seems a bit obvious when examining the first name column, so let’s look at a different example.

<pre><code class="sql">SELECT
	FirstName, LastName, SaleAmount
FROM
	SalesPeople
JOIN
	Transactions
ON
	SalesPeople.Id = Transactions.SalesPersonId
	AND Transactions.TypeId = @TransactionTypeId</code></pre>

A programmer not familiar with the data model could misunderstand that TypeId filtering is required when linking to Transactions. In this admittedly hypothetical example, the statement was really meant to filter out undesired Transactions for presentation to the user. This is a business logic concern and should be implemented in the WHERE clause.

Use JOIN syntax for data model linking, and not for business logic constraints. It’s far easier to understand the data model when this rule is followed throughout the schema.

### 'USING' Restricts your Convention

In the syntax example for USING, Table2’s primary key has to be the same name as the foreign key. The fact that this syntax directly restricts column naming convention is enough to keep me from ever implementing it.

### What did we learn?

<ul>
	<li>There are, in fact, three different syntaxes for joining tables.</li>
	<li>Table-Listing doesn’t allow differentiation between data model and business logic because you are forced to use the WHERE clause for both.</li>
	<li>USING makes assumptions about, and can even require the modification of, column naming convention, which could affect your whole organization.</li>
	<li>JOIN-ON is the most flexible of the three, but it is still important to keep business logic out of the JOIN clause in order to assist the reader in understanding the data model.</li>
</ul>

Thanks for reading,

Adam Krieger
