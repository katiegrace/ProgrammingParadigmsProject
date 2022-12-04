// document.getElementById("position-filter").onchange = applyPositionFilter;

function applyPositionFilter() {
    let selectElement = document.getElementById("filter");
    // 1, 2 or 3
    let value = selectElement.value;
    // Assistant Professor, Associate Professor, All
    let text = selectElement.options[selectElement.selectedIndex].text;
    // all faculty divs
    let allPosts = document.getElementsById("printfiltered");
    // show all elements
    if (text == "All Posts") {
        for (let i = 0; i < allPosts.length; i++) {
            allPosts[i].style.display = "block";
        }
    }
    else if (text == "Active Posts Only") {
        for (let i = 0; i < allPosts.length; i++) {
            let h3 = allPosts[i].querySelector("h3");
            let status = allPosts[i].position_status;
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
