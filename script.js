const brandCardTemplate = document.querySelector("[data-brand-template]");
const brandCardContainer = document.querySelector(
    "[data-brand-cards-container]"
);
const searchInput = document.querySelector("[data-search]");
const submitButton = document.querySelector("#submit-button");

let brands = [];

submitButton.addEventListener("click", (e) => {
    const value = searchInput.target.value.toLowerCase();
    brands.forEach((brand) => {
        const isVisible = brand.name.toLowerCase().includes(value);
        brand.element.classList.toggle("hide", !isVisible);
    });
});

fetch("brand-generation/clothingBrands.json")
    .then((res) => res.json())
    .then((data) => {
        brands = data.map((brand) => {
            const card = brandCardTemplate.content.cloneNode(true).children[0];
            const header = card.querySelector("[data-header]");
            const body = card.querySelector("[data-body]");
            header.textContent = brand.name;
            body.textContent = brand.rating;
            brandCardContainer.append(card);
            return {
                name: brand.name,
                rating: brand.rating,
                element: card,
            };
        });
    });
