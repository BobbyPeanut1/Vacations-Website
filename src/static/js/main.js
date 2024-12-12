
// error showing on page
const error = document.querySelector(".error");

if (error){
    document.body.style.overflow = "hidden";
    setTimeout(() => {
        document.body.style.overflow = "auto";
        error.parentNode.removeChild(error);
    }, 4000);
}

// ask the admin if he's sure he wants to delete a vacation
function confirmDelete(){
    const ok = confirm("Are you sure?");
    if (!ok){
        event.preventDefault(); 
    }
}

// add a scroll wheel to the y axis on a page if it has the class activeCheck
// needed for some pages when they go past the screen and break the footer position when not added
const activeCheck = document.querySelector(".activeCheck");

if (activeCheck){
    document.getElementById("main").style.overflowY = "scroll"; 
}

// clicks on the actual input that is sent with the form
// theres no way to modify the default html input text and image so this is a way to make a custom clickable file input area
function userClickedToChangeImage(){
    document.getElementById("image_file").click();
}

// displays the image after selecting it in our vacation
function loadFile(event){
    let image = document.getElementById("uploadFile"); // gets the element we want to display on
    image.src = URL.createObjectURL(event.target.files[0]); // creates a url to the image source from our file that we uploaded and links it to our element
    image.onload = function() {
        URL.revokeObjectURL(image.src); // deletes the reference url when we reload the page to save space
      }
}

// give each like/unlike form a connection to ajax to stop refreshing and save data correctly
// when we do on('submit'...) in the function and use a click to submit the form, if we click it again it will add another submit event and click them both
// this goes on and on so to counteract this we add the off() function before we add the submit event that removes all of our previous event handlers
// this way we always call the like/unlike function only once per click
function addLikeSubmit(vacationId) {
    $(document).off().on('submit',`#likeForm${vacationId}`,function(event) {
        event.preventDefault(); // prevents the input submission and page refresh
        $.ajax({
            type:'POST',
            url:'/vacations/like',
            data: {
                vacation_id: $(`#like${vacationId}`).val() 
            },

        })
    });

}

function addUnlikeSubmit(vacationId){
    $(document).off().on('submit',`#unLikeForm${vacationId}`,function(event) {
        event.preventDefault(); // prevents the input submission and page refresh
        $.ajax({
            type:'POST',
            url:'/vacations/unlike',
            data: {
                vacation_id: $(`#unlike${vacationId}`).val() 
            },

        })
    });

}

// user clicked to like or unlike
function changeLikeStateAndSubmit(vacationId) {
    const detailsAndLikes = document.getElementById(`detailsAndLikes${vacationId}`); // get the whole details "vacationDetailsAndLikes" div
    const heart = detailsAndLikes.querySelector(".heart"); // get heart div
    const likeAmount = detailsAndLikes.querySelector(`.vacationLikeAmount${vacationId}`); // get like display amount

    if (!heart.classList.contains("heartClick")){ // if the user clicked like
        const clickedLike = detailsAndLikes.querySelector(".hiddenLikeInputSubmit"); // get the input responsible for liking a vacation
        clickedLike.setAttribute("name", "vacation_id"); // give it a name so it can be fetched from the form in our facade
        clickedLike.click(); // simulate a user click to submit
        clickedLike.removeAttribute("name", "vacation_id"); // remove the name attribute after use so it can be attached to other likes/unlikes
        
        heart.classList.add("heartClick"); // add a clicked effect to the heart
        likeAmount.innerHTML = parseInt(likeAmount.innerHTML) + 1; // increase like amount
    }
    else{ // if the user clicked unlike
        const clickedUnlike = detailsAndLikes.querySelector(".hiddenUnlikeInputSubmit"); // get the input responsible for unliking a vacation
        clickedUnlike.setAttribute("name", "vacation_id"); // give it a name so it can be fetched from the form in our facade
        clickedUnlike.click(); // simulate a user click to submit
        clickedUnlike.removeAttribute("name", "vacation_id"); // remove the name attribute after use so it can be attached to other likes/unlikes

        heart.classList.remove("heartClick"); // remove the clicked effect to the heart
        likeAmount.innerHTML = parseInt(likeAmount.innerHTML) - 1; // decrease like amount
    }
}

