const elements = [
    { name: "Hydrogen", symbol: "H", atomicNumber: 1 },
    { name: "Helium", symbol: "He", atomicNumber: 2 },
    { name: "Lithium", symbol: "Li", atomicNumber: 3 },
    { name: "Carbon", symbol: "C", atomicNumber: 6 },
    { name: "Oxygen", symbol: "O", atomicNumber: 8 },
    // Add more as needed
];

const searchBox = document.getElementById("searchBox");
const resultDiv = document.getElementById("result");

searchBox.addEventListener("input", function () {
    const query = searchBox.value.toLowerCase();
    const element = elements.find(
        (e) =>
            e.name.toLowerCase() === query || e.symbol.toLowerCase() === query
    );

    if (element) {
        resultDiv.innerHTML = `
          <h3>${element.name} (${element.symbol})</h3>
          <p>Atomic Number: ${element.atomicNumber}</p>
        `;
    } else {
        resultDiv.innerHTML = query ? `<p>No element found.</p>` : "";
    }
});
