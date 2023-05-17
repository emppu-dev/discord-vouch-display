function updateMessages() {
    var container = document.getElementById("main-container");
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                container.innerHTML = xhr.responseText;
            } else {
                console.error("Error");
            }
        }
    };
    xhr.open("GET", "system/get.php", true);
    xhr.send();
    setTimeout(updateMessages, 5000);
}
updateMessages();