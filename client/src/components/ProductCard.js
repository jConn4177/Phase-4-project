import React from "react";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button"; // Add this for the button component from react-bootstrap
import "./ProductCard.css";

function ProductCard({ product, onAddToCart, handleProductClick }) {
  return (
    <Card className="prod-cards h-card">
      <Card.Img variant="top" src={product.image} className="prod-card-image" />

      <Card.Body onClick={() => handleProductClick(product)}>
        <Card.Title>{product.name}</Card.Title>
        <Card.Text>{product.description}</Card.Text>
        <Card.Text>Price: ${product.price}</Card.Text>
        <Card.Text>Amount in Stock: {product.count}</Card.Text>
        <Card.Text>Categories: {product.category}</Card.Text>
        {/* Add to Cart Button */}
        <Button variant="primary" onClick={(e) => {
          e.stopPropagation(); // This prevents the outer card click from being triggered
          onAddToCart && onAddToCart();
        }}>Add to Cart</Button>
      </Card.Body>
    </Card>
  );
}


export default ProductCard;
