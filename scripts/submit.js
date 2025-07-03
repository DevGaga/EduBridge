document.getElementById("submit-form").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
  
    alert("Thank you! Your opportunity has been submitted.");
  
    console.log("Submitted data:", data); // Later, send this to the backend
    e.target.reset();
  });
s  