// show like amount for every vacation
const likeAmount = document.getElementById("likeAmount");

if (likeAmount){
    const listLikes = JSON.parse(likeAmount.value);
    window.addEventListener('load', addLikedAmount((listLikes)));
    likeAmount.remove();
    
    function addLikedAmount(likeAmount){
        for (let i = 0; i < likeAmount.length; i++){
            let likeSpan = document.querySelector(`.vacationLikeAmount${likeAmount[i][0]}`);
            likeSpan.innerHTML = likeAmount[i][1];
        }
    }
}


// shows user the vacations he liked
const userLikes = document.getElementById("userLikes");

if (userLikes && userLikes.value != "{}"){
    const userLikesValue = userLikes.value;
    const objUserLikes = JSON.parse(userLikesValue);
    window.addEventListener('load', showUserLikes(objUserLikes));
    userLikes.remove();

    function showUserLikes(userLikes){
            const vacationIds = Object.values(userLikes)[0];
            for (let i = 0; i < vacationIds.length; i++){
                const detailsAndLikes = document.getElementById(`detailsAndLikes${vacationIds[i]}`);
                const heart = detailsAndLikes.querySelector(".heart");
                heart.classList.add("heartClick"); 
            }
    }
}

// cosmetics and extra functionality to the vacation page
// functions for actions we'll do a lot
function getVacationGrid(){
    const vacationGrid = document.querySelector(".vacationGrid");
    return vacationGrid;
}

function getVacationGridChildren(){
    const vacationGrid = document.querySelector(".vacationGrid");
    return vacationGrid.children;
}

// on loading check and update how long text is shown
const vacationPageCheck = document.querySelector(".vacationGrid");

if (vacationPageCheck){
    const gridChildren = getVacationGridChildren();
    for (let vacation of gridChildren){ 
        const descriptionDiv = vacation.querySelector(".vacationDescription");
        changeTextDisplay(descriptionDiv);
    }
}


// control how the user sees text in the vacation boxes
function changeTextDisplay(descriptionDiv){
    const textLength = descriptionDiv.innerText.length;
    if (textLength > 450){
        if (!descriptionDiv.classList.contains("addAfterShadow")){

            descriptionDiv.classList.add("addAfterShadow");
            descriptionDiv.classList.remove("removeAfterShadow");
            descriptionDiv.classList.remove("scrollText");
        }
        else{

            descriptionDiv.classList.remove("addAfterShadow");
            descriptionDiv.classList.add("removeAfterShadow");
            descriptionDiv.classList.add("scrollText");
        }
    }

}

// change how the vacations are shown on select change
function changeVacationsView(viewSelect){
    if (viewSelect.value === "allVacations"){
        showAllVacations(getVacationGridChildren());
    }
    else if (viewSelect.value === "LikedVacations"){
        showLikedVacations(getVacationGridChildren());
    }
}

function showAllVacations(vacationsGridChildren){

    for (let i = 0; i < vacationsGridChildren.length; i++){
        if (vacationsGridChildren[i].hidden === true);
        {
            vacationsGridChildren[i].hidden = false;
        }
    }
}

function showLikedVacations(vacationsGridChildren){

    for (let i = 0; i < vacationsGridChildren.length; i++){
        let isVacationLiked = vacationsGridChildren[i].querySelector(".heartClick");
        if (!isVacationLiked){
            vacationsGridChildren[i].hidden = true;
        }
    }
}

