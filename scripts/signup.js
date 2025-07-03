document.getElementById("signup-form").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
  
    // Demo: Just log and show alert
    console.log("Signup Data:", data);
    alert("Sign-up successful! (This will be linked to Django later)");
    e.target.reset();
  });
  