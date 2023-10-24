import React, { useState, useEffect } from "react";
import "./Cart.css";

function Cart() {
  const [cartItems, setCartItems] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/users/<int:user_id>/cart")
      .then((response) => response.json())
      .then((data) => setCartItems(data))
      .catch((error) => console.error("Error fetching cart items:", error));
  }, []);

  const handleRemoveItem = (productId) => {
    fetch(`http://127.0.0.1:5000/users/<int:user_id>/cart/${productId}`, {
      method: "DELETE",
    })
      .then(() => {
        setCartItems((prevItems) =>
          prevItems.filter((item) => item.id !== productId)
        );
      })
      .catch((error) => console.error("Error removing item from cart:", error));
  };

  return (
    <div className="cart-container">
      <h1>Your Cart</h1>
      {cartItems.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <ul>
          {cartItems.map((item) => (
            <li key={item.id}>
              <div className="cart-item">
                <div className="cart-item-details">
                  <h3>{item.productName}</h3>
                  <p>Quantity: {item.quantity}</p>
                </div>
                <button
                  className="remove-item"
                  onClick={() => handleRemoveItem(item.productId)}
                >
                  Remove
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Cart;
