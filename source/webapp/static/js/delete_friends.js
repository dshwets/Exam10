async function removeFriends(event) {
    event.preventDefault();
    let removefriendBtn = event.target.parentElement;
    let url = removefriendBtn.href;

    try {
        let response = await makeRequest(url, 'DELETE');
        let data = await response.text();
        console.log(data);
        event.target.parentElement.parentElement.remove()
    }
    catch (error) {
        console.log(error);
    }

}


window.addEventListener('load', function() {
    const btns = document.getElementsByClassName('btn btn-primary')
    for (let btn of btns) {btn.onclick = removeFriends}

});