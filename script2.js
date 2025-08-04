"use strict";

let brands = [];

const container = document.getElementById("brand-container");
const itemHeight = 30;
const visibleCount = Math.ceil(container.clientHeight / itemHeight);

async function loadData(url) {
    try {
        //Load data
        const response = await fetch(url);
        const data = await response.json();
        console.log("Data loaded:", data);
        brands = data;
        renderList(0);
    } catch (error) {
        console.error("Fetch error:", error);
    }
}

loadData("brand-generation/clothingBrands.json");

function renderList(startIndex = 0) {
    container.innerHTML = "";
    const endIndex = startIndex + visibleCount + 5;
    for (let i = startIndex; i < endIndex && i < brands.length; i++) {
        const div = document.createElement("div");
        div.textContent = brands[i].name;
        div.style.height = itemHeight + "px";
        container.appendChild(div);
    }
}

container.addEventListener("scroll", () => {
    const scrollTop = container.scrollTop;
    const startIndex = Math.floor(scrollTop / itemHeight);
    console.log(startIndex);
    renderList(startIndex);
});
