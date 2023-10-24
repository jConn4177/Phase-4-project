import React from "react";
import { Formik, Field, Form } from "formik";
import Button from "react-bootstrap/Button";
import "./NewProductForm.css";  // Assuming you have a corresponding CSS file

function ProductForm() {
  return (
    <div className="product-form">
      <div className="product-content">
        <h1>Create a Product:</h1>
        <Formik
          initialValues={{
            name: "",
            description: "",
            price: "",
            image: "",
            count: "",
            category: ""
          }}
          onSubmit={async (values) => {
            const response = await fetch("http://127.0.0.1:5000/products", {  // Assuming this is the endpoint to create a product
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(values),
            });

            const data = await response.json();

            if (response.status === 201) {
              alert("Product created successfully!");
            } else {
              alert(data.message || "Failed to create product.");
            }
          }}
        >
          <Form className="form-border">
            <label htmlFor="name">Name</label>
            <br />
            <Field id="name" name="name" placeholder="E.g., Stylish Sunglasses" />
            <br />

            <label htmlFor="description">Description</label>
            <br />
            <Field id="description" name="description" placeholder="E.g., Perfect for sunny days" />
            <br />

            <label htmlFor="price">Price</label>
            <br />
            <Field id="price" name="price" placeholder="E.g., 99.99" type="number" />
            <br />

            <label htmlFor="image">Image URL</label>
            <br />
            <Field id="image" name="image" placeholder="E.g., http://example.com/image.jpg" />
            <br />

            <label htmlFor="count">Count</label>
            <br />
            <Field id="count" name="count" placeholder="E.g., 10" type="number" />
            <br />

            <label htmlFor="category">Category</label>
            <br />
            <Field as="select" id="category" name="category">
              <option value="" label="Select category" />
              <option value="Aviator" label="Aviator" />
              <option value="Wayfarer" label="Wayfarer" />
              <option value="Round" label="Round" />
              <option value="Sports" label="Sports" />
              <option value="Designer" label="Designer" />
              <option value="Oversized" label="Oversized" />
              <option value="Cat-Eye" label="Cat-Eye" />
            </Field>
            <br />
            <br />

            <Button variant="primary" type="submit" className="form-button">
              Create Product
            </Button>
            <br />
          </Form>
        </Formik>
      </div>
    </div>
  );
}

export default ProductForm;
