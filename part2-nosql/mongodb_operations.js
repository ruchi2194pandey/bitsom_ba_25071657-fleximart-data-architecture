/******************************************************
 * MongoDB Operations – FlexiMart
 * Database: fleximart_nosql
 * Collection: products
 *
 * How to run:
 * mongosh mongodb_operations.js
 ******************************************************/

/*
Step 1: Import Data (Run from terminal ONE TIME)
mongoimport --db fleximart_nosql --collection products \
--file products_catalog.json --jsonArray
*/

// ----------------------------------------------------
// Switch to Database (VALID for JS execution)
// ----------------------------------------------------
db = db.getSiblingDB("fleximart_nosql");

// ----------------------------------------------------
// Operation 1: Basic Query
// Find all Electronics products priced below 50,000
// Return name, price, and stock only
// ----------------------------------------------------
db.products.find(
  { category: "Electronics", price: { $lt: 50000 } },
  { _id: 0, name: 1, price: 1, stock: 1 }
);

// ----------------------------------------------------
// Operation 2: Aggregation
// Find products with average review rating >= 4.0
// ----------------------------------------------------
db.products.aggregate([
  { $unwind: "$reviews" },
  {
    $group: {
      _id: "$name",
      avg_rating: { $avg: "$reviews.rating" }
    }
  },
  {
    $match: {
      avg_rating: { $gte: 4 }
    }
  },
  {
    $project: {
      _id: 0,
      product_name: "$_id",
      avg_rating: { $round: ["$avg_rating", 2] }
    }
  }
]);

// ----------------------------------------------------
// Operation 3: Update
// Add a new customer review to product ELEC001
// ----------------------------------------------------
db.products.updateOne(
  { product_id: "ELEC001" },
  {
    $push: {
      reviews: {
        user: "U501",
        rating: 5,
        comment: "Excellent product",
        review_date: new Date()
      }
    }
  }
);

// ----------------------------------------------------
// Operation 4: Complex Aggregation
// Calculate average price per category
// ----------------------------------------------------
db.products.aggregate([
  {
    $group: {
      _id: "$category",
      avg_price: { $avg: "$price" },
      product_count: { $sum: 1 }
    }
  },
  {
    $project: {
      _id: 0,
      category: "$_id",
      avg_price: { $round: ["$avg_price", 2] },
      product_count: 1
    }
  },
  {
    $sort: { avg_price: -1 }
  }
]);
