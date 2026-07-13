function validateFile() {
    let file = document.getElementById("file").value;

    if (file === "") {
        alert("Please select a file!");
        return false;
    }
    return true;
}

// 🔄 Refresh function
function resetPage() {
    window.location.href = "/";
}

