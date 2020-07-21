function generate() {
  results = document.getElementById("results");
  if (results.style.display == "none") {
    results.style.display = "flex";
  }
}
function onload() {
  results = document.getElementById("results");
  results.style.display = "none";
}