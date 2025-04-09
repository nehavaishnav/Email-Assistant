
const loading = document.getElementById("loading");
const refreshBtn = document.getElementById("refresh-btn");
const toggleThemeBtn = document.getElementById("toggle-theme");

async function fetchEmail() {
  loading.style.display = "block";
  try {
    const res = await fetch("/api/email");
    if (!res.ok) throw new Error("Failed to load");
    const data = await res.json();
    document.getElementById("from").textContent = data.from || "N/A";
    document.getElementById("subject").textContent = data.subject || "N/A";
    document.getElementById("body").textContent = data.original_email || "N/A";
    document.getElementById("summary").textContent = data.summary || "N/A";
    document.getElementById("reply").textContent = data.ai_reply || "N/A";
  } catch (err) {
    alert("Error loading email: " + err.message);
  } finally {
    loading.style.display = "none";
  }
}

refreshBtn.addEventListener("click", fetchEmail);

toggleThemeBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark");
});

// Load email on start
fetchEmail();
