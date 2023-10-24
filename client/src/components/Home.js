import React, { useState } from "react";
import HomeHeader from "./HomeHeader.js";
import ProductList from "./ProductList.js";
import "./Home.css";

function Home() {
  const [searchInput, setSearchInput] = useState("");
  return (
    <div>
      <HomeHeader searchInput={searchInput} setSearchInput={setSearchInput} />
      <h1>Whatcha gonna buy?</h1>
      <ProductList searchInput={searchInput} />

    </div>
  );
}

export default Home;
