import React from "react";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import ordersImage from "../images/orders.png"; // Import your default image
import "./ProductCard.css";

function ProductCard({ product, onAddToCart, handleProductClick }) {
  return (
    <Card className="prod-cards h-card">
      <Card.Img
        variant="top"
        src={product.image}
        className="prod-card-image"
        onError={(e) => {
          e.target.src = ordersImage; // Set a default image when the original image fails to load
        }}
      />

      <Card.Body onClick={() => handleProductClick(product)}>
        <Button
          variant="primary"
          className="form-button"
          onClick={(e) => {
            e.stopPropagation();
            onAddToCart && onAddToCart();
          }}
        >
          Add to Cart
        </Button>
        <Card.Title>{product.name}</Card.Title>
        <Card.Text>{product.description}</Card.Text>
        <Card.Text>Price: ${product.price}</Card.Text>
        <Card.Text>Amount in Stock: {product.count}</Card.Text>
        <Card.Text>Categories: {product.category}</Card.Text>
      </Card.Body>
    </Card>
  );
}

export default ProductCard;
