const myOpportunities = [
    {
      title: "Zambia Coding Challenge",
      org: "BongoHive",
      deadline: "2025-09-01"
    },
    {
      title: "University Graduate Fellowship",
      org: "UNZA",
      deadline: "2025-07-15"
    }
  ];
  
  const list = document.querySelector(".opportunity-list");
  
  myOpportunities.forEach((opp, index) => {
    const card = document.createElement("div");
    card.className = "opportunity-card";
    card.innerHTML = `
      <h3>${opp.title}</h3>
      <p><strong>Organization:</strong> ${opp.org}</p>
      <p><strong>Deadline:</strong> ${opp.deadline}</p>
      <div class="card-actions">
        <button class="edit-btn" onclick="editOpportunity(${index})">Edit</button>
        <button class="delete-btn" onclick="deleteOpportunity(${index})">Delete</button>
      </div>
    `;
    list.appendChild(card);
  });
  
  // Just demo alert functions
  function editOpportunity(index) {
    alert(`Edit functionality for opportunity #${index} coming soon`);
  }
  
  function deleteOpportunity(index) {
    alert(`Delete functionality for opportunity #${index} coming soon`);
  }
s  