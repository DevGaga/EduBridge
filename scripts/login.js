document.getElementById("login-form").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
  
    // Dummy validation (replace with Django auth later)
    if (data.email === "test@edubridge.com" && data.password === "password123") {
      alert("Login successful!");
      window.location.href = "dashboard.html";
    } else {
      alert("Invalid credentials. Try again.");
    }
  });
  