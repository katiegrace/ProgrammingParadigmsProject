// document.getElementById("position-filter").onchange = applyPositionFilter;
function applyPositionFilter() {
    //alert(post_list[0])
    let selectElement = document.getElementById("filter");
    let value = selectElement.value;
    let text = selectElement.options[selectElement.selectedIndex].text;
    //alert(text)
    // text is "Active Posts Only" or "All Posts" or "Inactive..." or "Posts with at least 1..."
    // 
    // all posts
    let allPosts = document.getElementsByClassName("printfiltered");
    // show all elements
    if (text == "All Posts") {
        for (let i = 0; i < allPosts.length; i++) {
            allPosts[i].style.visibility="visible"
            //alert(allPosts[i].value)
        }
    }
    // Show only active posts
    else if (text == "Active Posts Only") {
        for (let i = 0; i < allPosts.length; i++) {
            let status = allPosts[i].status;
            // STATUS is not accesible -- back end vs front end jaunt
           // alert(allPosts[i].value) // HTMLParagraph Element
            //alert(typeof allPosts[i]) // object
            // status is undefined so this is our issue
            //let pstatus = {{allPosts[i]|status}};
            if (status == "Active") {
               // allPosts[i].style.display = "block";
                allPosts[i].style.visibility="visible"
            }
            else {
                allPosts[i].style.visibility = "hidden";
            }

        }
    }
    /*
    else if (text == "Inactive Posts Only"){
        let status = allPosts[i].status;
        if (status == "Active") {
            // allPosts[i].style.display = "block";
            allPosts[i].style.visibility="hidden"
        }
        else {
            allPosts[i].style.visibility = "visible";
        }
    }*/
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
