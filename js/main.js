// main.js

// Grab modal elements
const modal = document.getElementById("petModal");
const modalImage = document.getElementById("modalImage");
const modalName = document.getElementById("modalName");
const modalType = document.getElementById("modalType");
const modalDescription = document.getElementById("modalDescription");
const modalContact = document.getElementById("modalContact");
const spanClose = document.getElementsByClassName("close")[0];

// Function to open modal with pet details
function openModal(pet) {
    modalImage.src = pet.image || "placeholder.jpg"; // fallback image
    modalName.textContent = pet.name;
    modalType.textContent = `Type: ${pet.type}`;
    modalDescription.textContent = pet.description;
    if (pet.owner) {
        modalContact.innerHTML = `
            <strong>Owner:</strong> ${pet.owner.name}<br>
            <strong>Email:</strong> <a href="mailto:${pet.owner.contact}">${pet.owner.contact}</a><br>
            <strong>Phone:</strong> <a href="tel:${pet.owner.phone}">${pet.owner.phone}</a>
        `;
    } else {
        modalContact.textContent = "Owner details not available";
    }
    modal.style.display = "block";
}

// Close modal on X click
spanClose.onclick = function() {
    modal.style.display = "none";
};

// Close modal on outside click
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

fetch("static/dpets.json")  // updated path
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const allPets = document.getElementById("all-pets");
        allPets.innerHTML = ""; // clear any existing content

        data.forEach(pet => {
            // Create pet card
            const card = document.createElement("div");
            card.className = "pet-card";

            // Image
            const img = document.createElement("img");
            img.src = pet.image ? pet.image : "images/placeholder.jpg"; // use relative path directly
            img.alt = pet.name;
            img.className = "pet-img";


            // Name
            const name = document.createElement("h3");
            name.textContent = pet.name;

            // Append to card
            card.appendChild(img);
            card.appendChild(name);

            // Click to open existing modal
            card.addEventListener("click", () => openModal(pet));

            // Append card to grid
            allPets.appendChild(card);
        });
    })
    .catch(error => {
        console.error("Error loading pets:", error);
        const allPets = document.getElementById("all-pets");
        allPets.innerHTML = "<p style='text-align:center;'>Could not load pets at this time.</p>";
    });

