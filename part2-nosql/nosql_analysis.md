# NoSQL Analysis – FlexiMart Product Catalog

## Section A: Limitations of RDBMS 

Relational databases struggle when handling highly diverse product data because they require a fixed schema. In an e-commerce system like FlexiMart, products such as smartphones, laptops, clothing, and footwear have completely different attributes. Representing these differences in a relational model would require either a large number of nullable columns or multiple product-specific tables, both of which increase complexity and reduce maintainability.

Frequent schema changes are another limitation. Whenever a new product type is introduced or a new attribute is added (e.g., battery type, shoe width, fabric blend), ALTER TABLE operations are required, which are expensive and risky in production systems.

Additionally, storing customer reviews in relational databases requires separate tables and complex joins. Reviews are naturally hierarchical data, and flattening them leads to performance overhead and complicated queries for analytics.

---

## Section B: Benefits of MongoDB 

MongoDB solves these challenges by using a flexible, document-based schema. Each product can store only the attributes relevant to it without enforcing a rigid structure. For example, electronics can store RAM and processor details, while clothing products can store size and fabric information in the same collection.

MongoDB supports embedded documents, allowing customer reviews to be stored directly inside the product document. This improves read performance and makes it easier to fetch complete product information in a single query.

Horizontal scalability is another major advantage. MongoDB supports sharding, enabling FlexiMart to scale product catalog data across multiple servers as traffic grows. This makes MongoDB highly suitable for handling large volumes of semi-structured product data in a dynamic e-commerce environment.

---

## Section C: Trade-offs 

One disadvantage of MongoDB is weaker support for complex transactions compared to relational databases. While MongoDB supports transactions, they are not as mature or efficient as those in MySQL for highly transactional systems.

Another drawback is data consistency. MongoDB typically favors eventual consistency, which can be problematic for systems requiring strict consistency, such as financial or inventory-critical operations.
