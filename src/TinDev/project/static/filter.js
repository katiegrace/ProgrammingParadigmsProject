// document.getElementById("position-filter").onchange = applyPositionFilter;
function applyPositionFilter() {
    let selectElement = document.getElementById("filter");
    let value = selectElement.value;
    let text = selectElement.options[selectElement.selectedIndex].text;
    // all posts
    let allPosts = document.getElementById("printfiltered");
    // show all elements
    if (text == "All Posts") {
        for (let i = 0; i < allPosts.length; i++) {
            allPosts[i].style.display = "block";
        }
    }
    // Show only active posts
    else if (text == "Active Posts Only") {
        for (let i = 0; i < allPosts.length; i++) {
            let status = allPosts[i].post_status;
            if (status == "Active") {
                allPosts[i].style.display = "block";
            }
            else {
                allPosts[i].style.display = "none";
            }

        }
    }
    /*else {
        for (let i = 0; i < allPosts.length; i++) {
            let h3 = allPosts[i].querySelector("h3");
            let position = h3.innerText.split(",")[0].trim();
            if (position == text) {
                allPosts[i].style.display = "block";
            } else {
                allPosts[i].style.display = "none";
            }
        }
    }*/
}
