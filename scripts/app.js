// scripts/app.js
const opportunities = [
    {
      title: "Mandela Scholarship",
      org: "University of Cape Town",
      deadline: "2025-08-15",
      link: "#"
    },
    {
      title: "AfDB Internship Program",
      org: "African Development Bank",
      deadline: "2025-07-20",
      link: "#"
    }
  ];
  
  const cardsContainer = document.querySelector(".cards");
  
  opportunities.forEach(opp => {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <h4>${opp.title}</h4>
      <p><strong>By:</strong> ${opp.org}</p>
      <p><strong>Deadline:</strong> ${opp.deadline}</p>
      <a href="${opp.link}" class="btn">Apply Now</a>
    `;
    cardsContainer.appendChild(card);
  });
  