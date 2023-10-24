import React, { useState, useEffect } from "react";
import ProductCard from "./ProductCard.js";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import "./ProductList.css";

function ProductList({ searchInput }) {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/products")
      .then((response) => response.json())
      .then(setProducts)
      .catch((error) => console.error("Error fetching products:", error));
  }, []);

  const searchWords = searchInput.toLowerCase().split(" ");
  const searchedProducts = Array.isArray(products)
    ? products.filter((product) => {
        return searchWords.every((word) => {
          const searchTerm = word.trim();
          return product.name.toLowerCase().includes(searchTerm);
        });
      })
    : [];

  const addToCart = (product) => {
    setCart((prevCart) => [...prevCart, product]);

    // Define the user ID. This is just a placeholder.
    // In a real-world scenario, the user ID would probably come from the logged-in user's state or context.
    const userId = 1;

    // Define the desired quantity.
    // This can be modified if you want to let users specify a quantity.
    const quantity = 1;

    fetch(`http://127.0.0.1:5000/users/${userId}/cart`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        product_id: product.id,
        quantity: quantity,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message === "Cart updated successfully") {
          console.log("Product added to cart in database");
        } else {
          console.error("Error adding to cart:", data.message);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <div>
      <ProdCardGrid1 products={searchedProducts} handleAddToCart={addToCart} />
      {/* You can also add a section here to display items in the cart if you wish */}
    </div>
  );
}

function ProdCardGrid1({ products, handleAddToCart, handleProductClick }) {
  return (
    <div className="card-container">
      <Row xs={1} md={3} className="g-3">
        {products.map((product, idx) => (
          <Col key={idx} className="my-3">
            <ProductCard
              key={product.id}
              product={product}
              onAddToCart={() => handleAddToCart(product)}
              handleProductClick={handleProductClick}
            />
          </Col>
        ))}
        {products.length === 0 && (
          <Col>
            <div>No products found.</div>
          </Col>
        )}
      </Row>
    </div>
  );
}

export default ProductList;