// change the order of the vacations shown
function changeVacationsOrder(orderSelect){
    if (orderSelect.value === "orderStartDate"){
        orderByStartDate(getVacationGrid());
    }
    else if (orderSelect.value === "orderPrice"){
        orderByPrice(getVacationGrid());
    }
    else if (orderSelect.value === "likedAmount"){
        orderByLikedAmount(getVacationGrid());
    }
}

function orderByStartDate(vacationGrid){

    // get the grid and create a new temp one to sort the children
    let vacationsGridChildren = vacationGrid.children;
    let newChildGrid = document.createElement("div"); 

    while (vacationsGridChildren.length != 0){
        let saveIndex = 0;
        let lowestDate = Date.parse("9999-12-31"); // set to the highest/lowest value possible for the particular variable on our/its constraints
        for (let i = 0; i < vacationsGridChildren.length; i++){
            let dateDivText = vacationsGridChildren[i].querySelector(".vacationDetails").innerText;
            let startDate = dateDivText.substring(0, 10); // get only the start date part from the text
            let timestampDate = Date.parse(startDate); // change the string to a date format we can do operations on 
            if (timestampDate < lowestDate){
                lowestDate = timestampDate;
                saveIndex = i;
            }
        }

        let earliestStartDate = vacationsGridChildren[saveIndex].parentNode.removeChild(vacationsGridChildren[saveIndex]); // removes and saves the div from the grid
        newChildGrid.appendChild(earliestStartDate); // adds it to our temp grid as a child
    }

    vacationGrid.replaceChildren(...newChildGrid.children); // add all the children sorted to our original grid by copying from our temp grid
}

function orderByPrice(vacationGrid){

    // get the grid and create a new temp one to sort the children
    let vacationsGridChildren = vacationGrid.children;
    let newChildGrid = document.createElement("div");
    while (vacationsGridChildren.length != 0){
        let saveIndex = 0;
        let lowestPrice = 10000; // set to the highest/lowest value possible for the particular variable on our/its constraints
        for (let i = 0; i < vacationsGridChildren.length; i++){
            let vacationPriceDiv = vacationsGridChildren[i].querySelector(".price"); 
            let vacationPriceText = vacationPriceDiv.innerText;
            let vacationPrice = (parseInt(vacationPriceText.substring(0, vacationPriceText.length - 1))); // get the price without the $ at the end and then make it an integer
            if (vacationPrice < lowestPrice){
                lowestPrice = vacationPrice;
                saveIndex = i;
            }
        }

        let lowestPricedVacation = vacationsGridChildren[saveIndex].parentNode.removeChild(vacationsGridChildren[saveIndex]); // removes and saves the div from the grid
        newChildGrid.appendChild(lowestPricedVacation); // adds it to our temp grid as a child
    }

    vacationGrid.replaceChildren(...newChildGrid.children); // add all the children sorted to our original grid by copying from our temp grid
}

function orderByLikedAmount(vacationGrid){

    // get the grid and create a new temp one to sort the children
    let vacationsGridChildren = vacationGrid.children;
    let newChildGrid = document.createElement("div");
    while (vacationsGridChildren.length != 0){
        let saveIndex = 0;
        let highestLikes = 0; // set to the highest/lowest value possible for the particular variable on our/its constraints
        for (let i = 0; i < vacationsGridChildren.length; i++){
            let vacationLikesDiv = vacationsGridChildren[i].querySelector(".vacationLikes");
            let vacationLikes = parseInt(vacationLikesDiv.children[1].innerText); // get the second child of the div(which displays the like amount), get its text and parse it to an integer
            if (vacationLikes > highestLikes){
                highestLikes = vacationLikes;
                saveIndex = i;
            }
        }

        let highestHeartAmount = vacationsGridChildren[saveIndex].parentNode.removeChild(vacationsGridChildren[saveIndex]); // removes and saves the div from the grid
        newChildGrid.appendChild(highestHeartAmount); // adds it to our temp grid as a child
    }

    vacationGrid.replaceChildren(...newChildGrid.children); // add all the children sorted to our original grid by copying from our temp grid

}