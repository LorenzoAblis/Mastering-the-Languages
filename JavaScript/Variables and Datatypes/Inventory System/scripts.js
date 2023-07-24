class Product {
    constructor(name, quantity, price) {
        this.name = name;
        this.quantity = quantity;
        this.price = price;
    }

    getNetValue() {
        return this.quantity * this.price;
    }
}

class Inventory {
    constructor() {
        this.products = [];
    }

    inventoryAddProduct(name, quantity, price) {
        const product = new Product(name, quantity, price);
        this.products.push(product);
    }

    inventoryRemoveProduct(name) {
        const index = this.products.findIndex(p => p.name === name);
        if (index!== -1) {
            this.products.splice(index, 1)[0];
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const inventory = new Inventory();
    const inventoryContainer = document.querySelector(".inventory-container");

    const addProductName = document.getElementById("add-product-name-input");
    const addProductQuantity = document.getElementById("add-product-quantity-input");
    const addProductPrice = document.getElementById("add-product-price-input");
    const addProductMissingField = document.getElementById("add-product-missing-field-warning");
    const addProductFormContainer = document.getElementById("add-product-form-container");

    const editProductName = document.getElementById("edit-product-name-input");
    const editProductQuantity = document.getElementById("edit-product-quantity-input");
    const editProductPrice = document.getElementById("edit-product-price-input");
    const editProductMissingField = document.getElementById("edit-product-missing-field-warning");
    const editProductFormContainer = document.getElementById("edit-product-form-container");

    let prevName = "";

    inventory.inventoryAddProduct("Laptop", 5, 1000);
    inventory.inventoryAddProduct("Smartphone", 15, 800);
    inventory.inventoryAddProduct("Headphones", 20, 100);
    inventory.inventoryAddProduct("Mouse", 50, 30);
    inventory.inventoryAddProduct("Keyboard", 30, 50);
    inventory.inventoryAddProduct("Monitor", 10, 200);
    inventory.inventoryAddProduct("Printer", 8, 150);
    inventory.inventoryAddProduct("Tablet", 12, 400);
    inventory.inventoryAddProduct("Camera", 3, 700);
    inventory.inventoryAddProduct("External Hard Drive", 25, 120);
    updateInventoryDisplay();

    function updateInventoryDisplay() {
        inventoryContainer.innerHTML = "";

        inventory.products.forEach(product => {
            const productFrame = document.createElement("div");

            productFrame.className = "product-frame"
            productFrame.id = "product-frame"
            productFrame.innerHTML = `
              <h1 class="product-title">${product.name}<h1>
              <h2 class="product-label">$${product.price} p/u<h2>
              <h2 class="product-label">${product.quantity} units<h2>
              <h3 class="product-netvalue">Net Value: $${product.getNetValue()}<h3>
              <button onclick="showEditProductForm('${product.name}', ${product.quantity}, ${product.price})" class="button" id="product-edit-button">Edit</button>
            `;
            inventoryContainer.appendChild(productFrame);
          });
    }

    function clearForms() {
        addProductName.value = "";
        addProductQuantity.value = "";
        addProductPrice.value = "";
        addProductMissingField.style.display = "none";
        addProductFormContainer.style.display = "none";
        editProductName.value = "";
        editProductQuantity.value = "";
        editProductPrice.value = "";
        editProductMissingField.style.display = "none";
        editProductFormContainer.style.display = "none";
    }

    function addProduct() {
        const name = addProductName.value;
        const quantity = addProductQuantity.value;
        const price = addProductPrice.value;

        if (name == "" || quantity == "" || price == "") {
            addProductMissingField.style.display = "flex";
        } else {
            inventory.inventoryAddProduct(name, quantity, price);
            updateInventoryDisplay(); 
            clearForms();
        }
    }

    function showAddProductForm() {
        addProductFormContainer.style.display = "flex";
    }

    function showEditProductForm(name, quantity, price) {
        editProductFormContainer.style.display = "flex";

        prevName = name;
        editProductName.value = name;
        editProductQuantity.value = quantity;
        editProductPrice.value = price;
    }

    function saveEdittedProduct() {
        const name = editProductName.value;
        const quantity = editProductQuantity.value;
        const price = editProductPrice.value;

        productToUpdate = inventory.products.find(p => p.name == prevName);
        
        if (name == "" || quantity == "" || price == "") {
            editProductMissingField.style.display = "flex";
        } else {
            productToUpdate.name = name;
            productToUpdate.quantity = quantity;
            productToUpdate.price = price;
            clearForms();
            updateInventoryDisplay();
        }
    }

    function deleteProduct() {
        inventory.inventoryRemoveProduct(prevName);
        clearForms();
        updateInventoryDisplay();
    }

    const productFunctions = {
        addProduct,
        showAddProductForm,
        clearForms,
        showEditProductForm,
        saveEdittedProduct,
        deleteProduct,
    };

    Object.assign(window, productFunctions);
});
